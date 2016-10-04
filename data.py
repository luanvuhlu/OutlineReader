# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
'''
Created on Oct 4, 2016

@author: luan vu
'''
from _pyio import __metaclass__

class Paragraph():
    '''
    Lọc những đoạn văn bản
    '''
    def __init__(self):
        self.school = None  
        # Khoa
        self.department = None
        # Bộ môn
        self.specialized_study = None
        # Nơi xuất bản
        self.location = None
        # Năm xuất bản
        self.year = None
        # Hệ đào tạo
        self.program_study_type = None
        self.subject = None
        self.credit_count = None
        # Loại môn học
        self.subject_required_type = False
        # Thôn tin giảng viên
        self.lecturer = []
        # Tóm tắt nội dung môn học
        self.subject_summary = None
        # Nội dung chi tiết môn học
class ObjectParser():
    __metaclass__ = ABCMeta
    @abstractmethod
    def parse(self, **params):
        pass
    @abstractmethod
    def is_in_process(self):
        pass
    @abstractmethod
    def get_last_index(self):
        pass
class Lecturer(ObjectParser):
    '''
    Giảng viên
    '''
    def __init__(self):
        # Học hàm/học vị
        self.degree = None
        self.name = None
        # Vị trí
        self.position = None
        self.email = None
        self.phone = None
class SpecializedStudy(ObjectParser):
    '''
    Bộ môn
    '''
    def __init__(self):
        self.address = None
        self.phone = None
        self.email = None
class Problem(ObjectParser):
    def __init__(self):
        # Số thứ tự
        self.index = None
        self.name = None
        self.sub_problem = []
class SubProblem(Problem):
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
