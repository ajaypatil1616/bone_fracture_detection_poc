from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, DateTime, func
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String, nullable = False)
    password = Column(String, nullable = False)
    email = Column(String, nullable =False)
    
    created_at = Column(DateTime(timezone = True), default = func.now())
    updated_at = Column(DateTime(timezone= True), default=func.now(), onupdate=func.now())