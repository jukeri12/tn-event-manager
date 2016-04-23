from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def LanderView(request):
    return render(request, 'frontpage.html')