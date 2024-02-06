from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URL = (f"postgresql://"
                           f"{os.environ['POSTGRES_USER']}:"
                           f"{os.environ['POSTGRES_PASSWORD']}@"
                           f"{os.environ['POSTGRES_HOST']}:5432/"
                           f"{os.environ['POSTGRES_DB']}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
