from flask import Flask, render_template
from products import product_list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', product_list = product_list)

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)