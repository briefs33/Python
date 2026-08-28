from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import json

subjects = [{"name": "Maths"}, {"name": "PE"}]

def hello_world(request):
    return HttpResponse("Hello Informatika s Misom")

def list_subjects(request):
    if request.method == "GET":
        return JsonResponse(subjects, safe = False, status = 200)
    elif request.method == "POST":
        subject = request.body

        print (subject)
        print (type(subject))

        subject_dict = json.loads(subject)

        print(subject_dict)
        print(type(subject_dict))

        subjects.append(subject)

#        return HttpResponse("Test")
        return JsonResponse(subject_dict, status = 200)