import sqlite3

def create_tables():
    conn=sqlite3.connect("myproject.db")
    cur=conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Products')
    cur.execute('DROP TABLE IF EXISTS Orders')


    cur.execute('''CREATE TABLE Products(
        ProductId INTEGER PRIMARY KEY,
        ProductName VARCHAR(255) NOT NULL,
        ProductDescription VARCHAR(255) NOT NULL,
        Price FLOAT,
        Stock INTEGER
    );
    ''')

    cur.execute('''CREATE TABLE Orders(
       OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
       Quantity INTEGER,
       Product_id INTEGER,
       FOREIGN KEY (Product_id) REFERENCES Products(ProductId)
    );
    ''')

    cur.execute('''
    INSERT INTO Products(ProductId,ProductName,ProductDescription,Price,Stock)
    Values(1,"Samsung","This is good product",45000.00,5)
    ''')

    conn.commit()
    conn.close()

create_tables()

