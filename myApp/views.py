from django.shortcuts import render
from django.shortcuts import redirect
from .forms import OuterForm,EventForm, OuterForm2
from .models import Outer,Event, Outer2, People,Find
import csv
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


#추가 사항
def start(request):
    events = []
    if(request.method == 'POST'):
        form = EventForm(request.POST)
        if form.is_valid():
            ev = form.save(commit = False)
            ev.save()
            return redirect('/start')
    else:
        form = EventForm
        events = Event.objects.all()
    context = {'form' : form, 'events' : events}
    return render(request,'start.html',context=context)

def setEvent(request):
    if(request.method == 'POST'):
        school = request.POST["school"]
        file = request.FILES["uploadedfile"]
        decoded_file = file.read().decode('utf-8-sig').splitlines()
        reader = csv.reader(decoded_file)
        event = Event.objects.get(id = request.POST["eventid"])
        for row in reader:
            people = People(
            event=event,
            school = school,
            name = row[0])
            print(people.event,people.school,people.name)
            people.save()
        return redirect('/setevent?eventid='+request.POST["eventid"])
    else:
        event = Event.objects.get(id = request.GET.get("eventid"))
        context = {'event' : event}
        return render(request,'setEvent.html',context=context)

def home2(request):
    objs = []
    people=[]
    if(request.method == 'POST'):
        event = Event.objects.get(id = request.POST["eventid"])
        person=Find.objects.get(id=request.POST["clickid"])
        print("!",person.name,person.school)
        outer=Outer2(name=person.name,
        school=person.school,
        event=event)
        print(outer.name,outer.school)
        outer.save()
        return redirect('/home2?eventid='+request.POST["eventid"])
    else:
        pass
    event = Event.objects.get(id = request.GET.get("eventid"))
    people=Find.objects.all()
    
    objs = Outer2.objects.filter(event=event)
    context = {'objs' : objs,'event' : event,'people':people}
    return render(request,'home2.html',context=context)

def find(request):
    objs = []
    people=[]
    event = Event.objects.get(id = request.POST["eventid"])
    name=request.POST["name"]
    people=People.objects.filter(event=event,name=name)
    for i in people:
        print(i.name,i.school)
        result=Find(name=i.name,school=i.school)
        result.save()
    return redirect('/home2?eventid='+request.POST["eventid"])

def comeback2(request):
    drecord = Outer2.objects.get(id = request.POST['clickid'])
    drecord.delete()
    return redirect('/home2?eventid='+request.POST["eventid"])