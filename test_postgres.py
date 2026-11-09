from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://de_user:REMOVED_PASSWORD@localhost:5432/de_training"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print(result.fetchone()[0])
