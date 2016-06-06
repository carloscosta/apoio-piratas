
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Answer
from .forms import AskForm


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = get_template('faqs/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    form = AskForm()
    try:
        question = Question.objects.get(pk=question_id)
        answer   = Answer.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Essa pergunta não foi feita ou ainda não foi respondida.")
    return render(request, 'faqs/detail.html', {'question': question, 'answer': answer, 'form': form})


def thanks(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            context = {
                'name': form.cleaned_data['your_name'],
                'email': form.cleaned_data['your_email'],
                'comment': form.cleaned_data['comment'],
            }
            template = get_template('faqs/thanks.html')
            return HttpResponse(template.render(context, request))
    else:
        raise Http404("Essa pergunta não foi feita ou ainda não foi respondida.")


def ask(request):
    form = AskForm()
    return render(request, 'faqs/ask.html', {'form': form})

