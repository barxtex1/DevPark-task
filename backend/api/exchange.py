import currencyapicom
from cfehome.settings import API_KEY

def make_exchange(validated_data, *args, **kwargs):
    """
    Make exchange using currencyapi 
    """

    # Check if currecyapicom API KEY exist
    if not API_KEY:
        return {
            "Error": "You must specify the API key in the manifest file"
        }

    # Create client for currencyapicom with valid API KEY
    client = currencyapicom.Client(API_KEY)

    # Currencies needs to be a list
    currencies_list = validated_data.get('output_currencies').split(',')


    # --- NotAllowed, only for plans with upgrade ---

    # result = client.convert(
    #     value = str(validated_data.get('amount')),
    #     date = validated_data.get('date').strftime("%Y-%m-%d"),
    #     base_currency = validated_data.get('input_currency'),
    #     currencies = currencies_list
    # )

    # --- Free plan ---

    # Historical Exchange Rates
    result = client.historical(
        date = validated_data.get('date').strftime("%Y-%m-%d"),
        base_currency = validated_data.get('input_currency'),
        currencies = currencies_list
    )

    amount = validated_data.get('amount')
    response = [
        {
            "currency": currency['code'],
            "amount": round(currency['value']*float(amount), 2)
        } 
        for currency in result['data'].values()
    ]
    
    return response
