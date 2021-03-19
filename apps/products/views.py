from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

def createSuperUser(request):
    create = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    return HttpResponse(create, content_type='text/plain')
