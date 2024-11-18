from django.urls import path,include
from . import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('',views.index,name="index"),
    path('question_submit/',views.question_submit,name="question_submit"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('*/',views.handler404,name="handler404"),
]
