from app import db, Student

# CRUD - Create Read Update Delete

## CREATE ###
# --------------------------------------------------------
## Create a new entry into table
manasi = Student('Manasi', 18)
db.session.add(manasi)
db.session.commit() # not technically saved until you commit

## READ ### read from Hours table to make queries on total hours, hours per user, etc.
# --------------------------------------------------------
## Read database
all_students = Student.query.all() # returns all objects in table
print(all_students)
print('\n')

## Select by ID
student_one = Student.query.get(1)
print(student_one.name) # should be first person we add, 'Matt'
print('\n')
## Filter by name
# this produces SQL code!!
students_18 = Student.query.filter_by(age=18) # if hours < num, date = date_range
print(students_18.all()) # should be ian, nihal, and manasi in this order
print('\n')
## UPDATE ###
# --------------------------------------------------------
student = Student.query.get(2) # forgets password? forgets email? or typos?
student.age = 17 # software eng watch out: catching data types e.g. 'seventeen' (Argument Testing)
db.session.add(student)
db.session.commit()

## DELETE ###
# --------------------------------------------------------
# notice - if you run this a few times in a row you will get errors -- WHY??
student = Student.query.get(3)
db.session.delete(student)
db.session.commit()


all_students = Student.query.all()
print(all_students)




# Data structures to consider:

# JSON - dict['key1']['key2'] = lighting fast, but need to know keys
# {'event1': {'date': 'June 17, 2020',
#             'hours': 2,
#             'pillar': 'WISE'},
#  'event2': {'date': 'June 20, 2020',
#             'hours': 3,
#             'pillar': 'WISTEM2D'}}


# option 1
# add on to existing hours e.g. adding to a total

# option 2
# appending hours to a list


