<h1 align ="center">Desafio 4Intelligence - Backend</h1>

<p align="center">

<img src="https://github.com/G-ilian/Desafio4Intelligence/blob/main/4intelligence-Logo.jpg" height="300" width="500" >
</p>
<p align="center">Figura 1 - Logo 4Intelligence</p>

<p>A aplicação em questão se trata de um web api, que é capaz de realizar um CRUD completo. Foi totalmente desenvolvida com Python e o framework escolhido para desenvolvimento foi o Django rest framework</p>

<p>O projeto foi desenvolvido para o desafio da 4Intelligence - Backend. </p>

### 💻 Funcionalidades
- Cadastrar fornecedores.
- Listar fornecedores.
- Atualizar dados de fornecedores.
- Deletar fornecedores.

### 🚀 Começando
Para obter uma cópia do projeto a fim de operá-lo/testá-lo em sua máquina,clone o repositório em uma pasta na sua máquina:
```
$ git clone https://github.com/G-ilian/Desafio4Intelligence
```
### 📋 Pré-requisitos para execução
- IDE para execução de códigos Python (ex: Visual Studio Code,PyCharm)
- Django
- Django Rest Framework

### 🔧 Instalação e execução
-Venv 
<p>Para uma melhor experiência ao executar a aplicação é recomendado a criação de um ambiente virtual (venv), que possibilitará isolar a aplicação e sua execução do nosso sistema operacional</p>
<p>Para a criação e ativação da venv siga os seguintes comandos: </p>
- Criação
<p>Obs: O nome da venv deve estar fora das aspas duplas</p> 

```
$ python -m venv "Nome da venv que você deseja criar"
```

- Ativação
Para windows(Lembrar sempre de verificar se está na raiz do projeto):

- Acessar a pasta venv

```
$ cd venv
```

- Acessar Scripts

```
$ cd Scripts
```

- Ativar a venv

```
$ activate
```

<p>
Posteriormente a esta ativação da venv volte até a pasta de origem de nome 'Desagio_Backend_4Intelligence'.Será necessário para isso executar o seguinte código por duas vezes:
</p>

```
$ cd ..
```

- Linux ou MacOS
```
$ source tutorial-env/bin/activate
```
**Preparação**
<p>Após termos feito a configuração e ativado nosso ambiente virtural, podemos então partir para a preparação para a execução do código</p>
<p>Para isto é necessário fazer a instalação do pré requisitos que permitem a execução, esta instalação pode ser feita através do comando no terminal</p>

```
$ pip install -r requirements.txt
```

### ⚙️ Executando os testes

<p>Após ter instalado todos os pré requisitos, podemos partir para a execução da API, para isto será necessário executar alguns comandos pelo terminal, estando na pasta raiz do projeto execute os seguinter códigos </p>

Inicialmente: 

```
$ python manage.py makemigrations
```
Logo em seguida:

```
$ python manage.py migrate
```

Por fim: 

```
$ python manage.py runserver
```

<p>Após este processo aparecerá então um link de um servidor, para testar a API podemos usar de nosso própio navegador, ou seja, pegamos o link gerado em nosso terminal colamos em um navegador qualquer e iniciamos nossos testes.</p>

:toolbox: Ferramentas

<p>A Web API desenvolvida tem como principal funcionalidade fazer um CRUD completo, para isto foram criados 4 endpoints, para cada uma dessas operações, estes podem ser acessados através das seguintes urls.</p>

:round_pushpin: Create
<p>Através deste metódo é possível criar um fornecedor, após a criação do mesmo bastar dar um POST, que ele já será incluído.</p>

```
$ 127.0.0.1:8000/create
```

:round_pushpin: Read
<p>Através deste metódo é possível listar todos os fornecedores que estão cadastrados.</p>

```
$ 127.0.0.1:8000/read
```

:round_pushpin: Update
<p>Através deste metódo é possível fazer a atualização de todos os campos, ou de somente um campo de um fornecedor. Lembrando que este metódo exige a presença do id do fornecedor específico do qual você deseja atualizar os dados.</p>

```
$ 127.0.0.1:8000/update/id
```

:round_pushpin: Delete 
<p>Através deste metódo é possível fazer a remoção de um usuário, tem o funcionamento análogo ao do Update, sendo necessário passar a id do fornecedor específico do qual você deseja deletar os dados.
</p>

```
$ 127.0.0.1:8000/delete/id
```

### 📦 Desenvolvimento
Devido a ser minha primeira experiência com API/Web APIS optei por deixar meus pacotes e pastas com as estruturas mais simplificadas o possível, bem como meus códigos de uma maneira mais simplificada. Portanto optei por organizar os arquivos da seguinte maneira:

📂 Desafio_Backend_4Intelligence/
    📂desafio_backend/
        📄_init_.py
        📄asgi.py
        📄settings.py
        📄urls.py
        📄wsgi.py

    📂Fornecedores/
            📂api/
               📄__init__.py
               📄serializers.py
               📄viewsets.py
            📂migrations/
               📄__init__.py 
        📄__init__.py
        📄admin.py
        📄apps.py
        📄models.py
        📄tests.py
        📄views.py


## ✒️ Autor

***Gabriel Ilian Fonseca Barboza** - [Gabriel](https://github.com/G-ilian)