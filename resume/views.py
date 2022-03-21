from django.http import HttpResponse
import json
from .models import User
from django.template import loader


def index(request):

    my_list = []


    user_details = User.objects.all()
    template = loader.get_template('resumes/index.html')

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
        #my_list.append(user_dict)

    uploaded = json.dumps(user_dict)

    context = {
        'User_details' : uploaded
    }
    print(context)

    #return HttpResponse(uploaded)
    return HttpResponse(template.render(context,request))