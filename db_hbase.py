import happybase

connection = happybase.Connection('localhost')
connection.open()
# テーブルを作成
connection.create_table(b'sns', {'blog': dict()})

table = connection.table(b'sns')
# データを作成
table.put(
    b'user1', {
        b'blog:bitcoin': b'user1 about bitcoin',
        b'blog:soccer': b'user1 about soccer'
    }
)

table.put(
    b'user2', {
        b'blog:soccer': b'user2 about soccer'
    }
)
# 確認
print(list(table.scan()))
print()
# user1のデータを確認
print(list(table.scan(row_prefix=b'user1')))
print()
# blogがsoccerのデータ確認
print(list(table.scan(columns=[b'blog:soccer'])))

connection.disable_table(b'sns')
connection.delete_table(b'sns')
