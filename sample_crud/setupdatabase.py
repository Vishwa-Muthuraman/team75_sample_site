from app import db, Student

# Creates all tables - transforms model classes to a database
db.create_all()

matt = Student('Matt', 25) # these inputs should come from UI
ian = Student('Ian', 18)
nihal = Student('Nihal', 18)

# add in bulk
db.session.add_all([matt, ian, nihal])

# or add individually
# db.session.add(matt) 
# probably how we would want to implement 
# imagine we have a create new user button

print(matt.id) # -> None
print(ian.__repr__)
# save changes to database
db.session.commit()
print(matt.id) # 1

# numpy => numpy datatype 
# custom class => class object, e.g. Student object

