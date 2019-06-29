from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
All the pages' url are registered in the /mock/url.py 
"""


def test(request):
    """
    url: http://127.0.0.1:8000/test
    template for frontend develop
    mock the data for page and assign it to the required template
    """
    template = 'test.html'
    data = {
        'test_data': 23333,
        'test_data2': 23123123,
        'test_array': [1, 2, 3, 4]

    }
    return render(request, template, data)


def index(request, page):
    """
    url: http://127.0.0.1:8000/
    """
    print('here', page)
    return latest_reviews(request, page)


def latest_reviews(request, page=1):
    """

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    reviews_paged = Review.query.order_by(Review.id.desc()).paginate(page=page, per_page=per_page)
    return render_template('latest-reviews.html', reviews=reviews_paged, title='全站最新点评', this_module='home.latest_reviews')
    tips: this.module 是标记当前模版名称的, flask相关用法
    """
    # 模拟登陆后情况 登陆前删掉下一行代码 User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # request.user = User.objects.get(username='john') 不用django自带的user了
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }
    object = [
            {
                'author': {
                    'username': 'test_username',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {
                    'username': 'test_username',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {
                    'username': 'test_username',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
                        {
                            'author': {
                                'username': 'test_username',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': 'test_username',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': 'test_username',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': 'test_username',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
        ],
    print(page, type(object), type([1, 2, 3, 4]))
    threads_pages = Paginator([
            {
                'author': {
                    'username': '1111',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {
                    'username': '222222',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {
                    'username': '333333',
                    'id': 23333333
                },
                'course': {
                    'id': 'EE110',
                    'name': 'test_name',
                    'teachers': [
                        {
                            'teacher_names_display': 'HammerWang'
                        },
                        {
                            'teacher_names_display': 'Zeratul'
                        },
                    ],
                },
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
                        {
                            'author': {
                                'username': '44444',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': '5555555',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': '666666666',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
                        {
                            'author': {
                                'username': '77777777',
                                'id': 23333333
                            },
                            'course': {
                                'id': 'EE110',
                                'name': 'test_name',
                                'teachers': [
                                    {
                                        'teacher_names_display': 'HammerWang'
                                    },
                                    {
                                        'teacher_names_display': 'Zeratul'
                                    },
                                ],
                            },
                            'contents': [
                                {
                                    'content': 'content content content content content',
                                    'publish_time': 'time'
                                }
                            ],
                            'id': 23333
                        },
        ], per_page=3, orphans=2)
    print(request.GET.get('page'))
    try:
        reviews = threads_pages.page(page)
    except PageNotAnInteger:
        reviews = threads_pages.page(1)
    except EmptyPage:
        reviews = threads_pages.page(threads_pages.num_pages)
    template = 'latest-reviews.html'
    print(threads_pages.page(2))
    data = {
        'reviews': reviews,
        'total': threads_pages.count,
        'title': '全站最新点评',
        'this_module': 'home.latest_reviews',
        'current_user': current_user

    }
    return render(request, template, data)


def follow_reviews(request, page):
    """

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    reviews_paged = Review.query.order_by(Review.id.desc()).paginate(page=page, per_page=per_page)
    return render_template('latest-reviews.html', reviews=reviews_paged, title='全站最新点评', this_module='home.latest_reviews')
    tips: this.module 是标记当前模版名称的, flask相关用法
    """
    # 模拟登陆后情况 登陆前删掉下一行代码 User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # request.user = User.objects.get(username='john') 不用django自带的user了
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }
    template = 'latest-reviews.html'
    threads_pages = Paginator([
        {
            'author': {
                'username': '1111',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '222222',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '333333',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '44444',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '5555555',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '666666666',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
        {
            'author': {
                'username': '77777777',
                'id': 23333333
            },
            'course': {
                'id': 'EE110',
                'name': 'test_name',
                'teachers': [
                    {
                        'teacher_names_display': 'HammerWang'
                    },
                    {
                        'teacher_names_display': 'Zeratul'
                    },
                ],
            },
            'contents': [
                {
                    'content': 'content content content content content',
                    'publish_time': 'time'
                }
            ],
            'id': 23333
        },
    ], per_page=3, orphans=2)
    try:
        reviews = threads_pages.page(page)
    except PageNotAnInteger:
        reviews = threads_pages.page(1)
    except EmptyPage:
        reviews = threads_pages.page(threads_pages.num_pages)
    print(threads_pages.page(2))
    data = {
        'reviews': reviews,
        'total': threads_pages.count,
        'title': '我关注的点评',
        'this_module': 'home.follow_reviews',
        'current_user': current_user
    }
    return render(request, template, data)


def popular(request, page):
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }

    popular_pages = Paginator([
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'term_ids': 'Fall 2018',
                'review_count': 23,
                'rate': {
                    'average_rate': 4.5,
                    'difficulty': 'hell',
                    'homework': 'EE101',
                    'grading': 'well',
                    'gain': 'many',
                },
                'id': 112233
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'term_ids': 'Fall 2018',
                'review_count': 233,
                'rate': {
                    'average_rate': 3.5,
                    'difficulty': 'hell',
                    'homework': 'EE102',
                    'grading': 'well',
                    'gain': 'many',
                },
                'id': 112233
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'term_ids': 'Fall 2018',
                'review_count': 23333,
                'rate': {
                    'average_rate': 2.5,
                    'difficulty': 'hell',
                    'homework': 'EE187',
                    'grading': 'well',
                    'gain': 'many',
                },
                'id': 112233
            }
        ], 3)
    try:
        courses = popular_pages.page(page)
    except PageNotAnInteger:
        courses = popular_pages.page(1)
    except EmptyPage:
        courses = popular_pages.page(popular_pages.num_pages)
    data = {
        'title': '热门课程',
        'courses': courses,
        'total': popular_pages.count,
        'this_module': 'course.popular',
        'deptlist': 'deptlist',
        'dept': 'department',
        'current_user': current_user,
        'range_list': [0, 1, 2, 3, 4]
    }
    return render(request, 'course-index.html', data)


def view_course(request, course_id):
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': True,
        'id': 23333,
        'is_followed': 1,  # todo: !!!新加是否推荐 1 = true 0 = false
    }
    course = {
        'id': 23333,
        'name': '计算机体系结构',
        'teachers': [
            {
                'id': 1,
                'image': '/static/bootstrap/image/test.jpg',
                'name': 'fivefiveopen',
                'dept': 'department',
                'homepage': 'https://www.baidu.com'
            },
            {
                'id': 2,
                'image': '/static/bootstrap/image/test.jpg',
                'name': 'fivefiveopen',
                'dept': 'department',
                'homepage': 'https://www.baidu.com'
            }
        ],
        'term_ids': 'CS110',
        'has_next': True,# delete
        'code': 'EE2103',
        'teachers_count': 3,
        'review_count': 12,
        'rate': {
                    'average_rate': 2.5,
                    'difficulty': 'hell',
                    'homework': 'EE187',
                    'grading': 'well',
                    'gain': 'many',
                },
        # add instructor note
        'course_type': "course_type",
        'dept': "dept_unknown",
        'course_level': "course_level", # delete
        'credit': 2,
        'homepage': 'https://www.baidu.com',
        'introduction': '简介之类的',
        'reviews': [
            {

                'content': [
                    {
                        'content': 'content',
                        'publish_time': 'time'
                    }
                ],
                'author': {
                    'username': 'fivefiveopen',
                    'id': 232323,
                    'course_rate': {
                        'average_rate': 2.5,
                        'difficulty': 'hell',
                        'homework': 'EE187',
                        'grading': 'well',
                        'gain': 'many',
                    },
                    'review_count': 23,
                    'term_ids': 'Fall 2012'
                },
                'id': 111, # pk
                'term': '2018 Fall',
                'is_upvoted': False,
                'upvote_count': 12,
            },
            {
                'upvote_count': 12,
                'content': [
                    {
                        'content': 'content',
                        'publish_time': 'time'
                    }
                ],
                'author': {
                    'username': 'fivefiveopen',
                    'id': 232323,
                    'course_rate': {
                        'average_rate': 9,
                        'difficulty': 'hell',
                        'homework': 'EE187',
                        'grading': 'well',
                        'gain': 'many',
                    },
                    'review_count': 23,
                    'term_ids': 23
                },
                'id': 22222,
                'term': '2018 Fall',
                'is_upvoted': True
            }
        ],
        # version 2
        'same_teacher_courses': [
            {
                'course_rate': {
                    'average_rate': 3.5,
                    'difficulty': 'hell',
                    'homework': 'EE182',
                    'grading': 'well',
                    'gain': 'many',
                },
                'term_ids': 'term',
                'review_count': 21,
                'id': 12312,
                'name': 'DT'
            }
        ],
        'downvoted': 'unknown',
        'following': 'unknown',
        'upvoted': 'unknown',
        'joined': 'unknown',
        'follow_count': 23,
        'downvote_count': 21,
    }
    data = {
        'course': course,
        'range_list': [0, 1, 2, 3, 4],
        'current_user': current_user,
    }
    return render(request, 'course.html', data)


def view_profile(request, user_id):
    """用户的个人主页,展示用户在站点的活跃情况"""
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }
    user = {
        'username': 'username',
        'is_student': True,
        'info': 'some information',
        'avatar': '/static/bootstrap/image/test.jpg',
        'reviews_count': 231,
        'courses_following_count': 9,
        # 最多显示三条评论
        'reviews': [
            {
                'course': {
                    'name': 'course_name',
                    'id': 565656,
                    'teachers': [
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        },
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        }
                    ],
                    'teacher_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',

            },
            {
                'course': {
                    'name': 'course_name',
                    'id': 565656,
                    'teachers': [
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        },
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        }
                    ],
                    'teacher_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',
            },
            {
                'course': {
                    'name': 'course_name',
                    'id': 565656,
                    'teachers': [
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        },
                        {
                            'image': '/static/bootstrap/image/test.jpg',
                            'name': 'fivefiveopen',
                            'dept': {
                                'name': 'dept_name'
                            },
                            'homepage': 'https://www.baidu.com'
                        }
                    ],
                    'teacher_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',
            }
        ],
    }
    data = {
        'user': user,
        'current_user': current_user
    }
    if user_id == 404:
        message = 'Sorry. But we could not find the user!'
        data = {
            'message': message,
            'status': False
        }
        return render(request, 'feedback.html', data)

    return render(request, 'profile.html', data)


def new_review(request, course_id):
    polls = [
        {'name': 'difficulty', 'display': '课程难度', 'options': ['简单', '中等', '困难'] },
        {'name': 'homework', 'display': '作业多少', 'options': ['不多', '中等', '超多'] },
        {'name': 'grading', 'display': '给分好坏', 'options': ['超好', '一般', '杀手'] },
        {'name': 'gain', 'display': '收获多少', 'options': ['很多', '一般', '没有'] },
    ]
    course = {
            'id': course_id,
            'semester_year': 2018,
            'name': 'course_name',
            'teachers': [
                {
                    'image': '/static/bootstrap/image/test.jpg',
                    'name': 'fivefiveopen',
                    'dept': {
                        'name': 'dept_name'
                    },
                    'homepage': 'https://www.baidu.com'
                },
                {
                    'image': '/static/bootstrap/image/test.jpg',
                    'name': 'fivefiveopen',
                    'dept': {
                        'name': 'dept_name'
                    },
                    'homepage': 'https://www.baidu.com'
                }
            ],
            'teacher_names_display': 'Test_teacher_name',
            'code': 'EVA110',
            'term_ids': [111, 222, 333, 44],
        }
    review = {
            'term': "unknown",
            'rate': 2.5,
            'content': 'lalala',
            'content_text': 'lalala'
        }
    data = {
        'course': course,
        'review': review,
        'polls': polls,
        'message': '谨言慎行，君子之道',
        'range_list': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render(request, 'new-review.html', data)


def catalog(request, page):
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }
    course = [
        {
            'course_id': 23333,
            'code': 'EE110',
            'name': 'mane',
            'credit': 4,
            'teachers_names_display': 'fivefiveopen',
            'score': 8.5,
            'suggest_count': 123,
            'time': '2019 Fall' # delete
        },
        {
            'course_id': 23333,
            'code': 'EE110',
            'credit': 4,
            'name': 'mane',
            'teachers_names_display': 'fivefiveopen',
            'score': 8.5,
            'suggest_count': 123,
            'time': '2019 Fall'
        },
        {
            'course_id': 23333,
            'code': 'EE110',
            'credit': 4,
            'name': 'mane',
            'teachers_names_display': 'fivefiveopen',
            'score': 8.5,
            'suggest_count': 123,
            'time': '2019 Fall'
        },
        {
            'course_id': 23333,
            'code': 'EE110',
            'credit': 4,
            'name': 'mane',
            'teachers_names_display': 'fivefiveopen',
            'score': 8.5,
            'suggest_count': 123,
            'time': '2019 Fall'
        }
    ]
    courses_pages = Paginator(course, 3)

    try:
        courses_page = courses_pages.page(page)
    except PageNotAnInteger:
        courses_page = courses_pages.page(1)
    except EmptyPage:
        courses_page = courses_pages.page(courses_pages.num_pages)

    data = {
        'current_user': current_user,
        'total': courses_pages.count,
        'this_module': 'home.catalog',
        'course': courses_page,
        'title': '课程目录',
    }
    return render(request, 'catalog.html', data)


def view_teacher_profile(request, teacher_id):
    courses = {
        'total': 213,
        'page': 23123,
        'has_next': True,
        'navigation': [0, 1, 2, 3],
        'items': [
            {
                'teacher_names_display': 'test_name',
                'introduction': 'introduction',
                'term_ids': 'pingqilaidexueqi',
                'review_count': 23,
                'code': 'EE110',
                'reviewed': True,
                'rate': {
                    'average_rate': 4.5,
                },
                'id': 112233 # course pk
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'introduction': 'introduction',
                'term_ids': 13,
                'review_count': 233,
                'code': 677,
                'reviewed': False,
                'rate': {
                    'average_rate': 7.7,
                },
                'id': 112233
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'introduction': 'introduction',
                'term_ids': 16,
                'review_count': 23333,
                'code': 6777,
                'reviewed': False,
                'rate': {
                    'average_rate': 8.7,
                },
                'id': 112233
            }
        ]
    }
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'is_student': False,
        'id': 23333
    }
    teacher = {
        'image': '/static/bootstrap/image/test.jpg',
        'name': 'teacher_test_name',
        'homepage': 'https://www.hao123.com',
        'dept': { # delete
            'name': 'dept_name'
        },
        'id': 55667 # pk
    }
    data = {
        'courses': courses,
        'current_user': current_user,
        'teacher': teacher,
        'range_list': [0, 1, 2, 3, 4]
    }
    return render(request, 'teacher-profile.html', data)


def not_found(request):
    """返回404页面"""
    return render(request, '404.html')


def about(request):
    """关于我们，网站介绍、联系方式"""
    return render(request, 'about.html')


def community_rules(request):
    """社区规范页面"""
    return render(request, 'community-rules.html')
