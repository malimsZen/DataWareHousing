import mysql.connector as msc 
import pandas as pd
import glob
import ibm_db




#Function to extract csv files and read.
def extract_csvfile(fileToExtract):
    data_file = pd.read_csv(fileToExtract)
    return data_file



def extraction():
    #The dataframe to be uploaded into the data warehouse
    csv_data = "/home/manablackman/Zen/DataWareHousing/FactTrips.csv"

    df = pd.read_csv(csv_data)
    return df

#Loading data into the database.
def load_data():
    dsn_hostname = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud" 
    dsn_uid = "bwv46471"       
    dsn_pwd = "Qj04pA9MaQk7bLhh"

    dsn_driver = "{IBM DB2 ODBC DRIVER}"
    dsn_database = "BLUDB"            
    dsn_port = "30367"               
    dsn_protocol = "TCPIP"           
    dsn_security = "SSL"           
    
    dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

    #print the connection string to check correct values are specified
    print(dsn)

    try:
        conn = ibm_db.connect(dsn, "", "")
        print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )

    data = extraction() #extraction function that returns a csv dataframe.
    print(data)

    lists_of_data = list([list(x) for x in data.values])
    sql="INSERT INTO MyFactTrips values(?,?)"

    stmt=ibm_db.prepare(conn,sql)
    ibm_db.execute_many(stmt,lists_of_data)


load_data()




