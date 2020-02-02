from django.shortcuts import render
from pladform.models import Blog, Author, Entry
# Create your views here.
from django.db.models import Avg, Count


def blogs_view(request, template_name):
    # blogs = Blog.objects.all()
    # blogs = Blog.objects.filter(entry__authors__name='Varlamov')
    blogs = Blog.objects.filter(entry__headline__contains='new')
    # blogs = Blog.objects.prefetch_related('entry_set')

    result = {
        'blogs': blogs,
    }
    return render(request, template_name, result)


def blog_view(request, template_name, pk):
    # blog = Blog.objects.get(pk=pk)
    # authors = Author.objects.filter(entry__headline__contains='new')

    #  Aggregate & Annotate
    # av_rating = Entry.objects.aggregate(Avg('rating'))
    # print(av_rating)
    entries = Entry.objects.annotate(num_authors=Count('authors'))
    print(entries[0].num_authors)
    entries = Entry.objects.annotate(Count('authors', distinc=True))
    print(entries[0].authors__count)
    # blog = Blog.objects.annotate(num_entries=Count('entry'))
    # print(blog)

    # entries = Entry.objects.filter(blog__pk=pk).select_related('blog')
    # entries = Entry.objects.filter(blog__pk=pk).values('blog__name', 'id', 'headline', 'body_text', 'rating')
    entries = Entry.objects.filter(blog__pk=pk).values('blog__name', 'id', 'headline', 'body_text', 'rating')
    # print(entries)
    # entries = Entry.objects.filter(blog_id=pk)
    # entries = Entry.objects.select_related('blog').get(blog__id=1)
    result = {
        # 'blogs': blogs,
        # 'authors': authors,
        'entries': entries,
        # 'entry': entries,
    }
    return render(request, template_name, result)
