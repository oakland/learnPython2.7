class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print "%s: %s" % (self.name, self.score)
		
bart = Student("Bart Simpson", 29)
lisa = Student("Lisa Simpson", 87)

bart.print_score()
lisa.print_score()