
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('lobby/<str:ques_code>',views.lobby,name='lobby'),
    # path('list-link/',views.listLink,name='list'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('username/',views.username,name='username'),
    path('join-team/<str:teamcode>',views.joinTeam,name='join-team'),
    path('create-team/',views.createteam,name='create-team'),
    path('submit/',views.submit,name='submit'),
    path('profile/',views.profile,name="profile"),
    path('aboutUs/',views.about,name="aboutUs")

] 