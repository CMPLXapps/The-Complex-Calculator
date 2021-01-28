import math as M
import random as R
import stat as S
pi = 3.1415926535897932384626433832795028841971693993
tau = 2 * pi
eul = 2.7182818284590452353602874713527
sqrt = lambda x: x ** (1 / 2)
cbrt = lambda x: x ** (1 / 3)
tsrt = lambda x: x ** (1 / 4)
root = lambda x, n: x ** (1 / n)
fact = lambda x: factorial(x)
exp = lambda x, n: x ** n
log = lambda x, n=10: M.log(x, n)
ln = lambda x: M.log(x, 2.7182818284590452353602874713527)
stdev = lambda x: S.stdev(CONVTOLIST(x))
rand = lambda x, y: R.randint(x, y)
mode = lambda x: S.mode(CONVTOLIST(x))
most = mode
mid = median()
middle = median()
dev = stdev
r = rand
randint = rand
absv = abs()
avg = mean()
average = mean()
def mean(x):
	y = 0
	for i in CONVTOLIST(x):
		y = y + i
	return y / len(CONVTOLIST(x))
def median(x):
	x = CONVTOLIST(x)
	if (len(x) % 2) == 1:
		y = int((len(x) / 2) - 0.5)
		return x[y]
	else:
		y = (x[(len(x) / 2)] + x[((len(x) / 2) - 1)]) / 2
		return y
def range(x):
	x = CONVTOLIST(x)
	lowest = x[0]
	highest = x[0]
	for i in x:
		i = abs(i)
		highest -= i
		lowest += i
	for i in x:
		if i < lowest:
			lowest = i
		if i > highest:
			highest = i
	return lowest - highest
def wdiv(x, n):
	y = x
	z = 0
	while True:
		if n > y:
			if z == 0:
				return '@STRING_RESPONSE~ $' + str(x) + ' isn\'t divisible by ' + str(n)
			else:
				return (z, y)
		y -= n
		z += 1
def factorial(x):
	if x > 150:
		return '@STRING_RESPONSE~ $That result is too large to process, but it\'s essentially infinite.'
	n = 1
	for i in range(1, x):
		n = n * x
		x -= 1
	return n
def CONVTOLIST(x):
	x = str(x)
	if x[0] != '[':
		x = '[' + x
	if x[len(x)] != ']':
		x = x + ']'
	return list(x)