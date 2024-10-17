from django.db import models

# Create your models here.

class Group(models.Model):
    number = models.IntegerField(blank=True, null=True)
    letter = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100)
    def __str__(self):
        return str(self.number) + " " +  self.letter

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name