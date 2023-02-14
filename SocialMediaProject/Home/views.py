from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.template import loader
from django import template
from Home.models import *
import json

# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':

                print(request.user)
                post_list = []
                post_dict = {}
                post_data_dict = {}
                posted_by = {}

                if request.user.profile_image:
                    print(request.user.profile_image)
                else:
                    print("no data")

                user_info = {
                    "name": request.user.name,
                    "image": request.user.profile_image.url if request.user.profile_image else None,
                    "user_id": request.user.id,
                }

                for post_obj in Post.objects.all().order_by('-id'):
                    # print(post_obj)

                    if Friend.objects.filter(user=request.user, friend=post_obj.user).exists():
                        print('inside the if ', post_obj)

                        # -------posted by Dict----------

                        posted_by['name'] = post_obj.user.name
                        posted_by['image'] = post_obj.user.profile_image.url if post_obj.user.profile_image.name else None
                        posted_by['id'] = post_obj.user.id

                        post_dict['posted_by'] = posted_by
                        posted_by = {}

                        # ------post data dict------------

                        post_data_dict["image"] = post_obj.image.url
                        post_data_dict["text"] = post_obj.text
                        post_data_dict["post_id"] = post_obj.id

                        post_dict['post'] = post_data_dict
                        post_data_dict = {}

                        # ------post list-----------------
                        post_list.append(post_dict)
                        post_dict = {}
                    print({"user_info": user_info, "post": post_list})
                context['status'] = 200
                context['massage'] = "OK"
                context['data'] = {"user_info": user_info, "post": post_list}

                return JsonResponse(context)

            context = {'segment': 'index', "user": request.user}

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


class SearchView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        # try:
        # print(request.META)
        

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            friend_list = []
            friend_dict = {}

            rest_user_list = []
            rest_user_dict = {}

            key = request.GET.get("key")
            if CustomUser.objects.filter(Q(name__icontains=key) | Q(email__icontains=key) | Q(mobile__icontains=key)).exists():

                for user_obj in CustomUser.objects.filter(Q(name__icontains=key) | Q(email__icontains=key) | Q(mobile__icontains=key)):

                    if Friend.objects.filter(user=request.user, friend=user_obj):

                        friend_dict['user_id'] = user_obj.id
                        friend_dict['name'] = user_obj.name
                        friend_dict['image'] = user_obj.profile_image.url if user_obj.profile_image.name else None
                        friend_dict['friend'] = True
                        friend_dict['request'] = False
                        friend_dict['blocked'] = False

                        friend_list.append(friend_dict)
                        friend_dict = {}
                    else:

                        rest_user_dict['user_id'] = user_obj.id
                        rest_user_dict['name'] = user_obj.name
                        rest_user_dict['image'] = user_obj.profile_image.url if user_obj.profile_image.name else None
                        rest_user_dict['friend'] = False

                        if FriendRequest.objects.filter(sender=request.user, resiver=user_obj, action=False, blocked=False).exists():

                            rest_user_dict['request'] = True

                        else:
                            rest_user_dict['request'] = False

                        if FriendRequest.objects.filter(sender=request.user, blocked=True).exists():

                            rest_user_dict['blocked'] = True
                        else:
                            rest_user_dict['blocked'] = False

                        rest_user_list.append(rest_user_dict)
                        rest_user_dict = {}

                search_result = friend_list+rest_user_list

                # print(search_result)

                context["status"] = 200
                context["massage"] = "ok"
                context["data"] = search_result
                return JsonResponse(context)

            context['status'] = 401
            context['massage'] = "User Not Found"
            context['data'] = []
            return JsonResponse(context)

        context = {'segment': 'index'}

        html_template = loader.get_template('home/search.html')
        # html_template = loader.get_template('signup.html')

        return HttpResponse(html_template.render(context, request))

        # except template.TemplateDoesNotExist:

        #     html_template = loader.get_template('home/404_page.html')
        #     return HttpResponse(html_template.render(context, request))

        # except:

        #     html_template = loader.get_template('home/500_page.html')
        #     return HttpResponse(html_template.render(context, request))

    def post(self, request, *args, **kwargs):
        context = {}
        try:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-1':
                user_data = json.loads(request.body.decode('UTF-8'))
                print('Request',user_data)

                FriendRequest

                context["status"] = 200
                context["massage"] = 'This is a POST request send'
                context["data"] = []
                return JsonResponse(context)

            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-2':
                user_data = json.loads(request.body.decode('UTF-8'))
                print('Cancel',user_data)

                context["status"] = 200
                context["massage"] = 'This is a POST request cancel'
                context["data"] = []
                return JsonResponse(context)

        except:

            context["status"] = 500
            context["massage"] = 'This is a POST request'
            context["data"] = []
            return JsonResponse(context)

        # # handle POST requests
        # data = {
        #     'message': 'This is a POST request'
        # }
        # return JsonResponse(data)

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


# class FriendRequestView(View):

#     def get(self, request, *args, **kwargs):

#         context = {}
#         try:
#             if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-1':

#                 context["status"] = 200
#                 context["massage"] = "ok"
#                 context["data"] = []
#                 return JsonResponse(context)

#             if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-2':

#                 context["status"] = 200
#                 context["massage"] = "ok"
#                 context["data"] = []
#                 return JsonResponse(context)

#         except:

#             context["status"] = 200
#             context["massage"] = "ok"
#             context["data"] = []
#             return JsonResponse(context)



#     def post(self, request, *args, **kwargs):

#         # handle POST requests
#         data = {
#             'message': 'This is a POST request'
#         }
#         return JsonResponse(data)

#     def put(self, request, *args, **kwargs):
#         # handle PUT requests
#         data = {
#             'message': 'This is a PUT request'
#         }
#         return JsonResponse(data)

#     def patch(self, request, *args, **kwargs):
#         # handle PATCH requests
#         data = {
#             'message': 'This is a PATCH request'
#         }
#         return JsonResponse(data)

#     def delete(self, request, *args, **kwargs):
#         # handle DELETE requests
#         data = {
#             'message': 'This is a DELETE request'
#         }
#         return JsonResponse(data)


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
