import mysql.connector

def allesSelecterenMethode():
    print("op naar de database")
    return "Dit komt van de methode van recpt allesSelecteren"

def tweedeAllesSelecterenMethode():
    mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM recept")

    myresult = mycursor.fetchall()
    eindstring = ""
    for x in myresult:
        print(x[1], " - ", x[3])
        eindstring += x[1]+", "
    return "yes: " + eindstring
print(tweedeAllesSelecterenMethode())
