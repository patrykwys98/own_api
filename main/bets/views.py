from rest_framework import generics, mixins
from rest_framework.response import Response


from .models import BlogabetBets, BlogabetAuthor
from .serializers import BetsSerializer


class BetMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView,):
    queryset = BlogabetBets.objects.all()
    serializer_class = BetsSerializer

    def perform_create(self, serializer):
        author_name = self.request.data.get('author_name')
        author = BlogabetAuthor.objects.filter(
            author_name=author_name).exists()
        if author:
            try:
                author = BlogabetAuthor.objects.get(author_name=author_name)
                if BlogabetBets.objects.filter(author=author, event=self.request.data['event'], start=self.request.data['start']).exists():
                    return Response({'message': 'Bet already exists'})
            except:
                author = ""
            serializer.save(author=author)
        else:
            try:
                author = BlogabetAuthor.objects.create(
                    author_name=author_name, author_yield=self.request.data['author_yield'], author_odds=self.request.data['author_odds'])
            except:
                author = ""
            serializer.save(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
