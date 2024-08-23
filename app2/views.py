from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Soy el index de app2</h1>")

def pagina2(request):
    html="""
    <h1 style="color:blue">Hola app2</h1>
    <h2>Soy un sub</h2>
    """
    return HttpResponse(html)