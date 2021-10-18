from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Note

class NameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('username', '')
        super(NameForm, self).__init__(*args, **kwargs)

        try:
            o = Note.objects.get(user=self.username)
        except Note.DoesNotExist:
            o = Note()

        # shared_users is a comma separated string
        shared_users_list = o.shared_users.split(',')
        text = forms.CharField(widget=forms.Textarea, initial=o.text)
    
        # Need to use the full user name list in case they don't have notes attached
        User = get_user_model()
        shared_users = forms.ModelMultipleChoiceField(
            queryset = User.objects.filter(~Q(username=self.username)),
            widget = forms.CheckboxSelectMultiple,
            initial = User.objects.filter(username__in=shared_users_list),
            required = False
        )

        self.fields = {
            'text': text, 
            'shared_users': shared_users
        }

        self.fields['text'].label = 'My Note'        

    def save(self, new_model):
        # Combine shared_users to comma separated string
        shared_users = [su['username'] for su in new_model['shared_users'].values()]
        shared_users = ','.join(shared_users)
        
        o = Note()
        o.user = new_model['user']
        o.text = new_model['text']
        o.shared_users = shared_users
        o.save()

        print('Saved Successfully')
        
        