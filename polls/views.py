from django.shortcuts import render,redirect
from polls.models import *

# Create your views here.
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'dashboard.html',{'stud':stud})

def add_staff(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        frm = StudentForm()
        if request.method == "POST":
            frm1 = StudentForm(request.POST,request.FILES)
            frm1.save()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'add_staff.html',{'frm':frm,'stud':stud})

def view_staff(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        all = Student.objects.all()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'view_staff.html',{'staff':all,'stud':stud})

def login(request):
    if 'user_id'  in request.session :
        return redirect('/dashboard') 
    msg = ""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        obj = Student.objects.filter(email=email,password=password)
        if obj.count()==1:
            studObj = obj.first()
            request.session['user_id'] = studObj.id
            return redirect('/dashboard')
        else:
            msg = "Invalid Email/Password"
    return render(request,'login.html',{'msg':msg})

def logout(request):
    del request.session['user_id']
    return redirect('/')

def sign_up(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        obj = Student(
            name=name,
            surname=surname,
            email=email,
            password=password,
            contact=contact
        )
        obj.save()
    return render(request,'Signup.html')

def editstaff(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        editId = request.GET.get('editId')
        std = Student.objects.get(pk=editId)
        frm1 = StudentForm(instance=std)
        if request.method == "POST":
            frm = StudentForm(request.POST,request.FILES,instance=std)
            frm.save()
            return redirect('/view_staff')
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'Edit_staff.html',{'frm':frm1,'stud':stud})

def deletestaff(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        delid = request.GET.get('deleteId')
        delete = Student.objects.filter(id=delid).delete()
        return redirect("/view_staff")

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        editId = request.session['user_id']
        std = Student.objects.get(pk=editId)
        frm1 = StudentForm(instance=std)
        if request.method == "POST":
            frm = StudentForm(request.POST,request.FILES,instance=std)
            frm.save()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'edit_profile.html',{'frm':frm1,'stud':stud})

def addslider(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        sldfrm = SliderForm()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        if request.method == "POST":
            sldfrmfrm = SliderForm(request.POST,request.FILES)
            sldfrmfrm.save()
        return render(request,'add_slider.html',{'stud':stud,'sldfrm':sldfrm})

def viewslider(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        all = Slider.objects.all()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'view_slider.html',{'slider':all,'stud':stud})

def editslider(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        editId = request.GET.get('editId')
        std = Slider.objects.get(pk=editId)
        frm1 = SliderForm(instance=std)
        if request.method == "POST":
            form = SliderForm(request.POST,request.FILES,instance=std)
            form.save()
            return redirect('/viewslider')
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'edit_slider.html',{'frm':frm1,'stud':stud})

def deleteslider(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        delid = request.GET.get('deleteId')
        delete = Slider.objects.filter(id=delid).delete()
        return redirect("/viewslider")

def addcategories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        sldfrm = CategoriesForm()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        if request.method == "POST":
            sldfrmfrm = CategoriesForm(request.POST,request.FILES)
            sldfrmfrm.save()
        return render(request,'add_categories.html',{'stud':stud,'sldfrm':sldfrm})

def viewcategories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        all = Categories.objects.all()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'view_categories.html',{'slider':all,'stud':stud})

def editcategories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        editId = request.GET.get('editId')
        std = Categories.objects.get(pk=editId)
        frm1 = CategoriesForm(instance=std)
        if request.method == "POST":
            form = CategoriesForm(request.POST,request.FILES,instance=std)
            form.save()
            return redirect('/viewcategories')
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        return render(request,'edit_categories.html',{'frm':frm1,'stud':stud})

def deletecategories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        delid = request.GET.get('deleteId')
        delete = Categories.objects.filter(id=delid).delete()
        return redirect("/viewcategories")

def addsubcategories(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        subcatfrm = SubCategoriesForm()
        editId = request.session['user_id']
        stud = Student.objects.get(id=editId)
        categories = Categories.objects.all()
        if request.method == "POST":
            subcatfrm = SubCategoriesForm(request.POST,request.FILES)
            subcatfrm.save()
        return render(request,'add_subcategories.html',{'stud':stud,'subcatfrm':subcatfrm,'categories':categories})
