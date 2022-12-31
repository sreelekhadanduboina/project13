from django.shortcuts import render

# Create your views here.

def operations2(request):
    d={'a':12,'b':123}
    return render(request,'operations2.html')