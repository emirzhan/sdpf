from abc import ABC, abstractmethod


# Strategy Pattern
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using credit card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin")


# Singleton Pattern
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log = []
        return cls._instance

    def add_log(self, message):
        self.log.append(message)


# Decorator Pattern
class DiscountDecorator(PaymentStrategy):
    def __init__(self, payment_strategy, discount):
        self.payment_strategy = payment_strategy
        self.discount = discount

    def pay(self, amount):
        discounted_amount = amount - self.discount
        self.payment_strategy.pay(discounted_amount)
        Logger().add_log(f"Applied discount of {self.discount} to the payment")


# Adapter Pattern
class NewPaymentAdapter(PaymentStrategy):
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        print(f"Converting amount {amount} to the old payment system format")
        self.payment_strategy.pay(amount)


# Observer Pattern (Expanded)
class OrderObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class EmailNotificationObserver(OrderObserver):
    def update(self, message):
        print(f"Sending email notification: {message}")


class SMSNotificationObserver(OrderObserver):
    def update(self, message):
        print(f"Sending SMS notification: {message}")


class InventoryObserver(OrderObserver):
    def update(self, message):
        print(f"Updating inventory: {message}")


# Factory Pattern
class PaymentStrategyFactory:
    def create_payment_strategy(self, payment_type):
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "paypal":
            return PayPalPayment()
        elif payment_type == "bitcoin":
            return BitcoinPayment()
        else:
            raise ValueError("Invalid payment type")


# Client code
class Order:
    def __init__(self, payment_type, observers):
        self.payment_strategy = PaymentStrategyFactory().create_payment_strategy(payment_type)
        self.observers = observers

    def process_order(self, amount):
        self.payment_strategy = DiscountDecorator(self.payment_strategy, 10)
        self.payment_strategy = NewPaymentAdapter(self.payment_strategy)

        self.payment_strategy.pay(amount)

        Logger().add_log(f"Order processed successfully. Amount: {amount}")

        for observer in self.observers:
            observer.update(f"Order processed successfully. Amount: {amount}")


if __name__ == "__main__":
    observers = [EmailNotificationObserver(), SMSNotificationObserver(), InventoryObserver()]
    order = Order(payment_type="bitcoin", observers=observers)
    order.process_order(150)

    # Accessing the log from the singleton Logger
    print("\nLog Messages:")
    for log_message in Logger()._instance.log:
        print(log_message)
