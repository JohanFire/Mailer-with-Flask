# Mailer-with-Flask

In this proyect I will create a Mail service, where I will be able to send &amp; receive emails in my own Email WebSite. Also It will be deployed to Heroku.

# Creación del ambiente virtual:

Dentro de la carpeta Mailer
python -m venv venv

# Activar ambiente virtual:

. venv/Scripts/activate
agregará "(venv)" a la izquierda de la línea de comandos

# ver el nombre de las DB en MySQL

usando esta comando :
SHOW DATABASES

# USANDO GIT BASH (MEJOR OPCION QUE CMD):

7.-
ejecutar las variables de entorno en la consola para poder ejecutar el script
. venv/Scripts/activate

- export FLASK_APP=todo
- export FLASK_ENV=development
- export FLASK_DATABASE_HOST='localhost'
- export FLASK_DATABASE_PASSWORD='manageDByeah'
- export FLASK_DATABASE_USER='chanchitoManager'
- export FLASK_DATABASE=''
- flask init-db

tiene que imprimir: "Base de datos inicializada."

# Crear archivo ".env" y no compartirlo con nadie

crearlo en la ruta base "./"

e instalar el paquete pip:

- pip install python-dotenv

# Definiendo Blueprints:

ahora al hacer cambios y hacer reload en el navegador NO se muestran los cambios, ya que definimos variables de producción, en consola se muestra el siguiente error:
flask run

- Serving Flask app 'mailer' (lazy loading)
- Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.

Para arreglarlo hay que cambiar el env a development:

- export FLASK_ENV=development
  esto cambia el enviroment a development
