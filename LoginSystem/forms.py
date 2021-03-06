from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **krwargs):
        super(SignupForm, self).__init__(*args, **krwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control col-12'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = 'Enter Username'
        self.fields['username'].help_text = ' '

        self.fields['password1'].widget.attrs['class'] = 'form-control col-12'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = 'Enter password'
        self.fields['password1'].help_text = '<div class="form-text text-muted ml-5"><small><ul><li>Your password ' \
                                            'can&#39;t be too similar to your other personal ' \
                                            'information.</li><li>Your password must contain at least 8 ' \
                                            'characters.</li><li>Your password can&#39;t be a commonly used ' \
                                            'password.</li><li>Your password can&#39;t be entirely ' \
                                            'numeric.</li></ul></small></div> '

        self.fields['password2'].widget.attrs['class'] = 'form-control col-12'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = 'Re-Type Password'
        self.fields['password2'].help_text = '<div class="form-text text-muted ml-5"><small>Enter the same password as ' \
                                            'before, ' \
                                            'for verification.</small></div> '
