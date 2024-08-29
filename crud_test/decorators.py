from django.shortcuts import redirect
from django.conf import settings

def unauthenticated_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return view_func(request, *args, **kwargs)
    return _wrapped_view