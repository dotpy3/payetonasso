from django.contrib.auth.decorators import login_required
from django.shortcuts import render

default_home = {
    'deactivated': False,
}

default_dashboard = {

}

def home(request):
    return render(request, 'index.html', default_home)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', default_dashboard)
