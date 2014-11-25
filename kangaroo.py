class kangaroo(object):
	def __init__(self,pouch_contents=[]):
		self.pouch_contents=pouch_contents
	def put_in_pouch(self,contents):
		self.pouch_contents.append(contents)
	def __str__(self):
		return object.__str__(self)+str(self.pouch_contents)
kanga=kangaroo()
roo=kangaroo()
kanga.put_in_pouch(roo)
print kanga
