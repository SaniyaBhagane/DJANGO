from django.shortcuts import render

# Create your views here.
def chai_home(request):
    return render(request, 'chai/all_chai.html')