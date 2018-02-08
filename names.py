"""Assignment: Names
Write the following function.

Part I
Given the following list:"""

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
"""
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel"""


for i in students:
    print i['first_name'] + " " + i['last_name']

        





