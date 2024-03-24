from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
    def clean_summary(self):
     summary = self.cleaned_data['summary']
     words = summary.split()
     if len(words) > 15:
          summary = ' '.join(words[:15]) + '...'
     return summary