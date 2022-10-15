from django import forms

from .models import PushInformation, SubscriptionInfo

from pushuser.models import PushUserModel

class WebPushForm(forms.Form):
    user = forms.CharField(max_length=255)
    status_type = forms.ChoiceField(choices=[
                                      ('subscribe', 'subscribe'),
                                      ('unsubscribe', 'unsubscribe')
                                    ])

    def save_or_delete(self, subscription, user, status_type):
        # Ensure get_or_create matches exactly
        data = {"user": None}

        if user:
            user, created = PushUserModel.objects.get_or_create(identifier=user)
            data["user"] = user


        data["subscription"] = subscription

        push_info, created = PushInformation.objects.get_or_create(**data)

        # If unsubscribe is called, that means need to delete the browser
        # and notification info from server. 
        if status_type == "unsubscribe":
            push_info.delete()
            subscription.delete()


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = SubscriptionInfo
        fields = ('endpoint', 'auth', 'p256dh', 'browser',)

    def get_or_save(self):
        subscription, created = SubscriptionInfo.objects.get_or_create(**self.cleaned_data)
        return subscription
