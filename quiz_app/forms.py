from django import forms
from django.forms import modelformset_factory, BaseModelFormSet
from quiz_app.models import *

# Form to get the Question
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)

# Create formset that generates multiple fields and handles the input.
# By default, when you create a formset from a model, the formset will use a
# queryset that includes all objects in the
# model (e.g., Answer.objects.all()). You can override this behavior by using the queryset argument.
class BaseAnswerFormSet(BaseModelFormSet):
    def __init__(self,*args,**kwargs):
        super(BaseAnswerFormSet, self).__init__(*args,**kwargs)
        self.queryset = Answer.objects.none()

# Form to get the Answers
# Generates 4 answer fields. The 'extra' argument performs this job.
AnswerForm = modelformset_factory(Answer, fields=('answer_text',), formset=BaseAnswerFormSet, extra=4)
