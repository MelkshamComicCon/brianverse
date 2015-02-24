from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Spend money in the store")
