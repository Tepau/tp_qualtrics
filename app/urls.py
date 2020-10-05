
from django.conf.urls import url
from .views import ContactList, ContactView, SurveyView


urlpatterns = [

    url(r'^contact/$', ContactList.as_view() , name='contact'),
    url(r'^new/$', ContactView.as_view() , name='new'),
    url(r'^survey/$', SurveyView.as_view() , name='survey'),


]