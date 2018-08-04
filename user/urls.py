from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update', views.update, name='update'),
]
