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
        user_dict["name"] = details.name
        user_dict["age"] = details.age
        my_list.append(user_dict)

    uploaded = json.dumps(my_list)

    context = {
        'User_details' : uploaded
    }
    print(context)

    #return HttpResponse(uploaded)
    return HttpResponse(template.render(context,request))