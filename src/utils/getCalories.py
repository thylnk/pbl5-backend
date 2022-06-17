from src.database import Calories


def get_by_name(name):
  result = Calories.query.filter_by(name1=name).first()
  if result is not None: 
    return result
  return False
