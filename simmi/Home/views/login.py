from django.shortcuts import render, redirect
from Home.models.contact import Contact
from django.views import View
import datetime as dt


class Login(View):

    def validateContact(self, contact):
        # form validation

        error_msg = None
        if not contact.name:
            error_msg = "Name required !"
        elif not contact.city:
            error_msg = "City required !"
        elif not contact.state:
            error_msg = "State required !"
        elif contact.isExists():
            error_msg = "A user-account already exists with this email"

        return error_msg

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        postData = request.POST
        name = postData.get('name')
        city = postData.get('city')
        state = postData.get('state')
        phone = postData.get('phone')
        email = postData.get('email')
        create_date = dt.datetime.now()
        error_msg = None

        contact = Contact(name=name,
                          city=city,
                          state=state,
                          phone=phone,
                          email=email,
                          create_date=create_date)
        error_msg = self.validateContact(contact)

        value = {
            'name': name,
            'city': city,
            'state':state,
            'phone': phone,
            'email': email
        }

        # registration of the contact (saving profile)
        if not error_msg:
            contact.register()
            request.session['email']=contact.email
            return redirect('homepage')

        else:
            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'login.html', data)

def logout(request):
    request.session.clear()
    return redirect('login')