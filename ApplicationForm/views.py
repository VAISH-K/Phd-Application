from django.shortcuts import render

# Create your views here.
def Application(request):
	if request.method == "POST":

		return render(request, 'phd.html')

		