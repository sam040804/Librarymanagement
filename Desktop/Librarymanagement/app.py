from flask import Flask, render_template, request, redirect, url_for
from models import db, Book, Member, Transaction
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# Home / Dashboard
@app.route('/')
def index():
    books = Book.query.all()
    members = Member.query.all()
    transactions = Transaction.query.all()
    return render_template('index.html', books=books, members=members, transactions=transactions)

# Add Book
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    quantity = request.form['quantity']
    new_book = Book(title=title, author=author, isbn=isbn, quantity=quantity)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('index'))

# Delete Book
@app.route('/delete_book/<int:id>')
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

# Add Member
@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['name']
    email = request.form['email']
    new_member = Member(name=name, email=email)
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for('index'))

# Delete Member
@app.route('/delete_member/<int:id>')
def delete_member(id):
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('index'))

# Borrow Book
@app.route('/borrow', methods=['POST'])
def borrow_book():
    book_id = request.form['book_id']
    member_id = request.form['member_id']
    book = Book.query.get(book_id)
    if book.quantity > 0:
        book.quantity -= 1
        transaction = Transaction(book_id=book_id, member_id=member_id, borrow_date=date.today())
        db.session.add(transaction)
        db.session.commit()
    return redirect(url_for('index'))

# Return Book
@app.route('/return/<int:transaction_id>')
def return_book(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    book = Book.query.get(transaction.book_id)
    if transaction.status == 'borrowed':
        transaction.status = 'returned'
        transaction.return_date = date.today()
        book.quantity += 1
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
