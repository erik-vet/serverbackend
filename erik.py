import mysql.connector
def methodeerik2():
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


def methodeerik(tweeword, driewoord):
    mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO recept (naam, aantalsterren) VALUES (%s, %s)"
    val = (tweeword, driewoord)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "Je recept is aangemaakt!" 
