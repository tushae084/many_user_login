from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

db={
    "user_1": {
        "username": "user1",
        "fullname": "user1 user1",
        "email": "user1@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_2": {
        "username": "user2",
        "fullname": "user2 user1",
        "email": "user2@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_3": {
        "username": "user3",
        "fullname": "user3 user1",
        "email": "user3@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_4": {
        "username": "user4",
        "fullname": "user4 user1",
        "email": "user4@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_5": {
        "username": "user5",
        "fullname": "user5 user1",
        "email": "user5@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
      "user_6": {
        "username": "user6",
        "fullname": "user6 user1",
        "email": "user6@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_7": {
        "username": "user7",
        "fullname": "user7 user1",
        "email": "user7@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_8": {
        "username": "user8",
        "fullname": "user8 user1",
        "email": "user8@gmail.com",
        "hashed-password": "",
        "disabled": False
    },
     "user_9": {
        "username": "user9",
        "fullname": "user9 user1",
        "email": "user9@gmail.com",
        "hashed-password": "",
        "disabled": False
    }
}





class User(BaseModel):
    username : str
    email: str | None=None
    full_name: str | None=None
    disabled: bool| None=None