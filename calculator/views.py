from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'calculator/calculator.html', {})

def submitquery(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            "q" : q,
            "ans" : ans,
            "error" : False
        }
        return render(request,'calculator/calculator.html',context=mydictionary)
    except:
        pass