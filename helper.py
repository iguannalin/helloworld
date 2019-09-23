#
# Helper functions
#
import sys, re

def isInvalid(key,val):
  print('isInvalid',key,val)
  if not key or not val:
    print('isInvalidKeyorVal',key,val)
    return True
  if sys.getsizeof(val) > 1000000:
    print('isInvalidValSize',key,val)
    return True
  elif len(key) < 1 or len(key) > 200:
    print('isInvalidKeySize',key,val)
    return True
  elif re.match('^[\w-]+$', key) is None:
    print('isInvalidKeyChar',key,val)
    return True
  return False