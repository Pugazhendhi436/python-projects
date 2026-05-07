import mysql.connector
from mysql.connector import Error

import pandas as pd 
try:
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="OLA"
)

    df = pd.read_sql("SELECT * FROM drive", conn)
    print(df)
except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")


from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:123456@localhost/OLA")

print(engine)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM drivers  LIMIT 5"))
    for row in result:
        print(row)
    conn.commit()