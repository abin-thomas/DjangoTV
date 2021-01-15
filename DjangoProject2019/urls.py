"""
Definition of urls for DjangoProject2019.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_Query', views.searchQuery, name ='searchShows'),
    path('searchResults/<id>', views.showsOfPerson, name="Shows_Persons"),
    path('showdetails/<show_ID>', views.tv_Show_Details, name ='seasons'),
    path('tvshow_masterdetails/', views.singleTvShow_Details, name ='seasondetails'),
    path('episodes/<season_num>', views.season_Show_Details, name ='episodes'),
    path('episodeDetails/<episode_num>', views.episode_Show_Details, name ='episode'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
