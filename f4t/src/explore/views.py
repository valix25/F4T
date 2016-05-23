# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from htmlPlot import clusterPlot

def index(request):
	template=loader.get_template('explore/index.html')
	return HttpResponse(template.render(request))

# remember clusterPlot(data_csv,l,kl,ku):
def run(request):
	# Get parameters from form..
	l=request.POST['feature']
	kl=request.POST['kmin']
	ku=request.POST['kmax']
	data_csv='../data/CA_WHS_HOUSEHOLD.csv'
	# Perform clustering
	context=clusterPlot(data_csv,l,kl,ku)
	return HttpResponseRedirect(reverse('explore:results',args=context))

# I think we need to deal with the rendering of the run function via a 
#different rendering function

def results(request, context):
	# Redirects back to main view..
    return render(request, 'explore/index.html', {'viz': context})
