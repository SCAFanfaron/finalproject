from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
