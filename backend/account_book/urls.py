from django.urls import path, include
from rest_framework import routers

from account_book.views import AccountBookListCreateView, AccountBookDiaryViewSet, diary_restore, MemoViewSet

router = routers.DefaultRouter()
router.register(r'(?P<account_book_id>\d+)/diary', AccountBookDiaryViewSet)
router.register(r'(?P<account_book_id>\d+)/diary/(?P<account_book_diary_id>\d+)/memo', MemoViewSet)

urlpatterns = [
    path('', AccountBookListCreateView.as_view()),
    path('', include(router.urls)),
    path('diary/<int:pk>/restore', diary_restore)
]
