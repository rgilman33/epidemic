from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    
    context_dict = {'boldmessage': "FOREVER BOLD"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'epidemic/index.html', context_dict)
    
def code(request):
    context_dict = {'boldmessage': "STILL 4EVER BOLD"}
    return render(request, 'epidemic/code.html', context_dict)
    
def model_description(request):
    context_dict = {'boldmessage': "STILL 4EVER BOLD"}
    return render(request, 'epidemic/model_description.html', context_dict)
    
def dashboard(request):
    context_dict = {'boldmessage': "STILL 4EVER BOLD"}
    return render(request, 'epidemic/dashboard.html', context_dict)
def about(request):
    return HttpResponse("best epidemic model ever. period.")
