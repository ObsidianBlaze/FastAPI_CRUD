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

#Creating the table
metadata.create_all(engine)

#importing pydantic
from pydantic import BaseModel

class NoteIn(BaseModel):
    text: str
    completed: bool

#Response to an api call
class Note(BaseModel):
    id: int
    text: str
    completed: bool

#Imporing fastapi related modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Creating an instance of the fastapi
app = FastAPI(title="Rest Api using fastapi mysql async endpoints")
#adding cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# for async features, Import databases
import databases
database = databases.Database(DATABASE_URL)

# Connecting the database on start of the app.
@app.on_event("startup")
async def startup():
    await database.connect()

# disconnecting the database on shutdown of the app.
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

#adding notes.
@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text= note.text, completed = note.completed)
    # Get inserted record
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}