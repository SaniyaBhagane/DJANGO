from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.
def all_chai(request):
    chai = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chai': chai})
