from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django import template
from django.template import loader
from Home.models import *
import json

# Create your views here.


class SignupView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('authentication/signup.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('authentication/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('authentication/500_page.html')
            return HttpResponse(html_template.render(context, request))

    def post(self, request, *args, **kwargs):

        context = {}
        try:
            signup_data = json.loads(request.body.decode('UTF-8'))

            if not CustomUser.objects.filter(user_name=signup_data.get("uname"), mobile=signup_data.get("mobile"), email=signup_data.get("email")).exists():

                if signup_data.get("password") == signup_data.get("conform_password"):

                    hash_password = make_password(signup_data.get("password"))
                    user_obj = CustomUser.objects.create(name=signup_data.get("name"), user_name=signup_data.get(
                        "uname"), mobile=signup_data.get("mobile"), email=signup_data.get("email"), password=hash_password, term_conditions=True)

                    if user_obj.id is not None:

                        context["status"] = 201
                        context["massage"] = 'user created'
                        context["data"] = True
                        return JsonResponse(context)

                    context["status"] = 403
                    context["massage"] = 'user not created'
                    context["data"] = False
                    return JsonResponse(context)

                context["status"] = 401
                context["massage"] = 'Password and Conform Password not matched'
                context["data"] = False
                return JsonResponse(context)

            elif CustomUser.objects.filter(user_name=signup_data.get("uname")).exists():
                context["status"] = 401
                context["massage"] = 'user name already exist'
                context["data"] = False
                return JsonResponse(context)

            elif CustomUser.objects.filter(mobile=signup_data.get("mobile")).exists():
                context["status"] = 401
                context["massage"] = 'user mobile already exist'
                context["data"] = False
                return JsonResponse(context)

            elif CustomUser.objects.filter(email=signup_data.get("email")).exists():
                context["status"] = 401
                context["massage"] = 'user name already exist'
                context["data"] = False
                return JsonResponse(context)

        except Exception as e:
            print(e)
            context["status"] = 500
            context["massage"] = str(e)
            context["data"] = False
            return JsonResponse(context)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)


class LoginView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('authentication/login.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('authentication/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('authentication/500_page.html')
            return HttpResponse(html_template.render(context, request))

    def post(self, request, *args, **kwargs):

        context = {}
        try:
            login_data = json.loads(request.body.decode('UTF-8'))

            if login_data.get("mobile",None) is not None and login_data.get("password",None) is not None:

                if CustomUser.objects.filter(mobile=login_data.get("mobile",None)).exists():

                    email=CustomUser.objects.get(mobile=login_data.get("mobile",None)).email
                    password=login_data.get("password")

                    user=authenticate(email=email,password=password)
                    if user is not None:
                        login(request,user)
                        context["status"] = 200
                        context["massage"] = 'login Succesfully'
                        context["data"] = True
                        return JsonResponse(context)

                    context["status"] = 401
                    context["massage"] = 'Mobile and Password not match'
                    context["data"] = False
                    return JsonResponse(context)

                context["status"] = 401
                context["massage"] = 'You are not register'
                context["data"] = False
                return JsonResponse(context)



            elif login_data.get("mobile",None) is  None :
                context["status"] = 401
                context["massage"] = 'Mobile is required'
                context["data"] = False
                return JsonResponse(context)

            elif login_data.get("password",None) is  None:
                context["status"] = 401
                context["massage"] = 'Password  is required'
                context["data"] = False
                return JsonResponse(context)



        except Exception as e:
            print(e)
            context["status"] = 500
            context["massage"] = str(e)
            context["data"] = False
            return JsonResponse(context)

    def put(self, request, *args, **kwargs):
        # handle PUT requests
        data = {
            'message': 'This is a PUT request'
        }
        return JsonResponse(data)

    def patch(self, request, *args, **kwargs):
        # handle PATCH requests
        data = {
            'message': 'This is a PATCH request'
        }
        return JsonResponse(data)

    def delete(self, request, *args, **kwargs):
        # handle DELETE requests
        data = {
            'message': 'This is a DELETE request'
        }
        return JsonResponse(data)

class LogoutView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'Logout'}
            logout(request)
            html_template = loader.get_template('authentication/login.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))