from django.urls import path, re_path

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, \
    TeacherDetailView, TeacherListView

app_name = 'organization'

urlpatterns = [
    # 课程机构首页
    path('list/', OrgView.as_view(), name="org_list"),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),

    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),

    # 讲师列表
    path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),

    # 访问机构讲师
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),
]
