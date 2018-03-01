from __future__ import print_function

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Student(BaseModel):
    __tablename__ = 'students'
    name = Column('name', String(255), nullable=False)
    login = Column('login', String(255))
    password = Column('password', String(255)) #hash
    avatar = Column('avatar', String(255)) #default='2183364644805e13920dc9aff277f44f' hash картошки
    cv = Column('cv', String(255)) #hash


class Employer(BaseModel):
    __tablename__ = 'employers'
    name = Column('name', String(255), nullable=False)
    login = Column('login', String(255))
    password = Column('password', String(255))  # hash
    avatar = Column('avatar', String(255))  # default='2183364644805e13920dc9aff277f44f' hash картошки
    contacts = Column('contacts', String(255))
    description = Column('description', String(1500))


class Event(BaseModel):
    '''
    темы дипломных работ или стажировки
    '''
    __tablename__ = 'events'
    name = Column('name', String(255))
    description = Column('description', String(1500))
    diploma = Column('diploma', Boolean) #true - если тема диплома, false - усли стажировка
    employer_id = Column('employer_id', Integer, ForeignKey('employers.id'))

    employer = relationship(Employer)



class Document(BaseModel):
    __tablename__ = 'documents'
    filename = Column('filename', String(255))
    link = Column('link', String(255))
    supervisor = Column('supervisor', String(255))
    text = Column('text', String(1000000))
    title = Column('title', String(500))
    type = Column('type', String(500))
    university = Column('description', String(255))
    year = Column('year', Integer)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))

    student = relationship(Student)

