from rest_framework import generics, mixins

from pladform.api.serializers import BLogSerializer
from pladform.models import Blog
from django.db.models import Q


class BlogRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BLogSerializer
    queryset = Blog.objects.all()


class BlogListCreateView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = BLogSerializer
    queryset = Blog.objects.all()
    permission_classes = []

    def get_queryset(self):
        qs = Blog.objects.all()
        query = self.request.GET.get('q')
        if query:
            qs = qs.filter(Q(tagline__icontains=query) | Q(name__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}

# perform_create(self, serializer):
#     serializer.save(some_data)
