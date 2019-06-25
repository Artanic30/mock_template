from django.shortcuts import render
from mock.models import *
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import datetime
import json


"""all the functions have the same function name as USTC"""


def follow_course(request):
    """
    Post: { course_id, subcription_level,
    """
    if request.method == "POST":
        print('follow here!')
        print(request.POST.get('course_id'), request.POST.get('subcription_level', None))
        return HttpResponse(json.dumps({'res': 'processed'}), content_type="application/json")


def vote_thread(request):
    """
    thread_id == course_id ???
    Post: { thread_id, score,
    :param request:
    :return:
    """
    print('vote success!')
    print(request.POST.get('thread_id'), request.POST.get('score', None))
    return HttpResponse(json.dumps({'res': 'processed', 'count': 233}), content_type="application/json")


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


def new_review(request):
    print(request, 'new_review')
    result = {
        'ok': True
    }
    return result
