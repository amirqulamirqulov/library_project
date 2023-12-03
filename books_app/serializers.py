from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'subtitle', 'description', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobning nomi harflardan tashkil topgan bo'lishi kerak"
                }
            )

        if Books.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bu kitob avvalroq kiritilgan"
                }
            )

        return data

    def validate_price(self, attr):
        if attr < 0 or attr > 99999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx xato kiritlgan"
                }
            )
        return attr