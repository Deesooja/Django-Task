from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.template import loader
from django import template
from Home.models import *
import json
from django.conf import settings
# from cloudinary.utils import cloudinary_url
from Home.MyModule.get_url import get_post_url, get_user_url

# Create your views here.

@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:
            context["base_url"]=settings.BASE_URL
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':

                # print(get_user_url(CustomUser.objects.get(id=1)))

                print("request.user", request.user)
                post_list = []
                post_dict = {}
                post_data_dict = {}
                posted_by = {}

                # if request.user.profile_image:
                #     print(request.user.profile_image)
                # else:
                #     print("no data")

                user_info = {
                    "name": request.user.name,
                    # "image": request.user.profile_image.url if request.user.profile_image else None,
                    "image": get_user_url(request.user),
                    "user_id": request.user.id,
                }

                for post_obj in Post.objects.all().order_by('-id'):
                    # print(post_obj)


                    if Friend.objects.filter(user=request.user, friend=post_obj.user).exists() or post_obj.user==request.user :
                        # print('inside the if ', post_obj)

                        # -------posted by Dict----------

                        posted_by['name'] = post_obj.user.name
                        # posted_by['image'] = post_obj.user.profile_image.url if post_obj.user.profile_image.name else None
                        posted_by['image'] = get_user_url(post_obj.user)
                        posted_by['id'] = post_obj.user.id

                        post_dict['posted_by'] = posted_by
                        posted_by = {}

                        # ------post data dict------------

                        # post_data_dict["image"] = post_obj.image.url
                        post_data_dict["image"] = get_post_url(post_obj)
                        post_data_dict["text"] = post_obj.text
                        post_data_dict["post_id"] = post_obj.id

                        post_dict['post'] = post_data_dict
                        post_data_dict = {}

                        # ------post list-----------------
                        post_list.append(post_dict)
                        post_dict = {}
                    # print({"user_info": user_info, "post": post_list})
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


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
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

            key = request.GET.get("key",None)
            if key:
                print("value")
            else:
                print("not value")
            print("key",key)
            if key:
                if CustomUser.objects.filter(Q(name__icontains=key) | Q(email__icontains=key) | Q(mobile__icontains=key)).exists():

                    for user_obj in CustomUser.objects.filter(Q(name__icontains=key) | Q(email__icontains=key) | Q(mobile__icontains=key)):
                        if request.user == user_obj:
                            continue

                        if Friend.objects.filter(user=request.user, friend=user_obj) or Friend.objects.filter(user=user_obj, friend=request.user) :

                            friend_dict['user_id'] = user_obj.id
                            friend_dict['name'] = user_obj.name
                            # friend_dict['image'] = user_obj.profile_image.url if user_obj.profile_image.name else None
                            friend_dict['image'] = get_user_url(user_obj)
                            friend_dict['friend'] = True
                            friend_dict['request'] = False
                            friend_dict['blocked'] = False

                            friend_list.append(friend_dict)
                            friend_dict = {}
                        else:

                            rest_user_dict['user_id'] = user_obj.id
                            rest_user_dict['name'] = user_obj.name
                            # rest_user_dict['image'] = user_obj.profile_image.url if user_obj.profile_image.name else None
                            rest_user_dict['image'] = get_user_url(user_obj)
                            rest_user_dict['friend'] = False

                            if FriendRequest.objects.filter(sender=request.user, resiver=user_obj, action=False, blocked=False, cancel_by_sender=False).exists():

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
                    context["key"] = key
                    return JsonResponse(context)

                context['status'] = 401
                context['massage'] = "User Not Found"
                context['data'] = []
                context["key"] = key
                return JsonResponse(context)
            context['status'] = 401
            context['massage'] = "Key Is None"
            context["key"] = key
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
                print('Request', user_data)
                user_data.get('user_id')
                user_obj = CustomUser.objects.get(id=user_data.get('user_id'))

                if FriendRequest.objects.filter(sender=request.user, resiver=user_obj).exists():

                    friend_request_obj = FriendRequest.objects.filter(
                        sender=request.user, resiver=user_obj).last()

                    atempt = friend_request_obj.atempt

                    new_atempt = atempt+1

                    new_friend_request_obj = FriendRequest.objects.create(
                        sender=request.user, resiver=user_obj, atempt=new_atempt)

                    if new_friend_request_obj.id is not None:
                        context['status'] = 201
                        context['massage'] = "Friend request send"
                        context['data'] = [
                            {"friend_request_id": new_friend_request_obj.id}]
                        return JsonResponse(context)

                else:

                    friend_request_obj = FriendRequest.objects.create(
                        sender=request.user, resiver=user_obj)

                    if friend_request_obj.id is not None:
                        context['status'] = 201
                        context['massage'] = "Friend request send"
                        context['data'] = [
                            {"friend_request_id": friend_request_obj.id}]
                        return JsonResponse(context)

            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-2':

                user_data = json.loads(request.body.decode('UTF-8'))
                print('Cancel', user_data)

                if FriendRequest.objects.filter(sender=request.user, resiver=user_data.get("user_id"), action=False, blocked=False, cancel_by_sender=False).exists():
                    friend_request_obj = FriendRequest.objects.filter(sender=request.user, resiver=user_data.get(
                        "user_id"), action=False, blocked=False, cancel_by_sender=False).last()
                    friend_request_obj.cancel_by_sender = True
                    friend_request_obj.save()
                    if friend_request_obj.id:
                        context["status"] = 200
                        context["massage"] = 'Friend request cancel'
                        context["data"] = []
                        return JsonResponse(context)

                    context["status"] = 200
                    context["massage"] = 'Friend request Not Canceled yet cancel'
                    context["data"] = []
                    return JsonResponse(context)

                context["status"] = 200
                context["massage"] = 'does not fund active request'
                context["data"] = []
                return JsonResponse(context)

        except:

            context["status"] = 500
            context["massage"] = 'This is a POST request'
            context["data"] = []
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


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class FriendRequestView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:

            context = {'segment': 'index'}
            user = request.user
            if FriendRequest.objects.filter(resiver=user, cancel_by_sender=False, action=False, accept=False, blocked=False).exists():

                friend_request = FriendRequest.objects.filter(
                    resiver=user, cancel_by_sender=False, action=False, accept=False, blocked=False)
                print(len(friend_request))
                context['friend_request'] = friend_request

            html_template = loader.get_template('home/friend_request.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))

    def post(self, request, *args, **kwargs):
        context = {}

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-1':

            friend_request_data = json.loads(request.body.decode('UTF-8'))
            friend_request_id = friend_request_data.get("friend_request_id")

            FriendRequest.objects.filter(
                id=friend_request_id).update(action=True, accept=True)
            friend_request_obj = FriendRequest.objects.get(
                id=friend_request_id)

            new_friend_obj = Friend.objects.create(
                user=friend_request_obj.resiver, friend=friend_request_obj.sender)

            if new_friend_obj.id:
                context["status"] = 200
                context["massage"] = 'friend Request accepted'
                context["data"] = []
                return JsonResponse(context)
            context["status"] = 401
            context["massage"] = 'friend Request not accepted'
            context["data"] = []
            return JsonResponse(context)


        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-2':

            friend_request_data = json.loads(request.body.decode('UTF-8'))
            friend_request_id=friend_request_data.get("friend_request_id")

            updated_row=FriendRequest.objects.filter(id=friend_request_id).update(action=True)

            if updated_row>0:
                context["status"] = 200
                context["massage"] = 'friend Request Rejected'
                context["data"] = []
                return JsonResponse(context)

            context["status"] = 401
            context["massage"] = 'friend Request Not Rejected'
            context["data"] = []
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


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class AllFriendsView(View):

    def get(self, request, *args, **kwargs):

            context = {}
        # try:
            context = {'segment': 'index'}
            all_friends_search_user=Friend.objects.filter(user=request.user).order_by("-id")
            context["all_friends_search_user"]=all_friends_search_user

            all_friends_search_friend=Friend.objects.filter(friend=request.user).order_by("-id")
            context["all_friends_search_friend"]=all_friends_search_friend


            # if Friend.objects.filter(Q(user=request.user)|Q(friend=request.user)).exists():

            #     for friends_obj in Friend.objects.filter(Q(user=request.user)|Q(friend=request.user)) :

            #         if friends_obj.user == request.user :

            #             context["all_friends"]=all_friends




            # context["all_friends"]=all_friends

            html_template = loader.get_template('home/all_friends.html')
            # html_template = loader.get_template('signup.html')

            return HttpResponse(html_template.render(context, request))

        # except template.TemplateDoesNotExist:

        #     html_template = loader.get_template('home/404_page.html')
        #     return HttpResponse(html_template.render(context, request))

        # except:

        #     html_template = loader.get_template('home/500_page.html')
        #     return HttpResponse(html_template.render(context, request))

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
        context={}
        
        id=kwargs.get("id")

        friend_obj=Friend.objects.get(id=id)
        deteted_data=friend_obj.delete()

        print(deteted_data)
        if deteted_data:

            context["status"] = 204
            context["massage"] = 'Unfriend  done'
            context["data"] = []
            return JsonResponse(context)

        context["status"] = 401
        context["massage"] = 'Unfriend  not done'
        context["data"] = []
        return JsonResponse(context)


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class ProfileAllView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:

            context = {'segment': 'index'}
            user_id = request.GET.get("user_id")

            if CustomUser.objects.filter(id=user_id).exists():
                context["user"] = CustomUser.objects.get(id=user_id)

            if Friend.objects.filter(user=user_id).exists():
                context["friend"] = Friend.objects.filter(user=user_id).count()
            else:
                context["friend"] = 0

            if Post.objects.filter(user=user_id).exists():

                context["post"] = Post.objects.filter(user=user_id).count()
            else:
                context["post"] = 0

            if FriendRequest.objects.filter(sender=request.user, resiver=user_id, action=False, blocked=False, cancel_by_sender=False).exists():

                context['request'] = True

            else:
                context['request'] = False

            if FriendRequest.objects.filter(sender=request.user, blocked=True).exists():

                context['blocked'] = True
            else:
                context['blocked'] = False

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

        context = {}
        try:
            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-1':
                user_data = json.loads(request.body.decode('UTF-8'))
                print('Request', user_data)
                user_data.get('user_id')
                user_obj = CustomUser.objects.get(id=user_data.get('user_id'))

                if FriendRequest.objects.filter(sender=request.user, resiver=user_obj).exists():

                    friend_request_obj = FriendRequest.objects.filter(
                        sender=request.user, resiver=user_obj).last()

                    atempt = friend_request_obj.atempt

                    new_atempt = atempt+1

                    new_friend_request_obj = FriendRequest.objects.create(
                        sender=request.user, resiver=user_obj, atempt=new_atempt)

                    if new_friend_request_obj.id is not None:
                        context['status'] = 201
                        context['massage'] = "Friend request send"
                        context['data'] = [
                            {"friend_request_id": new_friend_request_obj.id}]
                        return JsonResponse(context)

                else:

                    friend_request_obj = FriendRequest.objects.create(
                        sender=request.user, resiver=user_obj)

                    if friend_request_obj.id is not None:
                        context['status'] = 201
                        context['massage'] = "Friend request send"
                        context['data'] = [
                            {"friend_request_id": friend_request_obj.id}]
                        return JsonResponse(context)
                    context['status'] = 401
                    context['massage'] = "Friend request not  send"
                    context['data'] = []
                    return JsonResponse(context)

            if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-2':

                user_data = json.loads(request.body.decode('UTF-8'))
                print('Cancel', user_data)

                if FriendRequest.objects.filter(sender=request.user, resiver=user_data.get("user_id"), action=False, blocked=False, cancel_by_sender=False).exists():
                    friend_request_obj = FriendRequest.objects.filter(sender=request.user, resiver=user_data.get(
                        "user_id"), action=False, blocked=False, cancel_by_sender=False).last()
                    friend_request_obj.cancel_by_sender = True
                    friend_request_obj.save()
                    if friend_request_obj.id:
                        context["status"] = 200
                        context["massage"] = 'Friend request cancel'
                        context["data"] = []
                        return JsonResponse(context)

                    context["status"] = 401
                    context["massage"] = 'Friend request Not Canceled yet cancel'
                    context["data"] = []
                    return JsonResponse(context)
                context["status"] = 401
                context["massage"] = 'does not fund active request'
                context["data"] = []
                return JsonResponse(context)

        except:

            context["status"] = 500
            context["massage"] = 'This is a POST request'
            context["data"] = []
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


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class ProfileView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:

            context = {'segment': 'index'}

            if request.GET.get("user_id"):
                user_id = request.GET.get("user_id")
                context["user_check"] = False
            else:
                user_id = request.user.id
                context["user_check"] = True
            # print(user_id)
            # print(context["user_check"])

            if CustomUser.objects.filter(id=user_id).exists():
                context["user"] = CustomUser.objects.get(id=user_id)

            if Friend.objects.filter(user=user_id).exists():
                context["friend"] = Friend.objects.filter(user=user_id).count()
            else:
                context["friend"] = 0

            if Post.objects.filter(user=user_id).exists():

                context["post"] = Post.objects.filter(user=user_id).count()
                context["posted_data"] = Post.objects.filter(user=user_id)

                # print( len(context["posted_data"]))

            else:
                context["post"] = 0
                context["posted_data"] = []
            print('posted_data', len(context["posted_data"]))

            if FriendRequest.objects.filter(sender=request.user, resiver=user_id, action=False, blocked=False, cancel_by_sender=False).exists():

                context['request'] = True

            else:
                context['request'] = False

            if FriendRequest.objects.filter(sender=request.user, blocked=True).exists():

                context['blocked'] = True
            else:
                context['blocked'] = False

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
        context = {}
        # try:

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':

            profile_info_data = json.loads(request.body.decode('UTF-8'))

            user_id = request.user.id
            name = profile_info_data.get('name')
            user_name = profile_info_data.get('user_name')
            mobile = profile_info_data.get('mobile')
            email = profile_info_data.get('email')

            updated_data = CustomUser.objects.filter(id=user_id).update(
                name=name, user_name=user_name, mobile=mobile, email=email)

            if updated_data > 0:

                context["status"] = 200
                context["massage"] = 'Persional Detail updated'
                context["data"] = []
                return JsonResponse(context)

            context["status"] = 401
            context["massage"] = 'Persional Detail not  updated'
            context["data"] = []
            return JsonResponse(context)

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest-1':

            if request.FILES.get('profile_image') is not None:

                image_file = request.FILES.get('profile_image')

                user = request.user
                user.profile_image = image_file
                user.save()

                context["status"] = 200
                context["massage"] = 'Profile image Uploaded'
                context["data"] = {"profile_image_url": get_user_url(user)}
                return JsonResponse(context)

            context["status"] = 401
            context["massage"] = 'Profile image Not Uploaded'
            context["data"] = []
            return JsonResponse(context)

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
        context = {}

        print(kwargs.get("id"))
        post_id = kwargs.get("id")
        post_obj = Post.objects.get(id=post_id)

        detete_info = post_obj.delete()

        if detete_info:
            context["status"] = 204
            context["massage"] = 'Post Deleted'
            context["data"] = []
            return JsonResponse(context)

        context["status"] = 401
        context["massage"] = 'Post not  Deleted'
        context["data"] = []
        return JsonResponse(context)

        # # handle DELETE requests
        # data = {
        #     'message': 'This is a DELETE request'
        # }
        # return JsonResponse(data)


@method_decorator(login_required(login_url="/auth/login/"), name='dispatch')
class CreatePostView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        try:

            context = {'segment': 'index'}

            
                

            html_template = loader.get_template('home/create_post.html')
            # html_template = loader.get_template('signup.html')
            return HttpResponse(html_template.render(context, request))

        except template.TemplateDoesNotExist:

            html_template = loader.get_template('home/404_page.html')
            return HttpResponse(html_template.render(context, request))

        except:

            html_template = loader.get_template('home/500_page.html')
            return HttpResponse(html_template.render(context, request))

    def post(self, request, *args, **kwargs):
        context = {}
        # try:

        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            print(request.POST.get("text"))
            massage=request.POST.get("text")
            image_file = request.FILES.get('post_image')

            if image_file is not None and massage  is not None:

                new_post=Post.objects.create(user=request.user, image=image_file, text=massage)

                if new_post.id :
                    context["status"]=201
                    context["massage"]="created"
                    context["data"]=[]
                    return JsonResponse(context)

                context["status"]=401
                context["massage"]="not created"
                context["data"]=[]
                return JsonResponse(context)
                # print(image_file)
       

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
        context = {}

        print(kwargs.get("id"))
        post_id = kwargs.get("id")
        post_obj = Post.objects.get(id=post_id)

        detete_info = post_obj.delete()

        if detete_info:
            context["status"] = 204
            context["massage"] = 'Post Deleted'
            context["data"] = []
            return JsonResponse(context)

        context["status"] = 401
        context["massage"] = 'Post not  Deleted'
        context["data"] = []
        return JsonResponse(context)