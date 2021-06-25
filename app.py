from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__, template_folder="templates")

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
mars_collection = mongo.db.mars # reference to the mars collection

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    db_data = mars_collection.find_one()
    # Return template and data
    return render_template("index.html", exploration=db_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    # update the mongo database with costa_data
    # @TODO: YOUR CODE HERE!

    mars_collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
