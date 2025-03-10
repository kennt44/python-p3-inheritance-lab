#!/usr/bin/env python
from lib.user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Inherit from User
        self.knowledge = []  # Empty knowledge list

    def learn(self, info):
        """Add new knowledge to the student's knowledge list."""
        self.knowledge.append(info)
