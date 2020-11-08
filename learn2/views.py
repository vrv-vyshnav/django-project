from django.shortcuts import render

def index(request):
    return render(request, 'index.html'),
def main(request, username):
    return render(request, 'main.html', {
        "username" : username
    })