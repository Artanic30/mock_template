from django.shortcuts import render
from mock.models import *
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
import datetime
import json


"""all the functions have the same function name as USTC"""

def submit_review(request):
    """
    Post: { content, course_id, semester_year, semester_season, difficulty, workload, grading, gaining
    """
    print('reach submit function!')
    print(request.POST.get('content'), 2)
    if request.method == "POST":

        return HttpResponse(json.dumps({'res':'processed'}), content_type="application/json")
    else:
        return Http404


def follow_course(request):
    """
    Post: { course_id, subcription_level,
    """
    if request.method == "POST":
        print('follow here!')
        print(request.POST.get('course_id'), request.POST.get('subcription_level', None))
        return HttpResponse(json.dumps({'res': 'processed'}), content_type="application/json")


# delete

def review_upvote(request):
    """返回一个状态 ok = bool and message = str and count = int"""
    print(request.POST.get('thread_id'), 'review_upvote')
    result = {
        'res': 'processed',
        'count': 11
    }
    return JsonResponse(result)


def review_downvote(request):
    """返回一个状态 ok = bool and message = str and count = int"""
    print(request.POST.get('thread_id'), 'review_downvote')
    result = {
        'res': 'processed',
        'count': 888
    }
    return JsonResponse(result)


def review_cancel_vote(request):
    """返回一个状态 ok = bool and message = str and count = int"""
    print(request.POST.get('thread_id'), 'cancel_review_vote')
    result = {
        'res': 'processed',
        'count': 33
    }
    return JsonResponse(result)


def new_review(request):
    print(request, 'new_review')
    result = {
        'ok': True
    }
    return result
