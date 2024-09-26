from django import forms

class FeedbackForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='User Name')
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    feedback_message = forms.CharField(widget=forms.Textarea, label='Feedback Message')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        if not phone_number.isdigit() or len(phone_number) < 10:
            self.add_error('phone_number', "Phone number must contain only digits and have at least 10 characters.")
