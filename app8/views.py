from django.shortcuts import render
from django.views.generic import View
import json
from app8.models import CourseModel
from django.http import HttpResponse
from app8.forms import CourseForm
from django.core.serializers import serialize

class InsertCourse(View):
    def post(self,request):
        data=request.body
        dict_data=json.loads(data)
        #CourseModel(name=dict_data["name"],fee=dict_data["fee"]).save()
        cf = CourseForm(dict_data)
        if cf.is_valid():
            cf.save()
            json_data=json.dumps({"message":"Course is saved"})
        else:
            json_data=json.dumps({"error":cf.errors})

        return HttpResponse(json_data,content_type="application/json")

    def get(self,request,cid=0):
        try:
            res=CourseModel.objects.get(idno=cid)
            json_data=serialize("json",[res])
        except  CourseModel.DoesNotExist:
            json_data=json.dumps({"error":"Invalid course id"})

        return HttpResponse(json_data,content_type="application/json")

