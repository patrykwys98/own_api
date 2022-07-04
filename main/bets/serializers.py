from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BlogabetBets, BlogabetAuthor


class BlogabetAuthorSerializer(ModelSerializer):
    class Meta:
        model = BlogabetAuthor
        fields = '__all__'


class BetsSerializer(ModelSerializer):
    author = SerializerMethodField()
    author_yield = SerializerMethodField()
    author_odds = SerializerMethodField()

    class Meta:
        model = BlogabetBets
        fields = '__all__'

    def get_author(self, obj):
        try:
            return obj.author.author_name
        except:
            return None

    def get_author_yield(self, obj):
        try:
            return obj.author.author_yield
        except:
            return None

    def get_author_odds(self, obj):
        try:
            return obj.author.author_odds
        except:
            return None
