# Sistema de Gerenciamento de Clínica Médica

## Sobre o projeto

Este projeto é uma **API RESTful para gerenciamento de uma clínica médica**.

A proposta é permitir o cadastro e gerenciamento de:

- Especialidades médicas
- Médicos
- Pacientes
- Consultas

### Entidades previstas

#### Especialidade
Representa as áreas médicas da clínica.

Campos:
- `id`
- `nome`
- `descricao`

#### Médico
Representa os médicos da clínica.

Campos:
- `id`
- `nome`
- `crm`
- `telefone`
- `especialidade`

Relacionamento: uma `Especialidade` pode possuir vários `Médicos` (1:N).

#### Paciente
Representa as pessoas que realizam consultas na clínica.

Campos:
- `id`
- `nome`
- `cpf`
- `data_nascimento`
- `telefone`

#### Consulta
Representa o agendamento entre um médico e um paciente.

Campos:
- `id`
- `medico`
- `paciente`
- `data_hora`
- `observacoes`
- `status`

Status previstos:
- `Agendada`
- `Concluída`
- `Cancelada`

---

## Tecnologias

- Python
- Django
- Django REST Framework
- django-filter
- python-dotenv
- SQLite para desenvolvimento

---

## O que foi desenvolvido até o momento

Foram implementadas as entidades **Especialidade**, **Paciente** e **Medico**.

Apenas a Consulta continua prevista.

### Model

```python
class Especialidade(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
    )
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
```

### Unicidade do nome

O campo `nome` utiliza `unique=True`, impedindo que duas especialidades tenham o mesmo nome no banco.

Exemplo:

```text
Cardiologia → permitido
Cardiologia → não permitido
```

### Regra de negócio da descrição

Foi criado um `EspecialidadeService`.

A regra implementada é:

> A descrição da especialidade deve possuir mais de 5 caracteres.

Exemplo inválido:

```json
{
    "nome": "Cardiologia",
    "descricao": "E."
}
```

Exemplo válido:

```json
{
    "nome": "Cardiologia",
    "descricao": "Especialidade do coração"
}
```

### Filtro por nome

Foi criado um filtro com `django-filter` para pesquisar especialidades pelo nome.

Exemplo:

```http
GET /api/especialidades/?nome=cardio
```

O filtro utiliza `icontains`, permitindo pesquisar por parte do nome sem diferenciar maiúsculas e minúsculas.

### Paciente

```python
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(
        max_length=11,
        unique=True
    )
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
```

### Unicidade do CPF

O campo `cpf` utiliza `unique=True`, impedindo que dois pacientes tenham o mesmo CPF no banco.

Exemplo:

```text
12345678901 → permitido
12345678901 → não permitido
```

### Regras de negócio do paciente

Foi criado um `PacienteService`.

As regras são aplicadas na criação (`POST`) e na atualização (`PUT` e `PATCH`):

> O CPF deve conter exatamente 11 dígitos numéricos.

> A data de nascimento deve ser anterior a hoje.

Exemplo inválido:

```json
{
    "nome": "Ana Souza",
    "cpf": "123.456.789-01",
    "data_nascimento": "1990-05-10",
    "telefone": "11999999999"
}
```

```json
{
    "nome": "Ana Souza",
    "cpf": "12345678901",
    "data_nascimento": "2099-01-01",
    "telefone": "11999999999"
}
```

Exemplo válido:

```json
{
    "nome": "Ana Souza",
    "cpf": "12345678901",
    "data_nascimento": "1990-05-10",
    "telefone": "11999999999"
}
```

### Filtro por nome do paciente

Foi criado um filtro com `django-filter` para pesquisar pacientes pelo nome.

Exemplo:

```http
GET /api/pacientes/?nome=ana
```

O filtro utiliza `icontains`, permitindo pesquisar por parte do nome sem diferenciar maiúsculas e minúsculas.

### Medico

```python
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(
        max_length=20,
        unique=True
    )
    telefone = models.CharField(max_length=20)
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.CASCADE,
        related_name='medicos'
    )

    def __str__(self):
        return f"{self.nome} - {self.crm}"
```

### Unidade do CRM
O campo crm utiliza **unique=True**, garantindo que não existam dois médicos cadastrados com o mesmo CRM.

### Regras de negócio do médico

Foi criado um `MedicoService`.

As regras são aplicadas na criação (`POST`) e na atualização (`PUT` e `PATCH`):

> O campo CRM é obrigatório e não pode estar vazio..

> O telefone deve possuir pelo menos 8 dígitos.

Exemplo inválido:

```json
{
    "nome": "Carlos",
    "crm": "123456",
    "telefone": "12345",
    "especialidade": 1
}
```

Exemplo válido:

```json
{
    "nome": "Carlos",
    "crm": "123456",
    "telefone": "41999998888",
    "especialidade": 1
}
```

### Personalização de resposta no Serializer

O `MedicoSerializer` sobrescreve o método `to_representation()` para melhorar a exibição dos dados:


> No envio de dados (POST ou PUT), aceita o id numérico da chave estrangeira da especialidade.

> Na resposta de leitura (GET), substitui o ID numérico pelo nome da especialidade vinculada.

Exemplo de retorno JSON:

```json
{
    "id": 1,
    "nome": "Dr. Carlos",
    "crm": "123456",
    "telefone": "41999998888",
    "especialidade": "Cardiologia"
}
```

