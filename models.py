from sqlalchemy import Column, Integer, String
from setup_database import Base


# Define a class that represents a table in the database
# The class will inherit from Base, which connects it to the database's table-mapping system
class User(Base):
    # Define the name of the table in the database
    __tablename__ = 'users'

    # Define the columns in the 'users' table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)




