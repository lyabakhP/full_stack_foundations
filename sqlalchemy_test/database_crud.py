from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///FullStackFoundations/restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def getFromDB():
    restaurants = session.query(Restaurant).all()
    menuse = session.query(MenuItem).all()
    for restaurant in restaurants:
        print('Restaurant: {}'.format(restaurant.name))

    for menu in menuse:
        print('Menu: {}'.format(menu.name))

# getFromDB()

def updateDB():
    veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
    for veggieBurger in veggieBurgers:
        print('id: {}'.format(veggieBurger.id))
        print('price: {}'.format(veggieBurger.price))
        print('restaurant: {}'.format(veggieBurger.restaurant.name))
        print('\n')

# updateDB()

# getById = session.query(MenuItem).filter_by(id=1).one()
# print(getById.id)
# print(getById.price)
# print(getById.name)
# getById.price = '$0.00'
# session.add(getById)
# session.commit()
# print(getById.id)
# print(getById.price)
# print(getById.name)

# veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
# for veggieBurger in veggieBurgers:
#     if veggieBurger.price != '$0.00':
#         veggieBurger.price = '&???'
#         session.add(veggieBurger)
#         session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger').one()
veggieBurgerInfo = session.query(MenuItem).filter_by(id=veggieBurgers.id).one()
print(veggieBurgerInfo.id)
print(veggieBurgerInfo.price)
print(veggieBurgerInfo.name)

#delete
# spinach = session.query(MenuItem).filter_by(name='Veggie Burger').one()
# print(spinach.restaurant.name)
# session.delete(spinach)
# session.commit()

