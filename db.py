import datetime
from configparser import SafeConfigParser
import pyodbc

parser = SafeConfigParser()
parser.read('config.ini')


server=  parser.get('db', 'server')
database = parser.get('db', 'database')
username = parser.get('db', 'username')
password = parser.get('db', 'password')
conn = ""
cursor = None

def dbinit():
    print("pass")



def datatype(data1):
 
 
    try:
        datetime.datetime.strptime(data1, '%Y/%m/%d')
        return "datetime"
    except ValueError:
        try:
            int(data1)
            return "int"
        except ValueError:
            return "varchar (255)"


def recreateTable(tableName,data ):
    driver= '{ODBC Driver 18 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';Trusted_Connection=yes;TrustServerCertificate=yes')
    
    cursor = conn.cursor()
    sql = "DROP table " + tableName
    try: 
        cursor.execute(sql)
        cursor.commit()
    except:
        print('npoe')

    sql = "CREATE TABLE " + tableName +"  (" "micro_id int,"
    cols = []
    for key in data:
        if key == "":
            continue
        col = key + " "  + datatype(data[key])
        cols.append(col)

    sql = sql + ','.join(cols)
    sql = sql + ")"
    print(sql)
    try: 
        cursor.execute(sql)
        cursor.commit()
    except:
        print('nope')

def insertTable(tableName,data, microId ):
    driver= '{ODBC Driver 18 for SQL Server}'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';Trusted_Connection=yes;TrustServerCertificate=yes')
    cursor = conn.cursor()
    

    columns = ', '.join(data.keys())

 
    dat = []
    for key in data:
        dat.append(data[key])

    placeholders = "', '".join(dat)
    
    sql = "INSERT INTO %s (micro_id, %s ) VALUES (%s,'%s')" % (tableName, columns, microId, placeholders)
    print(sql)
    cursor.execute(sql)
    cursor.commit()

