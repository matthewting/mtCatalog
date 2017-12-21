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
user = session.query(User).delete()
category = session.query(Category).delete()
item = session.query(Item).delete()
session.commit()

# Soccer, id = 1
category = Category(name="Soccer", id=1)
session.add(category)
session.commit()

item = Item(id=1, added_by_user_id=1,title="Soccer Cleats", description="", added_on=datetime.datetime.utcnow(), category_id=1)
session.add(item)

item = Item(id=2, added_by_user_id=1,title="Jersey", description="", added_on=datetime.datetime.utcnow(), category_id=1)
session.add(item)

session.commit()

# Basketball , id = 2 
category = Category(name="Basketball", id=2)
session.add(category)
session.commit()

# Baseball , id = 3
category = Category(name="Baseball", id=3)
session.add(category)
session.commit()

item = Item(id=3, added_by_user_id=1,title="Bat", description="", added_on=datetime.datetime.utcnow(), category_id=3)
session.add(item)
session.commit()

# Frisbee , id = 4
category = Category(name="Frisbee", id=4)
session.add(category)
session.commit()

item = Item(id=4, added_by_user_id=1,title="Frisbee", description="", added_on=datetime.datetime.utcnow(), category_id=4)
session.add(item)
session.commit()

# Soccer item 3 and item 4
item = Item(id=5, added_by_user_id=1,title="Shinguards", description="", added_on=datetime.datetime.utcnow(), category_id=1)
session.add(item)

item = Item(id=6, added_by_user_id=1,title="Two shinguards", description="", added_on=datetime.datetime.utcnow(), category_id=1)
session.add(item)

session.commit()

# Snowboarding , id = 5 
category = Category(name="Snowboarding", id=5)
session.add(category)
session.commit()

item = Item(id=7, added_by_user_id=1,title="Snowboard", description="Best for any terrain and conditions. All-mountain snowboards perform anywhere on a mountain -- groomed runs, backcountry, even park and pipe. They may be directional (meaning downhill only) or twin-tip (for riding switch, meaning either direction). Most boarders ride all-mountain boards. Because of their versatillity, all-mountain boards are good for beginners who are still learning what terrain they like.", added_on=datetime.datetime.utcnow(), category_id=5)
session.add(item)
session.commit()

item = Item(id=8, added_by_user_id=1,title="Goggles", description="", added_on=datetime.datetime.utcnow(), category_id=5)
session.add(item)
session.commit()

# Rock Climbing , id = 6
category = Category(name="Rock Climbing", id=6)
session.add(category)
session.commit()

# Foosball , id = 7 
category = Category(name="Foosball", id=7)
session.add(category)
session.commit()

# Skating , id = 8
category = Category(name="Skating", id=8)
session.add(category)
session.commit()

# Hockey , id = 9
category = Category(name="Hockey", id=9)
session.add(category)
session.commit()



print "Manually inserted Items!"
