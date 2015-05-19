def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def doubling(x, y):
	a = 3.0
	p = 17

	lamb = (3.0*(x**2.0)+a)*modinv((2.0*y), p)%p
	xr = ((lamb**2.0) - (2.0*x))%p
	yr = ((lamb*x)-(lamb*xr)-(y))%p

	return xr, yr
	

def adding(x1, y1, x2, y2):
	p = 17
	a = 3.0
	if x2 == x1 and y1 == y2:
		lamb = ((3.0*(x1**2.0))+a) * modinv((2.0*y1), p)

	else:
		delta_x = x2-x1
		while delta_x<0:
			delta_x+=p

		if delta_x == 0 and y2==(-y1%p):
			return None, None
		else:
			lamb = (y2-y1) * modinv(delta_x,p)

	lamb = lamb%p
	x = ((lamb**2)-x1-x2)%p
	y = ((lamb*x1)-(lamb*x)-y1)%p
	#print lamb
	return x, y



## Addition
#x=3.0
#y=13.0

#for i in range(2, 29):
	#print "i:",i	
#	x, y = adding(3.0, 13.0, x, y)
#	if x == None:
#		print "["+str(i)+"]P = Infinity"
#		break
#	print "["+str(i)+"]P = ("+str(x) + ", " + str(y) + ")"


## Doubling
#x = 1
#y = 7
	
#count = 1
#for i in range(5):
#	x, y = doubling(x, y)
#	count = count*2
#	print "["+str(count)+"]P = ("+str(x) + ", " + str(y) + ")"


#print adding(7.0, 5.0, 7.0, 12.0)
print doubling(7, 5)




