from typing import Optional
from enum import Enum

from fastapi import FastAPI, Response, status, Query, Form
from pydantic import BaseModel

from subprocess import run, PIPE

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    full_name: Optional[str] = None

#FastApi will take care of filtering out all the data that
#is not declared in 
@app.post("/user/", response_model=UserOut, status_code=200)
async def create_user(user: UserIn):
    #run(["ls", "-lha"], shell=True)
    script = "cat >newfile.txt ^C"
    script2 = "echo '%s-%s-' >newfile.txt" % (user.username, user.password)
    run(script, shell=True)
    run(script2, shell=True)
    print("hello")
    #run(["echo", "Some text here.", "> filetext.txt"], shell=True)
    return user

@app.get("/user/{user_id}")
async def login(username: str, password:str):
    script3 = "cat newfile.txt"
    process3 = run(script3, shell=True, stdout=PIPE)
    login_details = process3.stdout.decode()
    file_username = login_details.split("-")[0]
    file_password = login_details.split("-")[1]
    print(file_username)
    print(username)
    if username == file_username and password == file_password:
        return("Login details match")
    else:
        return("Login details do not match records")

@app.get("/longprocess/{long_process}")
async def print_longprocess(process: str):
    process_script = "for i in {1..1000000}\n do\n echo 'Welcome $i times'\n done"
    run(process_script, shell=True)
    return process
    
#@app.post("/login/")
#async def login(username: str = Form(...), password: str = Form(...)):
    #return {"username": username}

"""
@app.get("/command/{command_id}")
async def read_command(command_id: str, q: Optional[str]= Query(None,regex="^ls")):
    if command_id == "ls -lha":
        #run([command_id], shell=True)
        run("ls -lha", stderr=PIPE, stdout=PIPE, shell=True, universal_newlines = True)
        #output = pl.stdout
    return command_id

"""
