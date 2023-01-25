from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def index():
    return render_template('index.html', boxes_number = 3, box_color = 'lightblue')

@app.route('/play/<int:boxes_number>')
def add_box(boxes_number):
    return render_template('index.html', boxes_number = boxes_number, box_color = 'lightblue')

@app.route('/play/<int:boxes_number>/<box_color>')
def add_box_color(boxes_number, box_color):
    return render_template('index.html', boxes_number = boxes_number, box_color = box_color)

if __name__ == "__main__":
    app.run(debug = True)