import atexit
from sqlalchemy import 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, func, create_engine, ForeignKey
from PG_DNS import PG_DSN

engine = create_engine(PG_DSN)
atexit.register(engine.dispose)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class OwnerModel(Base):

    __tablename__ = "Owners"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    created_time = Column(DateTime, server_default=func.now())

Base.metadata.create_all()