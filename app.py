from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Add_Drop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Item ID %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        submit_item = request.form['item']
        new_add = Add_Drop(item=submit_item)

        try:
            db.session.add(new_add)
            db.session.commit()
            return redirect('/')
        except:
            return "Cannot add database"
    
    else:
        submitted_adds = Add_Drop.query.order_by(Add_Drop.date_created).all()
        return render_template("index.html", submitted_adds=submitted_adds )

@app.route('/update/<int:id>', methods=['POST', "GET"])
def update(id):
    update_item = Add_Drop.query.get_or_404(id)

    if request.method == 'POST':
        update_item.item = request.form['update_item.item']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Cannot update item"
    else:
        return render_template('update.html', update_item=update_item)

@app.route('/delete/<int:id>')
def delete(id):
    delete_item = Add_Drop.query.get_or_404(id)

    try:
        db.session.delete(delete_item)
        db.session.commit()
        return redirect('/')
    except:
        return "Cannot delete database"

if __name__ == "__main__":
    app.run(debug=True)
    