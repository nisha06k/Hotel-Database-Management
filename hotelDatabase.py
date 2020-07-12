import sqlite3
#backend



def hotelData():
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS hotel (id INTEGER PRIMARY KEY, CusID text, Firstname text, Surname text, Gender text, \
        Address text, Mobile text, Nationality text, DateIn text, DateOut text, TotalCost text)")
    con.commit()
    con.close()

def addHotelRec(CusID, Firstname, Surname, Gender, Address, Mobile, Nationality, DateIn, DateOut, TotalCost):
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("INSERT INTO hotel VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", \
                (CusID, Firstname,Surname,Gender,Address, Mobile,Nationality,DateIn,DateOut,TotalCost))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel")
    rows=cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("DELETE FROM hotel WHERE id=?", (id,))
    con.commit()
    con.close


def searchData(CusID="", Firstname="", Surname="", Gender="", Address="", Mobile="", Nationality="", DateIn="", DateOut="", TotalCost=""):
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM hotel WHERE CusID=? OR Firstname=? OR Surname=? OR Gender=? OR Address=?  OR Mobile=? \
                OR Nationality=? OR DateIn=? OR DateOut=? OR TotalCost=? ", \
                (CusID, Firstname, Surname, Gender,Address, Mobile, Nationality, DateIn, DateOut, TotalCost))
    rows=cur.fetchall()  
    con.close()
    return rows 
    
def dataUpdate(id,CusID="", Firstname="",Surname="", Gender="", Address="", Mobile="", Nationality="", DateIn="", DateOut="", TotalCost=""):
    con=sqlite3.connect("hotel.db")
    cur = con.cursor()
    cur.execute("UPDATE hotel SET CusID=?, Firstname=?,Surname=?, Gender=?, Address=?, Mobile=?, Nationality=?, DateIn=?,DateOut=?,TotalCost=?, WHERE id=?", \
                (CusID, Firstname,Surname,Gender,Address, Mobile,Nationality,DateIn,DateOut,TotalCost,id))
    con.commit()
    con.close()



 

hotelData()



