from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    create_date = models.DateTimeField(blank=True)

    phone=models.CharField(max_length=15)
    email=models.EmailField()


    def register(self):
        self.save()

    @staticmethod
    def getContactByEmail(email):
        try:
            return Contact.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Contact.objects.filter(email=self.email):
            return True
        return False
