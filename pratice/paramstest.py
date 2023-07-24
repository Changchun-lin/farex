
def xxxa_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   for v in args:
       print('Optional argument (*args): ', v)
   for k, v in kwargs.items():
       print('Optional argument %s (*kwargs): %s' % (k, v))
xxxa_kwargs(1, 2, 3, 4, k1=5, k2=6)

#https://blog.csdn.net/helloxiaozhe/article/details/78959319/