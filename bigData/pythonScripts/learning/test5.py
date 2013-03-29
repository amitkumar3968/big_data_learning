class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Add your method here!
	def description(self):
		print "hippo's name %s" % (self.name)
		print "hippo's Age %d" % (self.age)

hippo = Animal("Jeffery", 8)
hippo.description()
