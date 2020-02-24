import os
from dotenv import load_dotenv
import datetime
import requests
import json
from flask import Blueprint, request, render_template

load_dotenv()
api_key = os.getenv("NYT_API_KEY", default="OOPS")

newroutes = Blueprint("newroutes", __name__)

@newroutes.route("/books_home")
@newroutes.route("/")
def newindex():
    print("VISITING THE NEW INDEX PAGE")
    return render_template("newhomepage.html")

@newroutes.route("/about")
def about():
    print("About")
    return render_template("about.html")

@newroutes.route("/contact")
def contact():
    print("Contact Us")
    return render_template("Contact.html")

@newroutes.route('/bookstoread', methods=["POST"])
def request_books_to_read():
    print("FINDING BOOKS...")
    print("FORM DATA:", dict(request.form))
    #return jsonify(request.form)

    genre_name = request.form["Bookgenre"]
    year_published = request.form["Year"]









    #genre_name="hardcover-fiction"
  
    request_url = f"https://api.nytimes.com/svc/books/v3/lists/current/{genre_name}.json?api-key={api_key}"
    response = requests.get(request_url)
    print(type(response))

    parsed_response = json.loads(response.text)
    books=parsed_response["results"]["books"]
    for b in books:
        print(b["rank"], b["title"], b["author"], b["description"])







    #product_name = request.form["product_name"]
    #flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    #return redirect("newhomepage.html")
    return render_template("booksresults.html", books=books, genre_name=genre_name)
