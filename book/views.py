from django.shortcuts import render
# 导入httpresponse模块
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo


# Create your views here.
def index(request):
    # return HttpResponse('ok')
    # request,           请求
    # template_name      模板名字
    # context
    # context={
    #     'name':'~~~~~~~~~~~~'
    # }
    # return render(request,'book/index.html',context=context)

    # 在这里实现，增删改查
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('ok')


##############增加数据######################
from book.models import BookInfo,PeopleInfo

# 方式1
book = BookInfo(
    name='Django1',
    pub_date='2000-2-11',
    readcount=100
)
# 必须调用对象的save方法才能将数据保存到数据库中
book.save()

# objects
BookInfo.objects.create(
    name='测试入门开发',
    pub_date='2000-2-11',
    readcount=100
)

#################修改###########
book=BookInfo.objects.get(id=6)
book.name='运维开发'
book.save()

#filter
BookInfo.objects.filter(id=7).update(name='爬虫入门',commentcount=666)

#########删除######

book=BookInfo.objects.get(id=10)
book.delete()
#
BookInfo.objects.filter(id=11).delete()
#
BookInfo.objects.filter(id=8).update(is_delete=True)



##########查询###########
try:
    BookInfo.objects.get(id=12)
except BookInfo.DoesNotExist:
    print('not result')

BookInfo.objects.all()

#########过滤查询############
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

#模型类名.objects.filter(属性名__运算符=位)      获取n个结果  n=0,1,2,..
#模型类名.objects.exclude(属性名__运算符=值)    获取n个结果  n=0,1,2,..
#模型关名.objects.get(性名运算符__运算符)         获取1个结果或者异常


# 查询编号为1的图书
BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=1)
BookInfo.objects.filter(pk=1)
# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
# 查询编号不等于3的图书
BookInfo.objects.exclude(id__gt=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1980-1-1')


#############################################

from django.db.models import F,Q

#模型名.objects.功能名(属性名__运算符=F('第二个属性名'))

#例：查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(readcount__gte=F('commentcount'))
#例：查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)


###并且查询####
# 例：查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(commentcount__gt=20).filter(id__lt=3)
BookInfo.objects.filter(commentcount__gt=20,id__lt=3)

################

#或者模型类.objects.功能名(Q(属性名__运算符=值)|Q(属性名__运算符=值)|....)
#并且语法：模型类名，objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&....)
#not非语法：模型类名.objects.filter(~Q(属性名__运算符=值))
# 例：查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(Q(commentcount__gt=20)&Q(id__lt=3))


################关联查询#########################################

# 查询书籍为1的所有人物信息

book=BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# 查询人物为1的书籍信息

################关联过滤查询#########################################

# 查询1 条件n
# `1模型类名.objects.功能名（n联模型类名小写__字段名__条件运算符=值）`
# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name='郭靖')

BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于30的所有人物

PeopleInfo.objects.filter(book__readcount__gt=30)





