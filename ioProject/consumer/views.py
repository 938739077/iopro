from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import forms
from . import models
import json
# Create your views here.
target_list = {
    "consumer_is_exist": 1,
}


def path_only_user(request):
    # print(request.POST)
    data = request.POST.get("TARGET")
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
            response = render_to_response('consumer/index.html', {'consumer': request.POST["Account"]})
            response.set_cookie("consumer", request.POST["Account"])
            return response
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
    log_form = forms.LoginForm()
    if request.method == "POST":
        consumer_input = forms.LoginForm(request.POST)
        if consumer_input.is_valid():
            consumer_act = request.POST.get("Account")
            consumer_pwd = request.POST.get("Password")
            is_exist = models.Consumer.objects.filter(Account=consumer_act)
            if is_exist:
                consumer = is_exist[0]
                if consumer_pwd == consumer.Password:
                    # response = HttpResponse()
                    # response.set_signed_cookie("consumer", consumer_act, salt='cookie')
                    response = render_to_response('consumer/index.html', {'consumer': consumer_act})
                    response.set_cookie("consumer", consumer_act)
                    return response
                else:
                    return render(request, 'consumer/login.html', {"form": log_form, "err_msg": "密码错误"})
            else:
                return render(request, 'consumer/login.html', {"form": log_form, "err_msg": "账号不存在"})
        else:
            err_message = consumer_input.errors
            return render(request, 'consumer/login.html', {"form": log_form, "err_msg": err_message})
    else:
        return render(request, 'consumer/login.html', {"form": log_form})


def consumer_log_out(request):
    response = HttpResponseRedirect('/user/index')
    response.delete_cookie("consumer")
    return response


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


def index(request):
    cookie = request.COOKIES.get("consumer")
    if cookie:
        response = render_to_response('consumer/index.html', {'consumer': cookie})
        response.set_cookie("consumer", cookie)
        return response
    else:
        return HttpResponseRedirect('/user/login')
