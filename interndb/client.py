from pymongo import MongoClient
from os import environ
client: dict = MongoClient(environ['mongodb'])

def get_certain(name: str):
  return client[name][name]
