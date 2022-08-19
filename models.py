
from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column((db.String(20)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(500))
    looking_for_talent = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String(1000))

    @property
    def serailize(self):
        return {
            'id':self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address
        }