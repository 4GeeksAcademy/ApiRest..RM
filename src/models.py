from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favorite_characters = db.relationship('Favorite_Characters', backref='user', lazy=True)
    favorite_planets = db.relationship('Favorite_Planets', backref='user', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
        }

class Characters(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    favorite_characters = db.relationship('Favorite_Characters', backref='characters', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color
        }

class Planets(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    diameter = db.Column(db.String(250), nullable=False)
    rotation_period = db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.String(250), nullable=False)
    residents = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    favorite_planets = db.relationship('Favorite_Planets', backref='planets', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "residents": self.residents,
            "films": self.films
        }

class Favorite_Characters(db.Model):
    __tablename__ = "favorite_characters"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }


class Favorite_Planets(db.Model):
    __tablename__ = "favorite_planets"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }


