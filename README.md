# Approved

O **Approved** é uma ferramenta de automação baseada em Python que utiliza o conceito de **ETL (Extract, Transform, Load)** para processar listas de aprovados em processos seletivos. O objetivo é transformar dados brutos em mensagens personalizadas, facilitando a comunicação entre a organização e os candidatos.

##  Funcionalidades

- **Extração Automática:** Leitura de arquivos `.csv` com dados de candidatos.
- **Transformação Inteligente:** Aplicação de lógica condicional para gerar mensagens personalizadas com base no status (Aprovado, Cadastro Reserva, etc.).
- **Geração de Relatórios:** Exportação de uma nova planilha pronta para uso em ferramentas de e-mail marketing ou disparadores de mensagens.

##  Tecnologias Utilizadas

- **Python 3.x**
- **Pandas:** Para manipulação e análise de dados de alto desempenho.
- **CSV:** Formato padrão de entrada e saída.

##  O Processo ETL

O projeto segue o fluxo clássico de engenharia de dados:

1.  **Extract (Extração):** O script lê o arquivo `aprovados.csv` contendo as colunas de nome, nota e resultado.
2.  **Transform (Transformação):** - Limpeza de dados (se necessário).
    - Criação da coluna `mensagem_cordial` utilizando f-strings para personalização.
3.  **Load (Carga):** O resultado é salvo em um novo arquivo (ex: `resultados_processados.csv`), mantendo a integridade dos dados originais.

##  Como Utilizar

1. Certifique-se de ter o Python e o Pandas instalados:
   ```bash
   pip install pandas