from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,FormView
from django.urls import reverse_lazy
from .forms import TesttitleForm,StudentForm,ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Student
from django.contrib.auth.models import User
from accounts.models import CustomUser

class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9

class MypageView(ListView):
    template_name = 'mypage.html'

@method_decorator(login_required, name='dispatch')
class CreateTitleView(CreateView):
    form_class = TesttitleForm
    template_name = 'title_form.html'
    success_url = reverse_lazy('scoreapp:done')

    def form_valid(self, form):
        titledata =form.save(commit=False)
        titledata.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreateScoreView(CreateView):
    form_class = StudentForm
    template_name = "score_form.html"
    success_url = reverse_lazy('scoreapp:done')

    def form_valid(self, form):
        scoredata = form.save(commit=False)
        scoredata.user = self.request.user
        scoredata.save()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'success.html'

class ScoreListView(ListView):
    template_name = 'index.html'
    queryset = Student.objects.all()

class StudentListView(ListView):
    template_name = 'stu_list.html'
    queryset = CustomUser.objects.all()

class JapaneseView(ListView):
    template_name = 'Japanese.html'
    queryset = Student.objects.order_by('-Japanese')

class MathView(ListView):
    template_name = 'Math.html'
    queryset = Student.objects.order_by('-Math')

class ScienceView(ListView):
    template_name = 'Science.html'
    queryset = Student.objects.order_by('-Science')

class SociologyView(ListView):
    template_name = 'Sociology.html'
    queryset = Student.objects.order_by('-Sociology')

class EnglishView(ListView):
    template_name = 'English.html'
    queryset = Student.objects.order_by('-English')
    

class StudentView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = Student.objects.filter(user=user_id).all()
        return user_list

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('scoreapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\nタイトル:{2}\nメッセージ:\n{3}' \
            .format(name, email, title, message)
        from_email = ''
        to_list = ['t9957652@gmail.com']
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,)
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)