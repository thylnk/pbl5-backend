from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Calories(db.Model):
  id=db.Column(db.Integer, primary_key=True, autoincrement=True)
  name=db.Column(db.Text, nullable=False)
  calories=db.Column(db.Float, nullable=False)
  name1=db.Column(db.Text)
  def __repr__(self):
    return f'<Calories id: {self.id} name: {self.name} calories: {self.calories} name1:{self.name1}  >'

