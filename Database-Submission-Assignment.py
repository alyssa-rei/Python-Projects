
import sqlite3


# Creating database
conn = sqlite3.connect('dBassignment.db')

# Executing database connection, creating table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_newdb( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_data TEXT \
        )")
    conn.commit()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

print(fileList)


# Creating for loop to iterate "fileList",
# Printing indices ending with ".txt"
for x in fileList:
    if x.endswith('.txt'):
        print(x)
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_newdb(col_data) VALUES (?)", (x,))
# Committing change(s), closing connection
    conn.commit()
conn.close()
