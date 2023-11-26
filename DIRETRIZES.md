A fim de obter uma melhor experiência de desenvolvimento e de visibilidade do código, deve se seguir as seguintes diretrizes de código em todos os arquivos do repositório:

## Diretrizes de Codificação

### Estilo de Código
- **Docstrings + TypeHints**: Todos os métodos e funções devem ser documentados usando o estilo de docstring do NumPy. Descrição clara do propósito da função, seus parâmetros, tipos de retorno e exemplos de uso. Também é essencial incluir type hints para melhorar a legibilidade e a manutenção do código.

    Exemplo:
    ```python
    def exemplo_funcao(parametro: int) -> bool:
        """
        Descrição breve da função.

        Parameters
        ----------
        parametro : int
            Descrição do parâmetro.

        Returns
        -------
        bool
            Descrição do valor de retorno.
        """
    ```
- **Variáveis (`snake_case`)**: 
    - Utilize `snake_case` para nomear variáveis. Isso significa usar letras minúsculas e sublinhados para separar palavras.
    - Exemplo: `tree`, `index`.

- **Classes (`CamelCase`)**: 
    - Nomeie classes usando `CamelCase`, onde cada palavra começa com uma letra maiúscula e sem espaços entre elas.
    - Exemplo: `AlgoritmoExemplo`, `ArvoreDeDecisao`.


### Princípios de Design
- **SOLID**: Tentar sempre seguir os princípios SOLID de design de software:
    - **S**ingle Responsibility Principle (Princípio da Responsabilidade Única)
    - **O**pen/Closed Principle (Princípio Aberto/Fechado)
    - **L**iskov Substitution Principle (Princípio da Substituição de Liskov)
    - **I**nterface Segregation Principle (Princípio da Segregação de Interface)
    - **D**ependency Inversion Principle (Princípio da Inversão de Dependência)

### Commits
 - Ao realizar um commit, detalhar o máximo possível as mudanças e melhoras no código.
