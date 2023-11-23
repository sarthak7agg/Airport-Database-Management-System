print("Efforts by:-   \nKARTIKEYA VASHISTHA 12A \n PRAKARSH PANWAR 12A \n SARTHAK AGGRAWAL 12A \n RISHANK SHARMA 12A")
print("THIS PROGRAM HELPS US TO EASILY ACCESS AND MANIPULATE AIRPORT DATABASE")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
def menu():
    c='y'
    while c=='Y' or c=='y':
        print("1. Add Record")
        print("2. Update Record")
        print("3. Delete Record")
        print("4. Display Record")
        print("5. Show Ticket")
        print("6. Number of seats in flights")
        print("7. Exiting")
        choice=int(input("Enter your choice="))
        if choice==1:
            addData()
        elif choice==2:
            updateData()
        elif choice==3:
            deleteData()
        elif choice==4:
            showData()
        elif choice==5:
            showticket()
        elif choice==6:
            seatcount()
        elif choice==7:
            print("You are now exit from program")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            break
    else:
        print("Wrong input")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
def addData():
    import mysql.connector

    a=int(input("Ticket Number="))
    db=mysql.connector.connect(host="localhost",user="root",password="piltoo10",database="airport")
    cursor=db.cursor()
    cursor.execute("SELECT TicketNO FROM flights")
    results=cursor.fetchall()

    if (a,) not in results: 
        import mysql.connector


        b=input("Flight Number=")
        c=input("Airline=")
        d=input("Name on Ticket=")
        e=input("Departure=")
        f=input("Arrival=")
        g=input("Departure Time=")
        h=input("Class=")
        i=input("Seat Number=")
        s="INSERT INTO flights VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(a,b,c,d,e,f,g,h,i)
        db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
        cursor=db.cursor()
        cursor.execute(s,t)
        db.commit()
        print("Record added")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    elif (a,) in results:
        print("Record already exist")
    #print("code failed")

    #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def updateData():
    import mysql.connector
    print("Re-insert records")
    try:
        a=int(input("Ticket Number="))
        b=input("Flight Number=")
        c=input("Airline=")
        d=input("Name on Ticket=")
        e=input("Departure=")
        f=input("Arrival=")
        g=input("Departure Time=")
        h=input("Class=")
        i=input("Seat Number=")
        s="""DELETE FROM flights WHERE TicketNO=%s"""
        t="""INSERT INTO flights VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        x=(a,b,c,d,e,f,g,h,i)
        db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
        cursor=db.cursor()
        cursor.execute(s,(a,))
        cursor.execute(t,x)
        db.commit()
        print("Record Updated")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    except Exception as e:
        print(e)
def deleteData():
    import mysql.connector
    p=int(input("Enter Ticket Number of passenger="))
    s="""DELETE FROM flights WHERE TicketNO= %s """
    db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
    cursor=db.cursor()
    cursor.execute(s,(p,))
    db.commit()
    print("Record deleted")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def showData():
    try:
        import mysql.connector
        db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
        cursor=db.cursor()
        cursor.execute("SELECT * FROM flights")
        results=cursor.fetchall()
        from tabulate import tabulate
        print(tabulate(results,headers=["TICKET-NO","FLIGHT-NO","AIRLINES","NAME ON TICKET","DEPARTURE","ARRIVAL","DEPARTURE TIME","CLASS","SEAT-NO"],tablefmt="pretty"))

        #for x in results:
            #print(x)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    except:
        print("Error, unable to display")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
def showticket():
    a=int(input("Enter Ticket Number="))
    import mysql.connector
    db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
    cursor=db.cursor()
    s="""SELECT * FROM flights WHERE TicketNO=%s"""
    cursor.execute(s,(a,))
    results=cursor.fetchall()
    from tabulate import tabulate
    print(tabulate(results,headers=["TICKET-NO","FLIGHT-NO","AIRLINES","NAME ON TICKET","DEPARTURE","ARRIVAL","DEPARTURE TIME","CLASS","SEAT-NO"],tablefmt="pretty"))
def seatcount():
    a=input("Enter Flight Number=")
    import mysql.connector
    db=mysql.connector.connect(host="localhost",user="root", password="piltoo10",database="airport")
    cursor=db.cursor()
    s="""SELECT COUNT(FlightNumber) FROM flights WHERE FlightNumber=%s"""
    cursor.execute(s,(a,))
    results=cursor.fetchall()
    from tabulate import tabulate
    print(tabulate(results,headers=["PASSENGERS"],tablefmt="pretty"))
menu()
