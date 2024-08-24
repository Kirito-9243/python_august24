import pymysql as py
import pymysql.err
import mysql.connector 


def connectdb(connectionobj):
    connectionobj = py.Connect(host="localhost",user="root",password="root123",
                           database="ishwar_db",port=3306,charset="utf8")
    print("Database connected successful!")
    return connectionobj

def disconnectdb(connectionobj):
    connectionobj.close()
    print("DB Disconnected!!")

def creation_fields(n):
    field_list = []
    field_dlist = []
    field_clist = []
    for i in range(1,n+1):
        field = input("Enter the",i,"field:")
        field_list.append(field)
        dfield = input("Enter",i,"'s datatype:")
        field_dlist.append(dfield)
        n_c =input("Enter",i,"'s constrains(',' after every constrain):")
        field_clist.append(n_c)
    return field_list,field_dlist,field_clist

def createTable():
    no_of_fields = int(input("Enter the number of fields:"))
    fields,datatypes,constrains = creation_fields(no_of_fields)
    createTable = "create table IF NOT EXISITS %s();" #id int prinmary key auto_increment,name varchar(50) not null
    name = input("Enter the name of the table:")
    try:
        conn = connectdb
        my_cursor = conn.cursor()
        my_cursor.execute(createTable,name)
        my_cursor.close()
    except Exception as err:
        # print(err)
        print("Table creation failed!!")
    else:
        disconnectdb(conn)

def deleteTable():
    deleteTable = "drop table  IF EXISTS %s;"
    tablename = input("Enter the name of the table to be deleted:")
    try:
        conn = connectdb
        my_cursor = conn.cursor()
        my_cursor.execute(deleteTable,tablename)
        print(tablename,"is deleted.")
        my_cursor.close()
    except Exception as err:
        # print(err)
        print("Table Deletion failed!!")
    else:
        disconnectdb(conn)

def insertrow():
    insertrow = "insert into %s(name) values(%s)"
    tablename = input("Enter the name of the table to insert:")
    name = input("Enter the name:")
    try:
        conn = connectdb
        my_cursor = conn.cursor()
        my_cursor.execute(insertrow,tablename,name)
        conn.commit()
        print("Row inserted.")
        my_cursor.close()
    except Exception as err:
        # print(err)
        print("Table Row Insertion failed!!")
    else:
        disconnectdb(conn)

# def searchrow():

