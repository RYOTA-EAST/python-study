import yaml

# yamlファイルに設定を書き込む
with open('config.yml', 'w') as yaml_file:
    yaml.dump({
        'web_server': {
            'host': '127.0.0.1',
            'port': 80
        },
        'db_server': {
            'host': '127.0.0.1',
            'port': 3306
        }
    }, yaml_file, default_flow_style=False)

# 読み込む
# with open('config.yml', 'r') as yaml_file:
#     data = yaml.load(yaml_file, Loader=yaml.FullLoader)
#     print(data, type(data))
#     print(data['web_server']['host'])
#     print(data['web_server']['port'])