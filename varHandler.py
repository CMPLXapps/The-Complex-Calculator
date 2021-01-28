import json
with open('cfg/var.json', 'r') as file:
	varDossier = json.load(file)
varDossier_old = varDossier.copy()
def updateVarDossier():
	global varDossier
	varDossier = {
	"a": a,
	"b": b,
	"c": c,
	"d": d,
	"e": e,
	"f": f
	}
	return
try:
	a = float(varDossier['a'])
except:
	a = 0
try:
	b = float(varDossier['b'])
except:
	b = 0
try:
	c = float(varDossier['c'])
except:
	c = 0
try:
	d = float(varDossier['d'])
except:
	d = 0
try:
	e = float(varDossier['e'])
except:
	e = 0
try:
	f = float(varDossier['f'])
except:
	f = 0
updateVarDossier()
class a_var:
	global a
	def set(self, value):
		value = eval(value)
		try:
			a = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		a = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			a = float(varDossier_old['a'])
		except:
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
class b_var:
	global b
	def set(self, value):
		value = eval(value)
		try:
			b = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		b = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			b = float(varDossier_old['b'])
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
class c_var:
	global c
	def set(self, value):
		value = eval(value)
		try:
			c = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		c = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			c = float(varDossier_old['c'])
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
class d_var:
	global d
	def set(self, value):
		value = eval(value)
		try:
			d = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		d = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			d = float(varDossier_old['d'])
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
class e_var:
	global e
	def set(self, value):
		value = eval(value)
		try:
			e = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		e = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			e = float(varDossier_old['e'])
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
class f_var:
	global f
	def set(self, value):
		value = eval(value)
		try:
			f = float(value)
			updateVarDossier()
			return '@STRING_RESPONSE~ $Variable Set!'
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $You can only set a variable to a number or the result of an equation.'
	def clear(self):
		f = 0
		updateVarDossier()
		return '@STRING_RESPONSE~ $Variable Cleared!'
	def revert(self):
		try:
			f = varDossier_old['f']
			updateVarDossier()
		except:
			updateVarDossier()
			return '@STRING_RESPONSE~ $The stored value for that variable was missing or misformatted.\nThe variable was not reverted.'
def save_variables():
	updateVarDossier()
	varDossier_old = varDossier.copy()
	with open('cfg/var.json', 'w') as file:
		json.dump(varDossier, file, indent=4)