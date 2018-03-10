#returns True if this student will pass their exam, and False if otherwise.
#a student passes their exam if they study for more than 5 hours but less
#than 40 (at 40, their brain turns to mush)
def pass_exam(hours_studied):
	if hours_studied < 40 and 5 < hours_studied:
		return True
	return False	
