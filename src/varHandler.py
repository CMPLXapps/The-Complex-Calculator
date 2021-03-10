#!usr/bin/env python3
import json
with open('cfg/var.json', 'r') as file:
	varDossier = json.load(file)
varDossier_old = varDossier.copy()
def updateVarDossier(*args, **kwargs):
	global varDossier
	varDossier = {'a': a.Value, 'b': b.Value, 'c': c.Value, 'd': d.Value, 'e': e.Value, 'f': f.Value}
class FloatExtender:
	def __init__(self, *args, **kwargs):
		self.Value = 0
	def __call__(self, *args, **kwargs):
		pass
	def __repr__(self, *args, **kwargs):
		return str(self.Value)
	#String Methods
	def __len__(self, *args, **kwargs):
		return len(str(self.Value))
	def __unicode__(self, *args, **kwargs):
		return unicode(str(self.Value))
	def __hash__(self, *args, **kwargs):
		return hash(str(self.Value))
	#Type Conversions
	def __str__(self, *args, **kwargs):
		return str(self.Value)
	def __float__(self, *args, **kwargs):
		return float(self.Value)
	def __int__(self, *args, **kwargs):
		return int(self.Value)
	def __nonzero__(self, *args, **kwargs):
		return bool(self.Value)
	def __complex__(self, *args, **kwargs):
		return complex(self.Value)
	def __oct__(self, *args, **kwargs):
		return oct(self.Value)
	def __hex__(self, *args, **kwargs):
		return hex(self.Value)
	def __index__(self, *args, **kwargs):
		pass
	#Augmentation
	def __pos__(self, *args, **kwargs):
		return +self.Value
	def __neg__(self, *args, **kwargs):
		return -self.Value
	def __abs__(self, *args, **kwargs):
		return abs(self.Value)
	def __invert__(self, *args, **kwargs):
		return ~self.Value
	def __round__(self, n=0, *args, **kwargs):
		return round(self.Value, n)
	def __iadd__(self, other, *args, **kwargs):
		self.Value += other
	def __isub__(self, other, *args, **kwargs):
		self.Value -= other
	def __imul__(self, other, *args, **kwargs):
		self.Value *= other
	def __ifloordiv__(self, other, *args, **kwargs):
		self.Value //= other
	def __idiv__(self, other, *args, **kwargs):
		self.Value /= other
	def __itruediv__(self, other, *args, **kwargs):
		pass
	def __imod__(self, other, *args, **kwargs):
		self.Value %= other
	def __ipow__(self, other, *args, **kwargs):
		self.Value **= other
	def __ilshift__(self, other, *args, **kwargs):
		self.Value <<= other
	def __irshift__(self, other, *args, **kwargs):
		self.Value >>= other
	def __iand__(self, other, *args, **kwargs):
		self.Value &= other
	def __ior__(self, other, *args, **kwargs):
		self.Value |= other
	def __ixor__(self, other, *args, **kwargs):
		self.Value ^= other
	#Operator Methods
	def __add__(self, other, *args, **kwargs):
		return self.Value + other
	def __sub__(self, other, *args, **kwargs):
		return self.Value - other
	def __mul__(self, other, *args, **kwargs):
		return self.Value * other
	def __floordiv__(self, other, *args, **kwargs):
		return self.Value // other
	def __truediv__(self, other, *args, **kwargs):
		return self.Value / other
	def __mod__(self, other, *args, **kwargs):
		return self.Value % other
	def __pow__(self, other, *args, **kwargs):
		return self.Value ** other
	#Comparison
	def __lt__(self, other, *args, **kwargs):
		return self.Value < other
	def __le__(self, other, *args, **kwargs):
		return self.Value <= other
	def __eq__(self, other, *args, **kwargs):
		return self.Value == other
	def __ne__(self, other, *args, **kwargs):
		return self.Value != other
	def __ge__(self, other, *args, **kwargs):
		return self.Value >= other
class VAR_TEMPLATE(FloatExtender):
	def __init__(self, Key, *args, **kwargs):
		self.Key = Key
		self.Value = float(varDossier[Key])
	def __repr__(self, *args, **kwargs):
		return f'Variable {self.Key.upper()}; {self.Value}' 
	@property
	def set(self, newValue, *args, **kwargs):
		try:
			self.Value = float(newValue)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except Exception as e:
			return f'@STRING_RESPONSE~ $An error occurred while programming the variable:\n\n{e}'
	@property
	def save(self, *args, **kwargs):
		return save_variables([self.Key, '0'])    # May return function object instead of return value
	@property
	def clear(self, *args, **kwargs):
		self.Value = 0.0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	@property
	def revert(self, *args, **kwargs):
		try:
			self.Value = float(varDossier_old[self.Key])
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Reverted!'
		except Exception as e:
			return f'@STRING_RESPONSE~ $Variable could not be reverted;\n{e}'
def save_variables(include=['a', 'b', 'c', 'd', 'e', 'f', '0'], *args, **kwargs):
	if not isinstance(include, list) and not isinstance(include, tuple) and not isinstance(include, str):
		return '@STRING_RESPONSE~ $Invalid Parameters'
	if isinstance(include, str):
		include = [include, '0']
	updateVarDossier()
	for i in include:
		if i == '0':
			continue
		varDossier_old[i] = varDossier[i]
	with open('cfg/var.json', 'w') as file:
		json.dump(varDossier_old, file, indent=4)
	return '@STRING_RESPONSE~ $Saved!'
a = VAR_TEMPLATE('a')
b = VAR_TEMPLATE('b')
c = VAR_TEMPLATE('c')
d = VAR_TEMPLATE('d')
e = VAR_TEMPLATE('e')
f = VAR_TEMPLATE('f')