### Filtro por nome da especialidade, nome do médico e CRM

Foi criado o `MedicoFilter` utilizando `django-filter`. A busca por especialidade navega pela chave estrangeira **(especialidade__nome)**, permitindo filtrar médicos diretamente pelo nome da especialidade médica.

Exemplos:

```HTTP
GET /api/medicos/?especialidade=cardio
GET /api/medicos/?nome=carlos
GET /api/medicos/?crm=123456
```
---

# Como executar o projeto do zero

## 1. Clonar o projeto

```powershell
git clone URL_DO_REPOSITORIO
cd projeto-django
```

## 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ative no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Atualizar o pip

```powershell
python -m pip install --upgrade pip
```

## 4. Instalar as dependências

```powershell
pip install -r requirements.txt
```

Caso ainda não exista `requirements.txt`:

```powershell
pip install django djangorestframework python-dotenv django-filter
```

## 5. Criar o `.env`

Na raiz do projeto:

```env
DEBUG=True
SECRET_KEY=django-insecure-chave-de-desenvolvimento
```

## 6. Verificar o projeto

```powershell
python manage.py check
```

Resultado esperado:

```text
System check identified no issues (0 silenced).
```

## 7. Criar e aplicar migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

O Django criará o banco SQLite `db.sqlite3`.

## 8. Executar

```powershell
python manage.py runserver
```

Servidor:

```text
http://127.0.0.1:8000/
```

API de especialidades:

```text
http://127.0.0.1:8000/api/especialidades/
```

API de pacientes:

```text
http://127.0.0.1:8000/api/pacientes/
```

API de medicos:

```text
http://127.0.0.1:8000/api/medicos/
```

---

# Testando a API

## Listar

```http
GET /api/especialidades/
```

## Buscar por ID

```http
GET /api/especialidades/1/
```

## Criar

```http
POST /api/especialidades/
```

```json
{
    "nome": "Cardiologia",
    "descricao": "Especialidade do coração"
}
```

## PUT

```http
PUT /api/especialidades/1/
```

```json
{
    "nome": "Cardiologia",
    "descricao": "Diagnóstico e tratamento de doenças do coração."
}
```

O `PUT` representa uma atualização completa.

## PATCH

```http
PATCH /api/especialidades/1/
```

```json
{
    "descricao": "Especialidade do sistema cardiovascular."
}
```

O `PATCH` permite uma atualização parcial.

## DELETE

```http
DELETE /api/especialidades/1/
```

## Filtrar por nome

```http
GET /api/especialidades/?nome=cardio
```

# Testando pacientes

## Listar

```http
GET /api/pacientes/
```

## Buscar por ID

```http
GET /api/pacientes/1/
```

## Criar

```http
POST /api/pacientes/
```

```json
{
    "nome": "Ana Souza",
    "cpf": "12345678901",
    "data_nascimento": "1990-05-10",
    "telefone": "11999999999"
}
```

## PUT

```http
PUT /api/pacientes/1/
```

```json
{
    "nome": "Ana Souza",
    "cpf": "12345678901",
    "data_nascimento": "1990-05-10",
    "telefone": "11988887777"
}
```

O `PUT` representa uma atualização completa. As regras de CPF e data de nascimento também são validadas.

## PATCH

```http
PATCH /api/pacientes/1/
```

```json
{
    "telefone": "11977776666"
}
```

O `PATCH` permite uma atualização parcial. Se `cpf` ou `data_nascimento` forem enviados, as mesmas regras são aplicadas.

## DELETE

```http
DELETE /api/pacientes/1/
```

## Filtrar por nome

```http
GET /api/pacientes/?nome=ana
```

# Testando medicos

## Listar

```http
GET /api/medicos/
```

## Buscar por ID

```http
GET /api/medicos/1/
```

## Criar

```http
POST /api/medicos/
```

```json
{
    "nome": "Carlos Eduardo",
    "crm": "123456",
    "telefone": "41999998888",
    "especialidade": 1
}
```

## PUT

```http
PUT /api/medicos/1/
```

```json
{
    "nome": "Carlos Eduardo Silva",
    "crm": "123456",
    "telefone": "41988887777",
    "especialidade": 1
}
```

O `PUT` representa uma atualização completa.

## PATCH

```http
PATCH /api/medicos/1/
```

```json
{
    "telefone": "41977776666"
}
```

O `PATCH` permite uma atualização parcial.

## DELETE

```http
DELETE /api/medicos/1/
```

## Filtrar por nome

```http
GET /api/medicos/?nome=carlos
```

## Filtrar por CRM

```http
GET /api/medicos/?crm=123456
```

## Filtrar por especialidade

```http
GET /api/medicos/?especialidade=cardiologia
```

---

# Arquitetura

O fluxo principal da aplicação é:

```text
Requisição HTTP
      ↓
URL / Router
      ↓
ViewSet
      ↓
Serializer
      ↓
Service
      ↓
Model / Banco de dados
```

### Model
Representa os dados e a estrutura das tabelas.

### Serializer
Responsável pela conversão e validação dos dados da API.

### ViewSet
Recebe as requisições HTTP e coordena as operações.

### Service
Concentra regras de negócio.

### Filter
Responsável pelos filtros de consulta da API.

---

# Estrutura atual

```text
projeto-django/
│
├── api/
│   ├── migrations/
│   ├── filters.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── db.sqlite3
```



