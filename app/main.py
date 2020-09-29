from enum import Enum
from typing import Optional
from pydantic import BaseModel
from subprocess import run, PIPE
from fastapi import FastAPI, Response, status, Query, Form
import mysql.connector


app = FastAPI()

d_host = 'db'
d_database = 'newdb'
d_port = '3306'
d_username = 'root'
d_password = 'my-secret-pw'
                                   
class UserIn(BaseModel):
    username: int
    password: str
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: int
    full_name: Optional[str] = None

@app.get("/test_user/{user_id}")
async def save_user(username: int, password: str):
    conn = mysql.connector.connect(host=d_host,
                                   user=d_username,
                                   password=d_password,
                                   database=d_database)
    cursor = conn.cursor(buffered=True)
    SQL_insert = "INSERT INTO user_id (userid, password) VALUES ({},{});".format(username, password)
    cursor.execute(SQL_insert)
    SQL_get = "SELECT * FROM user_id WHERE userid = {}".format(username)
    cursor.execute(SQL_get)
    c = cursor.fetchone()
    cursor.close()
    conn.close()
    return "changed"
    
@app.get('/testUserLogin')
async def login_user(username: int, password:str):
    conn = mysql.connector.connect(host=d_host,
                                   user=d_username,
                                   password=d_password,
                                   database=d_database)
    cursor = conn.cursor(buffered=True)
    cursor.execute('select * from user_id;')
    c = cursor.fetchall()
    cursor.close()
    conn.close()
    return c

@app.get("/longprocess/{long_process}")
async def print_longprocess(process: str):
    command = process.split(" ") 
    run(command, shell=True)
    process = run(command, stdout=PIPE)
    process = process.stdout.decode()
    return process



