import datetime
import time
class AplusB(object):

    @classmethod
    def _a(self,a,b,c=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),**kwargs):
        print(c)
        return a+b,c,kwargs,


number_sum,current_time,k=AplusB._a(1,2)
print(number_sum,current_time,k)
time.sleep(2)
number_sum,current_time,k=AplusB._a(3,4)
print(number_sum,current_time,k)