from constantsContainer import *
import math as M
import random as R
import stat as S
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
	lowest = 0
	highest = 0
	for i in x:
		i = abs(i)
		highest -= i
		lowest += i
	for i in x:
		if i < lowest:
			lowest = i
		if i > highest:
			highest = i
	RString = 'The lowest is ' + str(lowest) + ', and the highest is ' + str(highest)
	difference = highest - lowest
	return {"tag": "@DICT_RESPONSE~ $", "print": RString, "valid": True, "numbers": {"diff": difference, "interval": [lowest, highest]}}
def wdiv(x, n):
	y = x
	z = 0
	while True:
		if n > y:
			if z == 0:
				RString = str(x) + ' isn\'t divisible by ' + str(n)
				return {"tag": "@DICT_RESPONSE~ $", "print": RString, "valid": False, "numbers": []}
			else:
				RString = str(z) + ', with a remainder of ' + str(y)
				return {"tag": "@DICT_RESPONSE~ $", "print": RString, "valid": True, "numbers": [z, y]}
		y -= n
		z += 1
def factorial(x):
	assert (x <= 150), '@STRING_RESPONSE~ $That result is too large to process, but it\'s essentially infinite.'
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