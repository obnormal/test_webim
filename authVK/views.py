from django.shortcuts import redirect, render


def redirect_view(request):
    response = redirect('/accounts/vk/login/')
    return response

def main_page_view(request):
    return render(request, 'authVK/base_auth.html')