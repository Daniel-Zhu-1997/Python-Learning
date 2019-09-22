# climb bugs
# -*- coding: utf-8 -*-

import os, sqlite3

db_file =  'test.db'

# 初始数据:
'''
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute("insert into user values ('A-001', 'Adam', 95)")
cursor.execute("insert into user values ('A-002', 'Bart', 62)")
cursor.execute("insert into user values ('A-003', 'Lisa', 78)")
cursor.execute("insert into user values ('A-004', 'Lisa2', 78)")
cursor.close()
conn.commit()
conn.close()
'''
def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''SELECT name,score
FROM user
WHERE score > ?
ORDER BY score ASC;''', (low, ))
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()
    
# 测试:
# assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
# assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
# assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print(get_score_in(80, 95), 'Pass')
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('''SELECT name,score
FROM user;''')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()