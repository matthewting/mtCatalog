from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

from models import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Clean up the whole table first
users = session.query(User).all()
items = session.query(Item).all()

print ("------------------users list---------------------")
for user in users:
    print ('user.id: {0}'.format(user.id))
    print ('user.username: {0}'.format(user.username))
    print ('user.emailAddress: {0}'.format(user.emailAddress))
    print ("--------------------------------------------------")

print ("------------------items list---------------------")
for item in items:
    print ('item.id: {0}'.format(item.id))
    print ('item.titleName: {0}'.format(item.title))
    print ('item.added_by_user_id: {0}'.format(item.added_by_user_id))
    print ("--------------------------------------------------")
# session.commit()


print "printed report above!"
