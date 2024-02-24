from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'core/portfolio.html', { "projects": projects})