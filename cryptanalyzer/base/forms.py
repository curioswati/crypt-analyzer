from django import forms


class UploadFileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for i in range(1, 5):
            self.fields['file%d' % i] = forms.FileField(label="File %d" % i)


class SelectAlgorithmForm(forms.Form):
    algo_choices = [('aes', 'AES'),
                    ('des', '3DES'),
                    ('blowfish', 'BlowFish'),
                    ('twofish', 'TwoFish'),
                    ('rc6', 'RC6')]
    choice_field = forms.MultipleChoiceField(choices=algo_choices,
                                             widget=forms.CheckboxSelectMultiple)

class ContactForm(forms.Form):
    # Ref: https://learndjango.com/tutorials/django-email-contact-form
    def __init__(self, *args, **kwargs):
        '''
        Remove form field labels as we are only using placeholders.
        '''
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['message'].label = ''

    name = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your Name'})
                             )
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Contact Email'})
                             )
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Write your message here...'})
                              )
