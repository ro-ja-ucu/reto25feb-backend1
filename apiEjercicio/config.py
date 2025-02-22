import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session

# Cargar variables del archivo .env
load_dotenv()

DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
