from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_str_con = 'sqlite:///./pokemon.db'
engine = create_engine(sqlite_str_con)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()
