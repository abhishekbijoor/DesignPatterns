class PaymentGateway:
    def process_payment(self,amount):
        pass

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Payment ${amount} via Stripe")

class PaypalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Payment ${amount} via Paypal")



class PaymentMethod:
    def __init__(self,gateway:PaymentGateway):
        self.gateway = gateway
    
    def make_payment (self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print("using credit card for payment")
        self.gateway.process_payment(amount)

class CryptoPayment(PaymentMethod):
    def make_payment(self, amount): 
        print("using crypto for payment")
        self.gateway.process_payment(amount)


if __name__ == "__main__":
    stripegateway = StripeGateway()
    paypalgateway = PaypalGateway()

    creditcardpayment = CreditCardPayment(stripegateway)
    cryptoPayment = CryptoPayment(paypalgateway)

    creditcardpayment.make_payment(100)
    cryptoPayment.make_payment(299)