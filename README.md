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

# Buscar fuentes css de Google

1.- Ir a Google Fonts
2.- Buscar o elegir la fuente, en este caso "Raleway"
3.- En este caso elegí las fuentes: Regular 400, SemiBold 600
4.- Copiar los links generados y pegarlos en el css debajo del link del css y encima del título
5.- Para que aparezca la fuente, se tiene que indicar en el .css
font-family: 'Raleway', sans-serif;

# Enviar correos con SendGrid

https://sendgrid.com
pendiente...

# Hacer deploy en Heroku

https://www.heroku.com

Crearemos toda la app y todo desde la línea de comandos, no desde el panel de heroku

1.- buscar heroku install cli:
2.- descargar el instalador para 64 bits
3.- asegurarse de tener todo en git y actualizado
4.- crear .gitignore para ignorar: variables de entorno ".env", entorno virtual "venv/",
archivos \*.pyc, carpeta **pycache**, instance/
5.- en la consola, en la ruta, escribir: heroku create
6.- agregar plugin gratis de heroku para basededatos
heroku addons:create cleardb:ignite
7.- ver variables de entorno de la app en heroku
heroku config
8.- Setear variables de entorno:

la llave generada por CLEARDB_DATABASE_URL no se la tengo que pasar a nadie, pero en este caso las dejaré en el ReadME pues porque no importa esta base de datos.

heroku config
» Warning: heroku update available from 7.53.0 to 7.60.2.
=== stormy-tundra-09756 Config Vars
CLEARDB_DATABASE_URL: mysql://b494dc1005e67e:9f49634f@us-cdbr-east-06.cleardb.net/heroku_85e94c1bd6c9ec5?reconnect=true

heroku config:set FLASK_DATABASE_USER=b494dc1005e67e
heroku config:set FLASK_DATABASE=heroku_85e94c1bd6c9ec5
heroku config:set FLASK_DATABASE_PASSWORD=9f49634f
heroku config:set FLASK_DATABASE_HOST=us-cdbr-east-06.cleardb.net/
heroku config:set FROM_EMAIL=codejohan@gmail.com
(pendiente) heroku config:set SENDGRID_API_KEY=

(((( comando desde consola para cambiar el nombre a la app))))
heroku apps:rename newname

9.- pip install gunicorn (paquete para poder tomar la app y levantar un server y que se quede escuchando aún si la app llega a fracasar o generar un error en el runtime)
10.- ejecutar los siguientes comandos:
pip freeze > requirements.txt
echo "web: flask init-db; gunicorn mailer: 'create_app()'" > Procfile

11.- configurar 2 vars de entorno más
heroku config:set FLASK_APP=mailer
heroku config:set SECRET_KEY='millavesecreta'

12.- agregar los 2 nuevos archivos "Procfile" y "requirements.txt" al repo
git add .
git commit -m "Últimos cambios para primer push a Heroku"
git push
git push heroku main
