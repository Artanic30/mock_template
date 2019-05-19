from django import template

register = template.Library()
# 新注册一个filter要重启django


@register.filter(name='test_filter', is_safe=True)  # 过滤器在模板中使用时的name
def test_filter(value, arg='default value'):  # 把传递过来的参数arg替换为'~'
    return str(value) + str(123) + arg


@register.filter
def lower(value):
    return value.lower()


@register.filter(name='cut')  # 过滤器在模板中使用时的name
def myCut(value, arg):  # 把传递过来的参数arg替换为'~'
    print(value, type(arg), 231231)
    return value.replace(arg, '~')
