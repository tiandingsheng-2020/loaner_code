
from rest_framework import serializers
from .models import Loaner
from  django import forms
class LoanerForm(forms.ModelForm):
    class Meta:
        model = Loaner
        fields = ('loaner_sn', 'loaner_request', 'loaner_status')

class LoanerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loaner
        fields = ('loaner_sn', 'loaner_request', 'loaner_status')