from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from memo import views as memo_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('memo',memo_views.show,name='memo'),
    url(r'^modify/(?P<memokey>[0-9]+)/$', memo_views.modify, name='modify_memo'),
    url(r'^delete/(?P<memokey>[0-9]+)/$', memo_views.delete, name='delete_memo'),
    path('memos',memo_views.index,name='memo'),
    path('memo/create',memo_views.create,name='new_memo')
]
