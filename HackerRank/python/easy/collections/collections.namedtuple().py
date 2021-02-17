from collections import namedtuple

from collections import namedtuple

n = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
for _ in range(n):

    '''field1, field2, field3, field4 = input().split()
    student = Student(field1, field2, field3, field4)'''

    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total / n))


