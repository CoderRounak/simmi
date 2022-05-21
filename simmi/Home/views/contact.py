from django.shortcuts import render, redirect
from django.views import View
from Home.models.contact import Contact as modelContact
class Contact(View):
    def get(self, request):

        contact=modelContact.getContactByEmail(request.session.get('email'))

        data = {}
        data['contact'] = contact
        return render(request, 'contact.html', data)
