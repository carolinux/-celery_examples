from multi_server_workers import celeryapp

import time
import sys

from celery.result import AsyncResult

task_name = sys.argv[1]
task = celeryapp.send_task("multi_server_workers.tasks.{}".format(task_name),
                         kwargs={"x":12, "y":40})

#sys.exit(0) # even if i exit here, the task will finish!
res = task

while(isinstance(res,AsyncResult)):
    res = res.get() # synchronous wait
        
print res
