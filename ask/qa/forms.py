from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=256)
    text = forms.CharField(widget=forms.Textarea)
    #def clean(self):
        #return self.cleaned_data
    def save(self):
        #q = Question(**self.cleaned_data)
        #q.save()
        #return q
        return Question.objects.create(
            title=self.cleaned_data['title'],
            text=self.cleaned_data['text'],
            author=getattr(self, '_user', None),
        )

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()
    #def clean(self):
        #return self.cleaned_data
    def save(self):
        #a = Answer(**self.cleaned_data)
        #a.save()
        #return a
        return Answer.objects.create(
            text=self.cleaned_data['text'],
            question_id=self.cleaned_data['question'],
            author=getattr(self, '_user', None),
        )