from app.database import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("SELECT name, assigned_doctor FROM triage_patients LIMIT 10"))
    for row in result:
        print(row)
