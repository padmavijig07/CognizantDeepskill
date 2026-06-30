from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URL = "postgresql+psycopg2://postgres:mokitha%22005@localhost:5432/hr_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Student(Base):
    __tablename__ = "student_info"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    department = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# CREATE
student = Student(name="Bavishika", department="Computer Science")
session.add(student)
session.commit()

# READ
print("Students:")
for s in session.query(Student).all():
    print(s.id, s.name, s.department)

# UPDATE
student = session.query(Student).filter_by(name="Bavishika").first()
student.department = "AI & DS"
session.commit()

# DELETE
student = session.query(Student).filter_by(name="Bavishika").first()
session.delete(student)
session.commit()

print("CRUD Operations Completed Successfully!")