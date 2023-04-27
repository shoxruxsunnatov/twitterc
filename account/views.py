from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from main.models import Account, Tweet
from account.forms import EditProfileForm


class CustomLogoutView(LogoutView):
    next_page = 'main:welcome'


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class ProfileView(TemplateView):
    template_name = 'account/profile.html'
    

    def get(self, req, *args, **kwargs):
        self.user = req.user

        return super().get(req, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        account = Account.objects.get(user=self.user)
        tweets  = Tweet.objects.filter(account=account)

        context['account'] = account
        context['tweetcount'] = tweets.count()
        context['tweets'] = tweets
        
        return context
    

@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class ProfileEditView(TemplateView):
    template_name = 'account/edit.html'


    def get(self, req, *args, **kwargs):
        self.user = req.user

        return super().get(req, *args, **kwargs)
    
    
    def post(self, req, *args, **kwargs):
        self.user = req.user

        account = Account.objects.get(user=req.user)

        form = EditProfileForm(req.POST, req.FILES, instance=account)
        if form.is_valid():
            form.save()

            return redirect('account:profile')

        return super().get(req, *args, **kwargs)
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['account'] = Account.objects.get(user=self.user)
        context['form'] = EditProfileForm()
        return context
    

class RegisterView(TemplateView):

    def post(self, req, *args, **kwargs):

        username = req.POST.get('username')
        password = req.POST.get('password')
        action = req.POST.get('action')

        if action == 'sign_up':
            fullname = req.POST.get('fullname')

            user = User.objects.create(
                username=username,
                is_staff=True
            )
            user.set_password(password)

            Account.objects.create(
                user=user,
                fullname=fullname
            )
            user.save()

            user = authenticate(username=username, password=password)
            if user:
                login(req, user)

                return redirect('main:home')
        
        elif action == 'login':
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)

                return redirect('main:home')
                
        return redirect('main:welcome')


    def get(self, req, *args, **kwargs):
        if req.user.is_authenticated:
            
            return redirect('main:home')
        
        return redirect('main:welcome')


