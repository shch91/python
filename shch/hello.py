import redis
import sys
import time

r=redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
try:
    id=sys.argv[1]
except:
    print('input argument error')
    sys.exit(0)
if r.llen(id)>=5 and time.time()-float(r.lindex(id,4))<=3600:
    print("you are forbidden logining" )
else:
    print("you are allow to login")
    r.lpush(id,time.time())