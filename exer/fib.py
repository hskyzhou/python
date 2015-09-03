def fib(n):
	if n == 1 or n == 2 :
		return 1
	else :
		i = 2 
		f1 = 1
		f2 = 1
		while i < n :
			f3 = f1 + f2
			f1 = f2
			f2 = f3