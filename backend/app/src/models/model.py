from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    JSON,
    String,
    Text,
    text,
)
from sqlalchemy.orm import relationship
from backend.app.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = { "schema": "management" }
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=True)
    role = Column(String(50), nullable=False, index=True, server_default="user")
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
                        
    # Oauth fields
    oauth_provider = Column(String(50), nullable=True)
    oauth_id = Column(String(255), nullable=True)
    avatar_url = Column(String(500), nullable=True)
    
    # TODO: Check if you need to add relationship for users
    
class Site(Base):
    __tablename__ = "sites"
    __table_args__ = { "schemas" : "management" }
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False, index=True)
    content = Column(JSON)
    address = Column(String (255), nullable=False)
    image = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    
    properties = relationship("Property", back_populates="site", cascade_all="all, delete-orphan")
    units = relationship("Units", back_populates="site", cascade_all="all, delete-orphan")
    
class Property(Base):
    __tablename__ = "properties"
    __table_args__ = { "schema" : "management"}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    content = Column(JSON)
    address = Column(String(255), nullable=False)
    area = Column(String(100), nullable=True)
    image = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    
    site = relationship("Site", back_populates="properties", cascade="all, delete-orphan")
    units = relationship("Units", back_populates="property", cascade="all, delete-orphan")
    
    
class Unit(Base):
    __tablename__ = "units"
    __table_args__ = { "schema" : "management"}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    content = Column(JSON)
    area = Column(String(100), nullable=True)
    image = Column(String(255), nullable=True)
    
    site = relationship("Site", back_populates="units", cascade="all, delete-orphan")
    property = relationship("Property", back_populates="units", cascade="all, delete-orphan")