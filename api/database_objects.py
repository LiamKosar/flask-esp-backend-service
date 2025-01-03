from pony.orm import Database, Required, PrimaryKey, Set, Optional
import os

# Connects to the Vercel PostgreSQL database
# URL is https://vercel.com/liamkosars-projects/esp-next-testing/stores/postgres/store_1lBBRyI1kqynAq2d/data
# Ensures only one connection per session
def connect_to_database():
    db = Database()
    POSTGRES_URL = os.getenv('POSTGRES_URL')
    db.bind(provider='postgres', dsn=POSTGRES_URL)
    return db

db = connect_to_database()

class User(db.Entity):
    _table_ = 'User'
    email = PrimaryKey(str, 255)
    first_name = Optional(str, 50)
    last_name = Optional(str, 50)
    phone_number = Optional(str, 20)
    devices = Set('Device')
    vehicles = Set('Vehicle')

class Device(db.Entity):
    _table_ = 'device'
    mac_address = PrimaryKey(str, 17)
    version = Required(str, 10)
    runtime = Optional(float, default=0)
    date_updated = Required(str, 50)
    user = Optional(User, reverse='devices', column='user_email', default='kosar.liam@gmail.com')
    vehicle = Optional('Vehicle', reverse='device')

class MaintenanceProcedure(db.Entity):
    _table_ = 'maintenanceprocedure'
    id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    description = Optional(str)
    interval = Required(float)
    current_interval = Optional(float, default=0)
    vehicle = Required('Vehicle', reverse='maintenance_procedures', column="vehicle_id")

class Vehicle(db.Entity):
    _table_ = 'vehicle'
    vehicle_id = PrimaryKey(int, auto=True)
    name = Required(str, 100)
    runtime = Optional(float, default=0)
    image_url = Optional(str, 255)
    date_updated = Required(str, 50)
    device = Optional(Device, reverse='vehicle', column="mac_address", unique=True)
    user = Required(User, reverse='vehicles', column="user_email")
    maintenance_procedures = Set(MaintenanceProcedure)

db.generate_mapping(create_tables=False)