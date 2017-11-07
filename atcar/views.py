

from django.shortcuts import render
from django.http import HttpResponse
from atcar.forms import carMform

# Create your views here.
def index(request):
	return render(request, "bsmain.html", {})
	#return HttpResponse("<h2>Make $10,000 USD a month </h2>");
    
    
def upload(request):
    
    
    
    return httpResponse("")

	
def addvehicle(request):
		if request.method == 'POST':
			form = carMform(request.POST)
			if form.is_valid():
				form.cleaned_data
				form.save()
				#add user.id to add to sellerid when querying db
				return	HttpResponseRedirect('detail')			

		else:
			form = carMform()
		return render(request, 'atcar/addvehicle.html', {'form':form})	
    