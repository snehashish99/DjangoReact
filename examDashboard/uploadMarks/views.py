from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .models import exam_data

# Create your views here.

def submit_data(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        roll = request.GET.get('roll')
        gender = request.GET.get('gender')
        physics = request.GET.get('physics')
        chemistry = request.GET.get('chemistry')
        maths = request.GET.get('maths')

        #average = (physics + maths + chemistry)/3
        #average = round(average,2)

        #save here
        exam_data.objects.create(
            name = name,
            roll = roll,
            gender = gender,
            physics = physics,
            chemistry = chemistry,
            maths = maths,
        )
    return redirect('http://localhost:3000/')   

def get_data(request): 

    all_data = exam_data.objects.all()
    data=[]
    for i in all_data:
        data.append({
            'name' : i.name,
            'roll' : i.roll,
            'gender' : i.gender,
            'physics' : i.physics,
            'chemistry' : i.chemistry,
            'maths' : i.maths,
        })
    jsonresponse = {'data':data}

    return JsonResponse(jsonresponse)