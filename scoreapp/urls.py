from django.urls import path
from . import views

app_name = 'scoreapp'

urlpatterns = [
    path('',
    views.ScoreListView.as_view(), 
    name='index'),

    path('mypage/',
    views.MypageView.as_view(),
    name='mypage'),

    path('titleform/',
    views.CreateTitleView.as_view(),
    name='titleform'),

    path('scoreform/',
    views.CreateScoreView.as_view(),
    name='scoreform'),

    path('done/',
    views.SuccessView.as_view(),
    name='done'),

    path('contact/',
    views.ContactView.as_view(),
    name='contact'),

    path('studentlist/',
    views.StudentListView.as_view(),
    name='studentlist'),

    path('student/<str:user>',
    views.StudentView.as_view(),
    name='student'),

    path('Japaneselist/',
    views.JapaneseView.as_view(),
    name='Japaneselist'),

    path('Mathlist/',
    views.MathView.as_view(),
    name='Mathlist'),
    
    path('Sciencelist/',
    views.ScienceView.as_view(),
    name='Sciencelist'),

    path('Sociologylist/',
    views.SociologyView.as_view(),
    name='Sociologylist'),

    path('Englishlist/',
    views.EnglishView.as_view(),
    name='Englishlist'),
]