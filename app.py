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

@app.route('/meals')
def get_meals():
    meals = list(db.Meals.find())
    comments = list(db.comment.find())
    return render_template('meals.html', meal=meals, comment=comments)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        
        meals = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
        db.recipe.insert_one(meals)
        
        return render_template("drinks.html", recipe=meals)
    
    drinks = db.recipe.find()
    return render_template("add.html")


@app.route("/added", methods=["POST", "GET"])
def added():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        
        Meals = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
        db.Meals.insert_one(Meals)
        meals = db.Meals.find()
      
        return render_template("meals.html", meal=meals)
    
    return render_template("added.html")

@app.route("/added2", methods=["POST", "GET"])
def added2():
    return render_template("added2.html")


@app.route("/added22", methods=["POST", "GET"])
def added22():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        
    Dessert = {"title": title, "description": description, "ingredients": ingredients, "instructions": instructions}
    db.Dessert.insert_one(Dessert)
    dessert = db.Dessert.find()
    return render_template("dessert.html", dessert=dessert)
    
    return render_template("added2.html")


@app.route('/drinks')
def get_drinks():
    drinks = db.recipe.find()
    return render_template('drinks.html', recipe=drinks)

@app.route('/strawberry')
def strawberry():
    return render_template('strawberry.html')


@app.route('/dessert')
def dessert():
    dessert = db.Dessert.find() 
    return render_template('dessert.html', dessert=dessert)

@app.route('/success')
def success():
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
    return render_template('drinks.html',drinks=recipes)

@app.route('/edit_meals', methods=['POST'])
def edit_meals():
    if request.method == "POST":
        id = request.form.get("edit")
        return render_template('editmeal.html', id=id)
    
@app.route('/edit2', methods=['POST'])
def edit_meal2():
    if request.method == "POST":
     id = request.form.get("id")
     title = request.form.get("title")
     description = request.form.get("description")
     ingredients = request.form.get("ingredients")
     instructions = request.form.get("instructions")
     
     db.Meals.update_one( { "_id":  ObjectId(id)}, { '$set': { "title": title, "ingredients":ingredients,"description":description, "instructions":instructions} } ) 
     meals = db.Meals.find()
     
     return render_template('meals.html', meal=meals)

@app.route('/add_comment/<meal_id>', methods=['POST'])
def add_comment(meal_id):
    comment = request.form["comment"]
    comm = {"comment": comment, "item_id": ObjectId(meal_id)}
    db.comment.insert_one(comm)
    
    print(f"Comment added to meal ID: {meal_id}")

    meals = list(db.Meals.find())
    comments = list(db.comment.find())
    return render_template('meals.html', meal=meals, comment=comments)

    
@app.route('/delete_comment', methods=['POST'])
def delete_comment():
    if request.method == "POST":
        delete_id = request.form.get("delete")
        db.comment.delete_one({'_id': ObjectId(delete_id)})
    comments = db.comment.find()
    meals = db.Meals.find()
    return render_template('meals.html', meal=meals, comment=comments)


@app.route('/edit_comment/<comment_id>', methods=['GET', 'POST'])
def edit_comment(comment_id):
    if request.method == 'POST':
        comment_text = request.form['comment-text']
        db.comments.update_one(
            
            {'_id': ObjectId(comment_id)},
            {'$set': {'text': comment_text}}
        )
        print("com id", comment_id)
        print("com text", comment_text)
        
        comments = db.comment.find()
        meals = db.Meals.find()
        db.session.commit()
        return redirect(url_for('get_meals',meal=meals, comment=comments))  # Replace 'show_post' with the appropriate route

    # Fetch the comment data from the database
    comment = db.comments.find_one({'_id': ObjectId(comment_id)})
    return render_template('meals.html', meal=meals,  comment=comment)

# @app.route('/edit_comment/<comment_id>', methods=['GET', 'POST'])
# def edit_comment(comment_id):
#     if request.method == 'POST':
#         comment_text = request.form['comment_text']
#         db.comment.update_one(
#             {'_id': ObjectId(comment_id)},
#             {'$set': {'comment': comment_text}}  # Corrected the field name to 'comment'
#         )
#         print("com id", comment_id)
#         print("com text", comment_text)
        
#         # Fetch all comments and meals after editing
#         comments = db.comment.find()
#         meals = db.Meals.find()
#         return redirect(url_for('get_meals'))  # Redirect to the meals page after editing

    # Fetch the comment data from the database
    comment = db.comment.find_one({'_id': ObjectId(comment_id)})
    return render_template('edit_comment.html', comment=comment)  # Create a new template for editing comments



if __name__ == '__main__':
    app.run(debug=True)
