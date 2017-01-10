import time
from functools import partial

from celery import chord
from celery.result import allow_join_result

from . import celeryapp

@celeryapp.task
def add(x,y):
    print "starting sleep add"
    time.sleep(3) 
    print "end sleep add"
    return x+y

@celeryapp.task
def slowadd(x,y):
    print "starting sleep slowadd"
    time.sleep(20) 
    print "end sleep slowadd"
    return x+y

@celeryapp.task
def tsum(list_of_num, x=0, y=0):
    return sum(list_of_num)+x+y

@celeryapp.task
def run_chord(x,y):
    callback = tsum.subtask(kwargs={"x":x,"y":y})
    header = [add.subtask((i, i)) for i in xrange(3)]
    result = chord(header)(callback)
    # tasks waiting for other tasks to finish in this way is inefficient: 
    # http://docs.celeryq.org/en/latest/userguide/tasks.html#task-synchronous-subtasks
    # with allow_join_result():
    #     res = result.get()
    #     print "Chord result: {}".format(res)
    return result.delay()
