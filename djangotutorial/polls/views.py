from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import Question
from .models import Post

def blog(request):
    posts = Post.objects.order_by("-fecha")
    return render(request, "blog.html", {"posts": posts})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    return HttpResponse(
        f"Estás votando sobre la pregunta {question_id}."
    )

def portfolio(request):
    return render(request, 'index.html')