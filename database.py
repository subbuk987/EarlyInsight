from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = 'mysql+pymysql://root:subbu2727@localhost:3306/health'

engine = create_engine(database_url)

sessionlocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionlocal
    try:
        yield db
    finally:
        db.close()