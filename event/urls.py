from django.urls import path

from event import views


app_name = 'event'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('event', views.EventListView.as_view(), name='event'),
    path('event/add', views.EventCreateView.as_view(), name='event_add'),
    path('event/<int:pk>/edit', views.EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete', views.EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('event/<int:pk>/bookmark', views.bookmark_event, name='event_bookmark'),
]
