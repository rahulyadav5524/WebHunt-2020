from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from .models import Team,TeamRelation,Question,AnswerLog,Ranks,Profile
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response

import datetime        
import pytz 

question_urls={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11%40°33'34.6N73°55'25.9W",12:"1"}
# Create your views here.
@api_view(['GET'])
def home(request):
    if request.user.is_authenticated:
        if TeamRelation.objects.filter(user=request.user).exists():
            teamrelation = TeamRelation.objects.get(user=request.user)
            cur_que = teamrelation.team.cur_ques_no
            return redirect('lobby',question_urls[cur_que])
        else:
            return redirect('lobby',question_urls[1])
    else:
        return render(request,'html/index.html')

def about(request):
    return render(request,'html/aboutus.html')

@login_required(login_url='/signin/')
def lobby(request,ques_code):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
    print(current_time)
    d = {'inteam':False}
    d['result_out']=True
    d['contest_running']=False
    d['contest_ended']=True


    # if(current_time.day >= 27):
    #     d['contest_running']=True
    # if(current_time.day == 28 and current_time.hour >= 5):
    #     d['contest_ended']=True
    #     d['contest_running']=False


    
    user = request.user
    d['profile'] = False
    rank_list = Ranks.objects.order_by('-cur_ques_no','created_at')
    if Profile.objects.filter(user=user).exists():
        d['profile'] = Profile.objects.get(user=user)
    if TeamRelation.objects.filter(user=user).exists():
        d['inteam'] = True
        teamrelation = TeamRelation.objects.get(user=user)
        d['team'] = teamrelation.team
        members = list(map(lambda teamrelation: teamrelation.user,
                        TeamRelation.objects.filter(team=teamrelation.team)))
        d['members'] = members

        d['cur_ques_no'] = teamrelation.team.cur_ques_no
        if(d['cur_ques_no'] > 11):
            d['team_completed']=True
        else:
            d['ques'] = Question.objects.get(ques_no=teamrelation.team.cur_ques_no)
            d['team_completed']=False

        
        cur_rank = 0
        for rank in rank_list:
            cur_rank += 1
            if(rank.team == teamrelation.team):
                break

        print(cur_rank)
        d['cur_rank'] = cur_rank
            

    team_question = []
    all_teams = Team.objects.all()
    for team in all_teams:
        team_question.append(str(team.team_name)+'?'+str(team.cur_ques_no))
    d['team_question'] = team_question
    team_ranks = []
    # i=1
    for rank in rank_list:
        team_ranks.append(str(rank.team.team_name))
        # i+=1
    d['team_ranks']=team_ranks
    # d['inteam']=False
    print(d)
    return render(request,'html/lobby.html',d)

def signin(request):
    if(request.user.is_authenticated == False):
        if(request.method == 'POST'):
            email = request.POST['email']
            if(User.objects.filter(email = email).exists()):
                password = request.POST['password']
                username = User.objects.get(email=email).username
                user = authenticate(username=username,password=password)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request,'Login Successful')
                    return redirect('signin')
                else:
                    messages.error(request,'Invalid Credentials')
                    return redirect('signin')
            else:
                messages.error(request,'Invalid Email')
                return redirect('signin')
        else:
            return render(request,'html/signin.html')
    else:
        return redirect('home')

@login_required(login_url='/signin/')
def signout(request):
    auth_logout(request)
    messages.success(request,"Signout Successful")
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        if TeamRelation.objects.filter(user=request.user).exists():
            teamrelation = TeamRelation.objects.get(user=request.user)
            cur_que = teamrelation.team.cur_ques_no
            return redirect('lobby',question_urls[cur_que])
        else:
            return redirect('lobby',question_urls[1])
    else:
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email is already registered')
                return redirect('signup')
            totallength = len(list(User.objects.filter(username = name)))
            temp_username = str(name) + str(totallength)
            print(password) 
            user = User.objects.create_user(first_name=name,username = temp_username,email = email,password = password)
            if user:
                messages.success(request,'User Is Created')
                auth_login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('lobby',question_urls[1])
            else:
                messages.error(request,'Error In Signup')
                return redirect('signup')
        else:
            return render(request,'html/signup.html')   

