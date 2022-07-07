from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BlogabetBets, BlogabetAuthor, Dyscipline, ZawodTyperBets, ZawodTyperAuthor, ForumBukmacherskieBets, ForumBukmacherskieAuthor



#! Dyscipline Serializer
class DysciplineSerializer(ModelSerializer):
    class Meta:
        model = Dyscipline
        fields = ['dyscipline_name']

#! Blogabet Serializers
class BlogabetAuthorSerializer(ModelSerializer):
    class Meta:
        model = BlogabetAuthor
        fields = '__all__'

class BlogabetBetsSerializer(ModelSerializer):
    author = SerializerMethodField()
    author_yield = SerializerMethodField()
    author_odds = SerializerMethodField()
    dyscipline_name = SerializerMethodField()

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

    def get_dyscipline_name(self, obj):
        try:
            return obj.dyscipline.dyscipline_name
        except:
            return None


#! Zawód typer serializer
class ZawodTyperAuthorSerializer(ModelSerializer):
    class Meta:
        model = ZawodTyperAuthor
        fields = '__all__'

class ZawodTyperBetsSerializer(ModelSerializer):
    author = SerializerMethodField()
    author_effective = SerializerMethodField()
    author_odds = SerializerMethodField()
    dyscipline_name = SerializerMethodField()

    class Meta:
        model = ZawodTyperBets
        fields = '__all__'

    def get_author(self, obj):
        try:
            return obj.author.author_name
        except:
            return None

    def get_author_yield(self, obj):
        try:
            return obj.author.author_effective
        except:
            return None

    def get_author_odds(self, obj):
        try:
            return obj.author.author_odds
        except:
            return None

    def get_dyscipline_name(self, obj):
        try:
            return obj.dyscipline.dyscipline_name
        except:
            return None