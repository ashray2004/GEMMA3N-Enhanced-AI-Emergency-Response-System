from app.database import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("PRAGMA table_info(triage_patients)"))
    for row in result:
        print(row)
