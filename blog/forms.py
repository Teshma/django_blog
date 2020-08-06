from django import forms
from .models import Post, CV

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "text")

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ("title", "first_section", "first_section_text", 
        "second_section", "second_section_text", "third_section", "third_section_text",
        "fourth_section", "fourth_section_text", "fifth_section", "fifth_section_text",
        "sixth_section", "sixth_section_text", "seventh_section", "seventh_section_text")