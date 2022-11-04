from rest_framework import serializers

from .models import AccountBook, AccountBookDiary, Memo


class AccountBookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20)

    class Meta:
        model = AccountBook
        fields = ['id', 'name']


class AccountBookDiarySerializer(serializers.ModelSerializer):
    account_book_name = serializers.ReadOnlyField(
        source='account_book.name',
        read_only=True
    )
    status = serializers.ChoiceField(
        AccountBookDiary.StatusChoices.choices,
        help_text='"I" 는 수입 / "E" 는 지출. 둘 중 하날 선택해서 입력하세요.'
    )

    class Meta:
        model = AccountBookDiary
        fields = ['id', 'account_book_name', 'money', 'status']


class AccountBookDiaryDetailSerializer(AccountBookDiarySerializer):
    memo = serializers.SerializerMethodField()

    @staticmethod
    def get_memo(obj):
        return MemoSerializer(obj.memo, many=True).data

    class Meta(AccountBookDiarySerializer.Meta):
        fields = AccountBookDiarySerializer.Meta.fields + ['memo']


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id', 'content']
