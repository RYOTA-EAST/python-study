import sqlite3
# :memory:でメモリー上に作成
# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory:')

# マウスのカーソルのようなものが必要
curs = conn.cursor()
# テーブル作成（executeの中にSQL文を書く）
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')

# データ作成
curs.execute('INSERT INTO persons(name) values("Mike")')
curs.execute('INSERT INTO persons(name) values("Nancy")')
curs.execute('INSERT INTO persons(name) values("Jun")')

# データ更新
curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')

# データ削除
curs.execute('DELETE FROM persons WHERE name = "Michel"')
# コミットしないと保存されない
conn.commit()

# データの読み取り(SQL文の後にcurs.fetchallで出力)
curs.execute('SELECT * from persons;')
print(curs.fetchall())

curs.close()
conn.close()
