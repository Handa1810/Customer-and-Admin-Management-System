from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key" 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ADMIN_NAME = "Yash"
ADMIN_EMAIL = "Yash18"
ADMIN_PIN = "1810"

class Project(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(200), nullable=False)
    item_desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    cust_pin = db.Column(db.Integer, nullable=False)  

    def __repr__(self) -> str:
        return f"{self.sno} - {self.item_name}"

class Info(db.Model):
    cust_name = db.Column(db.String(200), nullable=False)
    cust_mail = db.Column(db.String(500), nullable=False)
    cust_pin = db.Column(db.Integer, primary_key=True)

    def __repr__(self) -> str:
        return f"{self.cust_name} - {self.cust_pin}"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cust_name = request.form.get("cust_name")
        cust_mail = request.form.get("cust_mail")
        cust_pin = request.form.get("cust_pin")

        if cust_name == ADMIN_NAME and cust_mail == ADMIN_EMAIL and cust_pin == ADMIN_PIN:
            return redirect(url_for("admin"))
        else:
            customer = Info.query.filter_by(cust_name=cust_name, cust_mail=cust_mail, cust_pin=cust_pin).first()
            if customer:
                session['cust_pin'] = cust_pin  
                return redirect(url_for("customer_dashboard"))
            else:
                return "Invalid credentials! Please check your details or contact admin."

    return render_template("index.html")


@app.route("/admin")
def admin():
    customers = Info.query.all()  
    return render_template("admin.html", customers=customers)


@app.route("/admin/add_customer", methods=["POST"])
def add_customer():
    cust_name = request.form.get("cust_name")
    cust_mail = request.form.get("cust_mail")
    cust_pin = request.form.get("cust_pin")

    new_customer = Info(cust_name=cust_name, cust_mail=cust_mail, cust_pin=cust_pin)
    db.session.add(new_customer)
    db.session.commit()

    return redirect(url_for("admin"))


@app.route("/admin/delete_customer/<int:cust_pin>")
def delete_customer(cust_pin):
    customer = Info.query.filter_by(cust_pin=cust_pin).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()

    return redirect(url_for("admin"))


@app.route("/admin/update_customer/<int:cust_pin>", methods=["GET", "POST"])
def update_customer(cust_pin):
    customer = Info.query.get_or_404(cust_pin)
    if request.method == "POST":
        customer.cust_name = request.form['cust_name']
        customer.cust_mail = request.form['cust_mail']
        customer.cust_pin = request.form['cust_pin']
        db.session.commit()

        return redirect(url_for("admin"))

    return render_template("update_customer.html", customer=customer)


@app.route("/customer", methods=["GET", "POST"])
def customer_dashboard():
    if request.method == "POST":
        cust_pin = session.get('cust_pin')

        item_name = request.form['item']
        item_desc = request.form['desc']
        new_item = Project(item_name=item_name, item_desc=item_desc, cust_pin=cust_pin)
        db.session.add(new_item)
        db.session.commit()

        return redirect("/customer")

    all_items = Project.query.filter_by(cust_pin=session.get('cust_pin')).all()  
    return render_template("customer.html", allItems=all_items)


@app.route("/customer/delete/<int:sno>")
def delete(sno):
    item = Project.query.filter_by(sno=sno).first()
    if item:
        db.session.delete(item)
        db.session.commit()

    return redirect("/customer")


@app.route("/customer/update/<int:sno>", methods=["GET", "POST"])
def update_item(sno):
    item = Project.query.get_or_404(sno)

    if request.method == "POST":
        updated_name = request.form['item']
        updated_desc = request.form['desc']

        item.item_name = updated_name
        item.item_desc = updated_desc
        item.date_created = datetime.utcnow()
        db.session.commit()

        return redirect("/customer")

    return render_template("update_item.html", item=item)


@app.route("/admin/view_items/<int:cust_pin>")
def view_items(cust_pin):
    customer_items = Project.query.filter_by(cust_pin=cust_pin).all()
    return render_template("view_items.html", customer_items=customer_items)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

