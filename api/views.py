from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from main.models import Tweet, Account, TweetImage


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class TweetsBase(TemplateView):

    default_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs-PGo1B' \
        '0hrjWowbqSwAeIhX2_5-K_Z16S0w7N3pByi47-_4TWBLRZ01mLjdsMrNfjhJ8&usqp=CAU'

    def get(self, req, *args, **kwargs):
        
        account_id = kwargs.get('account_id')

        if account_id:
            account = get_object_or_404(
                Account,
                id=account_id
            )
            tweets = Tweet.objects.filter(account=account)
        else:
            tweets = Tweet.objects.all()

        data = []

        for tweet in tweets:
            obj = model_to_dict(tweet)
            obj['date'] = tweet.date
            obj['account'] = {
                'fullname': tweet.account.fullname, 
                'username': tweet.account.user.username,
                'profile_image': tweet.account.profile_image.url if tweet.account.profile_image else self.default_img,
            }

            image = TweetImage.objects.filter(tweet=tweet).first()
            if image:
                obj['tweet_image'] = image.image.url
                
            data.append(obj)

        return JsonResponse(data, safe=False)


class ProfileTweets(TweetsBase):

    def get(self, req, *args, **kwargs):

        kwargs = {
            'account_id': Account.objects.get(user=req.user).pk
        }

        return super().get(req, *args, **kwargs)


class AccountDetailTweets(TweetsBase):

    def get(self, req, *args, **kwargs):

        user = get_object_or_404(User, username=kwargs.get('username'))
        kwargs = {
            'account_id': Account.objects.get(user=user).pk
        }

        return super().get(req, *args, **kwargs)


@method_decorator(login_required(login_url='main:welcome'), name='dispatch')
class SearchView(TemplateView):

    default_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs-PGo1B' \
        '0hrjWowbqSwAeIhX2_5-K_Z16S0w7N3pByi47-_4TWBLRZ01mLjdsMrNfjhJ8&usqp=CAU'

    def get(self, req, *args, **kwargs):
        
        query = kwargs.get('query')
        if query and len(query.strip()) > 0:
            accounts = Account.objects.filter(fullname__icontains=query.strip())

            data = []

            for account in accounts:
                obj = {
                    'fullname': account.fullname, 
                    'username': account.user.username,
                    'bio': account.bio,
                    'profile_image': account.profile_image.url if account.profile_image else self.default_img,
                }

                data.append(obj)

            return JsonResponse(data, safe=False)
        
        else:
            return JsonResponse([], safe=False)




