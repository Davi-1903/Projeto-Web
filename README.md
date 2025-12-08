# Projeto Web

## 📋 Sobre o Projeto

Este sistema foi criado para resolver a falta de um canal formal e organizado onde a comunidade escolar possa compartilhar ideias de melhoria. Ele permite que alunos e funcionários enviem sugestões, acompanhem seu status e recebam feedback da administração de forma transparente e estruturada.

### Principais Funcionalidades

**Para Alunos e Funcionários:**
- Cadastro e login com diferenciação automática por domínio de email
- Enviar sugestões com título e descrição
- Visualizar todas as sugestões da comunidade
- Acompanhar o status das próprias sugestões
- Ver histórico de respostas dos administradores

**Para Administradores:**
- Painel administrativo completo
- Visualizar e gerenciar todas as sugestões
- Alterar status das sugestões (pendente, em análise, aprovada, implementada, recusada)
- Responder às sugestões
- Registrar descrição de implementação

## Tecnologias Utilizadas

- **Python**
- **Flask** - Framework web
- **Flask-Login** - Gerenciamento de autenticação
- **SQLAlchemy** - ORM para banco de dados
- **PyMySQL** - Driver MySQL
- **Werkzeug** - Segurança da aplicação (hashing de senhas)
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## Como Rodar?

### Pré-requisitos

- Python 3.8 ou superior
- MySQL ou MariaDB instalado e rodando
- pip (gerenciador de pacotes Python)

### Passo a Passo

#### 1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd projeto-web
```

#### 2. **Crie um ambiente virtual**
```bash
python -m venv venv
```

#### 3. **Ative o ambiente virtual**

No Windows:
```bash
venv\Scripts\activate
```

No Linux/Mac:
```bash
source venv/bin/activate
```

#### 4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

#### 5. **Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URI=mysql+pymysql://usuario:senha@localhost/nome_do_banco
```

Substitua:
- `sua_chave_secreta_aqui` por uma string aleatória segura
- `usuario` pelo usuário do MySQL
- `senha` pela senha do MySQL
- `nome_do_banco` pelo nome do banco de dados que deseja usar

#### 6. **Crie o banco de dados**

Entre no MySQL e crie o banco:
```sql
CREATE DATABASE nome_do_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 7. **Execute a aplicação**
```bash
python app.py
```

Ou usando Flask:
```bash
flask run
```

#### 8. **Acesse o sistema**

Abra seu navegador e acesse: `http://localhost:5000`

## Tipos de Usuário

O sistema identifica automaticamente o tipo de usuário baseado no domínio do email:

- **@aluno.com** - Acesso de aluno
- **@funcionario.com** - Acesso de funcionário
- **@admin.com** - Acesso administrativo completo

### Exemplo de Cadastro

Para testar o sistema, você pode criar usuários com os seguintes emails:
- `joao@aluno.com` - Será cadastrado como aluno
- `maria@funcionario.com` - Será cadastrado como funcionário
- `admin@admin.com` - Terá acesso administrativo

## Status das Sugestões

As sugestões podem ter os seguintes status:

- **Pendente** - Sugestão recém-criada, aguardando análise
- **Em Análise** - Sendo avaliada pela administração
- **Aprovada** - Sugestão aprovada para implementação
- **Implementada** - Já foi implementada (requer descrição)
- **Recusada** - Não será implementada

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.