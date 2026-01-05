import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

connection = pymysql.connect(
    host=os.getenv('RDS_HOST'),
    user=os.getenv('RDS_USER'),
    password=os.getenv('RDS_PASSWORD'),
    database=os.getenv('RDS_DB_NAME'),
    charset='utf8mb4',
    port=int(os.getenv('RDS_PORT')),
    connect_timeout=10
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("test:", result)

    connection.close()  
except Exception as e:
    print("An error occurred:", e)