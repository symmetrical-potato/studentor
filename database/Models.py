from __future__ import print_function

from sqlalchemy import Column, Integer, String, Float, text, ForeignKey, Enum, DateTime, func, Boolean
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_mixins import AllFeaturesMixin

Base = declarative_base()


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Student(BaseModel):
    __tablename__ = 'student'


class Employer(BaseModel):
    __tablename__ = 'employer'


class Event(BaseModel):
    __tablename__ = 'event'


class Document(BaseModel):
    __tablename__ = 'document'
