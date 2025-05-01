# Basic Setup - (can be done in different ways, but this is a common approach)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine that connects to the SQLite database file 'my_database.db'
engine = create_engine("sqlite:///my_database.db")

# Create a session that allows us to interact with the database
# The session is used to execute SQL queries and manage transactions
Session = sessionmaker(bind=engine)
session = Session()

# The base class is used to define models (tables) that will be mapped to the database
Base = declarative_base()


