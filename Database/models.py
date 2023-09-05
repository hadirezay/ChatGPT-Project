from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()

class Question(Base):
    __tablename__ = "Questions"

    Question_ID = Column(Integer, primary_key=True, autoincrement=True)
    Question = Column(Text, nullable=False)
    Model_version = Column(String(255), nullable=False)
    parameter = Column(String(255), nullable=False)

    answers = relationship("Answer", back_populates="question")
    history_entries = relationship("History", back_populates="question")

class Answer(Base):
    __tablename__ = "Answers"

    Answer_ID = Column(Integer, primary_key=True, autoincrement=True)
    Question_ID = Column(Integer, ForeignKey("Questions.Question_ID"), nullable=False)
    Answer = Column(Text, nullable=False)
    Grading = Column(Integer, nullable=False)
    Comments = Column(Text)

    question = relationship("Question", back_populates="answers")
    history_entries = relationship("History", back_populates="answer")

class History(Base):
    __tablename__ = "History"

    Chat_ID = Column(Integer, primary_key=True, autoincrement=True)
    Question_ID = Column(Integer, ForeignKey("Questions.Question_ID"), nullable=False)
    Answer_ID = Column(Integer, ForeignKey("Answers.Answer_ID"), nullable=False)
    Question = Column(Text, nullable=False)
    Answer = Column(Text, nullable=False)
    Grading = Column(Integer, nullable=False)
    Comments = Column(Text)
    Model_version = Column(String(255), nullable=False)
    parameter = Column(String(255), nullable=False)
    time_stamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    question = relationship("Question", back_populates="history_entries")
    answer = relationship("Answer", back_populates="history_entries")

# Create the database engine
engine = create_engine("mysql://root:NewtRails4@localhost/ChatGPTSEPA_DB", echo=True)
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
