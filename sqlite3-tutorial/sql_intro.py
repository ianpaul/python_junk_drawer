import sqlite3 

db = sqlite3.connect('books.db')

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    title text NOT NULL,
    author text NOT NULL,
    price real);''')

## go to https://sqlitebrowser.org
# https://docs.python.org/3/library/sqlite3.html

cur.execute('''INSERT INTO books(id, title, author, price)
         VALUES('1', 'Untold Stories', 'Alan Bennett', '11.99')''')

book_list = [('2', 'Lucky Jim', 'Kingsley Amis', '9.99'),
             ('3', 'Animal Farm', 'George Orwell', '7.49'),
             ('4', 'Why I am so Clever', 'Friedrich Nietzche', '1.99'),
             ('5', 'Human Compatible: AI and the Problem of Control', 'Stuart J. Russell', '4.99'),
             ('6', 'Life 3.0: Being Human in the Age of Artifical Intelligence', 'Max Tegmark', '13.99'),
             ('7', 'Superintelligence: Paths, Dangers, Dangers, Strategies', 'Nick Bostrom', '8.36')
             ]
cur.executemany('''INSERT INTO books(id, title, author, price)
         VALUES(?,?,?,?)''',book_list)

cur.execute('SELECT * FROM books')
print(cur.fetchall())

db.commit()
db.close()