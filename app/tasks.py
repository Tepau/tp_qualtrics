import json

import requests
from celery import shared_task


@shared_task
def create_new_contact(firstname, lastname, email):
    headers = {'X-API-TOKEN': 'eCaTZTJ67f6folFZjPUvR5g1THGtcYFGSL8zhnlC', 'Content-Type': 'application/json'}
    body = {'firstName': firstname, 'lastName': lastname, 'email': email, 'unsubscribed': True}
    r = requests.post('https://fra1.qualtrics.com/API/v3/mailinglists/CG_3Piuw6PMWmCwvHc/contacts', headers=headers,
                      data=json.dumps(body, indent=4))
    return 'Contact created with success!'

