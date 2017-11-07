from atcar.models import atcar_cars
from django.forms import ModelForm, Textarea, DateTimeField







class carMform(ModelForm):

		class Meta:
			model = atcar_cars
			fields = [
                      'make', 
                      'model', 
                      'year', 
                      'color',
                      'intcolor',
                      'enginesize',
			          'body', 
                      'mileagekm', 
                      'price', 
                      'addinfo', 
                      'transmission', 
                      'fuel',
                      'steer',
                      'doors',
                      
                     
                     ]
			widget =  {
			         'addinfo': Textarea(attrs={'cols': 80, 'rows': 20}),
						}