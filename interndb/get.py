from .client import get_certain
def get_one(id: int, categorie: str):
  return get_certain(categorie).find_one({"_id": id})
