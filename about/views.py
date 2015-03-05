from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

def about(request):
	# request the context of the request.
	# the context contains information such as the client's machine details, for example
	context = RequestContext(request)

	# construct a dictionary to pass to the template engine as its context.
	content = {}

	return render_to_response('about/about.html', content, context)

def brians(request):
	# request the context of the request.
	# the context contains information such as the client's machine details, for example
	context = RequestContext(request)

	# construct a dictionary to pass to the template engine as its context.
	content = {}

	return render_to_response('about/brians.html', content, context)

def location(request):
	# request the context of the request.
	# the context contains information such as the client's machine details, for example
	context = RequestContext(request)

	# construct a dictionary to pass to the template engine as its context.
	content = {}

	return render_to_response('about/location.html', content, context)

def history(request):
	# request the context of the request.
	# the context contains information such as the client's machine details, for example
	context = RequestContext(request)

	# construct a dictionary to pass to the template engine as its context.
	content = {}

	return render_to_response('about/history.html', content, context)

def contact(request):
	# request the context of the request.
	# the context contains information such as the client's machine details, for example
	context = RequestContext(request)

	# construct a dictionary to pass to the template engine as its context.
	content = {}

	return render_to_response('about/contact.html', content, context)
