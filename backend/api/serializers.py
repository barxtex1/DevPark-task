from rest_framework import serializers
from .models import Currencies




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
        


        # You can add more custom validation logic here

        return value
    

    def validate_output_currencies(self, value):
        """
        Custom validation for output_currencies
        """
        # Example: Check if the value contains only letters
        if not value.isalpha():
            raise serializers.ValidationError("Only letters are allowed in your_char_field.")

        # You can add more custom validation logic here

        return value