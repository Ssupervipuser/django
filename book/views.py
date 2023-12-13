from django.shortcuts import render
#导入httpresponse模块
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('ok')
    #request,           请求
    #template_name      模板名字
    #context
    context={
        'name':'~~~~~~~~~~~~'
    }
    return render(request,'book/index.html',context=context)