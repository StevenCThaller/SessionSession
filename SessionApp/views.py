from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'x' in request.session:
        print("X is", request.session['x'])
    return render(request, "index.html")

def setthings(request):
    request.session['x'] = request.POST['x']
    return redirect('/showx')

def showthings(request):
    if 'x' not in request.session:
        return redirect('/')
    print(request.session['x'])
    return render(request, "showx.html")

def logout(request):
    request.session.flush()
    return redirect('/')

