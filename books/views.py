from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, ReviewForm
import datetime

class HomeView(TemplateView):
    template_name = 'books/home.html'

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.order_by('-created_at')
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.full_clean()
            review.save()
            return redirect('book_detail', id=self.object.id)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'id': self.object.id})

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('book_list')

class CurrentTimeView(TemplateView):
    def get(self, request, *args, **kwargs):
        now = datetime.datetime.now()
        return HttpResponse(f"<h1>Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}</h1>")
