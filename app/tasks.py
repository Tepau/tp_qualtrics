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


@shared_task
def contact_list():
    my_list = []
    headers = {'X-API-TOKEN': 'eCaTZTJ67f6folFZjPUvR5g1THGtcYFGSL8zhnlC'}
    r = requests.get('https://fra1.qualtrics.com/API/v3/directories/POOL_3emqkuBXr2bdFQC/contacts', headers=headers)
    for user in r.json()['result']['elements']:
        if user['firstName'] is not None and user['lastName'] is not None and user['email'] is not None:
            dico = {'prenom': user['firstName'], 'nom': user['lastName'], 'email': user['email']}
            my_list.append(dico)
    return dico