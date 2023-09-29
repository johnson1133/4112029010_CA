# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:23:01 2023

@author: User
"""

import sqlite3


conn = sqlite3.connect('BBQ.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS meat (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  price INTEGER,
                  quantity INTEGER
                  )''')


cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('beaf', 55, 10)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)")


cursor.execute("SELECT * FROM meat")
print("新增三筆資料後的表格內容:")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")


cursor.execute("SELECT * FROM meat")
print("\n修改價格和數量後的表格內容:")
for row in cursor.fetchall():
    print(row)


cursor.execute("DELETE FROM meat WHERE price = 40")


cursor.execute("SELECT * FROM meat")
print("\n刪除價格為 40 的資料後的表格內容:")
for row in cursor.fetchall():
    print(row)


conn.commit()
conn.close()

