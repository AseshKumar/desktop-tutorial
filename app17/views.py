from django.shortcuts import render,redirect
from app17.models import Employee
from django.contrib import messages


def Show(request):
    return render(request,"index.html")


def employee_add(request):
    return render(request,"employee_add.html")


def save_employee(request):
    id=request.POST.get("t1")
    nm=request.POST.get("t2")
    sa=request.POST.get("t3")
    Employee(idno=id,name=nm,salary=sa).save()
    messages.success(request,"Resgistations Done")
    return redirect("employee_add")


def view_emplo(request):
    res=Employee.objects.all()
    return render(request,"view_emplo.html",{"data":res})


def update(request):
    us =request.GET.get("id")
    result =Employee.objects.get(idno=us)
    return render(request,"update.html",{"data":result})


def udate_employeee(request):
    q=request.POST.get('t1')
    w=request.POST.get('t2')
    r=request.POST.get('t3')
    Employee.objects.filter(idno=q).update(name=w,salary=r)
    return redirect("view_emplo")


def delete(request):
    do=request.GET.get("no")
    Employee.objects.filter(idno=do).delete()
    return redirect("view_emplo")