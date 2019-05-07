# Rodar Projeto Python no Windows

### Crie o virtual env
python -m venv .venv

### Crie o arquivo manage.bat
Crie na pasta .venv/Scripts com o conteúdo: <br>
python.exe "%VIRTUAL_ENV%\..\manage.py" %*

### Ative o virtual env
.venv/Scripts/activate.bat

### Instale os requirements
pip install -r requirements.txt

### Faça as migrações
manage makemigrations <br>
manage migrate

### Rode o projeto
manage runserver
