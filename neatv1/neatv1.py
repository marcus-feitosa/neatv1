import retro 
import numpy as np
import cv2
import neat
import pickle
env = retro.make(game='SuperMarioWorld-Snes', state='YoshiIsland2', players=1)
from rewards import *

img_array = []

def evaluate_genomes(genomes, config) -> None:
    """Runs the evaluation of genomes, based on config and past genomes.

    Parameters
    ----------
    genomes:
        The genomes of the agent, which contains the information about a specie
    config :
        Configuration of the NEAT
    """
    for genome_id, genome in genomes:
        game_status_observation = env.reset()
        action = env.action_space.sample() # action with generic sample

        iny, inx, inc = env.observation_space.shape

        inx = int(inx/8)
        iny = int(iny/8)

        # Create a Recurrent Neural Network.
        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)

        current_max_fitness = 0
        pontuation = 0
        frame = 0
        counter = 0
        score = 0
        score_tracker = 0
        coins = 0
        coins_tracker = 0
        yoshi_coins = 0
        yoshi_coins_tracker = 0
        x_pos_previous =  0
        y_pos_previous = 0
        checkpoint = False
        checkpoint_value = 0
        end_of_level = 0
        power_ups =  0
        power_ups_last = 0
        jump =  0


        done = False

        while not done:
            env.render()
            frame += 1
            
            #Aqui são feitas operações de imagem para agilizar o processamento dela pela rede neural
            game_status_observation = cv2.resize(game_status_observation, (inx, iny))
            game_status_observation = cv2.cvtColor(game_status_observation, cv2.COLOR_BGR2GRAY)
            game_status_observation = np.reshape(game_status_observation, (inx, iny))

            imgarray = game_status_observation.flatten()

            nnOutput = net.activate(imgarray)   
            
            game_status_observation, rew, done, game_info = env.step(nnOutput)        

            score = game_info['score']
            coins = game_info['coins']
            dead = game_info['dead']
            x_pos = game_info['x']
            y_pos = game_info['y']
            jump = game_info['jump']
            checkpoint_value = game_info['checkpoint']
            end_of_level = game_info['endOfLevel']
            power_ups = game_info['powerups']

            # Add to fitness score if mario gains points on his score.
            if score > 0:
                if score > score_tracker:
                    pontuation = (score * SCORE_MULT)
                    score_tracker = score
            
            # Add to fitness score if mario gets more coins.
            if coins > 0:
                if coins > coins_tracker:
                    pontuation += COINS*(coins - coins_tracker)
                    coins_tracker = coins
        
            # As mario moves right, reward him slightly.
            if x_pos > x_pos_previous:
                if jump > 0:
                    pontuation += RIGHT_MOVEMENT
                pontuation += x_pos * PROGESSION_MULT
                x_pos_previous = x_pos
                counter = 0
            # If mario is standing still or going backwards, penalize him slightly.
            else: 
                counter += 1
                pontuation += STAND_STILL                      
            
            # Award mario slightly for going up higher in the y position (y pos is inverted).
            #JUMP MOVE
            if y_pos < y_pos_previous:
                pontuation += UP_MOVEMENT
                y_pos_previous = y_pos

            #SE POWER_UPS == 1, MARIO ESTÁ COM UM COGUMELO. RECOMPENSE-O.
            elif power_ups == 1:
                if power_ups_last == 1 or power_ups_last == 0:
                    pontuation += POWER_UP_KEEP      
                elif power_ups_last == 2: 
                    pontuation += POWER_UP_LOST

            #SE POWER_UPS == 2, MARIO ESTÁ COM A CAPA. RECOMPENSE-O.
            elif power_ups == 2:
                pontuation += POWER_UP_CAPE_KEEP
                
            power_ups_last = power_ups
            
            #CHECKPOINT
            if checkpoint_value == 1 and checkpoint == False:
                pontuation += CHECKPOINT
                checkpoint = True
            
            #END OF LEVEL
            if end_of_level == 1:
                pontuation += END_OF_LEVEL
                done = True

            #STAND STILL FOR TOO LONG
            if counter == 1000:
                pontuation -= STAND_STILL_TOO_LONG
                done = True                

            #DEATH
            if dead == 0:
                pontuation -= DEAD
                done = True 
            
            if done == True:
                #Posição onde Mario encontra o primeiro inimigo (considerando o chão)
                #Se ele morre aqui, perde pontos. Caso contrario, recebe recompensa.
                #Ideal seria retirar isso, não sei se se manterá.
                if 1280 < int(x_pos) < 1290:
                    pontuation -= 12000
                if x_pos > 1290:
                    pontuation += 10000
                print(x_pos)
                print(genome_id, pontuation)

            genome.fitness = pontuation
            
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                     'config-feedforward')

checkpoint = "neat-checkpoint-54"
population = neat.Population(config)
population = neat.Checkpointer.restore_checkpoint(f"neat_checkpoints/{checkpoint}")

population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)
population.add_reporter(neat.Checkpointer(10))

winner = population.run(evaluate_genomes)

with open('winner.pkl', 'wb') as output:
    pickle.dump(winner, output, 1)
