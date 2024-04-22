from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class toDoList(models.Model):
    todo_title = models.CharField(max_length=100)
    todo_description = models.CharField(max_length=250, blank= True, null= True)
    todo_created_on = models.DateField(default= datetime.datetime.today)
    todo_modified_on = models.DateField(auto_now= True)
    todo_is_completed = models.BooleanField(default= False)
    todo_created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.todo_created_by} - {self.todo_title} - {self.todo_description}"