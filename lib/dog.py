from models import Dog
from sqlalchemy import (
    create_engine,
    desc,
    func,
    CheckConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint,
    Index,
    Column,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


def create_table(base, engine):
    base.metadata.create_all(engine)


def save(session, dog):
    session.add(dog)
    session.commit()


def get_all(session):
    dog = session.query(Dog).all()
    return dog


def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()
    return query


def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).first()
    return query


def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter((Dog.name == name) & (Dog.breed == breed)).first()
    return query


def update_breed(session, dog, breed):
    update = session.query(Dog).filter(Dog.breed).update({Dog.breed: breed})
    return update