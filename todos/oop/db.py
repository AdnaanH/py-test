# db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine('sqlite:///todo.db')  # Same DB file
Session = sessionmaker(bind=engine)

# Create tables if not exist
Base.metadata.create_all(engine)
