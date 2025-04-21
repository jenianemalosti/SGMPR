**# Sistema de Gestão e Monitoramento de Produção Rural (SGMPR)#**

## Descrição

O **Sistema de Gestão e Monitoramento de Produção Rural (SGMPR)** foi desenvolvido para atender às necessidades de pequenos produtores rurais. O sistema visa otimizar o processo de gestão, controle e monitoramento de informações relacionadas aos produtores, insumos e produção rural, usando Python, Oracle Database, e exportação/importação de dados para JSON.

Este projeto foi desenvolvido como parte de uma atividade acadêmica, aplicando conhecimentos sobre estruturas de dados, manipulação de arquivos, integração com banco de dados e construção de sistemas interativos por meio de uma interface de linha de comando (CLI).

## Requisitos

- **Python**: 3.13.2
- **Oracle Database**: Xe (versão 18c ou superior)
- **Biblioteca**: `oracledb`
- **Sistema Operacional**: Windows, Linux ou macOS

## Funcionalidades

- **Cadastro de Produtores**: Permite o cadastro de produtores com informações como nome, propriedade e tipo de cultivo.
- **Alteração e Exclusão de Produtores**: Permite alterar ou excluir os dados dos produtores.
- **Listagem de Produtores**: Exibe a lista completa de produtores cadastrados.
- **Cadastro e Monitoramento de Insumos**: Cadastro de insumos (sementes, fertilizantes, etc.). Monitoramento da quantidade e tipo dos insumos.
- **Relatório de Insumos**: Geração de relatório com a soma total de insumos por tipo e unidade.
- **Exportação e Importação de Dados em JSON**: Exportação dos dados dos produtores para um arquivo JSON. Importação de dados de produtores de um arquivo JSON.
- **Geração de Relatório de Insumos em TXT**: Geração de relatório em formato texto, armazenando as informações sobre insumos.

## Instalação

### 1. Configuração do Ambiente

#### Passo 1: Instalar Python 3.13.2
Baixe e instale o Python 3.13.2 em [python.org](https://www.python.org/downloads/release/python-1312/). Certifique-se de adicionar o Python ao PATH durante a instalação.

#### Passo 2: Instalar a Biblioteca `oracledb`
Com o Python instalado, execute o seguinte comando para instalar a biblioteca `oracledb`:

```bash
pip install oracledb**
2. Configuração do Oracle Database
Instale o Oracle Database XE (versão 18c ou superior).

Configure o banco de dados com as credenciais (usuário system, senha 1234, e service_name xe).

3. Banco de Dados
Acesse o banco de dados e crie as tabelas necessárias (produtores, insumos) usando o SQL fornecido no código.

Uso
1. Execução do Sistema
Para iniciar o sistema, execute o script Python principal. Isso irá abrir um menu de opções no terminal:

bash
Copiar código
python main.py
No menu interativo, você pode escolher entre várias opções, como cadastrar produtores, listar produtores, gerar relatórios, etc.

2. Exemplo de Funcionalidade
Cadastrar Produtor: O sistema solicita os dados do produtor e os armazena no banco de dados.

Gerar Relatório de Insumos: O sistema calcula e exibe o total de cada tipo de insumo.

Exportação para JSON: Exporta todos os dados dos produtores para um arquivo produtores.json.

3. Comandos Básicos
Voltar ao menu principal: Após cada operação, o sistema perguntará se você deseja voltar ao menu principal ou sair.

Arquivos no Repositório
main.py: Script principal do sistema.

produtores.json: Arquivo gerado para exportação de dados dos produtores.

relatorio_insumos.txt: Arquivo gerado para relatório de insumos.

Contribuidores
GABRIEL LUIGI FORTUNATO DE SANTA – 563710

JENIANE JOICE MALOSTI DE OLIVEIRA – 561936

LUCAS XAVIER – 563436

MARCUS VINICIUS DE ANDRADE – 564544

MAYARA PRADO GOES – 564058

Considerações Finais
Este sistema foi desenvolvido com foco em usabilidade e eficiência para pequenos produtores rurais, permitindo que as informações sobre a produção e insumos sejam facilmente gerenciadas e acessadas.

Com a integração ao banco de dados Oracle e a possibilidade de exportação/importação de dados em JSON, o sistema facilita o armazenamento e a manipulação de informações.
