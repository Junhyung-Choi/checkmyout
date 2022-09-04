from django.shortcuts import render
from django.shortcuts import redirect
from .forms import OuterForm
from .models import Outer

# Create your views here.
def home(request):
    objs = []
    if(request.method == 'POST'):
        form = OuterForm(request.POST)
        if form.is_valid():
            outer = form.save(commit = False)
            outer.save()
            return redirect('/')
    else:
        form = OuterForm
        objs = Outer.objects.all()
    context = {'form' : form, 'objs' : objs}
    return render(request,'home.html',context=context)

def comeback(request):
    drecord = Outer.objects.get(id = request.POST['clickid'])
    drecord.delete()
    form = OuterForm
    objs = Outer.objects.all()
    context = {'form' : form, 'objs' : objs}
    return render(request,'home.html',context=context)