from django.shortcuts import render
from django.http import HttpResponse

import random
# Create your views here.

def home(request):
#	return HttpResponse('Hello my Friend !!')
	return render(request, 'pwdgenerator/home.html')


def password(request):

	characters = list('abcdefghijhklmnopqrstuvwxyz')
	
	if request.GET.get('UpperCase'):
		characters.extend(list('ABCDEFGHIJHLMNOPQRSTUVWXYZ'))

	if request.GET.get('Numbers'):
		characters.extend(list('0987654321'))

	if request.GET.get('SpecialChar'):
		characters.extend(list('~`!@#$%^&*'))

	thepassword = ''

	pwdlength = int(request.GET.get('length'))

	for x in range(pwdlength):
		thepassword += random.choice(characters)

	return render(request, 'pwdgenerator/password.html',{'password':thepassword})


def aboutus(request):
	return render(request, 'pwdgenerator/aboutus.html')