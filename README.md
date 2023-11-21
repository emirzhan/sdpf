# sdpf
Final project - Design Patterns 
Introduction 
This repository contains the code for Final project, where we explore and implement various design patterns in a Java application. 
The goal is to show how these patterns can be used to add functionalities, create objects, and adapt classes while keeping the code flexible and easy to maintain. 
Project Structure 
The project is a demonstration of several design patterns in the context of a simplified order processing system. Here's a brief overview of each pattern's role in the project: 
 
1. Strategy Pattern: 
   - Represented by PaymentStrategy, CreditCardPayment, and PayPalPayment. 
   - Allows you to select a payment strategy (credit card or PayPal) interchangeably. 
 
2. Singleton Pattern: 
   - Implemented with the Logger class. 
   - Ensures there is only one instance of the logger, providing a centralized log for the application. 
 
3. Decorator Pattern: 
   - Illustrated by the DiscountDecorator. 
   - Dynamically adds a discount to the chosen payment strategy. 
 
4. Adapter Pattern: 
   - Demonstrated by NewPaymentAdapter. 
   - Adapts a new payment system to the existing payment strategy interface. 
 
5. Observer Pattern: 
   - Shown through OrderObserver, EmailNotificationObserver, and SMSNotificationObserver. 
   - Allows various observers (email and SMS notification) to be notified when an order is processed. 
 
6. Factory Pattern: 
   - Represented by PaymentStrategyFactory. 
   - Creates instances of payment strategies based on a given payment type.
