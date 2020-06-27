import requests
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render


def redirect_view(request):
    response = redirect('/accounts/vk/login/')
    return response

def auth_page_view(request):
    return render(request, 'authVK/base_auth.html')

@login_required(login_url='auth_page/')
def get_friends_view(request):
    uid = SocialAccount.objects.get(user_id=request.user.id).uid
    try:
        response = requests.get('https://api.vk.com/method/friends.get?user_id={}&order=random&count=5&fields=photo_100&access_token=2d05bd122d05bd122d05bd121a2d777f9c22d052d05bd1273f6eb4c98f05580c32cb469&v=5.110'.format(uid))
        friends_list = response.json()['response']['items']
        if friends_list:
            context = {'user': request.user,
                       'friends': friends_list,
                       }
            return render(request, 'authVK/main_page.html', context=context)
        return HttpResponse('Sorry, we can\'t search your friends')
    except KeyError:
        print('Ошибка доступа к странице')
        return HttpResponse('Forbidden')