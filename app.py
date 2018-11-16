class Member:
	def __init__(self, full_name):
		self.full_name = full_name
		

class Student(Member):
	def __init__(self, full_name, reason):
		super().__init__(full_name)
		self.reason = reason
	def introduction:
		print(f'Hi, my name is {self.full_name}, I came here for {self.reason}.')

class Teacher(Member):
	def __init__(self, full_name, bio, skills)
		super().__init__(full_name)
		self.bio = bio
		self.skills = skills
	def add_skills(skills):
		self.skills

	def introduction:
		print(f'Hi, my name is {self.full_name}, {self.bio} and I teach {self.skills}.')


class Workshop:
	def __init__(self, date, subject):
		self.date = date
		self.subject = subject
		self.students = []
		self.teachers = []
	def add_participant(self, participant):
		if participant.type == 'Instructor':
			self.instructors.append(participant)
		else:
			slef.students.append(participant)
	def print_details(self):
		instructor_list = ''
		student_list = ''
		for i, instructor in enumerate(self.instructors):
			if i < len(self.instructors) - 1:
				instructor_list += instructor.full_name + ', '
			else:
				instructor_list += 'and ' + instructor.full_name


my_workshop.add_participant(Harry)
my_workshop.add_participant(Hermione)
my_workshop.add_participant(Ron)
Workshop.print_details()
















		





