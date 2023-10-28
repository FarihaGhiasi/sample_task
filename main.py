from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime, timedelta
from db import engine  

# to define the SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    registration_date = Column(Date)

# creating user table
Base.metadata.create_all(engine)

# session
Session = sessionmaker(bind=engine)
session = Session()

# to generate some random data
for i in range(20):
   
    name = f'User_{i}'

    today = datetime.now()
    one_year_ago= today - timedelta(days=365)
    registration_date = one_year_ago + timedelta(days=random.randint(1, 365))

    
    user = User(name=name, registration_date=registration_date)
    session.add(user)



print("Created the 'users' table and inserted 20 dummy records.")


# to delete data older than 2023, 1, 9 

threshold_date = datetime(2023, 1, 9)

records_to_delete = session.query(User).filter(User.registration_date < threshold_date).all()

# to delete the records
for record in records_to_delete:
    session.delete(record)


session.commit()
session.close()

print(f"Deleted records where the date is older than {threshold_date}.")





