from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import AccountBook, AccountBookDiary, Memo
from .serializers import AccountBookSerializer, AccountBookDiarySerializer, MemoSerializer, \
    AccountBookDiaryDetailSerializer


class AccountBookViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBookSerializer
    queryset = AccountBook.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.pk)

    def perform_create(self, serializer):
        user = get_user_model().objects.get(pk=self.request.user.pk)
        serializer.save(user=user)
        return super().perform_create(serializer)


class AccountBookDiaryViewSet(viewsets.ModelViewSet):
    queryset = AccountBookDiary.objects.filter(is_delete=False).all()

    def get_queryset(self):
        return self.queryset.select_related('account_book').filter(
            is_delete=False,
            account_book__user_id=self.request.user.pk,
            account_book_id=self.kwargs['account_book_id'])

    def perform_create(self, serializer):
        account_book = get_object_or_404(AccountBook,
                                         user=self.request.user.pk,
                                         pk=self.kwargs['account_book_id'])
        serializer.save(account_book=account_book)
        return super().perform_create(serializer)

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AccountBookDiaryDetailSerializer
        return AccountBookDiarySerializer


class MemoViewSet(viewsets.ModelViewSet):
    serializer_class = MemoSerializer
    queryset = Memo.objects.all()

    def get_queryset(self):
        fk_qs = AccountBookDiary.objects.filter(
            is_delete=False,
            account_book__user_id=self.request.user.pk,
        )
        if fk_qs.exists():
            return self.queryset.select_related('account_book_diary').filter(
                account_book_diary=fk_qs.get(pk=self.kwargs['account_book_diary_id']),
            )
        return fk_qs

    def perform_create(self, serializer):
        account_book_diary = get_object_or_404(AccountBookDiary,
                                               account_book__user=self.request.user.pk,
                                               pk=self.kwargs['account_book_diary_id'])
        serializer.save(account_book_diary=account_book_diary)
        return super().perform_create(serializer)


@api_view(['GET'])
@login_required
def diary_restore(request, pk):
    queryset = AccountBookDiary.objects.filter(
        account_book__user=request.user.pk,
    )
    if queryset.exists():
        instance = queryset.get(pk=pk, account_book__user=request.user.pk)
        instance.is_delete = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({
        'message': 'Not Found'  # 보안상의 이유로 404 로 response 함
    }, status=status.HTTP_404_NOT_FOUND)
