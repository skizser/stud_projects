from datetime import datetime
from app import db 

class Competition(db.Model):  # таблица Соревнования
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    place = db.Column(db.String(200), nullable=False)
    timeplace = db.Column(db.INT, nullable=False)
    competitiondetail = db.relationship('CompetitionDetail', backref=db.backref('competition'), lazy='dynamic')

    def __repr__(self):
        return '<Competition %r>' % self.id


class Horses(db.Model):  # таблица Лошади
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.INT, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    competitiondetail = db.relationship('CompetitionDetail', backref=db.backref('horses'), lazy='dynamic')


    def __repr__(self):
        return '<Horses %r>' % self.id


class Jockeys(db.Model):   # таблица Жокеи
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.INT, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    rating = db.Column(db.String(200), nullable=False)
    competitiondetail = db.relationship('CompetitionDetail', backref=db.backref('jockeys'), lazy='dynamic')

    def __repr__(self):
        return '<Jockeys %r>' % self.name


class Owners(db.Model):   # таблица Владельцы
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.INT, nullable=False)
    horses = db.relationship('Horses', backref=db.backref('owners'), lazy='dynamic')

    def __repr__(self):
        return '<Owners %r>' % self.id


class CompetitionDetail(db.Model): #таблица связей
    id = db.Column(db.Integer, primary_key=True)
    id_jockey = db.Column(db.Integer, db.ForeignKey('jockeys.id'))
    id_horse = db.Column(db.Integer, db.ForeignKey('horses.id'))
    id_competition = db.Column(db.Integer, db.ForeignKey('competition.id'))
    winner_place = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<CompetitionDetail %r>' % self.id