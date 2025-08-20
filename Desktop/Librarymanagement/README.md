# **Library Management System**  

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Flask](https://img.shields.io/badge/Flask-2.x-orange) ![SQLite](https://img.shields.io/badge/SQLite-3.39-lightgrey) ![License](https://img.shields.io/badge/License-MIT-green)

---

## **Project Overview**

The **Library Management System (LMS)** is a **web-based application** to manage books, members, and borrowing/returning transactions efficiently.  

**Key Features:**
- Add, view, and delete books and members.
- Borrow and return books with automatic status updates.
- Responsive design for desktop and mobile.
- Modern UI with forms, tables, and icons.

**Tech Stack:**
- Backend: **Python Flask**
- Frontend: **HTML5, CSS3, Font Awesome**
- Database: **SQLite**
- Deployment: Localhost / Heroku / PythonAnywhere

---

## **Folder Structure**

Librarymanagement/
│
├─ app.py # Main Flask application
├─ models.py # Database models using SQLAlchemy
├─ templates/ # HTML templates
│ └─ index.html
└─ static/ # CSS and static files
└─ style.css

yaml
Copy
Edit

---

## **Installation & Setup**

1. **Clone the repository**
```bash
git clone <your-repo-link>
cd Librarymanagement
Install dependencies

bash
Copy
Edit
python3 -m pip install flask flask_sqlalchemy
Run the application

bash
Copy
Edit
python3 app.py
Open in Browser

cpp
Copy
Edit
http://127.0.0.1:5000/
Usage
Books Section

Add new books with title, author, ISBN, and quantity.

Delete existing books.

Members Section

Add new members with name and email.

Delete existing members.

Borrow/Return Section

Borrow a book by selecting Book ID and Member ID.

Return borrowed books.

Track borrowing history and status.

Screenshots
Books Section:

Members Section:

Borrow/Return Section:

(Replace placeholders with actual screenshots)

Future Enhancements
Add search and filter for books and members.

Track overdue books and fines.

Include user authentication for librarians.

Add a dashboard with statistics and charts.

Deploy online using Heroku or PythonAnywhere.
