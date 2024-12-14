# import the standard Django Forms
# from built-in library
from django import forms

# 
class new_page_form(forms.Form):
    article_name = forms.CharField(label="Article Name", min_length=8, max_length=20)
    article_text = forms.CharField(label="Article Content", min_length=1, widget=forms.Textarea)

class edit_page(forms.Form):
    article_text = forms.CharField(label="Article Content", min_length=1, widget=forms.Textarea)