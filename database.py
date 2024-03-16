import sqlite3 as sql


global cur,db

dbs = sql.connect("gyaanConnect.db")
cur = dbs.cursor()        

def sqlInsert(cursor_command):

    cursor_command
    dbs.commit()


def sqlAccess(cursor_command):   
    
    cursor_command
    data = cur.fetchall()
    return data

if __name__ == '__main__':
    pass