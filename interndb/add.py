from .client import get_certain
def add(id: int, to_add: dict, categorie: str) -> None:
  db = get_certain(categorie)
  to_add['_id']: int = id
  try:
    db.insert_one(to_add)
  except:
    db.update_one({'_id': id},{'$set': to_add})
  return None
