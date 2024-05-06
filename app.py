from bson import ObjectId
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/customer"
mongo = PyMongo(app)
db = mongo.db


# Signup
@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        # Declare variables
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Adding user to the database
        user = {"name": name, "surname": surname, "email": email, "password": password}
        db.user.insert_one(user)
        return redirect(url_for('login'))
    
    return render_template('signup.html')


# Login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists in the database
        user = db.user.find_one({"email": email, "password": password})
        if user:
            return redirect(url_for('home'))
      
    return render_template('login.html')

 


@app.route("/", methods=['GET', 'POST'])
def index():
  return render_template('admin.html')


@app.route("/home", methods=['GET', 'POST'])
def home(): 
  return render_template('index.html')
# Other routes
@app.route('/meals')
def meals():
    # Handle Meals page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('grilled_cheese.html')


@app.route('/drinks')
def drinks():
    # Handle Drinks page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('drinks.html')

@app.route('/strawberry')
def strawberry():
    # Handle Drinks page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('strawberry.html')


@app.route('/cookies')
def cookies():
    # Handle Dessert page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('cookies.html')

@app.route('/success')
def success():
    # Handle success page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
