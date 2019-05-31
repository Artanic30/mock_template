from django.shortcuts import render
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


def index(request):
    """
    url: http://127.0.0.1:8000/
    """
    return latest_reviews(request)


def latest_reviews(request):
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
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
        'is_student': False,
        'id': 23333
    }
    reviews_paged = {
        'total': 234,
        'page': 2,
        'items': [
            {
                'author': {
                    'username': 'test_username',
                    'id': 23333333
                },
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            }
        ],
        'navigation': [0, 1, 2, 3],
        'has_prev': True,
        'is_hidden': False,
        'prev_num': 23123,
        'has_next': True
    }
    template = 'latest-reviews.html'
    data = {
        'reviews': reviews_paged,
        'title': '全站最新点评',
        'this_module': 'home.latest_reviews',
        'current_user': current_user

    }
    return render(request, template, data)


def follow_reviews(request):
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
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
        'is_student': False,
        'id': 23333
    }
    reviews_paged = {
        'total': 234,
        'page': 2,
        'items': [
            {
                'author': {
                    'username': 'test_username',
                    'id': 23333333
                },
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            },
            {
                'author': {'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'code': 'EE110'},
                'contents': [
                    {
                        'content': 'content content content content content',
                        'publish_time': 'time'
                    }
                ],
                'id': 23333
            }
        ],
        'navigation': [0, 1, 2, 3],
        'has_prev': True,
        'is_hidden': False,
        'prev_num': 23123,
        'has_next': True
    }
    template = 'latest-reviews.html'
    data = {
        'reviews': reviews_paged,
        'title': '我关注的点评',
        'this_module': 'home.follow_reviews',
        'current_user': current_user
    }
    return render(request, template, data)


def popular(request):
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
        'is_student': False,
        'id': 23333
    }
    courses = {
        'total': 213,
        'page': 23123,# delete
        'has_next': True,# delete
        'navigation': [0, 1, 2, 3],
        'items': [
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
        ]
    }
    data = {
        'title': '热门课程',
        'courses': courses,
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
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
        'is_student': False,
        'id': 23333
    }
    user = {
        'is_authenticated': True,
        'is_admin': True
    }
    course = {
        'id': 23333,
        'name': 'CS110计算机体系结构',
        'teachers': [
            {
                'image': '/static/bootstrap/image/test.jpg',
                'name': 'fivefiveopen',
                'dept': 'department',
                'homepage': 'https://www.baidu.com'
            },
            {
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
        'reviewed': False,
        'reviews': [
            {
                'is_hidden': False,
                'content': [
                    {
                        'content': 'content',
                        'publish_time': 'time'
                    }
                ],
                'rate': 8.5,
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
                'id': 23333, # pk
                'term': '2018 Fall',
                'is_upvoted': True
            },
            {
                'is_hidden': True,
                'rate': 3.5,
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
                    'term_ids': 23
                },
                'id': 23333,
                'term': '2018 Fall',
                'is_upvoted': True
            }
        ],
        'is_hidden': False,
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
        'upvote_count': 12
    }
    data = {
        'course': course,
        'range_list': [0, 1, 2, 3, 4],
        'current_user': current_user,
        'user': user
    }
    return render(request, 'course.html', data)


def view_profile(request, user_id):
    """用户的个人主页,展示用户在站点的活跃情况"""
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
        'is_student': False,
        'id': 23333
    }
    user = {
        'username': 'username',
        'is_student': True,
        'info': 'some information',
        'review_count': 12,
        # 最多显示三条评论
        'reviews': [
            {
                'is_hidden': False,
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
                    'teachers_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',
                'id': 2333

            },
            {
                'is_hidden': False,
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
                    'teachers_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',
                'id': 2333

            },
            {
                'is_hidden': True,
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
                    'teachers_names_display': 'Test_teacher_name',
                },
                'term_display': 'dispaly_terms',
                'update_time': 19260817,
                'content': 'review_content',
                'id': 404

            }
        ],
        'courses_following_count': 9,
        'avatar': '/static/bootstrap/image/test.jpg',
        'reviews_count': 231
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
            'teachers_names_display': 'Test_teacher_name',
            'courseries': 'EVA110',
            'joined_term': 222,
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
        'is_new': True
    }
    return render(request, 'new-review.html', data)


def catalog(request):
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
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
    data = {
        'current_user': current_user,
        'this_module': 'home.catalog',
        'course': course,
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
                'teachers': 'test_name', # delete
                'teacher_names_display': 'test_name',
                'name': 'course_name', # delete
                'introduction': 'introduction',
                'term_ids': 'pingqilaidexueqi',
                'review_count': 23,
                'courseries': 'EE110',# change to code
                'reviewed': False,
                'rate': {
                    'average_rate': 4.5,
                    'difficulty': 'hell',# delete
                    'homework': 'EE101',# delete
                    'grading': 'well',# delete
                    'gain': 'many',# delete
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
                'courseries': 677,
                'reviewed': False,
                'rate': {
                    'average_rate': 7.7,
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
                'introduction': 'introduction',
                'term_ids': 16,
                'review_count': 23333,
                'courseries': 6777,
                'reviewed': False,
                'rate': {
                    'average_rate': 8.7,
                    'difficulty': 'hell',
                    'homework': 'EE187',
                    'grading': 'well',
                    'gain': 'many',
                },
                'id': 112233
            }
        ]
    }
    current_user = {
        'is_authenticated': True,
        'username': 'TestName',
        'unread_notification_count': 4,
        'latest_notifications_text': ['latest_notifications_text1', 'latest_notifications', 'latest_notifications3'],
        'courses_joined': ['EE1110', 'SI100B', 'CS120'],
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
