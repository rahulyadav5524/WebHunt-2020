from django.contrib import admin

from .models import Team,TeamRelation,Question,AnswerLog,Ranks,Profile
# Register your models here.
admin.site.register((Team,TeamRelation,Question,AnswerLog,Ranks,Profile))