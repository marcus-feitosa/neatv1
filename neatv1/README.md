"""
# Treinamento de IA usando NEAT

## Bibliotecas:
- Bibliotecas: retro, numpy, opencv-python (cv2), neat-python

## Processo NEAT

NEAT (NeuroEvolution of Augmenting Topologies) é um algoritmo genético para a evolução de redes neurais artificiais. Ele começa com uma população inicial de redes neurais simples e as evolui ao longo do tempo através de processos inspirados na evolução biológica, como mutação, crossover e seleção natural.

## Funcionamento do Código

- **Inicialização do Ambiente:** O jogo "Super Mario World" é carregado usando a biblioteca Retro, com especificações de estado e jogadores.

- **Estrutura da Rede Neural:** Utilizamos uma rede neural recorrente, que é mais adequada para lidar com dados sequenciais e temporais, características inerentes aos jogos. Configurações da rede neural se encontram no arquivo `config-feedforward`.

- **Processamento de Imagens:** As imagens do jogo são processadas (redimensionadas e convertidas para escala de cinza) para simplificar a entrada na rede neural.

- **Função de Avaliação de Genomas:** A função `evaluate_genomes` é a função principal do processo de treinamento. Ela avalia cada genoma (agente) na população, determinando seu desempenho no jogo.

- **Critérios de Fitness:** O fitness (pontuação) de cada genoma é calculado com base em vários fatores, como pontuação, moedas coletadas, progressão no nível, uso de power-ups e sobrevivência.

- **Evolução e Seleção:** Após cada rodada de avaliação, os genomas são selecionados com base em seu fitness, e novos genomas são criados por meio de cruzamentos e mutações.

- **Checkpoint e Restauração:** O sistema salva periodicamente o estado da evolução (checkpoints) e permite a restauração para continuar o treinamento de um ponto específico.


