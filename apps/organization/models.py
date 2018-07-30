from datetime import datetime

from django.db import models

# Create your models here.


# 城市字典
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    # 城市描述：备用不一定展示出来
    desc = models.CharField(max_length=200, verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    # 机构描述，后面会替换为富文本展示
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(default='pxjg',max_length=20, choices=(('pxjg',''),('gr','个人'),('gx','高校')), verbose_name='机构类型')
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name="机构logo",
        max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    # 一个城市可以有很多课程机构，通过将city设置外键，变成课程机构的一个字段
    # 可以让我们通过机构找到城市
    city = models.ForeignKey(CityDict, verbose_name="所在城市", on_delete=models.CASCADE)
    # 学习人数
    students = models.IntegerField(default=0, verbose_name='学习人数')
    # 课程数
    course_nums = models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        # 获取课程机构教师数量
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name
# 讲师
class Teacher(models.Model):
    # 一个机构会有很多老师，所以我们在讲师表添加外键并把课程机构名称保存下来
    # 可以使我们通过讲师找到对应的机构
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age = models.IntegerField(default=18, verbose_name="年龄")
    image = models.ImageField(default='',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)