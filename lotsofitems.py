from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Hardware_Category, Hardware_Item, User


engine = create_engine('sqlite:///hardwarestorecatalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
#adding users
User1 = User(name="Shule Fukuhara", email="swftwinsy@gmail.com",
             picture='user1.jpg')
session.add(User1)
session.commit()

User2 = User(name="Marina Urrutia", email="murrutia.aws@gmail.com",
                 picture='user2.jpg')
session.add(User2)
session.commit()


# First Category "Building Materials"
category1 = Hardware_Category(user_id=1,name="Building Materials", description="Within this category you will find all materials necesary to build walls and fences.")
session.add(category1)
session.commit()

#Items in category Building Materials
Item1 = Hardware_Item(user_id=1,name="Concrete Mix", description="dries completely within 24 hours, ideal for patios and walkways. 40 lbs", price="$24.47",category=category1)
session.add(Item1)
session.commit()


Item2 = Hardware_Item(user_id=1,name="Drywall Panel", description="Gypsum patcing panel drywall, Small design is ideal for lightweight repair jobs.",price="$4.98", category=category1)
session.add(Item2)
session.commit()

Item3 = Hardware_Item(user_id=1,name="Bricks", description="Flat bricks , box of 50 units, dimmensions: 2 x 7 x 1/2",price="$68.00", category=category1)
session.add(Item3)
session.commit()

#Second Category Bath and Faucets

category2 = Hardware_Category(user_id=2,name="Bath and Faucets", description ="within this category you will find all items necesary for the average bathroom")
session.add(category2)
session.commit()

Item1 = Hardware_Item(user_id=2,name="Faucet", description="single hole bathroom faucet in chrome.",price="$89.00", category=category2)
session.add(Item1)
session.commit()

Item2 = Hardware_Item(user_id=2,name="Bathtub", description="everyday bathtub , Acrylic Bath and Shower kit with Left Drain in White.",price="$379.00", category=category2)
session.add(Item2)
session.commit()

Item3 = Hardware_Item(user_id=2,name="Sink", description="Pedestal Combo Bathromm Sink in white.",price="$144.00", category=category2)
session.add(Item3)
session.commit()

#Third Category Electrical
category3 = Hardware_Category(user_id=1,name="Electrical", description ="withing this category you will find all items necesary to all electrical installations necesary for a home.")
session.add(category3)
session.commit()

Item1 = Hardware_Item(user_id=1,name="Lightbulb", description="Watt equivalent spiral non-dimmaable CFL light Bulb soft white . 4 pack",price="$5.97", category=category3)
session.add(Item1)
session.commit()

Item2 = Hardware_Item(user_id=1,name="Wire", description="250ft 14/2 solid romex simpull cu W/G wire",price="$45.97", category=category3)
session.add(Item2)
session.commit()

Item3 = Hardware_Item(user_id=1,name="Electrical Pliers", description="combination electricians wire strippers.",price="$24.97", category=category3)
session.add(Item3)
session.commit()


#Fourth category Flooring
category4 = Hardware_Category(user_id=1,name="Flooring", description ="In this category you will find all necesary items to install and accessories the floor of your home.")
session.add(category4)
session.commit()

Item1 = Hardware_Item(user_id=1,name="Tile", description="Bengal Brown 11.77 in x 11.57 in x 8 nn Stone. Self- Adhesive Wall Mosaic.",price="$13.66", category=category4)
session.add(Item1)
session.commit()

Item2 = Hardware_Item(user_id=1,name="Rug", description="Asha gray 9 ft. x 13 ft. Area Rug.",price="$39.98", category=category4)
session.add(Item2)
session.commit()

Item3 = Hardware_Item(user_id=1,name="Hardware Flooring", description="Hickory Heritage Grey Hand Sculputed 3/4 in thick x4 in Wide x Randon Lenght Solid Hardwood. ",price="$5.99", category=category4)

session.add(Item3)
session.commit()


print "added items by categories!"
