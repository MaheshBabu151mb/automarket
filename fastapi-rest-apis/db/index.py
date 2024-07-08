from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import os

# DB_URL = os.environ['DB_URL'] 


DB_URL = "postgresql://avnadmin:AVNS_25aaE9ObriOz2qNOl5X@pg-1629d2c5-prathamjagga123-cbe1.h.aivencloud.com:13791/automarket?sslmode=require"

def createDBSession():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

session,_ = createDBSession()

def getDBStatus():
    try:
        session.execute(text("SELECT 1"))
        return 1
    except Exception as e:
        print("ERROR: ", e)
        return 0

def runSQL(query):
    try:
        result = session.execute(text(query))
        session.commit()
        return result
    except Exception as e:
        print(e)
        return False
