from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import translation
from django.views.decorators.http import require_POST

from .decorators import superuser_login_required


def bad_request(request, exception=None):
    return render(request, 'errors/bad_request.html', status=400)


def permission_denied(request, exception=None):
    return render(request, 'errors/permission_denied.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'errors/page_not_found.html', status=404)


def server_error(request):
    return render(request, 'errors/server_error.html', status=500)


@superuser_login_required
def simulated_error(request):
    raise Exception('Simulated error')


@require_POST
def change_language(request):
    user_language = request.POST.get('language')
    redirect_to = request.POST.get('redirect_to', None)
    translation.activate(user_language)

    if redirect_to:
        response = redirect(redirect_to)
    else:
        response = HttpResponse(status=204)

    response.set_cookie('language_code', user_language)
    return response
