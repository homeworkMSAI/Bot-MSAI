from pony.orm import *

db = Database()

# Create models
class Fire(db.Entity):
	link_fire = Required(str)

class Water(db.Entity):
    link_water = Required(str)

class Earth(db.Entity):
    link_earth = Required(str)
	


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

db.generate_mapping(create_tables=True)

# Save in Database
@db_session
def save():
    p1 = Fire(link_fire="fire1.jpg")
    p2 = Fire(link_fire="fire2.jpg")
    p3 = Fire(link_fire="fire3.jpg")

    p4 = Water(link_water="water1.jpg")
    p5 = Water(link_water="water2.jpg")
    pp = Water(link_water="water3.jpg")
    ppp = Water(link_water="water4.jpg")
    p6 = Water(link_water="water5.jpg")
    p6 = Water(link_water="water6.jpg")

    p7 = Earth(link_earth="earth1.jpg")
    p8 = Earth(link_earth="earth2.jpg")
    p9 = Earth(link_earth="earth3.jpg")


@db_session
def return_fire(number):
    p = Fire[number]
    return p.link_fire

@db_session
def return_water(number):
    p = Water[number]
    return p.link_water

@db_session
def return_earth(number):
    p = Earth[number]
    return p.link_earth
    
# save()

fire1, fire2, fire3 = return_fire(1), return_fire(2), return_fire(3)
water1, water2, water3, water4, water5, water6 = return_water(1), return_water(2), return_water(3), return_water(4), return_water(5), return_water(6)
earth1, earth2, earth3 = return_earth(1), return_earth(2), return_earth(3)


