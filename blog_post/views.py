from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel
from django.urls import reverse_lazy
from django import forms

class BlogList(ListView):
    template_name = 'list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'detail.html'
    model = BlogModel

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title', 'content', 'category')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # formにCSSをあてる
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class BlogCreate(CreateView):
    template_name = 'create.html'
    model = BlogModel
    #fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
    form_class = PostForm

class BlogDelete(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')