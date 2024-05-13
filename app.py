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
    return render_template('meals.html')



@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        # Process the form data when the request method is POST
        # Add the recipe to the user's favorites or perform any necessary operations
        # based on the submitted data
        
        # Example: Access the form data
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        
        # Process the recipe_name data as needed
        
        # Example: Add the recipe to the user's favorites in the database
        # add_recipe_to_favorites(recipe_name)
        recipes = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
        db.recipe.insert_one(recipes)
        # Redirect to a different page after processing the form data
        return redirect(url_for("drinks"))
    
    # If the request method is GET or not a POST request
    # Render the add.html template for the user to view the form
    return render_template("add.html")


@app.route("/added", methods=["POST", "GET"])
def added():
    if request.method == "POST":
        # Process the form data when the request method is POST
        # Add the recipe to the user's favorites or perform any necessary operations
        # based on the submitted data
        
        # Example: Access the form data
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        
        # Process the recipe_name data as needed
        
        # Example: Add the recipe to the user's favorites in the database
        # add_recipe_to_favorites(recipe_name)
        Meals = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
        db.Meals.insert_one(Meals)
        # Redirect to a different page after processing the form data
        return redirect(url_for("meals"))
    
    # If the request method is GET or not a POST request
    # Render the add.html template for the user to view the form
    return render_template("added.html")


@app.route('/drinks')
def get_drinks():
    recipes = db.recipe.find()
    return render_template('drinks.html', recipes=recipes)

@app.route('/meals')
def get_meals():
    meals = db.Meals.find()  # Assuming 'Meals' is the collection name in your MongoDB
    return render_template('meals.html', meals=meals)


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


@app.route('/dessert')
def dessert():
    # Handle Dessert page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('dessert.html')

@app.route('/success')
def success():
    # Handle success page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('success.html')


    
    

if __name__ == '__main__':
    app.run(debug=True)
