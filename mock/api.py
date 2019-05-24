from django.http import JsonResponse


def follow_user(request):
    """关注用户 返回一个状态 ok = bool 和 message =  string"""
    result = {
        'ok': True,
        'message': 'success or failure!'
    }
    return JsonResponse(result)


def unfollow_user(request):
    """不关注用户 返回一个状态 ok = bool 和 和 message =  string"""
    result = {
        'ok': True,
        'message': 'success or failure!'
    }
    return JsonResponse(result)
