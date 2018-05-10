from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from accounts.models import Profile


class AppSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        p = Profile(user=user)
        p.save()

        return user
