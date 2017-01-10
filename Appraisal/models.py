from django.db import models
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse


class Employee(models.Model):
    Names = models.ForeignKey(User, max_length=30, default=1)
    Email = models.EmailField
    Contacts = models.IntegerField
    Branch = models.CharField(max_length=30)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '{}'.format(self.Names)


class Department(models.Model):
    Name = models.CharField(max_length=30)
    Leader = models.ForeignKey(Employee)
    Department_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.Name)


class Post(models.Model):
    Title = models.CharField(max_length=30)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.Title)


class Question(models.Model):
    About_me = models.CharField(max_length=150)
    Title = models.ForeignKey(Post)
    Department = models.ForeignKey(Department)
    Strength_of_your_department = models.CharField(max_length=300)
    Weakness_of_your_department = models.CharField(max_length=300)
    Personal_challenges_about_work = models.CharField(max_length=350)
    Best_Employee_or_Co_worker = models.ForeignKey(Employee)
    Comment_about_work_relations_at_Anppcan = models.CharField(max_length=300)
    Shortly_advise_Anppcan_on_what_you_feel_must_change = models.CharField(max_length=300)

    def __str__(self):
        return '{} | {}'.format(self.About_me, self.Title)
