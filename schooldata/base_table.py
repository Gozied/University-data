""" The abstract class 'Base Table' defines abstract Methods that must be implemented"""
from abc import ABC, abstractmethod
import os, sys
import csv

class BaseTable(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass








