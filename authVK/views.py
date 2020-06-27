import requests
from allauth.socialaccount.models import SocialAccount, SocialToken
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
    social_account = SocialAccount.objects.get(user_id=request.user.id)
    access_token = SocialToken.objects.get(account_id=social_account.id).token
    try:
        response = requests.get('https://api.vk.com/method/friends.get?user_id={}&order=random&count=5&fields=photo_100&access_token={}&v=5.110'.format(social_account.uid, access_token))
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