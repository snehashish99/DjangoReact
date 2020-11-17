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

        average = (int(physics) + int(maths) + int(chemistry))/3
        average = round(average,2)

        #save here
        exam_data.objects.create(
            name = name,
            roll = roll,
            gender = gender,
            physics = physics,
            chemistry = chemistry,
            maths = maths,
            average = average,
        )
    jsonresponse = {'status':'success'}
    return JsonResponse(jsonresponse)   

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
            'average': i.average,
        })
    jsonresponse = {'data':data}

    return JsonResponse(jsonresponse)