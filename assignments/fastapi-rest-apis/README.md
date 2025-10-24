# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Os estudantes vão construir uma API REST simples usando o framework FastAPI. A tarefa introduz conceitos de endpoints, validação com Pydantic e como executar a aplicação localmente.

## 📝 Tasks

### 🛠️ Criar uma API básica (Endpoints CRUD simples)

#### Description
Implemente uma API que permita listar itens, criar um novo item e recuperar um item por ID.

#### Requirements
Completed program should:

- Expor um endpoint GET `/items` que retorne todos os itens
- Expor um endpoint POST `/items` que crie um novo item (com `name` e `description`)
- Expor um endpoint GET `/items/{id}` que retorne um item por ID ou 404 se não existir
- Usar Pydantic para modelos de entrada/saída

### 🛠️ Persistência (opcional avançado)

#### Description
Como exercício opcional, persista dados em um banco SQLite usando uma biblioteca leve (por exemplo, SQLModel ou SQLAlchemy).

#### Requirements
Completed program should:

- Substituir a lista em memória por um armazenamento persistente (SQLite)
- Garantir que os dados persistam entre reinícios

---

## Como rodar (localmente)

1. Instale dependências:

```bash
pip install fastapi uvicorn
```

2. Execute a aplicação:

```bash
uvicorn starter-code:app --reload
```

3. Abra `http://127.0.0.1:8000/docs` para ver a documentação automática (Swagger UI).

## Critérios de avaliação

- Endpoints funcionais conforme descrito
- Uso correto de Pydantic para validação
- Código limpo e bem documentado
- (Opcional) Persistência com SQLite

Boa sorte! Encoraje o uso do `/docs` para inspecionar a API durante o desenvolvimento.
