from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import time, datetime
from importlib import import_module, __import__
import os, sys, timeit, random

sys.path.append(os.path.join(os.path.dirname(__file__), "Data Structure"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.before_request
def create_all():
    db.create_all()

class Items_Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    data_structure = db.Column(db.String(200), nullable=False)
    sort_time = db.Column(db.Integer, default=0)
    search_time = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Item ID %r>' % self.id

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        submitted_add_items = Items_Model.query.order_by(Items_Model.date_created).all()
        return render_template("index.html", submitted_add_items =submitted_add_items)
        
    else:
        if request.form['data']:
            item =" ".join(map(str,random.choices(list(range(999)), k = 10)))
            if request.form['data_structure'] != "Random":
                new_add = Items_Model(item=item, data_structure= request.form['data_structure'])
            else:
                new_add = Items_Model(item=item, data_structure= random.choice(['Python list', 'Linked list', 'Binary Search Tree']))
        else:
            submit_item = request.form['item']
            new_add = Items_Model(item=submit_item)

        try:
            db.session.add(new_add)
            db.session.commit()
            return redirect('/')
        except:
            return "Cannot add database"

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    update_item = Items_Model.query.get_or_404(id)

    if request.method == 'GET':
        return render_template('update.html', update_item=update_item)
        
    else:
        temp = update_item.item.split()
        temp[int(request.form['updateItemIndex'])] = request.form['update_item_value']
        update_item.item = " ".join(temp )
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Cannot update item"

@app.route('/delete/<int:id>')
def delete(id):
    delete_item = Items_Model.query.get_or_404(id)

    try:
        db.session.delete(delete_item)
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot delete database"
    
@app.route('/sort/<id>', methods=['GET','POST'])
def sort(id):
    sort_item = Items_Model.query.get_or_404(id)

    if request.form['sortItem'] == "Bubble Sort":
        sort_mode = import_module('Data Structure Sort.1 Bubble Sort')
        sort_ans = sort_mode.bubble_sort(list(map(int,sort_item.item.split())))
        sort_item.item = " ".join(list(map(str,sort_ans[0])))
        sort_item.sort_time = sort_ans[1]
    elif request.form['sortItem'] == "Insertion Sort":
        sort_mode = import_module('Data Structure Sort.3 Insertion Sort')
        sort_ans = sort_mode.insertion_sort(list(map(int,sort_item.item.split())))
        sort_item.item = " ".join(list(map(str,sort_ans[0])))
        sort_item.sort_time = sort_ans[1]
    
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot sort data"

@app.route('/search/<id>', methods=['GET','POST'])
def search(id):
    search_item = Items_Model.query.get_or_404(id)
    search_item_list = search_item.item.split()

    if search_item.data_structure == "Python list":
        data_mode = import_module('Data Structure.1 1 List')
        search_item.search_time = data_mode.search(search_item_list, search_item_list[int(request.form['searchItem'])])

    elif search_item.data_structure == "Linked list":
        data_mode = import_module('Data Structure.2 1 Linked list')
        data_instance = data_mode.LinkedList()
        for i in search_item_list:
            data_instance.insertTail(i)
        search_item.search_time = data_instance.searchNodeTime(search_item_list[int(request.form['searchItem'])])

    elif search_item.data_structure == "Binary Search Tree":
        data_mode = import_module('Data Structure.4 4 Binary Search Tree')
        data_instance = data_mode.BST(search_item.item.split())
        search_item.search_time = data_instance.search(search_item_list[int(request.form['searchItem'])])

    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot search data"
        
if __name__ == "__main__":
    app.run(debug=True)



    
    