from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_server = os.getenv("DATABASE_SERVER")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
database_pwd = os.getenv("DATABASE_PWD")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{database_user}:{database_pwd}@{database_server}/{database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'ssl':{'fake_flag_to_enable_tls':True}}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()