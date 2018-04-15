from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/update$', views.update, name='update'),
]
