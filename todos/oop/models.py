from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    done = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, desc='{self.description}', done={self.done})>"
