import contextlib


def is_ok_job():
    try:
        print('do something')
        raise Exception('Error')
        return True
    except Exception:
        return False

def cleanup():
    print('clean up1')

def cleanup2():
    print('clean up2')



with contextlib.ExitStack() as stack:
    stack.callback(cleanup)
    stack.callback(cleanup2)

    @stack.callback
    def cleanup3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.push()