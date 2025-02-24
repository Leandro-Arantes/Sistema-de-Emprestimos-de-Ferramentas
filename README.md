# Sistema de Empréstimos de Ferramentas

Este projeto é um sistema simples para gerenciar empréstimos de ferramentas, utilizando um banco de dados SQLite e uma interface gráfica feita com Tkinter.

## Funcionalidades

- Adicionar ferramentas ao sistema.
- Registrar empréstimos de ferramentas.
- Registrar devoluções de ferramentas.
- Listar todas as ferramentas e empréstimos.

## Tecnologias Utilizadas

- **Python 3**
- **SQLite**: Banco de dados para armazenar ferramentas e empréstimos.
- **Tkinter**: Biblioteca para criar a interface gráfica.

## Como Usar

### Pré-requisitos

- Python 3 instalado.
- Instale as dependências:

```
  pip install -r requirements.txt
```

## Executando o Projeto
Clone o repositório:
  ```bash
git clone https://github.com/seuusuario/sistema_emprestimos.git
cd sistema_emprestimos
```
### Execute o projeto:

``` 
python main.py 
```
## Estrutura do Projeto
```
sistema_emprestimos/
├── docs/                     # Documentação do projeto
├── src/                      # Código-fonte
│   ├── controller/           # Lógica de controle
│   ├── models/               # Lógica de banco de dados
│   ├── views/                # Interface gráfica
│   ├── utils/                # Utilitários
│   └── app/                  # Configuração da aplicação
├── img/                      # Imagens (se necessário)
├── tests/                    # Testes (se necessário)
├── README.md                 # Documentação principal
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
└── main.py                   # Ponto de entrada do projeto
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Abra uma issue ou envie um pull request!

## Autor

* 👤 Leandro Arantes
* GitHub: @Leandro-Arantes
* Projeto: Sistema de Empréstimos de Ferramentas

### Colaboração 
* 👤 Otávio Augusto
* GitHub: @otavioaugust1

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.