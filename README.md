# Backend-Challenge SHIPAY<br><br>

## 📋 Descrição do Projeto<br><br>

#### Este projeto é uma API REST desenvolvida em Python utilizando o framework Flask,  
#### para gerenciar usuários, seus papéis (roles) e permissões (claims).  

<br>

### - desempenho  
### - testes  
### - manutenibilidade  
### - boas práticas de engenharia de software!  
<br><br>

## 🚀 Funcionalidades da API<br><br>

### **Criação de Usuários:**  
#### Endpoint para criar novos usuários com dados como nome, e-mail, papel (role)  
#### e senha (opcional). Se não informada, uma senha será gerada automaticamente.  
<br>

### **Listar Permissões dos Usuários:**  
#### Endpoint para buscar todas as permissões de um usuário, juntamente com seu papel, nome e e-mail.  
<br>

### **Obter Papéis por ID de Usuário:**  
#### Endpoint para retornar o papel associado a um usuário específico pelo ID.  
<br><br>


## 📁 Estrutura de Pastas e Arquivos<br><br>

```plaintext
.
├── .venv/                 # -> Ambiente virtual
│             
├── models/                # -> Modelos representando tabelas do banco de dados
│   ├── __init__.py
│   │
│   ├── claim.py
│   │
│   ├── role.py
│   │
│   ├── user.py
│   │
│   └── user_claim.py
│
├── routes/                 # -> Rotas da API
│   ├── create_user_route.py
│   │
│   ├── get_role_by_user_id_route.py
│   │
│   └── get_user_claims_route.py
│
├── services/              # -> Serviços de lógica de negócios
│   ├── __init__.py
│   │
│   ├── create_user_service.py
│   │
│   ├── generate_password_service.py
│   │
│   ├── get_user_claims_service.py
│   │
│   └── get_role_by_user_id_service.py
│
├── .env                   # -> Variáveis de ambiente
│       
├── .gitignore             # -> Ignorar arquivos e diretórios no git
│
├── app.py                 # -> main
│
├── config.py              # -> Configuração do SQLAlchemy
│
├── db.py                  # -> Inicialização do banco de dados
│
└── requirements.txt       # -> Dependências do projeto

```

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python

- **Framework:** Flask

- **ORM:** SQLAlchemy

- **Banco de Dados:** PostgreSQL (Hospedado no Tembo)

- **Ferramentas:**

  - DBeaver para gerenciamento do banco
  - Insomnia para testes de API
 
<br>


## 🖥️ Configuração e Execução do Projeto Localmente

### Pré-requisitos

- Python 3.7  
- PostgreSQL  
- Ambiente virtual configurado (venv)  
- Ferramenta de gerenciamento do banco de dados (DBeaver, DBvisualizer, etc)

  <br>

### Passos

1. **Clone o repositório:**

    ```bash
    
    git clone <URL_DO_PROJETO>
    
    cd <NOME_DO_PROJETO>
    
    ```
    <br>

2. **Crie o ambiente virtual:**

    ```bash
    
    python -m venv .venv
    source .venv/bin/activate  # Linux ou Mac
    .venv\Scripts\activate     # Windows
    
    ```
    <br>

3. **Instale as dependências:**

    ```bash
    
    pip install -r requirements.txt
    
    ```
    <br>

4. **Configure o arquivo `.env`:**

    Crie ou edite o arquivo `.env` com as seguintes variáveis:

    ```env
    DB_HOST=<SEU_HOST>
    DB_PORT=5432
    DB_USER=<SEU_USUARIO>
    DB_PASSWORD=<SUA_SENHA>
    DB_NAME=<SEU_DATABASE>
    ```
<br><br>
    

5. **Inicie o banco de dados:** <br><br>

   **Certifique-se de que o PostgreSQL está em execução e as tabelas foram criadas.**         
                                                                                            
   ##### **OBS: A ferramenta TEMBO é utilizada para manter o banco de dados ativo**            
                                                                                              
   ##### **com isso, foi construído em ambiente de desenvolvimento do desenvolvedor deste**    
                                                                                              
   ##### **projeto, com isso, será necessário configurar um novo ou entrar em contato para**   
                                                                                              
   ##### **que seja disponibilizado**                                                 
<br><br>
   
## Execute a aplicação:<br>

```
python app.py

```
<br>

## Acesse a aplicação em:

```
http://127.0.0.1:5000

```
<br>

## 📖 Uso da API<br>



### Obter Permissões de Usuários<br>
#### 🟢📥 GET <br>
### /api/user_claims<br>
#### Retorno:

```

[

  {

    "claim_description": "Visualizar logs de erros",
    "role_description": "Suporte T\u00e9cnico",
    "user_email": "felipe.pereira@techcompany.com",
    "user_name": "Felipe Pereira"

  },
  {

    "claim_description": "Acesso total ao sistema",
    "role_description": "Desenvolvedor",
    "user_email": "TheAlex@techcorp.com",
    "user_name": "Alex Tig"

  },
  {

    "claim_description": "Acesso total ao sistema",
    "role_description": "Desenvolvedor",
    "user_email": "caio.gabriel@techcorp.com",
    "user_name": "Caio Gabriel"

  }
]

```

<br>

### Obter Papel por ID de Usuário <br>
### 🟢📥GET <br>
#### /api/role_by_user_id/<int:user_id><br>
#### Retorno:

```
{

  "user_id": 1,
  "user_name": "Caio Gabriel",
  "role": 2,
  "role_description": "Admin"

}

```


### Criar Usuário <br>
### POST 🟡📤 POST <br>
#### /api/create_user <br>


```
{

  "name": "Caio Gabriel",
  "email": "caio.gabriel@techcorp.com",
  "role_id": 2

},

{

  "name": "Luiza Amorin",
  "email": "luizaamorin@techcorp.com",
  "role_id": 3,
  "password": "SenhaLuiza123" -> Senha opcional!

}

```


