import mysql.connector as mysql
from tabulate import tabulate

# insert MySQL Database information here
HOST = "localhost"
DATABASE = "db-test"
USER = "app1.0.0"
PASSWORD = ""

# connect to the database
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
# get server information
print(db_connection.get_server_info())

# get the db cursor
cursor = db_connection.cursor()
# get database information
cursor.execute("select database();")
database_name = cursor.fetchone()
print("[+] You are connected to the database:", database_name)

# insert data

#data source
books = [
    {
        "name": "Automate the Boring Stuff with Python: Practical Programming for Total Beginners",
        "author": "Al Sweigart",
        "price": 17.76,
        "url": "https://amzn.to/2YAncdY"
    },
    {
        "name": "Python Crash Course: A Hands-On, Project-Based Introduction to Programming",
        "author": "Eric Matthes",
        "price": 22.97,
        "url": "https://amzn.to/2yQfQZl"
    },
    {
        "name": "MySQL for Python",
        "author": "Albert Lukaszewski",
        "price": 49.99,
    }
]
# iterate over books list
for book in books:
    id = book.get("id")
    name = book.get("name")
    author = book.get("author")
    price = book.get("price")
    url = book.get("url")

# insert each data sig. as row in mysql
# insert each book as a row in MySQL
    cursor.execute("""insert into book (id, name, author, price, url) values (
        %s, %s, %s, %s, %s
    )
    """, params=(id, name, author, price, url))
    # commit insertion

    print(f"[+] Inserted the book: {name}")
    #db_connection.commit()