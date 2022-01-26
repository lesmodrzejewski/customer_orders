from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Order List', orders=orders)

@app.route('/orders/<index>')
def show_order(index):
  order = orders[int(index)]
  return render_template('order.html', order=order)