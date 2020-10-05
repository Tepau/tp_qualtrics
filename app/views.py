import json

from django.contrib import messages
from django.shortcuts import render
import requests
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, FormView

from .models import Contact
from .form import ContactForm

from .tasks import create_new_contact
from django.conf import settings

class ContactList(View):
    template_name = "app/contact.html"
    model = Contact

    def get(self, request, *args, **kwargs):
        my_list = []
        headers = {'X-API-TOKEN': settings.API_KEY}
        r = requests.get('https://fra1.qualtrics.com/API/v3/directories/' + settings.DIRECTORY_ID + '/contacts', headers=headers)

        my_rep = r.json()['result']['elements']
        last_rep = [user for user in my_rep if user['firstName'] is not None and user['lastName'] is not None and user['email'] is not None]

        return render(request, "app/contact.html", locals())


class ContactView(FormView):
    template_name = 'app/newContact.html'
    form_class = ContactForm
    success_url = '/app/contact/'

    def form_valid(self, form):
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        email = form.cleaned_data['email']
        create_new_contact.delay(firstname, lastname, email)

        return super().form_valid(form)


class SurveyView(View):
    def get(self, request):
        headers = {'X-API-TOKEN': settings.API_KEY}
        r = requests.get('https://ca1.qualtrics.com/API/v3/survey-definitions/' + settings.SURVEY_ID, headers=headers)
        dico = {'id': r.json()['result']["SurveyID"], 'name': r.json()['result']["SurveyName"]}
        return render(request, "app/survey.html", locals())



