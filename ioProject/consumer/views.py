from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import forms
from . import models
import json
# Create your views here.
target_list = {
    "consumer_is_exist": 1,
}


def path_only_user(request):
    # print(request.POST)
    data = request.POST["TARGET"]
    flag = target_list[data]
    if flag == 1:
        return consumer_is_exist(request)
    return HttpResponse("ERROR REQUEST")


def consumer_register(request):
    consumer_form = forms.ConsumerForm()
    if request.method == "POST":
        consumer_input = forms.ConsumerForm(request.POST)
        if consumer_input.is_valid():
            _consumer = models.Consumer()
            temp_set = {
                "Account": request.POST["Account"],
                "Password": request.POST["Password"],
                "Name": request.POST["Name"],
                "Gender": request.POST["Gender"],
                "BirthDay": request.POST["BirthDay"],
                "Phone": request.POST["Phone"],
                "Email": request.POST["Email"],
            }
            _consumer.create_self(temp_set)
            _consumer.save()
            return HttpResponse("SUCCESS")
        else:
            err_message = consumer_input.errors
            return render(request, 'consumer/register.html', {"form": consumer_form, "errors": err_message})
    return render(request, 'consumer/register.html', {"form": consumer_form})


def consumer_is_exist(request):
    is_exist = models.Consumer.objects.filter(Account=request.POST["ACT"]).exists()
    if is_exist:
        result = {'result': "true"}
    else:
        result = {"result": "false"}
    return HttpResponse(json.dumps(result))


def consumer_log_in(request):
    return render(request, 'consumer/login.html')


def consumer_log_out(request):
    pass


def interface_test(request):
    meta = request.META.items()
    html = []
    for k, v in meta:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        print(str(k) + ":" + str(v))
    # consumer = models.Consumer
    # consumer_list = consumer.objects.all()
    # con = consumer_list[0]
    # print(consumer_list)
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
