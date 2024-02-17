from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class CurrencyTestCase(APITestCase):
    def test_valid_exchange(self):
        """
        Test valid input data for currency exchange enpoint
        """
        url = reverse('currency-exchange')
        params = {
            "input_currency": 'pln',
            "output_currencies": 'eur,usd,amd',
            "amount": 123.45,
            "date": '2023-08-24'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_wrong_input_currency(self):
        """
        Test invalid input currency
        """
        # unknown currency code
        url = reverse('currency-exchange')
        params = {
            "input_currency": 'abc',
            "output_currencies": 'eur,usd,amd',
            "amount": 123.45,
            "date": '2023-08-24'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_wrong_output_format(self):
        """
        Test invalid output currency format
        """
        # unknown currency code
        url = reverse('currency-exchange')
        params = {
            "input_currency": 'pln',
            "output_currencies": ',eur,,usd,amd',
            "amount": 123.45,
            "date": '2023-08-24'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        params['output_currencies'] = 'eur|usd,amd'
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        params['output_currencies'] = 'eur,usda,amd'
        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_wrong_amount(self):
        """
        Test invalid amount
        """
        # unknown currency code
        url = reverse('currency-exchange')
        params = {
            "input_currency": 'pln',
            "output_currencies": 'eur,usd,amd',
            "amount": 123.4552,
            "date": '2023-08-24'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_wrong_datetime(self):
        """
        Test invalid datetime
        """
        # unknown currency code
        url = reverse('currency-exchange')
        params = {
            "input_currency": 'pln',
            "output_currencies": 'eur,usd,amd',
            "amount": 123.45,
            "date": '21-05-2023'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
