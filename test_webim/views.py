from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse
from django.shortcuts import redirect, render
def get_friends(request):
    uid = SocialAccount.objects.get(user_id=request.user.id).uid
    # response = request.get('')
    return HttpResponse(uid)
