

from app import db

class Updatelist(db.Model):

    __tablename__ = 'updatelists'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(2000))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, data):
        self.data = data[:30]

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Updatelist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Updatelist: {}>".format(self.data)

    def __str__(self):
        return self.data

class StudentToCourse(db.Model):

    __tablename__='student_to_course'

    student_roll_no = db.Column(db.Integer, db.ForeignKey('student.roll_no'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    class_attended = db.Column(db.Integer)
    student = db.relationship("Student", back_populates="courses")
    course = db.relationship("Course", back_populates="students")

    # def __init__(self, rollno, courseid, class_attended):
    #     self.student_roll_no = rollno
    #     self.course_id = courseid
    #     self.class_attended = class_attended

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @staticmethod
    # def get_all():
    #     return StudentToCourse.query.all()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

    def __str__(self):
        return self.student_roll_no + ' to ' + self.course_id

class Student(db.Model):

    __tablename__='student'

    roll_no = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship("Department", back_populates="student")
    year_num = db.Column(db.Integer, db.ForeignKey('year.num'))
    year = db.relationship("Year", back_populates="students")
    name=db.Column(db.String(200))
    username = db.Column(db.String(100))
    # batch = db.relationship("Batch", back_populates="students")
    courses = db.relationship("StudentToCourse", back_populates='student')

    def __init__(self, rollno, depid, ye, name, username):
        self.roll_no = rollno
        self.department_id = depid
        self.year_num = ye
        self.name = name
        self.username = username

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Student.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return self.roll_no

class ProfessorToCourse(db.Model):

    __tablename__='professor_to_course'

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    professor = db.relationship("Professor", back_populates="courses")
    course = db.relationship("Course", back_populates="professors")

    # def __str__(self):
    #     return self.professor_id + ' to ' + self.course_id

class Professor(db.Model):

    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    username=db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship("Department", back_populates="professors")
    course = db.relationship("ProfessorToCourse", back_populates="professor")

    def __init__(self, id, name,username, depid):
        self.id = id
        self.department_id = depid
        self.name = name
        self.username = username    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Professor.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return self.id + ' name: ' + self.name


class Year(db.Model):

    __tablename__ = 'year'
    
    num = db.Column(db.Integer, primary_key=True)
    students = db.relationship("Student", back_populates="year")
    courses = db.relationship("Course", back_populates="year")

    def __init__(self, year):
        self.num = year    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Year.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __str__(self):
        return self.num
    

class Department(db.Model):

    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    professors = db.relationship("Professor",back_populates="department")
    students = db.relationship("Student", back_populates="department")

    def __init__(self, id, name):
        self.id = id
        self.name = name
            
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Updatelist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __str__(self):
        return self.id + ' name ' + self.name

class Courses(db.Model):

    __tablename__='course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    student = db.relationship("StudentToCourse", back_populates="course")
    professor=db.relationship("ProfessorToCourse", back_populates="course")
    department = db.relationship("Department", back_populates="courses")
    year = db.relationship("Year", back_populates="courses")
    optional = db.Column(db.Boolean, unique=False, default=False)
    credits = db.Column(db.Integer)
    num_of_classes = db.Column(db.Integer)
    num_of_tutorial = db.Column(db.Integer)
    num_of_practicals = db.Column(db.Integer)

    def __init__(self,id,name,optional,credits,numclasses,numtut,numprac):
        self.id = id
        self.name = name
        self.opal = optional
        self.credits = credits
        self.num_of_classes = numclasses
        self.num_of_tutorial = numtut
        self.num_of_practicals = numprac    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Updatelist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def __str__(self):
        return self.id + ''




# class Batch(db.Model):

#     __tablename__='batchs'
#     department = db.relationship("Department", back_populates="students")
#     year = db.relationship("Year", back_populates="batch")
