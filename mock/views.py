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
        'items': [{
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 20181012,
                'content': 'test_content',
                'id': 23333
            },
            {
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 20181012,
                'content': 'test_content',
                'id': 23333
            },
            {
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 23333, 'name': 'test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 20181012,
                'content': 'test_content',
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
        'items': [{
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 5, 'name': 'follow_test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 19261113,
                'content': 'test_content',
                'id': 23333
            },
            {
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 3, 'name': 'follow_test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 19640823,
                'content': 'test_content',
                'id': 23333
            },
            {
                'author': {'avatar': '/static/bootstrap/image/test.jpg', 'username': 'test_username', 'id': 23333333},
                'course': {'id': 2, 'name': 'follow_test_name', 'teacher_names_display': 'HammerWang', 'teachers': True},
                'publish_time': 20110417,
                'content': 'test_content',
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
        'this_module': 'home.latest_reviews',
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
        'page': 23123,
        'has_next': True,
        'navigation': [0, 1, 2, 3],
        'items': [
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'introduction': 'introduction',
                'term_ids': 14,
                'review_count': 23,
                'rate': {
                    'average_rate': 4.5,
                    'difficulty': 'hell',
                    'homework': 'EE101',
                    'grading': 'well',
                    'gain': 'many',
                }
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'introduction': 'introduction',
                'term_ids': 13,
                'review_count': 233,
                'rate': {
                    'average_rate': 3.5,
                    'difficulty': 'hell',
                    'homework': 'EE102',
                    'grading': 'well',
                    'gain': 'many',
                }
            },
            {
                'teachers': 'test_name',
                'teacher_names_display': 'test_name',
                'name': 'course_name',
                'introduction': 'introduction',
                'term_ids': 16,
                'review_count': 23333,
                'rate': {
                    'average_rate': 2.5,
                    'difficulty': 'hell',
                    'homework': 'EE187',
                    'grading': 'well',
                    'gain': 'many',
                }
            }
        ]
    }
    data = {
        'title': '热门课程',
        'courses': courses,
        'this.module': 'course.popular',
        'deptlist': 'deptlist',
        'dept': 'department',
        'current_uer': current_user,
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
        'is_admin': False
    }
    course = {
        'name': 'CS110计算机体系结构',
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
        'term_ids': 'CS110',
        'has_next': True,
        'courseries': 23123,
        'teachers_count': 3,
        'review_count': 12,
        'rate': {
                    'average_rate': 2.5,
                    'difficulty': 'hell',
                    'homework': 'EE187',
                    'grading': 'well',
                    'gain': 'many',
                },
        'join_type': "join_type",
        'teaching_type': "teaching_type",
        'course_type': "course_type",
        'dept': "dept_unknown",
        'course_level': "course_level",
        'credit': 2,
        'homepage': 'https://www.baidu.com',
        'introduction': '简介之类的',
        'last_edit_time': "19260817",
        'reviewed': True,
        'reviews': [{
            'is_hidden': False,
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
            'id': 23333
        },
            {
                'is_hidden': False,
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
                'id': 23333
            }
        ],
        'is_hidden': False,
        'related_courses': [{
            'teacher_names_display': 'Faker',
        }],
        'same_teacher_courses': [{
            'course_rate': {
                'average_rate': 2.5,
                'difficulty': 'hell',
                'homework': 'EE187',
                'grading': 'well',
                'gain': 'many',
            },
            'term_ids': 23,
            'review_count': 21
        }]
    }
    data = {
        'course': course,
        'range_list': [0, 1, 2, 3, 4],
        'current_uer': current_user,
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
        'is_student': True,
        'info': 'some information',
        'review_count': 12,
        'classes_joined_count': 4,
        # 最多显示三条评论
        'reviews': [
            {
                'is_hidden': False,
                'course': {
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
        # 只显示前六门课
        'courses_following': [{
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
                    'introduction': '简介之类的',
                },
            {
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
                'introduction': '简介之类的',
            }
        ],
        'classes_joined': [
            {
                'course_id': 23333,
                'course': {
                    'name': 'class_joined_course_name',
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
                    'reviewed_by': True,
                },
                'term': 'some_terms'
            }
        ],
        'avatar': '/static/bootstrap/image/test.jpg',
        'description': 'some descriptions',
        'homepage': 'www.github.com',
        'following_count': 23,
        'follower_count': 12,
        'reviews_count': 231
    }
    data = {
        'user': user,
        'current_user': current_user
    }
    if user_id == 404:
        message = _('Sorry. But we could not find the user!')
        data = {
            'message': message,
            'status': False
        }
        return render(request, 'feedback.html', data)

    return render(request, 'profile.html', data)


def not_found(request):
    """返回404页面"""
    return render(request, '404.html')


def about(request):
    """关于我们，网站介绍、联系方式"""
    return render(request, 'about.html')


def community_rules(request):
    """社区规范页面"""
    return render(request, 'community-rules.html')
