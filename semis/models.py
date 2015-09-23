from django.db import models


class User_info(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    user_id = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=10, null=False)
    dept_id = models.IntegerField()
    team_id = models.IntegerField()
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    employee = models.CharField(max_length=15)
    rank_id = models.IntegerField()
    level_id = models.IntegerField()
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name