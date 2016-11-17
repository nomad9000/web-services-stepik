from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=256)
    text = forms.CharField(widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q

class AnswerForm(forms.Form):
    text = forms.CharField()
    question = forms.IntegerField()
    def clean(self):
        return self.cleaned_data
    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a