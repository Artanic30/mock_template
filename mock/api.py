from django.http import JsonResponse
from django.shortcuts import render


"""all the functions have the same function name as USTC"""
def follow_user(request): # delete
    """关注用户 返回一个状态 ok = bool 和 message =  string"""
    result = {
        'ok': True,
        'message': 'success or failure!'
    }
    return JsonResponse(result)


def unfollow_user(request): # delete
    """不关注用户 返回一个状态 ok = bool 和 和 message =  string"""
    result = {
        'ok': True,
        'message': 'success or failure!'
    }
    return JsonResponse(result)


def follow(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 11
    }
    return JsonResponse(result)


def unfollow(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 22
    }
    return JsonResponse(result)


def downvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 33
    }
    return JsonResponse(result)


def undo_downvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 44
    }
    return JsonResponse(result)


def upvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 55
    }
    return JsonResponse(result)


def undo_upvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    result = {
        'ok': True,
        'count': 66
    }
    return JsonResponse(result)


def join(course_id):# delete
    """返回一个状态 ok = bool """
    result = {
        'ok': True,
    }
    return JsonResponse(result)


def quit(course_id):# delete
    """返回一个状态 ok = bool """
    result = {
        'ok': True,
    }
    return JsonResponse(result)


def review_upvote():
    """返回一个状态 ok = bool and message = str and count = int"""
    result = {
        'ok': True,
        'message': 'success',
        'count': 77
    }
    return JsonResponse(result)


def review_cancel_upvote():
    """返回一个状态 ok = bool and message = str and count = int"""
    result = {
        'ok': True,
        'message': 'success',
        'count': 88
    }
    return JsonResponse(result)


def delete_review(): # delete
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def show_comments(request):# delete
    user = {
        'is_authenticated': True,
        'is_admin': True
    }
    review = {
        'id': 23333,
        'comments': [
            {
                'author': {
                    'username': 'author_name'
                },
                'content' 'comment_content'
                'id': 777777,
                'publish_time': "19260817"
            }
        ]
    }
    data = {
        'review': review,
        'user': user
    }
    return render(request, 'review-comments.html', data)


def review_new_comment():# delete
    result = {
        'ok': True,
        'message': 'success',
        'content': 'comment_content'
    }
    return JsonResponse(result)


def delete_comment():# delete
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def hide_review():# delete
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def unhide_review():# delete
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def new_review(request):
    result = {
        'ok': True
    }
    return result
