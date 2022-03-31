from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import User,Education, Certification, Workexperience
from django.template import loader
from django.http import FileResponse

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


    work_experience_items =  Workexperience.objects.all()

    for work_experience_item in work_experience_items:
        workexperience = {}
        responsibility_list = []
        workexperience["From Year"] = work_experience_item.yearfrom
        workexperience["To Year"] = work_experience_item.yearto
        workexperience["Company"] = work_experience_item.company
        workexperience["Project Role"] = work_experience_item.projectrole
        responsibility_list.append(work_experience_item.responsibility1)
        responsibility_list.append(work_experience_item.responsibility2)
        responsibility_list.append(work_experience_item.responsibility3)
        responsibility_list.append(work_experience_item.responsibility4)
        responsibility_list.append(work_experience_item.responsibility5)
        responsibility_list.append(work_experience_item.responsibility6)
        responsibility_list.append(work_experience_item.responsibility7)
        responsibility_list.append(work_experience_item.responsibility8)
        responsibility_list.append(work_experience_item.responsibility9)
        responsibility_list.append(work_experience_item.responsibility10)
        workexperience["Responsibilities"] = responsibility_list




    context = {
        'User_details' : user_uploaded,
        'education_details': education_uploaded,
        'certification_details': certification,
        'work_experience' : workexperience

    }


    print(type(str(context)))

    return HttpResponse(template.render(context,request))
    #return JsonResponse(user_dict, json_dumps_params={'indent': 2})


def download(request):
  file=open('resume/static/Shannon_CV.pdf','rb')
  response =FileResponse(file)
  response['Content-Type']='application/octet-stream'
  response['Content-Disposition']='attachment;filename="Shannon_CV.pdf"'
  return response





