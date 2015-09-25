from django.db import models
import locale

class Cost_type_info(models.Model):
    cost_type_id = models.AutoField(primary_key=True)
    cost_type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.cost_type_name


class Project_info(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class Rank_info(models.Model):
    rank_id = models.AutoField(primary_key=True)
    rank_name = models.CharField(max_length=10)

    def __str__(self):
        return self.rank_name


class Team_info(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name


class Level_info(models.Model):
    level_id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=10)

    def __str__(self):
        return self.level_name


class Dept_info(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=20)

    def __str__(self):
        return self.dept_name


class User_info(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=10, null=False)
    dept_id = models.ForeignKey(Dept_info)
    team_id = models.ForeignKey(Team_info)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    employee = models.CharField(max_length=15)
    rank_id = models.ForeignKey(Rank_info)
    level_id = models.ForeignKey(Level_info)
    reg_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Pay_info(models.Model):
    pay_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(User_info)
    pay_name = models.CharField(max_length=20)
    card_num = models.CharField(max_length=4, null=True)

    def __str__(self):
        return "{0}[{1}]".format(self.pay_name, self.card_num)


class Spend(models.Model):
    spend_id = models.AutoField(primary_key=True)
    id = models.ForeignKey(User_info)
    cost = models.IntegerField()
    cost_type_id = models.ForeignKey(Cost_type_info)
    reg_date = models.DateTimeField(auto_now_add=True)
    project_id = models.ForeignKey(Project_info)
    comment = models.CharField(max_length=100)
    pay_type = models.ForeignKey(Pay_info)
    modify_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}[￦{1}, {2}]".format(self.id.name, locale.format('%d', self.cost, 1), self.cost_type_id.cost_type_name)


class Favorite_category(models.Model):
    favorite_id = models.AutoField(primary_key=Team_info)
    id = models.ForeignKey(User_info)
    cost_type_id = models.ForeignKey(Cost_type_info)

