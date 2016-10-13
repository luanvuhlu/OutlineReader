# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
from data import Paragraph
'''
Created on Oct 13, 2016

@author: luan vu
'''

class Counter():
    def __init__(self):
        self.__index = 0
    def get_index(self):
        return self.__index
    def incre(self):
        self.__index+=1
        return self.get_index()
    def decre(self):
        self.__index-=1
        return self.get_index()
class AbstractParser():
    __metaclass__ = ABCMeta
    def __init__(self, counter=None):
        if not counter:
            counter = Counter()
        self.counter = counter
    @abstractmethod
    def parse(self, **params):
        pass
    @abstractmethod
    def get_data(self):
        pass
class ParagraphParse(AbstractParser):
    def __init__(self, counter=None):
        super(ParagraphParse, self).__init__(counter)
        self.__paragraph = Paragraph()
    @abstractmethod
    def get_data(self):
        return self.__paragraph
    @abstractmethod
    def parse(self, **params):
        
        pass