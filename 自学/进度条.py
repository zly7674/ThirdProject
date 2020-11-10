import sys
import time
def jindu():
      while True:
         for i in range(11):
                time.sleep(0.5)
                print('\r{0}'.format('▉'*i,(i*10)), end='')




jindu()
