import datetime
import sys
import json
from contextlib import redirect_stdout, redirect_stderr


class Task:
    def __init__(self, task_id, args):
        self._task_id = task_id
        self._args = args

    def log(self, message):
        log = {
            'task-id': self._task_id,
            'timestamp': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
            'log-message': message
        }
        print(json.dumps(log))

    def exec(self):
        self.log('EXEC EC2 TASK')
        self.log(self._args)


if __name__ == '__main__':
    log_file_handle = None
    try:
        task_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        log_file_path = f'/opt/poc-s3-lambda-ec2/logs/task-{task_id}.log'
        log_file_handle = open(log_file_path, 'w')
        with redirect_stdout(log_file_handle), redirect_stderr(log_file_handle):
            task = Task(task_id, sys.argv)
            task.exec()
    finally:
        if log_file_handle is not None:
            log_file_handle.close()
