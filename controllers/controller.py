from app import app
from flask import render_template
from models.order_list import order_list as order_list

@app.route('/')
def index():
    return "Landing page"

@app.route('/orders')
def orders():
    return render_template('index.html', order_list = order_list)

@app.route('/orders/<index>')
def orders_index(index):
    order_number = int(index)
    return render_template('order.html', title = "Individual Order", order = order_list[order_number])