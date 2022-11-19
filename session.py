from sqlalchemy.orm import sessionmaker

engine = None
Session = sessionmaker(bind=engine)
