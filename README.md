# ROBUST CONTROL

Simulações executadas durante a disciplina de Controle Robusto (PGNE612).

## Organização dos diretórios

- exercices: Diretório com a solução das atividades computacionais utilizando Jupiter Notebook;
- src: Diretório com os códigos de simulação das aulas práticas;

## Descrição dos arquivos

- .gitignore: Lista arquivos e pastas que o Git deve ignorar (não versionar), como virtualenvs, caches, arquivos temporários, builds, segredos locais etc.
- .python-version: Indica a versão do Python a ser usada no projeto
- pyproject.toml: Arquivo de configuração padrão para projetos Python. Define metadados do pacote (nome, versão), dependências, scripts, build-system (PEP 517/518) e configurações de ferramentas (ruff, black, mypy, pytest, etc.).
- uv.lock: Arquivo de “lock” gerado pelo gerenciador uv, fixando versões exatas das dependências (e hashes) para builds reprodutíveis. Não é editado manualmente; é usado para garantir que todos instalem exatamente as mesmas versões.