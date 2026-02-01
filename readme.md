# 📊 Data Pipeline Project

Projeto de pipeline de dados utilizando **PostgreSQL via Docker**, **Python** e execução de **scripts SQL**, com estrutura organizada para ingestão, processamento e análises (incluindo uso futuro de LLMs).

---

## 🧰 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Docker**
- **Docker Compose**
- **Python 3.10+**
- **Git** (opcional, mas recomendado)
- **Ollama** (https://ollama.com/library/llama3.1)

---

## 🐘 Banco de Dados (PostgreSQL)

O PostgreSQL é executado via **Docker Compose**.

### Subir o banco
```bash
docker-compose up -d
```

```bash
Estrutura do Projeto
.
├── data_src/        # Fontes de dados (CSV, JSON, etc)
├── sql/             # Scripts SQL (DDL / DML)
├── scripts/         # Scripts Python do pipeline
├── llm_insights/    # Análises e outputs gerados por LLMs
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### ⚠️ Importante

- Os arquivos dentro de data_src/ devem existir
- Os nomes dos arquivos devem ser exatamente os mesmos referenciados nos scripts Python


### Configuração do Banco (DBConnection)
```python
## Informar corretamente as credenciais do banco

def cria_conexao():
    return psycopg2.connect(
        dbname="mydatabase",
        user="admin",
        password="admin",
        host="localhost",
        port="5959"
    )
```

### Executar
```bash
python3 Run-Pipeline.py
```