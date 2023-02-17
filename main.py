from student import Student

student1 = Student("Ben")
student1.add_test(92)
student1.add_test(94)
student1.add_test(90)
student1.add_test(96)
student1.add_test(87)
print(student1.test_scores)
print(student1.get_average())
