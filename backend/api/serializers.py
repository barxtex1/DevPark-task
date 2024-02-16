from rest_framework import serializers
from .models import Currencies
from django.urls import reverse
import re



class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ['code']



class CurrencyExchangeSerializer(serializers.Serializer):
    input_currency = serializers.CharField(required=True, max_length=10)
    output_currencies = serializers.CharField(required=True, max_length=255)
    amount = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    date = serializers.DateField(required=True, format="%Y-%m-%d")
    


    def validate_input_currency(self, value):
        """
        Custom validation for input_currency
        """
        # Check if the value contains only letters
        if not value.isalpha():
            raise serializers.ValidationError("Only letters are allowed in input_currency")
        

        # Converts a string into upper case
        value = value.upper()

        
        # Check if input currency is in the db
        if not Currencies.objects.filter(code=value).exists():
            currency_list_enpoint = reverse('currency-list')
            path = self.context['request'].build_absolute_uri(currency_list_enpoint)
 
            raise serializers.ValidationError([
                "Input currency does not exist in currencies", 
                f"A list of valid currencies can be found at: {path}"
            ])

        return value
    

    def validate_output_currencies(self, value):
        """
        Custom validation for output_currencies
        """
        # Define a regex pattern for letters and commas
        pattern = re.compile("^[a-zA-Z,]+$")
        if not bool(pattern.match(value)):
            raise serializers.ValidationError("Currency codes should be separated by a comma. Example: 'EUR,USD,AMD'")
        
        # Converts a string into upper case
        value = value.upper()
        values_list = value.split(',')

        # Check if list is not empty and does not contain empty string
        if not len(values_list) or '' in values_list:
            raise serializers.ValidationError("Wrong format of output currencies. Example: 'EUR,USD,AMD'")


        # Check if every code is no the db
        for code_ in values_list: 
            if Currencies.objects.filter(code=code_).exists():
                continue

            currency_list_enpoint = reverse('currency-list')
            path = self.context['request'].build_absolute_uri(currency_list_enpoint)
 
            raise serializers.ValidationError([
                f"Currency code '{code_}' does not exist in currencies", 
                f"A list of valid currencies can be found at: {path}"
            ])


        return value