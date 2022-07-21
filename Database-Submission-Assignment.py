
import sqlite3



conn = sqlite3.connect('dBassignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_newdb( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_data TEXT \
        )")
    conn.commit()
conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

print(fileList)


for x in fileList:
    if x.endswith('.txt'):
        print(x)
    


conn = sqlite3.connect('dBassignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_newdb(col_data) VALUES (?)", (x, ))
    conn.commit()
conn.close()
