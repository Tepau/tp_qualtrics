
from django.conf.urls import url
from .views import ContactList, ContactView, SurveyView, DistributionView


urlpatterns = [

    url(r'^contact/$', ContactList.as_view() , name='contact'),
    url(r'^new/$', ContactView.as_view() , name='new'),
    url(r'^survey/$', SurveyView.as_view() , name='survey'),
    url(r'^list/$', DistributionView.as_view() , name='list'),


]