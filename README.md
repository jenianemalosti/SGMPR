# FIAP - Faculdade de Informática e Administração Paulista

# Nome do projeto: Sistema de Gestão e Monitoramento de Produção Rural (SGMPR)

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a> Gabriel Luigi Fortunato de Santa - RM563710</a>
- <a> Jeniane Joice Malosti de Oliveira - RM561936</a>
- <a> Lucas Xavier - RM563436</a> 
- <a> Marcus Vinicius de Andrade - RM564544</a> 
- <a> Mayara Prado Goes - RM564058</a>


## 👩‍🏫 Professores:
### Tutor(a) 
- <a>Lucas Gomes Moreira</a>
### Coordenador(a)
- <a> André Godoi Chiovato</a>


## 📜 Descrição

O Sistema de Gestão e Monitoramento de Produção Rural (SGMPR) foi desenvolvido para atender às necessidades de pequenos produtores rurais. O sistema tem como objetivo otimizar o processo de gestão, controle e monitoramento de informações relacionadas aos produtores, insumos e produção rural.

Desenvolvido em Python com integração ao Oracle Database, o sistema também realiza exportação e importação de dados em JSON, além de geração de relatórios em formato TXT. A aplicação foi implementada por meio de uma interface de linha de comando (CLI), e faz parte de uma atividade acadêmica focada na aplicação de estruturas de dados, manipulação de arquivos e integração com banco de dados.

Principais Funcionalidades:
Cadastro, listagem, alteração e exclusão de produtores;

Cadastro e monitoramento de insumos;

Geração de relatórios de insumos por tipo e unidade (em TXT);

Exportação e importação de dados em JSON.

Com foco em usabilidade e eficiência, o SGMPR é uma ferramenta prática para auxiliar pequenos produtores no gerenciamento da produção agrícola*


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

<b>pycache</b>: Diretório gerado automaticamente para armazenar arquivos compilados do Python.

<b>.gitattributes</b>: Arquivo de configuração do Git.

<b>README.md</b>: Guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

<b>db.py</b>: Script responsável pela integração com o banco de dados (conexões e consultas).

<b>main.py</b>: Script principal que executa a interface CLI e manipula os dados do sistema.

<b>produtores.json</b>: Arquivo gerado para exportação de dados dos produtores.

<b>relatorio.txt</b>: Relatório de dados gerais (se necessário, exemplo de relatório simples).

<b>relatorio_insumos.txt</b>: Relatório detalhado sobre os insumos cadastrados.

<b>relatorios.py</b>: Script para geração dos relatórios em formato de texto (relatório de insumos, por exemplo).

<h2>🔧 Como executar o código</h2>

<p><strong>Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.</strong></p>

<h3>✅ Pré-requisitos</h3>
<ul>
    <li><strong>Python</strong>: 3.13.2 ou superior</li>
    <li><strong>Oracle Database XE</strong> (versão 18c ou superior)</li>
    <li><strong>Sistema Operacional</strong>: Windows, Linux ou macOS</li>
    <li><strong>Biblioteca</strong>: <code>oracledb</code></li>
</ul>

<h3>🚀 Instalação</h3>

<h4>Fase 1 – Ambiente</h4>
<ol>
    <li><strong>Instalar Python</strong><br>
        <a href="https://www.python.org/downloads/release/python-1312/" target="_blank">Baixe o Python 3.13.2 aqui</a><br>
        Certifique-se de adicionar o Python ao <strong>PATH</strong> durante a instalação.
    </li>
    <li><strong>Instalar a biblioteca <code>oracledb</code></strong><br>
        Abra o terminal e execute o seguinte comando:
        <pre><code>pip install oracledb</code></pre>
    </li>
</ol>

<h4>Fase 2 – Banco de Dados</h4>
<ol>
    <li><strong>Instalar Oracle Database XE (18c+)</strong><br>
        Após a instalação, configure o banco de dados com as seguintes credenciais:
        <ul>
            <li><strong>Usuário</strong>: system</li>
            <li><strong>Senha</strong>: 1234</li>
            <li><strong>Service Name</strong>: xe</li>
        </ul>
    </li>
    <li><strong>Criação de Tabelas</strong><br>
        Acesse o banco de dados e crie as tabelas necessárias (produtores, insumos) utilizando o script SQL que está disponível no repositório.
    </li>
</ol>

<h4>Fase 3 – Execução</h4>
<ol>
    <li><strong>Rodar o sistema</strong><br>
        No terminal, execute o seguinte comando para iniciar o sistema:
        <pre><code>python main.py</code></pre>
        O sistema abrirá um menu interativo com as opções para cadastrar, listar produtores, gerar relatórios, etc.
    </li>
</ol>

<h3>🗃 Histórico de lançamentos</h3>
<ul>
 
</ul>

<h3>📋 Licença</h3>
<p>
</p>
