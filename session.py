import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = os.environ.get("DB_URI")
if DB_URI is None:
    raise Exception("DB_URI env variable is not set ")

engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
