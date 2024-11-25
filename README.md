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

### **🆕 Criação de Usuários:**  
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

### 📋✅ Pré-requisitos

- Python 3.7  
- PostgreSQL  
- Ambiente virtual configurado (venv)  
- Ferramenta de gerenciamento do banco de dados (DBeaver, DBvisualizer, etc)

  <br>

### ➡️ Passos

1. **🌀📂 Clone o repositório:**

    ```bash
    
    git clone <URL_DO_PROJETO>
    
    cd <NOME_DO_PROJETO>
    
    ```
    <br>

2. **🆕 Crie o ambiente virtual:**

    ```bash
    
    python -m venv .venv
    source .venv/bin/activate  # Linux ou Mac
    .venv\Scripts\activate     # Windows
    
    ```
    <br>

3. **🛠️ Instale as dependências:**

    ```bash
    
    pip install -r requirements.txt
    
    ```
    <br>

4. **⚙️ Configure o arquivo `.env`:**

    Crie ou edite o arquivo `.env` com as seguintes variáveis:

    ```env
    DB_HOST=<SEU_HOST>
    DB_PORT=5432
    DB_USER=<SEU_USUARIO>
    DB_PASSWORD=<SUA_SENHA>
    DB_NAME=<SEU_DATABASE>
    ```
<br>

5. **💾 Inicie o banco de dados:** <br><br>

   **Certifique-se de que o PostgreSQL está em execução e as tabelas foram criadas.** 
                                                                                      <br><br> 
   ##### **OBS: A ferramenta TEMBO é utilizada para manter o banco de dados ativo**            
                                                                                              
   ##### **com isso, foi construído em ambiente de desenvolvimento do desenvolvedor deste**    
                                                                                              
   ##### **projeto, com isso, será necessário configurar um novo ou entrar em contato para**   
                                                                                              
   ##### **que seja disponibilizado**                                                 
<br><br>
   
## ▶️🚀 Execute a aplicação:<br>

```
python app.py

```
<br>

## 🔑 Acesse a aplicação em:

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

<br><br>

## 🚀 Deploy para Produção <br>

### 🛠️ Requisitos <br>

Antes de iniciar o deploy, certifique-se de que possui: <br>

- Conta na AWS para criar e configurar um **S3 Bucket**.  
- Conta no **Render** (ou **Railway**).  
- Banco de dados configurado e hospedado (sugestão: AWS RDS ou o próprio PostgreSQL do Render/Railway).  
- Arquivo `.env` configurado com as credenciais necessárias.  


<br>

### ☁️🌐 Deploy da API no Render <br>

1. **Crie um novo serviço no Render:** <br>
   - Acesse [Render](https://render.com).
   - Crie um novo serviço **Web Service** e conecte o repositório do seu projeto (GitHub ou GitLab).

<br>

2. **Configure as variáveis de ambiente:** <br>
   - No painel de configurações do Render, adicione as variáveis do seu arquivo `.env`.

<br>

3. **Adicione um arquivo `start` no `requirements.txt`:** <br>
   - Inclua o Gunicorn para servir sua aplicação em produção:
     ```plaintext
     gunicorn==20.1.0
     ```
   - Crie um arquivo `Procfile` no projeto com o comando para iniciar a aplicação:
     ```plaintext
     web: gunicorn app:app
     ```

<br>

4. **Deploy:**
   - O Render automaticamente detectará as configurações e realizará o deploy.
   - Após o deploy, você terá uma URL pública para acessar sua API.

---

<br>

### 🗂️🪣 Configuração do AWS S3 <br>

1. **Crie um Bucket no S3:**
   - Acesse o console AWS e crie um bucket no S3 para armazenar arquivos ou dados estáticos.
   - Configure permissões de leitura/gravação.

<br>

2. **Integre o S3 no projeto:**
   - Instale o `boto3` para interagir com o S3:

<br>


     pip install boto3
     

     
<br>


   - Configure as credenciais do S3 no seu arquivo `.env`:
     ```
     
     AWS_ACCESS_KEY_ID=<SUA_CHAVE_DE_ACESSO>
     AWS_SECRET_ACCESS_KEY=<SUA_CHAVE_SECRETA>
     S3_BUCKET_NAME=<SEU_BUCKET>
     
     ```

<br>
     
   - Exemplo de código para enviar arquivos ao S3:
     ```
     import boto3

     s3 = boto3.client('s3')
     bucket_name = "SEU_BUCKET"

     def upload_file_to_s3(file_path, s3_key):
         s3.upload_file(file_path, bucket_name, s3_key)
     ```

<br>

### ✅ Teste Final <br>

1. **Teste a API:**  
   - Utilize ferramentas como **Insomnia** ou **Postman** para validar os endpoints da sua API.

<br>


2. **Teste o S3:**

   - Envie um arquivo ao bucket usando a integração no código e verifique se ele foi armazenado corretamente.



