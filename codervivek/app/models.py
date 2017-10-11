

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

class StudentToCourse(db.Model):

    __tablename__='student_to_course'

    student_roll_no = db.Column(db.Integer, db.ForeignKey('student.roll_no'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    class_attended = db.Column(db.Integer)
    student = db.relationship("Student", back_populates="courses")
    course = db.relationship("Course", back_populates="students")

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


class Professor(db.Model):

    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    username=db.Column(db.String(100))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship("Department", back_populates="professors")


class Year(db.Model):

    __tablename__ = 'year'
    
    num = db.Column(db.Integer, primary_key=True)
    students = db.relationship("Student", back_populates="year")
    courses = db.relationship("Course", back_populates="year")
    

class Department(db.Model):

    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    professors = db.relationship("Professor",back_populates="department")
    students = db.relationship("Student", back_populates="department")



class Courses(db.Model):

    __tablename__='course'

    id = db.Column(db.Integer, primary_key=True)
    student = db.relationship("StudentToCourse", back_populates="course")
    department = db.relationship("Department", back_populates="courses")
    year = db.relationship("Year", back_populates="courses")
    optional = db.Column(db.Boolean, unique=False, default=False)
    credits = db.Column(db.Integer)
    num_of_classes = db.Column(db.Integer)
    num_of_tutorial = db.Column(db.Integer)
    num_of_practicals = db.Column(db.Integer)




# class Batch(db.Model):

#     __tablename__='batchs'
#     department = db.relationship("Department", back_populates="students")
#     year = db.relationship("Year", back_populates="batch")
