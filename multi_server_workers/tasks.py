import time

from celery import chord

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
def tsum(list_of_num):
    return sum(list_of_num)

@celeryapp.task
def run_chord(x,y):
    callback = tsum.subtask()
    header = [add.subtask((i, i)) for i in xrange(100)]
    result = chord(header)(callback)
    res = result.get()
    print "Chord result: {}".format(res)
    return res
