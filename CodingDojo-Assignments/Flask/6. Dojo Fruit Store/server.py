from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # Student information from request form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']

    # Fruits information from request form data
    strawberry_count = request.form['strawberry']
    raspberry_count = request.form['raspberry']
    apple_count = request.form['apple']

    count = int(strawberry_count) + int(raspberry_count) + int(apple_count)  

    print(f"Charging {first_name} {last_name} for {count} fruits")
    return render_template("checkout.html", firstName = first_name , last_name = request.form['last_name'], student_id = request.form['student_id'], count = count, strawberry_count = request.form['strawberry'], raspberry_count = request.form['raspberry'],apple_count = request.form['apple'])
    return redirect('/')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    