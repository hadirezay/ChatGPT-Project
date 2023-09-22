from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Text, DateTime, VARCHAR, Enum, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Request(Base):
    __tablename__ = "request"

    prompt_id = Column(Integer, primary_key=True, autoincrement=True)
    creation_date = Column(DateTime, nullable=False)
    model = Column(VARCHAR(255), nullable=False)
    msg_system_role = Column(Enum('System', 'Assistant', 'User'), nullable=False)
    msg_content = Column(String(255), nullable=False)
    max_tokens = Column(Integer, nullable=False)
    temperature = Column(Float, nullable=False)
    top_probability = Column(Float, nullable=False)
    frequency_penalty = Column(Float, nullable=False)
    presence_penalty = Column(Float, nullable=False)
    stop = Column(String(255))

class Response(Base):
    __tablename__ = "response"

    response_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    prompt_id = Column(Integer, nullable=False)
    id = Column(VARCHAR(255), nullable=False)
    response = Column(String(255), nullable=False)
    creation_date = Column(DateTime, nullable=False)
    prompt_tokens = Column(Integer, nullable=False)
    completion_tokens = Column(Integer, nullable=False)
    total_tokens = Column(Integer, nullable=False)

    request = relationship("Request", foreign_keys="Request.prompt_id")

class Analytics_Performance(Base):
    __tablename__ = "analytics_performance"

    analytics_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    prompt_id = Column(Integer, nullable=False)
    response_id = Column(Integer, nullable=False)
    response_time = Column(VARCHAR(255), nullable=False)

    request = relationship("Request", foreign_keys="Request.prompt_id")
    response = relationship("Response", foreign_keys="Response.response_id")

# Create the database engine
engine = create_engine("mysql://root:NewtRails4@localhost/ChatGPTSEPA_DB", echo=True)
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()