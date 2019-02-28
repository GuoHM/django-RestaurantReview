from .models import User


def is_login(request):
    if 'userid' not in request.session:
        return False
    return True


def get_current_user(request):
    return User.objects.get(user_id=request.session['userid'])