from os import environ
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class QuestionModel(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc))

session_maker = sessionmaker(bind=create_engine(environ.get('DATABASE_URL')))

def save_new_question(question: str, answer: str) -> None:
    with session_maker() as session:
        session.add(QuestionModel(question=question, answer=answer))
    session.commit()
