import contextlib
import os

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

# suppress抑圧するm、エラーが出ても何も出さない
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')