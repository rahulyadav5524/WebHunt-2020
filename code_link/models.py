from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.


class Question(models.Model):
    ques_no = models.IntegerField()
    # ques_image = models.ImageField(null=True,blank=True)
    ques_url = models.TextField(default="")
    answer = models.TextField()

    class Meta:
        ordering = ['ques_no']
    
    def __str__(self):
        return str(self.ques_no) + " " + str(self.answer)

import random
import string

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    no_of_member = models.IntegerField(default=1)
    team_leader = models.ForeignKey(User,on_delete=models.CASCADE,related_name='leader')
    team_code = models.SlugField(null=True, blank=True)
    cur_ques_no = models.IntegerField(default=1)
    last_ques_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.team_name

    def save(self,*args,**kwargs):
        if(self.team_code == None):
            team_code = slugify(get_random_string(8))
            has_team_code = Team.objects.filter(team_code = team_code).exists()
            count = 1
            while has_team_code:
                count += 1
                team_code = slugify(self.team_name) + '-' + str(count)
                has_team_code = Team.objects.filter(team_code = team_code).exists()
            
            self.team_code = team_code
        super().save(*args,**kwargs)


class TeamRelation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='member')
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='related_team')

    class Meta:
        unique_together = ['user','team']

    def __str__(self):
        return self.user.username + " " + self.team.team_name

    
class AnswerLog(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    ques_no = models.IntegerField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created_at']

    def __str__(self):
        return str(self.team.team_name) + " " + str(self.ques_no)+ " " + str(self.answer) + " " + str(self.created_at)

class Ranks(models.Model):
    team = models.ForeignKey(Team,on_delete=models.PROTECT)
    cur_ques_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['cur_ques_no','created_at']

    def __str__(self):
        return self.team.team_name + " " + str(self.cur_ques_no) +" " + str(self.created_at)
        # Entry.objects.order_by('-pub_date', 'headline')


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    roll_no = models.CharField(max_length=8)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username + " " + self.roll_no
    