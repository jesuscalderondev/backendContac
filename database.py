from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Boolean, Date, Time, Column, or_, and_, Uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from uuid import uuid4
import psycopg2
from os import getenv
from dotenv import load_dotenv

hostname = getenv('HOSTNAME')
db = getenv('DATABASE')
user = getenv('USER')
password = getenv('PASSWORD')
port = getenv('PORT')

engine = create_engine(f'postgresql://{user}:{password}@{hostname}:{port}/{db}')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Uuid, primary_key=True, default=uuid4())
    email = Column(String(225), nullable=False)
    username = Column(String(17), nullable=False)
    password = Column(String(20), nullable=False)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password