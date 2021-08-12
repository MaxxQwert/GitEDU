from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean
import psycopg2
engine = create_engine("postgresql+psycopg2://postgres:000@localhost/postgres")
metadata = MetaData()

users_table = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("full_name", String(32), default=False),
)
pass
if __name__ == "__main__":
    metadata.create_all(engine)