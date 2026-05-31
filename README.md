# Projeto de Autenticação com Flask

Descrição curta

Projeto exemplo em Flask que implementa um sistema básico de autenticação de usuários (registro, login, logout, recuperação de sessão). O objetivo é servir como base para aplicações web que precisam de autenticação segura usando Flask e extensões comuns.

Principais funcionalidades

- Registro de usuário com validação básica
- Login com verificação de senha (hash seguro)
- Logout e proteção de rotas (login_required)
- Exemplo de endpoints RESTful para autenticação
- Integração com banco de dados via SQLAlchemy
- Suporte a migrações com Flask-Migrate

Tecnologias

- Python 3.8+ (recomendado)
- Flask
- Flask-Login
- Flask-Migrate
- Flask-SQLAlchemy
- Werkzeug (para hashing de senhas)

Requisitos

- Git
- Python 3.8 ou superior
- Virtualenv / venv (recomendado)

Instalação

1. Clone o repositório:

```bash
git clone <URL-do-repositório>
cd <nome-do-repositório>
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

Configuração (variáveis de ambiente)

Defina as variáveis de ambiente necessárias antes de executar a aplicação. Exemplo usando um arquivo `.env` ou exportando no terminal:

- `FLASK_APP` — nome do módulo da aplicação (ex: `app.py` ou `run.py`)
- `FLASK_ENV` — `development` ou `production`
- `SECRET_KEY` — chave secreta para sessões
- `DATABASE_URL` — URI do banco de dados (ex: `sqlite:///app.db` ou `postgresql://user:pass@localhost/dbname`)

Exemplo `.env` (usar com cuidado, não comitar em repositório público):

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=uma_chave_secreta_forte
DATABASE_URL=sqlite:///app.db
```

Banco de dados e migrações

Este projeto usa SQLAlchemy e Flask-Migrate para gerenciar o esquema do banco.

Inicializar migrações:

```bash
flask db init
flask db migrate -m "Criar tabelas iniciais"
flask db upgrade
```

Executando a aplicação

```bash
flask run
# ou, se usar um arquivo de execução direto
python run.py
```

Endpoints (exemplos)

Observação: estes são exemplos comuns — ajuste conforme a implementação do seu projeto.

- POST /api/auth/register — registrar novo usuário
  - Body (JSON): `{"email": "user@example.com", "password": "senha"}`
- POST /api/auth/login — autenticar usuário
  - Body (JSON): `{"email": "user@example.com", "password": "senha"}`
- POST /api/auth/logout — encerrar sessão
- GET /api/user/profile — perfil do usuário (protegido)

Exemplo de uso com `curl`:

```bash
# Registrar
curl -X POST -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"senha"}' \
  http://localhost:5000/api/auth/register

# Login
curl -X POST -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"senha"}' \
  -c cookie.txt \
  http://localhost:5000/api/auth/login

# Acessar rota protegida usando cookie salvo
curl -b cookie.txt http://localhost:5000/api/user/profile
```

Testes

Inclua testes unitários e/ou de integração conforme necessário. Para rodar testes com `pytest`:

```bash
pip install -r requirements-dev.txt
pytest
```

Boas práticas de segurança

- Nunca armazene senhas em texto simples; sempre use hashing seguro (por ex. `werkzeug.security.generate_password_hash`).
- Use HTTPS em produção e proteja cookies com `Secure` e `HttpOnly`.
- Defina um `SECRET_KEY` forte e mantenha-o em segredo (gerenciador de segredos ou variáveis de ambiente).
- Valide e sanitize entradas do usuário.
- Considere limitar tentativas de login (rate limiting) e medidas anti-brute-force.

Estrutura sugerida de diretórios

```
project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── routes.py
│   │   └── forms.py
│   └── templates/
├── migrations/
├── tests/
├── requirements.txt
├── requirements-dev.txt
└── run.py
```

Contribuição

Contribuições são bem-vindas. Abra uma issue ou envie um pull request descrevendo as mudanças.

Licença

Escolha uma licença apropriada (por exemplo, MIT) e adicione um arquivo `LICENSE`.

Contato

Para dúvidas ou suporte, abra uma issue neste repositório.
