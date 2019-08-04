import os

from flask import Flask, render_template, request

categories = [
{
	'id' : '1',
	'name' : 'Grocery',
	'img' : 'img1.jpg'
},

{
	'id' : '2',
	'name' : 'Fashion Wear',
	'img' : 'img2.jpg'
},

{
	'id' : '3',
	'name' : 'Shoes',
	'img' : 'img3.jpg'
},

{
	'id' : '4',
	'name' : 'Stationary',
	'img' : 'img4.jpg'
}

]


items = []

def put_item(category, iden, name, img):
	info = {
		'category' : category,
		'iden' : iden,
		'name' : name,
		'img' : img
	}
	items.append(info)
	return

def remove_item(iden):
	ele = 0
	flag = 0
	for ind,item in enumerate(items):
		if item['iden'] == iden:
			ele = ind
			flag = 1
			break
	if flag == 1:
		items.pop(ele)
	return


def add_item_by_category(category, iden, name, img):
	return put_item(category, iden, name, img)

def select_products(category):
	ans = []
	for item in items:
		if item['category'] == category:
			ans.append(item)
	return ans

def get_products_by_category(category):
	try:
		return select_products(category)
	except:
		None

def delete_item_by_category(iden):
	return remove_item(iden)


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass


	@app.route('/home')
	def home():
		return render_template('home.html', categories=categories)

	@app.route('/add_items')
	def add_items():
		category = request.args.get('category')
		iden = request.args.get('iden')
		name = request.args.get('name')
		img = request.args.get('img')
		add_item_by_category(category, iden, name, img)
		return 'Added Successfully'

	@app.route('/delete_items')
	def delete_items():
		iden = request.args.get('iden')
		delete_item_by_category(iden)
		return 'Deleted Successfully'



	@app.route('/products/<category>')
	def products(category):
		prods = get_products_by_category(category)
		if prods == None:
			return '404 error'
		else:
			return render_template('products.html', prods = prods)




	return app

