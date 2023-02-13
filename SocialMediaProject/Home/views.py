from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django import template

# Create your views here.

class IndexView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            
            context = {'segment': 'index'}

            html_template = loader.get_template('home/index.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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



class MassageView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('home/massage.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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


class NotificationView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('home/notifications.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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


class ProfileAllView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('home/profile_all.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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


class ProfileView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('home/profile.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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


class SearchView(View):
    
    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context = {'segment': 'index'}

            html_template = loader.get_template('home/search.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))
        
        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))


    def post(self, request, *args, **kwargs):

        # handle POST requests
        data = {
            'message': 'This is a POST request'
        }
        return JsonResponse(data)


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



