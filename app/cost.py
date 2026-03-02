from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.config import DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    complexity_score = Column(Float)
    model_used = Column(String)
    latency = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)


def log_query(data):
    db = SessionLocal()
    log_entry = QueryLog(
        query=data["query"],
        complexity_score=data["complexity_score"],
        model_used=data["model_used"],
        latency=data["latency"]
    )
    db.add(log_entry)
    db.commit()
    db.close()