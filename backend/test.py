from app.sql_app.database import Base, engine

Base.metadata.create_all(bind=engine)
