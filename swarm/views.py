from django.shortcuts import render
from .PSO import PSO
# Create your views here.
def index(request):
    xvarmin             = []
    xvarmax             = []
    nvar                = 0
    npop                = 0
    ngen                = 0
    nrep                = 0
    tInitPop            = 0
    tMetOtim            = 0
    tFO                 = ""
    parada              = ""
    c1                  = 0
    c2                  = 0
    w                   = 0
    return render(request, 'swarm/swarm.html', {})

def submitPart1(request):
    
    nvar        = request.GET['nvar']
    npop        = request.GET['npop']
    ngen        = request.GET['ngen']
    nrep        = request.GET['nrep']
    tFO         = request.GET['tFO']
    tInitPop    = request.GET['tInitPop']
    parada      = request.GET['tFO']
    mydictionary = {
        "nvar"      : nvar,
        "npop"      : npop,
        "ngen"      : ngen,
        "nrep"      : nrep,
        "tFO"       : tFO,
        "tInitPop"  : tInitPop,
        "parada"    : parada,
    }
    return render(request, 'swarm/swarm-1.html', context=mydictionary)
    

def submitPart2(request):
    pass