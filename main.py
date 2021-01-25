import urllib
import os

host_server = os.environ.get('host_server', 'localhost')
database_name = os.environ.get('database_name', 'fastapi')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'root')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', '')))
DATABASE_URL = 'mysql://{}:{}@{}/{}'.format(db_username,db_password, host_server, database_name)

# Importing pymysql and accessing cursors
import pymysql.cursors
# Creating a connection with mysql
# connection = pymysql.connect(
#     host = "localhost",
#     user = "root",
#     database = "fastapi",
#     cursorclass=pymysql.cursors.DictCursor)
# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)

# importing sqlalchemy in order to write easier database code / expressions
import sqlalchemy

metadata = sqlalchemy.MetaData()

# Creating a table using sqlalchemy
notes = sqlalchemy.Table(
    "notes",
    metadata,
    # Creating a column...
    sqlalchemy.column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.column("text", sqlalchemy.String),
    sqlalchemy.column("completed", sqlalchemy.Boolean),
)

#Setting up the sqlalchemy engine
engine = sqlalchemy.create_engine(DATABASE_URL,encoding='latin1', echo=True)
