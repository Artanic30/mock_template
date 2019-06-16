from django.http import JsonResponse
from django.shortcuts import render


"""all the functions have the same function name as USTC"""


def follow(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'follow_course')
    result = {
        'ok': True,
        'count': 11
    }
    return JsonResponse(result)


def unfollow(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'unfollow_course')
    result = {
        'ok': True,
        'count': 22
    }
    return JsonResponse(result)


def downvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'downvote')
    result = {
        'ok': True,
        'count': 33
    }
    return JsonResponse(result)


def undo_downvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'undo_downvote')
    result = {
        'ok': True,
        'count': 44
    }
    return JsonResponse(result)


def upvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'upvote')
    result = {
        'ok': True,
        'count': 55
    }
    return JsonResponse(result)


def undo_upvote(course_id):
    """返回一个状态 ok = bool 和 count = int """
    print(course_id, 'undo_upvote')
    result = {
        'ok': True,
        'count': 66
    }
    return JsonResponse(result)


def review_upvote(id):
    """返回一个状态 ok = bool and message = str and count = int"""
    print(id, 'review_upvote')
    result = {
        'ok': True,
        'message': 'success',
        'count': 77
    }
    return JsonResponse(result)


def review_cancel_upvote(id):
    """返回一个状态 ok = bool and message = str and count = int"""
    print(id, 'cancel_review_upvote')
    result = {
        'ok': True,
        'message': 'success',
        'count': 88
    }
    return JsonResponse(result)


def hide_review(id):
    print(id, 'hide_review')
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def unhide_review(id):
    print(id, 'unhide_review')
    result = {
        'ok': True,
        'message': 'success',
    }
    return JsonResponse(result)


def show_comments(request):
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


def new_review(request):
    print(request, 'new_review')
    result = {
        'ok': True
    }
    return result


def delete_comment(id):
    print(id, 'delete_review')
    result = {
        'ok': True
    }
    return result
