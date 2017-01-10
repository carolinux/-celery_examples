from multi_server_workers import celeryapp

import time
import sys

task_name = sys.argv[1]
task = celeryapp.send_task("multi_server_workers.tasks.{}".format(task_name),
                         kwargs={"x":12, "y":40})

res = task.get() # synchronous wait
print "Result {}".format(res)
