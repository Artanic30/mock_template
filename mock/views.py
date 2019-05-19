from django.shortcuts import render
from django.contrib.auth.models import User
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
    return render(request, template, {'data': data})


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
        'courses_joined': ['EE1110', 'SI100B', 'CS120']

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
        'courses_joined': ['EE1110', 'SI100B', 'CS120']

    }
    courses = {
        'total': 213,
        'page': 23123,
        'has_next': True,
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
        'range_list': [0, 1, 2, 3, 4],
        'result_rate1': 3,
        'result_rate2': 2

    }
    return render(request, 'course-index.html', data)


def not_found(request):
    """返回404页面"""
    return render(request, '404.html')
