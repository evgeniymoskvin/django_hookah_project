from django import forms
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, Select
from django.contrib.admin.widgets import AdminDateWidget, AdminSplitDateTime


class AdminSendForm(forms.Form):
    message = forms.CharField(label="<Message>", max_length=300, help_text="Пиши сюда", widget=forms.Textarea(attrs={"placeholder": "Введите текст",
                                              "class": "form-control"}))
