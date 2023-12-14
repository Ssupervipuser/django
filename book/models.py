from django.db import models


# Create your models here.

# 准备书籍列表新的模型类
class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, )
    commentcount = models.IntegerField(default=0, )
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'  # 在admin站点中现时的名称

    def __str__(self):
        return self.name


# 准备人物列表信息的模型类

class PeopleInfo(models.Model):
    GENDER_CHOICE={
        (1,'male'),
        (2,'female')
    }

    name = models.CharField(max_length=20)
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=200, null=True)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='peopleinfo'

    def __str__(self):
        return self.name