from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  ListView, UpdateView)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown

# def birthday(request, pk=None):
#     if pk is not None:
#         instance = get_object_or_404(Birthday, pk=pk)
#     else:
#         instance = None
#     form = BirthdayForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance
#     )
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, 'birthday/birthday.html', context)

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 5

class BirthdayMixin:
    model = Birthday

class BirthdayCreateView(BirthdayMixin, CreateView):
    form_class = BirthdayForm

class BirthdayUpdateView(BirthdayMixin, UpdateView):
    form_class = BirthdayForm

class BirthdayDeleteView(BirthdayMixin, DeleteView):
    success_url = reverse_lazy('birthday:list')

class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context
