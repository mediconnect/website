from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def forbidden_username_validator(value):
    forbidden_username = ['admin', 'settings', 'news', 'about', 'help',
                          'signin', 'signup', 'signout', 'terms', 'privacy',
                          'cookie', 'new', 'login', 'logout', 'administrator',
                          'join', 'account', 'username', 'root', 'blog',
                          'user', 'users', 'billing', 'subscribe', 'reviews',
                          'review', 'blog', 'blogs', 'edit', 'mail', 'email',
                          'core', 'job', 'jobs', 'contribute', 'newsletter',
                          'shop', 'profile', 'register', 'auth',
                          'authentication', 'campaign', 'config', 'delete',
                          'remove', 'forum', 'forums', 'download',
                          'downloads', 'contact', 'blogs', 'feed', 'feeds',
                          'faq', 'intranet', 'log', 'registration', 'search',
                          'explore', 'rss', 'support', 'status', 'static',
                          'media', 'setting', 'css', 'js', 'follow',
                          'activity', 'questions', 'articles', 'network', ]

    if value.lower() in forbidden_username:
        raise ValidationError('This is a reserved word.')


def invalid_username_validator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('Enter a valid username.')


def unique_email_validator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('User with this Email already exists.')


def unique_username_ignore_case_validator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('User with this Username already exists.')


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Usernames may contain <strong>alphanumeric</strong>, <strong>_</strong> and '
                  '<strong>.</strong> characters')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm your password",
        required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=75)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="First Name",
        required=True)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Last Name",
        required=True)
    telephone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Telephone",
        required=False)
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Address",
        required=False)
    zipcode = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Zipcode",
        required=False)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(forbidden_username_validator)
        self.fields['username'].validators.append(invalid_username_validator)
        self.fields['username'].validators.append(
            unique_email_validator)
        self.fields['email'].validators.append(unique_email_validator)

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match'])
        return self.cleaned_data


class SearchForm(forms.ModelForm):
    query = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
    )

    class Meta:
        model = User
        exclude = []
        fields = []

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)