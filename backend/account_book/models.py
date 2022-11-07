from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class AccountBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20,
        help_text='가계부 이름을 지어 주세요.',
    )

    class Meta:
        db_table = 'account_book'
        ordering = ['-id']


class AccountBookDiary(models.Model):
    class StatusChoices(models.TextChoices):
        INCOME = 'I', '수입'
        EXPENDITURE = 'E', '지출'

    account_book = models.ForeignKey(AccountBook, on_delete=models.CASCADE)
    money = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text='금액을 적어 주세요.',
    )
    status = models.CharField(
        max_length=1,
        choices=StatusChoices.choices,
        blank=True,
    )
    is_delete = models.BooleanField(
        help_text='삭제 여부',
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'account_book_diary'


class Memo(models.Model):
    account_book_diary = models.ForeignKey(AccountBookDiary,
                                           on_delete=models.CASCADE,
                                           related_name='memo')
    content = models.TextField(help_text='가계부 내용을 입력해주세요.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'memo'
