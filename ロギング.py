import logging

# ログをファイルに保存する
# logging.basicConfig(filename='test.log', level=logging.INFO)
# フォーマットを作成する（時間を表示）
formatter = '%(asctime)s:%(message)s'
# ログのレベルを決める
logging.basicConfig(level=logging.INFO, format=formatter)

logging.info('info {}'.format('test'))

logging.basicConfig(level=logging.INFO)


# ログにフィルターをかける
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return 'password' not in log_message


logger = logging.getLogger(__name__)
logger.addFilter(NoPassFilter())
logger.info('from main')
logger.info('from main password = "test"')

logger.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})