from waste_managment.extensions import db


class Restaurant(db.Model):
    """Represents a restaurant entity with an ID and name."""

    id = db.Column(db.Integer, primary_key=True)
    # Use a single name column; 200 chars to be safe
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.name}>'
