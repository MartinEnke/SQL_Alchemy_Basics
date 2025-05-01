from setup_database import session, Base, engine
from models import User


# this creates tables in the database
Base.metadata.create_all(engine)


# Add User
def add_user(name, email):
    new_user = User(name=name, email=email)

    session.add(new_user)
    session.commit() # save
    print("User added")


def delete_user(id):
    # Query the user by id
    user_to_delete = session.query(User).filter_by(id=id).one()  # Fetch the user by id

    if user_to_delete:
        session.delete(user_to_delete)  # Delete the fetched user
        session.commit()  # Commit the transaction
        print("User deleted")
    else:
        print(f"User with id {id} not found")


def update_user(name, new_email):
    user_to_update = session.query(User).filter_by(name=name).first()

    if user_to_update:
        user_to_update.email = new_email
        session.commit()
        print(f"User {user_to_update.name}'s email updated to {new_email}")


def show_all_users():
    users = session.query(User).all()
    if users:
        for user in users:
            print(f"User {user.id}: {user.name}, {user.email}")
    else:
        print("No users found")


#add_user("Joey", "joey@gmail.com")
#delete_user(2)
update_user("David", "david@gmail.com")

show_all_users()



'''first(), all(), or one():
first(): If you expect one or no result (which is common when querying by a unique id), 
first() fetches the first result or returns None if no user is found. 
It's safe if you're not sure whether there will be a matching record.

all(): If you want to fetch all records matching the query, 
all() will return a list of all matching users. 
However, for deleting a single user by id, this is not necessary, 
because you expect only one user for that id.

one(): If you're sure that there should only be exactly one record matching the query,
one() will return that user or raise an exception if there are no results or more than one result.
'''