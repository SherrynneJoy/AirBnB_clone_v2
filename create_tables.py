from sqlalchemy import create_engine
from models import Base

# Replace 'your_database_url' with your actual database URL
database_url = 'mysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'
engine = create_engine(database_url, echo=True)

# Bind the engine to the Base class
Base.metadata.create_all(bind=engine)