@login_required(login_url='/signin/')
def username(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        print(new_username)
        if User.objects.filter(username=new_username).exists():
            messages.warning(request,'Username Is Already Taken')
            print('Username Is Already Taken')
            return redirect('username')
        user=request.user
        user.username = new_username
        print(new_username)
        print(user.username)
        user.save()
        return redirect('lobby',question_urls[1])
    else:
        return render(request,'html/username.html') 

@login_required(login_url='/signin/')
@api_view(['GET'])
def joinTeam(request,teamcode):
    # current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
    # if(current_time.day >= 27 ):
    #     messages.error(request,"You cannot Join a Team Now")
    #     return redirect('lobby',question_urls[1])
    user = request.user
    if Team.objects.filter(team_code=teamcode).exists():
        team = Team.objects.get(team_code=teamcode)
        print(team)
        team_members = list(map(lambda teamreleation: teamreleation.user,
                            TeamRelation.objects.filter(team=team)))
        if user in team_members:
            messages.warning(request,"You are already in this team")
            return redirect('lobby',question_urls[team.cur_ques_no])
        if(team.no_of_member == 4):
            messages.warning(request,"Team is Already Full")
            return redirect('lobby',question_urls[1])
        team.no_of_member += 1
        team.save()
        team_relation = TeamRelation.objects.create(team=team,user=user)
        return redirect('lobby',question_urls[team.cur_ques_no])
    else:
        messages.error(request,"Wrong Team Code")
        return redirect('lobby',question_urls[1])

@login_required(login_url='/signin/')
def createteam(request):
    # current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
    # if(current_time.day >= 27):
    #     messages.error(request,"You Cannot Create a Team Now")
    #     return redirect('lobby',question_urls[1])
    team_name = request.GET['teamname']
    if TeamRelation.objects.filter(user=request.user).exists():
        messages.error(request,'You are already in a team')
        team = Team.objects.get(user=req.user)
        return redirect('lobby',question_urls[team.cur_ques_no])
    team = Team.objects.create(team_name=team_name,team_leader = request.user)
    teamrelation = TeamRelation.objects.create(team=team,user=request.user)
    rank = Ranks.objects.create(team=team,cur_ques_no=1)
    messages.success(request,'Team Created')
    return redirect('lobby',question_urls[1])

@login_required(login_url='/signin/')
def submit(request):
    # current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))  
    # if(current_time.day >= 28):
    #     messages.error(request,"Contest is Ended")
    #     return redirect('lobby',question_urls[1])
    answer = request.GET['answer']
    user = request.user
    team = TeamRelation.objects.get(user=user).team
    cur_question_no = team.cur_ques_no
    question = Question.objects.get(ques_no=cur_question_no)
    log = AnswerLog.objects.create(team=team,ques_no=cur_question_no,answer=answer)
    if(question.answer == answer):
        team.cur_ques_no += 1
        team.save()
        messages.success(request,"Correct Answer")
        rank = Ranks.objects.get(team=team)
        rank.cur_ques_no = team.cur_ques_no
        rank.save()
        if rank.cur_ques_no > 11:
            return redirect('lobby',question_urls[1])
        else:
            return redirect('lobby',question_urls[team.cur_ques_no])
    else:
        messages.error(request,'Wrong Answer')
        return redirect('lobby',question_urls[cur_question_no])


@login_required(login_url='/signin/')       
def profile(request):
    if request.method == 'POST' and Profile.objects.filter(user=request.user).exists() == False:
        new_username = request.POST['profile_username']
        phone_no = request.POST['phoneno']
        roll_no = request.POST['roll_no']
        user = request.user
        user.username == new_username
        user_profile = Profile.objects.create(user=user,roll_no=roll_no,phone_no=phone_no)
        if(TeamRelation.objects.filter(user=user).exists()):
            team = TeamRelation.objects.get(user=user).team
            messages.success(request,'Profile Is Updated')
            return redirect('lobby',question_urls[team.cur_ques_no])
        else:
            return redirect('lobby',question_urls[1])
    else:
        return redirect('lobby',question_urls[team.cur_ques_no])


