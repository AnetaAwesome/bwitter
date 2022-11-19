from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:root@localhost:3306/bwitter")
Session = sessionmaker(bind=engine)
