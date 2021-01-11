from django.shortcuts import render

# Create your views here.
def kit_register(request):
    return render(request, "kit/kit_register.html")