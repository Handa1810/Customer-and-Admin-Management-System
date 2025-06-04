<h1 align="center">💼 Customer & Admin Management System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Flask-%20Web%20App-blue?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/SQLite-Database-%2300C853?style=for-the-badge&logo=sqlite"/>
  <img src="https://img.shields.io/badge/HTML+CSS-Frontend-%23f06292?style=for-the-badge&logo=html5"/>
</p>

---

> ⚙️ A complete backend-focused project using **Flask** and **SQLAlchemy**, built for managing customers and item data through role-based dashboards for Admin and Customer.

---

## 🧩 Project Overview

🎯 This app provides:
- 🔐 Secure customer & admin login
- ✍️ Admin tools to create/update/delete/view customers
- 📦 Customers can manage their own item inventories
- 🧠 Backend logic implemented fully in Python (Flask + SQLAlchemy)

---

## 🎮 Terminal Preview

```bash
Welcome to the Customer Inventory Portal 🗃️

🧑 Login as Admin or Customer
🔏 Admin can manage all customer accounts and view their items
🗃️ Customers can log in with pin, and manage their own inventory
```

---

## 🧠 Core Logic Snapshot

```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if user == ADMIN:
            return redirect("/admin")
        elif user in db:
            return redirect("/customer")
        else:
            return "Invalid credentials"
```

---

## 🗂️ Folder Structure

```
Customer-Admin-Management/
│
├── main.py                    # Flask main backend logic
├── project.db                 # SQLite database file
│
├── static/
│   ├── style.css              # App styling
│   └── images/                # UI assets
│
├── templates/
│   ├── index.html             # Login page
│   ├── admin.html             # Admin dashboard
│   ├── customer.html          # Customer dashboard
│   ├── update_customer.html   # Customer update form
│   ├── update_items.html      # Item update form
│   └── view_items.html        # Admin's view of customer items
```

---

## 🔐 Admin Login Details

```txt
Name:  Yash
Email: Yash18
PIN:   1810
```

---

## 🧪 Technologies Used

| Layer     | Stack                          |
|-----------|-------------------------------|
| Backend   | Python, Flask, SQLAlchemy      |
| Frontend  | HTML5, CSS3                    |
| Database  | SQLite                         |
| Hosting   | Run locally on Flask dev server|

---

## ⚙️ How to Run This App

```bash
# 1. Clone this repo
git clone https://github.com/Handa1810/Customer-and-Admin-Management-System.git
cd Customer-and-Admin-Management-System

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install flask flask_sqlalchemy

# 4. Run the application
python main.py

# 5. Visit in browser
http://127.0.0.1:8000/
```

---

## 📸 Screenshots (Add yours!)

> 🖼️ Add screenshots like:
> - Login Page  
> - Admin Dashboard  
> - Customer Panel  
> - Update Forms

---

## 💡 Future Improvements

- 🔐 Implement hashed password login
- 📱 Responsive design with Bootstrap or Tailwind
- 🔍 Add search and filters in admin panel
- ☁️ Deploy on Render / Railway / Heroku

---

## 🧠 Designed & Developed By

> **Yash** — Focused on backend architecture, database logic & real-world use-case design.

---

## 📜 License

This project is licensed under the **MIT License**.

---

<p align="center">
  <img src="https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif" width="300" alt="Thanks for visiting!">
  <br/>
  ⭐ If you like this project, please give it a star!
</p>
