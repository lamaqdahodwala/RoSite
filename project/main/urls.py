from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect', views.redirection, name='redirection'), 
    path('userid/<int:uid>', views.userid, name='redirection')
]