import mysql.connector

# conn = mysql.connector.connect(host='127.0.0.1')
# mysqlもカーソルが必要（データベースを作成）
# cursor = conn.cursor()
# cursor.execute('CREATE DATABASE test_mysql_database')
#
# cursor.close()
# conn.close()

conn = mysql.connector.connect(host='127.0.0.1', database='test_mysql_database')
cursor = conn.cursor()
# テーブル作成
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')
# データ作成
cursor.execute('INSERT INTO persons(name) values("Ryo")')
# データ更新
# cursor.execute('UPDATE persons set name = "Michel" WHERE  id = 1')
# cursor.execute('DELETE FROM persons WHERE  id = 2')

conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

cursor.close()
conn.close()