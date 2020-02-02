from django.urls import path
from pladform.api.views import BlogRudView, BlogListCreateView


urlpatterns = [
    # path('blogs/', blogs_view, {'template_name': 'blogs.html'},
    #      name='blog'),
    path('blogs/<int:pk>/', BlogRudView.as_view(), name='blogs_rud'),
    path('blogs/', BlogListCreateView.as_view(), name='blogs_create'),
]


