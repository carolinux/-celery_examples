import time
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
