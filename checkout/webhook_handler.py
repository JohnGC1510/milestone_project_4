from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle a generic/unknown webhook """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle a webhook for a successful payment intent """
        intents = event.data.object
        print(intents)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle a webhook for a failed payment intent """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
