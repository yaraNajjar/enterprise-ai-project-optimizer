from db.database import engine
from db.models import Base

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database initialized")
