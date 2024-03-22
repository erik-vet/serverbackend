from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
mydb = mysql.connector.connect(
        host="yc2403allpurpose.mysql.database.azure.com",  #port erbij indien mac
        user="yc2403admin",
        password="abcd1234ABCD!@#$",
        database="demopythondag"
    )

# Route to display recipes
@app.route('/')
def display_recipes():
    # Connect to the database   
    # conn = mysql.connector.connect(**demopythondag)
    cursor = mydb.cursor()

    # Fetch data from the database
    cursor.execute("SELECT naam FROM recept")
    recipes = cursor.fetchall()

    # Close the database connection
    # cursor.close()
    # mysql.close()

    # Render the HTML template with fetched data
    return render_template('recept.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
