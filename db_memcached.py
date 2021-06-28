import sqlite3
import time

import memcache
db = memcache.Client(['127.0.0.1:11211'])

# timeはキャッシュを何秒保持するか
# db.set('web_page', 'value1', time=3)
# time.sleep(1)
# print(db.get('web_page'))

# db.set('counter', 0)
# db.incr('counter', 1)
# print(db.get('counter'))

conn = sqlite3.connect('test_sqlite3.db')
curs = conn.cursor()
# curs.execute(
#     'CREATE TABLE persons('
#     'employ_id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# curs.execute('INSERT INTO persons(name) values("Mike")')
# conn.commit()
# conn.close()


# sqliteとキャッシュ組み合わせる
def get_employ_id(name):
    # キャッシュ(memcache)にある場合、キャッシュを利用する
    employ_id = db.get(name)
    if employ_id:
        return employ_id
    # ない場合sqliteから探す
    curs.execute(
        'SELECT * FROM persons WHERE name = "{}"'.format(name)
    )
    person = curs.fetchone()
    # sqliteにもない場合エラーを出す
    if not person:
        raise Exception('No employ')
    employ_id, name = person
    # sqliteの内容を60秒キャッシュに保持する
    db.set(name, employ_id, time=60)
    return employ_id


print(get_employ_id("Mike"))