from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone

from blog.models import Post


class BlogListView(View):
    def get(self, request, **kwargs):
        now = timezone.now()
        posts = Post.objects.select_related(
            'auhor'
        ).filter(
            published_date__lte=now
        ).order_by('-published_date')

        return render(
            request,
            'blog/list.html',
            {'posts': posts})


class BlogDetailView(View):
    def get(self, request, post_slug, **kwargs):
        post = Post.objects.get(slug=post_slug)

        return render(
            request,
            'blog/detail.html',
            {'post': post}
        )