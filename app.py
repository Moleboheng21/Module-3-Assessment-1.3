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

    #Exammple: Render a template
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
        drinks = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
        db.recipe.insert_one(drinks)
        # Redirect to a different page after processing the form data
        return render_template("drinks.html", recipe=drinks)
    drinks = db.recipe.find() 
    
    # If the request method is GET or not a POST request
    # Render the add.html template for the user to view the form
    return render_template("add.html" )


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
        # add_recipe_to_favorites(recipe_name)"image": image,
        Meals = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions, }
        db.Meals.insert_one(Meals)
        meals = db.Meals.find() 
        print(meals)
      
        # Redirect to a different page after processing the form data
        return render_template("meals.html", meal=meals)
    
    # If the request method is GET or not a POST request
    # Render the add.html template for the user to view the form
    return render_template("added.html")

@app.route("/added2", methods=["POST", "GET"])
def added2():
    return render_template("added2.html")


@app.route("/added22", methods=["POST", "GET"])
def added22():
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
    Dessert = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
    db.Dessert.insert_one(Dessert)
    dessert = db.Dessert.find() 
        # Redirect to a different page after processing the form data
    return render_template("dessert.html", dessert=dessert)
    
    # If the request method is GET or not a POST request
    # Render the add.html template for the user to view the form
    return render_template("added2.html")



@app.route('/drinks')
def get_drinks():
    drinks = db.recipe.find()
    return render_template('drinks.html', recipe=drinks)

@app.route('/meals')
def get_meals():
    meals = db.Meals.find()  # Assuming 'Meals' is the collection name in your MongoDB
    return render_template('meals.html', meal=meals)


# @app.route('/dessert')
# def get_dessert():
#    dessert = db.Dessert.find()  # Assuming 'Meals' is the collection name in your MongoDB
#    return render_template('dessert.html', dessert=dessert)



@app.route('/strawberry')
def strawberry():
    # Handle Drinks page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('strawberry.html')


@app.route('/dessert')
def dessert():
    dessert = db.Dessert.find() 
    # Handle Dessert page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('dessert.html', dessert=dessert)

@app.route('/success')
def success():
    # Handle success page logic here
    # You can return a rendered template or a response

    # Example: Render a template
    return render_template('success.html')

@app.route('/delete_meals', methods=['POST'])
def delete_meals():
    if request.method == "POST":
     delete_id = request.form.get("delete")
     db.Meals.delete_one({'_id': ObjectId(delete_id)})
     meals = db.Meals.find()
    return render_template('meals.html', meal=meals)
    
@app.route('/delete_dessert', methods=['POST'])
def delete_dessert():
    if request.method == "POST":
     delete_id = request.form.get("delete")
     db.Dessert.delete_one({'_id': ObjectId(delete_id)})
     dessert = db.Dessert.find()
    return render_template('dessert.html', dessert=dessert)

@app.route('/delete_drinks', methods=['POST'])
def delete_drinks():
    if request.method == "POST":
     delete_id = request.form.get("delete")
     db.Dessert.delete_one({'_id': ObjectId(delete_id)})
    recipes = db.Dessert.find()
    return render_template('drinks.html',drinks=recipes )



@app.route('/edit2', methods=['POST'])
def edit_meals2():
    if request.method == "POST":
     id = request.form.get("id")
     title = request.form.get("title")
    description = request.form.get("description")
    ingredients = request.form.get("ingredients")
    instructions = request.form.get("instructions")
     
    db.Meals.update_one( { "_id":  ObjectId(id)}, { '$set': { "title": title, "ingredients":ingredients,"description":description, "instructions":instructions} } ) 
    meals = db.Meals.find()
     
    return render_template('meals.html', meal=meals)




@app.route('/edit_comment/<int:meal_id>/<int:comment_id>', methods=['PUT'])
def edit_comment(meal_id, comment_id):
    data = request.get_json()
    text = data.get('text')
    if text:
        for meal in meals:
            if meal['_id'] == meal_id:
                for comment in meal['comments']:
                    if comment['_id'] == comment_id:
                        comment['text'] = text
                        return jsonify({"message": "Comment edited successfully"}), 200
                return jsonify({"error": "Comment not found"}), 404
        return jsonify({"error": "Meal not found"}), 404
    else:
        return jsonify({"error": "Text is required"}), 400

@app.route('/reply_comment/<int:meal_id>/<int:comment_id>', methods=['POST'])
def reply_comment(meal_id, comment_id):
    data = request.json
    author = data.get('author')
    text = data.get('text')
    if author and text:
        for meal in meals:
            if meal['_id'] == meal_id:
                comments = meal['comments']
                if comment_id < len(comments):
                    comments[comment_id].setdefault('replies', []).append({"author": author, "text": text})
                    return jsonify({"message": "Reply added successfully"}), 200
                else:
                    return jsonify({"error": "Comment not found"}), 404
        return jsonify({"error": "Meal not found"}), 404
    else:
        return jsonify({"error": "Author and text are required fields"}), 400



@app.route('/meals', methods=['POST'])
def edit_add():
    if request.method == "POST":
        id = request.form["id"]
        title = request.form["title"]
        Ingredients = request.form["Ingredients"]
        Instructions = request.form["Instructions"]

        return render_template('add.html', id=id,name=title, Ingredients=Ingredients, Instructions=Instructions)

@app.route('/add', methods=['POST'])
def edit1_meals():
    if request.method == "POST":
        id = request.form["id"]
        title = request.form["title"]
        Ingredients = request.form["Ingredients"]
        Instructions = request.form["Instructions"]
        db.Meals.update_one( { "_id":  ObjectId(id)}, { '$set': { "title": title, "Ingredients":Ingredients, "Instructions":Instructions} } ) 
        meals = []

        for i in db.Meals.find():
            meals.append(i)
            
    return render_template('add.html', meal=meals)
    
@app.route('/comment', methods=['POST'])
def comment():
    if request.method == "POST":
        comment = request.form["comment"]
        id = request.form["id"]
        comm = {"comment": comment, "item_id": id}
        db.comment.insert_one(comm)
        
        meals = db.Meals.find()
        comments = db.comment.find()
        print(meals)
            
        return render_template('meals.html', meal=meals, comment=comments, id=id)
    

@app.route('/delete_comment', methods=['POST'])
def delete_comment():
    if request.method == "POST":
     delete_id = request.form.get("delete")
     db.comment.delete_one({'_id': ObjectId(delete_id)})
     comments= db.comment.find()
    return render_template('meals.html', comment=comments)
  
    
if __name__ == '__main__':
    app.run(debug=True)
