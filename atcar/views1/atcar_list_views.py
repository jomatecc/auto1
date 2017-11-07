from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from atcar.models import atcar_cars




def list_all(request):
   # if request.method == 'POST':
        cars = atcar_cars.objects.all()
    
        return render(request, 'atcar/listcars.html', {"cars": cars})

def list_all1(request):
   # if request.method == 'POST':
        cars = atcar_cars.objects.all()
        return render(request, 'atcar/listcars1.html', {"cars": cars})

def list_all2(request):
   # if request.method == 'POST':
        cars = atcar_cars.objects.all()
        paginator = Paginator(cars, 10) #show 5 items in list
        page = request.GET.get('page')
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)
        return render(request, 'atcar/listcars2.html', {"cars": cars})

def list_all3(request):
   # if request.method == 'POST':
        cars = atcar_cars.objects.all()
        return render(request, 'atcar/listcars3.html', {"cars": cars})


def list_all4(request):
   # if request.method == 'POST':
        cars = atcar_cars.objects.all()
        return render(request, 'atcar/listcars4.html', {"cars": cars})
   # return HttpResponse("Make $10000 usd every month")
	
def list_make(request, page):
    if request.method == 'POST':
        make = request.POST['make']
        cars = atcar_cars.objects.filter(make=make)
        return render(request, 'atcar/listmake.html', {'cars':cars, 'make':'honda'})
    else:
       # make = request.GET('make')
        cars = atcar_cars.objects.filter(make='honda')
        return render(request, 'atcar/listmake.html', {'cars': cars})

	
def list_by_make(request):
	return HttpResponse("Make $10000 usd every month")
	
def list_by_model(request):
	return HttpResponse("Make $10000 usd every month")
		
def list_price_range(request):
	return HttpResponse("Make $10000 usd every month")
	
def list_by_year(request): 
	return HttpResponse("Make $10000 usd every month")
	
def detail_list(request, pk):
    #if method.request() == 'POST':
    car = atcar_cars.objects.get(pk=id)
    return render(request, 'atcar/detail.html', {'car': car})

def seller_listing(request):
	return HttpResponse("Make $10000 usd every month")