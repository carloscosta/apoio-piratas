#encoding: utf-8

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class QuestionStatus:
    PENDING  = 'PE'
    APPROVED = 'AP'

_question_status = QuestionStatus()

QUESTION_STATUS_CHOICES = (
    (_question_status.PENDING, _(u'Pending')),
    (_question_status.APPROVED, _(u'Approved')),
)

class Question(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2, choices=QUESTION_STATUS_CHOICES,
        default=_question_status.PENDING)
    pub_date = models.DateTimeField('date published')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name=u'Question'
        verbose_name_plural=u'Questions'

    def __str__(self):
        return self.text

    def is_upperclass(self):
        return self.question_status in (self.PENDING, self.APPROVED)

    def was_published_recently(self):
        if self.question_status == self.APPROVED:
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def answers(self):
        return self.answer_set.count()

    def has_accepted_answer(self):
        return len(self.answer_set.filter(accepted=True)) == 1

    def accepted_answer(self):
        return self.answer_set.get(accepted=True)


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    vote = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100),])
    pub_date = models.DateTimeField(_(u'date published'))
    accepted = models.BooleanField(_(u'Accepted'), default=False)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name=u'Answer'
        verbose_name_plural=u'Answers'

    def was_answered_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return "%s" % (self.text[:20])

    def save(self, *args, **kwargs):
        if self.accepted:
            accepteds = Answer.objects.filter(question=self.question, accepted=True)
            if len(accepteds) > 0:
                for a in accepteds:
                    a.accepted = False
                    a.save()

        super(Answer, self).save(*args, **kwargs)
