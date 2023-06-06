from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'remote'
app.config['MYSQL_DATABASE_PASSWORD'] = 'dev123'
app.config['MYSQL_DATABASE_DB'] = 'db_crud'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)