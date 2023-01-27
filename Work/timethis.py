import time
def timethis(func):
  start=time.time()
  r=func(*args,**kwargs)
  end=time.time()
  print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
