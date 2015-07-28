import random
def has_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s) - 1):
	if s[i] == s[i + 1]:
	    return True
    return False

def random_bdays(n):
    t = []
    for i in range(n):
	bday = random. randint(1, 365)
	t.append(bday)
    return t

def count_matches(students, samples):
    count = 0
    for i in range(samples):
	t = random_bdays(students)
	if has_duplicates(t):
	    count += 1
    return count

num_students = 23
num_simulations = 1000
count = count_matches(num_students, num_simulations)

print 'After %d simulations' %num_simulations
print 'with %d students' %num_students
print 'there were %d simulations with at least one match' %count

