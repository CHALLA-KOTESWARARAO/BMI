from django.shortcuts import render

# Create your views here.
def bmi_cal(request):
    bmi=0
    height=0
    weight=0
    if request.method=='POST':
        height=float(request.POST.get("height"))
        weight=float(request.POST.get("weight"))
        if height and weight:
            bmi=weight/((height/100)**2)
            bmi=round(bmi,2)
    return render(request,"bmi.html",{"bmi":bmi,"height":height,"weight":weight})

