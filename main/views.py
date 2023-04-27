from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from main.models import Account, Tweet
from account.views import ProfileView


class WelcomePage(TemplateView):
    template_name = 'main/index.html'

    def get(self, req, *args, **kwargs):
        if req.user.is_authenticated:
            
            return redirect('main:home')
        
        return super().get(req, *args, **kwargs)


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class HomeView(TemplateView):
    template_name = 'main/home.html'


    def get(self, req, *args, **kwargs):
        self.account = Account.objects.get(user=req.user)

        return super().get(req, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['account'] = self.account
        context['tweets'] = Tweet.objects.all()

        return context


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class AddTweet(TemplateView):
    

    def get(self, req, *args, **kwargs):

        raise Http404

    
    def post(self, req, *args, **kwargs):
        text = req.POST.get('text')

        if text is not None and 0 < len(text) <= 280:
            account = Account.objects.get(user=req.user)

            tweet = Tweet.objects.create(
                account=account,
                text=text
            ) 

        return redirect('main:home')


class AccountDetailView(ProfileView):
    template_name = 'main/account_detail.html'


    def get(self, req, *args, **kwargs):

        self.user = get_object_or_404(User, username=kwargs.get('username'))

        return super().get(self, req, *args, **kwargs)


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class SearchView(TemplateView):
    template_name = 'main/search.html'


    def get(self, req, *args, **kwargs):
        self.query = req.GET.get('q', ' ')

        return super().get(req, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.query

        return context