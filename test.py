import pyodbc
import pandas as pd

def fetch_data():                      
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=pocserver007.database.windows.net;DATABASE=POC;UID=demo;PWD=User@2021')
                          
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Transactions")
    for row in cursor.fetchall():
        print(",".join(list(row)))
        break
            
    conn.commit()
    cursor.close()
    conn.close()
    return (",".join(list(row)))   

global list1
list1 = ["Ram","Lal"]

def count():
    return " ".join(list1)