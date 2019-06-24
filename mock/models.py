from django.db import models
from django.contrib.auth.models import AbstractUser

from jsonfield import JSONField


class User(AbstractUser):
    nickname = models.CharField(max_length=50, unique=True)


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    homepage = models.URLField()


class Semester(models.Model):
    class Meta:
        # 联合约束 元组参数不同则可以数据库中创建
        unique_together = [['year', 'season']]

    year = models.SmallIntegerField(verbose_name="学年（9月-次年7月）")
    FALL = 1
    SPRING = 2
    SUMMER = 3
    season = models.SmallIntegerField(choices=(
        (FALL, 'Fall'),      # 秋学期
        (SPRING, 'Spring'),  # 春学期
        (SUMMER, 'Summer'),  # 暑学期
        )
    )


class Course(models.Model):
    code = models.CharField(max_length=20, verbose_name="课程代码")
    name = models.CharField(max_length=50, verbose_name="课程名称")
    genre = models.CharField(max_length=50, verbose_name="课程类别")  # TODO: 课程类别外键到新表？
    credit = models.SmallIntegerField(verbose_name="学分")
    SIST = 1
    SLST = 2
    SPST = 3
    SEM = 4
    SCA = 5
    IMS = 6
    GE = 7
    OAA = 8
    school = models.SmallIntegerField(choices=(
        (SIST, "信息科学与技术学院"),
        (SLST, "生命科学与技术学院"),
        (SPST, "物质科学与技术学院"),
        (SEM, "创业与管理学院"),
        (SCA, "创意与艺术学院"),
        (IMS, "数学科学研究所"),
        (GE, "通识教育中心"),
        (OAA, "教学事务处"),
        ), verbose_name="开课单位"
    )
    classHour = models.SmallIntegerField(verbose_name="总课时")
    # TODO: 课程英文名? 本研修读、建议修读专业、建议修读年级(用Tag?)
    semesters = models.ManyToManyField(Semester)
    homepage = models.URLField(null=True)
    subscribers = models.ManyToManyField(
        User,
        through='Subscription',
    )
    instructors = models.ManyToManyField(Instructor)
    instructorNotes = models.ManyToManyField(
        User,
        through='InstructorNote',
	related_name='notes'
    )

    # TODO: cache course rating
    def calc_rating(self,):#Bayesian average with year_decrease
        sum_rat=0
        num_rat=0
        current_year = Semester.objects.all().aggregate(max=models.Max('year'))['max']
        avg_users=(current_year-2018)*45
        semester_rate=Semester.objects.filter(course=self).annotate(avg=models.Avg  ('thread__courseRating'),sum=models.Sum('thread__courseRating'),num=models.Count  ('thread__courseRating'))
        for semester_rate in semester_rate:
            num_rat+=1/(current_year - semester_rate.year+1)
            sum_rat+=1/(current_year - semester_rate.year+1)*(avg_users*semester_rate.avg   +semester_rate.sum)/(semester_rate.num+avg_users)
        return sum_rat/num_rat

    # TODO: cache course metrics
    def calc_difficulty(self):  # calculate course difficulty, but not cache
        easy = models.Count('thread', filter=models.Q(thread__courseDifficulty=Thread.EASY))
        medium = models.Count('thread', filter=models.Q(thread__courseDifficulty=Thread.MEDIUM))
        hard = models.Count('thread', filter=models.Q(thread__courseDifficulty=Thread.HARD))
        return self.objects.aggregate(easy=easy, medium=medium, hard=hard)

    def calc_workload(self):  # calculate course workload, but not cache
        light = models.Count('thread', filter=models.Q(thread__courseWorkload=Thread.EASY))
        medium = models.Count('thread', filter=models.Q(thread__courseWorkload=Thread.MEDIUM))
        heavy = models.Count('thread', filter=models.Q(thread__courseWorkload=Thread.HARD))
        return self.objects.aggregate(light=light, medium=medium, heavy=heavy)

    def calc_grading(self):  # calculate course grading, but not cache
        lot = models.Count('thread', filter=models.Q(thread__courseGain=Thread.EASY))
        medium = models.Count('thread', filter=models.Q(thread__courseGain=Thread.MEDIUM))
        little = models.Count('thread', filter=models.Q(thread__courseGain=Thread.HARD))
        return self.objects.aggregate(lot=lot, medium=medium, little=little)


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    NOTIFY = 1
    ADMIN = 2
    STAFF = 3
    TEACHER = 4
    level = models.SmallIntegerField(choices=(
        (NOTIFY, 'Notify'),   # 学生订阅: 通知
        (ADMIN, 'Admin'),     # 校院管理员: 修改课程基本信息
        (STAFF, 'Staff'),     # TA: 修改课程基本信息、发表TA评论
        (TEACHER, 'Teacher')  # 开课老师: 修改课程所有信息、发表"老师的话"
        ),
        default=NOTIFY
    )


class Thread(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    TAName = models.CharField(max_length=50, null=True)
    content = JSONField()  # TODO:Thread.content格式
    courseRating = models.SmallIntegerField()  # 星级评分
    EASY = 1
    MEDIUM = 2
    HARD = 3
    courseDifficulty = models.SmallIntegerField(choices=(
        # 课程难度
        (EASY, 'easy'),      # 简单
        (MEDIUM, 'medium'),  # 中等
        (HARD, 'hard'),      # 困难
    ))
    courseWorkload = models.SmallIntegerField(choices=(
        # 作业多少
        (EASY, 'light'),     # 不多
        (MEDIUM, 'medium'),  # 中等
        (HARD, 'heavy'),     # 超多
    ))
    courseGrading = models.SmallIntegerField(choices=(
        # 给分好坏
        (EASY, 'friendly'),  # 超好
        (MEDIUM, 'medium'),  # 一般
        (HARD, 'strict'),    # 杀手
    ))
    courseGain = models.SmallIntegerField(choices=(
        # 收获多少
        (EASY, 'lot'),       # 很多
        (MEDIUM, 'medium'),  # 一般
        (HARD, 'little'),    # 没有
    ))

    # TODO: cache thread vote
    def count_votes(self):  # count thread likes and dislikes, but not cache
        like = models.Count('vote', filter=models.Q(vote__score=Vote.LIKE))
        dislike = models.Count('vote', filter=models.Q(vote__score=Vote.DISLIKE))
        return self.objects.aggregate(like=like, dislike=dislike)


class Vote(models.Model):
    # 对点评的like与dislike
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LIKE = 1
    CANCELED = 0
    DISLIKE = -1
    score = models.SmallIntegerField(choices=(
        (LIKE, 'like'),          # 很多
        (CANCELED, 'canceled'),  # 一般
        (DISLIKE, 'dislike'),    # 没有
        ), default=CANCELED
    )


class InstructorNote(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
