from django.shortcuts import render

# Create your views here.
def paginaprincipal(request):
	return render(request, 'apptarea1/paginaprincipal.html')


def futbol(request):
	return render(request, 'apptarea1/futbol.html')

def volley(request):
	return render(request, 'apptarea1/volley.html')

def futsal(request):
	return render(request, 'apptarea1/futsal.html')	

def sincontrincante(request):
	return render(request, 'apptarea1/sincontrincante.html')