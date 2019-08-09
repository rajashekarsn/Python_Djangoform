from django import forms
from .models import MemberRegister


class MemberRegisterForm(forms.ModelForm):
    applicant_first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    applicant_last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    applicant_mobile = forms.IntegerField(label='Mobile Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    applicant_occupation = forms.CharField(label='Occupation', widget=forms.TextInput(attrs={'class': 'form-control'}))
    applicant_company = forms.CharField(label='Company', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # spouse_first_name = forms.CharField(label='Spouse First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # spouse_last_name = forms.CharField(label='Spouse Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # spouse_mobile = forms.IntegerField(label='Spouse Mobile Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # spouse_occupation = forms.CharField(label='Spouse Occupation', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # spouse_company = forms.CharField(label='Spouse Occupation', widget=forms.TextInput(attrs={'class': 'form-control'}))
    applicant_ca_homeNumber = forms.IntegerField(label='House Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ca_street_name = forms.CharField(label='Street Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ca_place = forms.CharField(label='Place', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ca_pincode = forms.CharField(label='PIN', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_homeNumber = forms.IntegerField(label='India House Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_street_name = forms.CharField(label='India Street Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_place = forms.CharField(label='India Place', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_pincode = forms.CharField(label='India PIN', widget=forms.TextInput(attrs={'class': 'form-control'}))
    in_conatctNumber = forms.IntegerField(label='India Contact Number', widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = MemberRegister
        fields = '__all__'