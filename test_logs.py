from app.cost import SessionLocal, QueryLog

db = SessionLocal()
logs = db.query(QueryLog).all()

for log in logs:
    print(log.id, log.query, log.model_used, log.latency)

db.close()