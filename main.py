import datetime
import sys
import time
from contextlib import redirect_stdout, redirect_stderr

if __name__ == '__main__':
    try:
        log_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        log_file_path = f'logs/task-{log_timestamp}.log'
        log_file_handle = open(log_file_path, 'w')
        with redirect_stdout(log_file_handle), redirect_stderr(log_file_handle):
            print('EXEC EC2 TASK')
            print(sys.argv)
    finally:
        if log_file_handle is not None:
            log_file_handle.close()
