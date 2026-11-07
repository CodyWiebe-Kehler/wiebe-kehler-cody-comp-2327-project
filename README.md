# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s). Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Cody Wiebe-Kehler

## Assignment 2

## Assignment 3
This addition of the assignment added the fee and events packages. 

The fee package contains the FeeStrategy interface and its concrete subclasses 
which are implemented on the modified transaction classes to calculate transaction fees. 

The events package implements the Observer pattern via the Event class, the EventListener
interface, and its concrete class LoggingListener. This package allowed for the
transaction class to be modified to notify its listeners when a transaction is
processed.