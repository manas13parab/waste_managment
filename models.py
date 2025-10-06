from waste_managment.extensions import db

class Restaurant(db.Model):
    """
    Represents a restaurant entity with an ID and name.

    Attributes:
        id (int): Primary key for the restaurant.
        name (str): Name of the restaurant, cannot be null.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.name}>'
