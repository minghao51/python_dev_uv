# Data Engineering Development Environment

A standardized development environment setup using `uv` Python package manager, featuring Dagster for orchestration, dbt for transformations, DuckDB for data storage, and Astro Starlight for documentation.

## 🚀 Features

- Fast Python environment management with `uv`
- Data orchestration with Dagster
- Data transformation with dbt
- Local data warehousing with DuckDB
- Jupyter notebooks support for exploration
- Documentation with Astro Starlight
- Dev container configuration for consistent development experience

## 📁 Project Structure

```
.
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
├── docs/
│   ├── src/
│   │   ├── content/
│   │   └── assets/
│   └── astro.config.mjs
├── notebooks/
│   └── examples/
├── src/
│   ├── dagster_home/
│   │   ├── workspace.yaml
│   │   └── dagster.yaml
│   ├── dbt/
│   │   ├── models/
│   │   ├── tests/
│   │   ├── macros/
│   │   ├── seeds/
│   │   └── dbt_project.yml
│   └── pipelines/
│       └── assets/
├── tests/
│   ├── integration/
│   └── unit/
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 🛠 Prerequisites

- Docker Desktop
- Visual Studio Code with Remote Development extension
- Git

## 🏃‍♂️ Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Open in VS Code with Dev Containers:
```bash
code .
```
- When prompted, click "Reopen in Container"
- Wait for the container to build and initialize

3. Initialize the Python environment:
```bash
uv venv
source .venv/bin/activate  # On Unix
# or
.venv\Scripts\activate  # On Windows
```

4. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## 🔧 Component Setup

### Dagster
- Start the Dagster webserver:
```bash
dagster dev
```
- Access the Dagster UI at `http://localhost:3000`

### DuckDB
- DuckDB is included in the requirements and ready to use
- Database files will be stored in `data/`

### dbt
- Configure your dbt project:
```bash
cd src/dbt
dbt init
```
- Update `profiles.yml` with DuckDB connection

### Documentation
- Start the documentation server:
```bash
cd docs
npm install
npm run dev
```
- Access the documentation at `http://localhost:4321`

## 📝 Development Workflow

1. Create a new feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Develop your data pipelines in `src/pipelines/`
3. Create dbt models in `src/dbt/models/`
4. Document your changes in `docs/src/content/`
5. Test your changes:
```bash
pytest tests/
dbt test
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📚 Additional Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [Dagster Documentation](https://docs.dagster.io)
- [dbt Documentation](https://docs.getdbt.com)
- [DuckDB Documentation](https://duckdb.org/docs)
- [Astro Starlight Documentation](https://starlight.astro.build)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details