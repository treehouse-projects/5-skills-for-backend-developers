import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE articles (title TEXT, content TEXT)')
cursor.execute('INSERT INTO articles (title, content) VALUES ("First post...", "From my new blog app!")')
cursor.execute('INSERT INTO articles (title, content) VALUES ("We got a puppy!", "Her name is Chai.")')
conn.commit()
conn.close()
