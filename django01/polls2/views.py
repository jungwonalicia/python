from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("나의 2번째 홈페이지")
# return HttpResponse("<a href=http://www.naver.com>나의 2번째 홈페이지</a>")
    return HttpResponse("<a href=index2>나의 2번째 홈페이지-다른 사이트로 이동.</a>")

# 페이지 연결 index--> index2
def index2(request):
    # return HttpResponse("나의 2번째 홈페이지-사이트 추가....!!!")
    return HttpResponse("<a href=index3>다른 페이지로 이동 테스트</a>")

def index3(request):
    return HttpResponse("<a href=/polls>나의 1번째 홈페이지로 이동</a>")
