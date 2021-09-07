from django.shortcuts import render
from students.models import stud_info
# Create your views here.

def listone(request):
    try:
        unit = stud_info.objects.get(cName='YB')
    except:
        errormessage = '(error message!)'
    return render(request, 'listone.html',locals())

def listall(request):
    stud_infomation = stud_info.objects.all().order_by('id')
    return render(request, 'listall.html', locals())

def listall2(request):
    stud_infomation = stud_info.objects.all().order_by('id')
    return render(request, 'listall2.html', locals())

def insert(request):
    if request.method  == 'POST':
        cName = request.POST['name']
        cSex = request.POST['sex']
        cDob = request.POST['dob']
        cEmail = request.POST['email']
        cPhone = request.POST['phone']
        cAddr = request.POST['addr']
        unit = stud_info.objects.create(cName = cName, cSex = cSex, cDob = cDob, cEmail = cEmail, cPhone = cPhone, cAddr = cAddr)
        unit.save() # save data
        stud_infomation = stud_info.objects.all().order_by('-id')
        return render(request, 'insert.html', locals())
    else:
        return render(request, 'insert.html', locals())
def modify(request):
    name = request.GET['name']
    unit = stud_info.objects.get(cName = name)
    if request.method == 'POST':
        unit.cName = request.POST['name']
        unit.cSex = request.POST['sex']
     #   dob = request.POST['post']
        #dob = ((dob.replace('year', '-')).replace('month','-').replace('day','-'))
        unit.cDob = request.POST['dob']
        unit.cEmail = request.POST['email']
        unit.cPhone = request.POST['phone']
        unit.cAddr = request.POST['addr']
        unit.save() # save data
        stud_infomation = stud_info.objects.all().order_by('-id') # short by invert id
        return render(request,'listall.html', locals())

    else:
        sex = unit.cSex
        dob = unit.cDob
        email = unit.cEmail
        addr = unit.cAddr
        phone = unit.cPhone
        return render(request, 'modify.html', locals())

def delete(request,id=None):
    name = request.GET['name']
    unit = stud_info.objects.get(cName = name)
    unit.delete()
    stud_infomation = stud_info.objects.all().order_by('-id')
    return render(request, 'listall.html', locals())

