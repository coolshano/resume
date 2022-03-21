from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import User,Education, Certification
from django.template import loader

template = loader.get_template('resumes/index.html')

def index(request):

    user_details = User.objects.all()

    for details in user_details:
        user_dict = {}
        hobby_list = []
        user_dict["country"] = details.country
        user_dict["address"] = details.address
        user_dict["mobile"] = details.mobile
        user_dict["email"] = details.email
        hobby_list.append(details.hobby1)
        hobby_list.append(details.hobby2)
        hobby_list.append(details.hobby3)
        user_dict["hobbies"] = hobby_list

    user_uploaded = json.dumps(user_dict)


    education_details = Education.objects.all()

    for education_item in education_details:
        education = {}
        education["degree"] = education_item.degree
        education["higher national diploma [Edexcel UK]"] = education_item.degree

    education_uploaded = json.dumps(education)

    certification_items = Certification.objects.all()

    for certification_item in certification_items:
        certification = {}
        multi_aws = []
        certification["ITIL"] = certification_item.certification1
        certification["Kubernetes"] = certification_item.certification2
        multi_aws.append(certification_item.certification3)
        multi_aws.append(certification_item.certification4)
        multi_aws.append(certification_item.certification5)
        certification["AWS"] = multi_aws




    context = {
        'User_details' : user_uploaded,
        'education_details': education_uploaded,
        'certification_details': certification
    }


    print(type(str(context)))

    return HttpResponse(template.render(context,request))
    #return JsonResponse(user_dict, json_dumps_params={'indent': 2})





