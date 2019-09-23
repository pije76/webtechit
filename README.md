# WebIT Django assessment

## Purpose

To check that your knowledge/research ability to use the Django framework meets what's required of a python role with WebIT.

### Assessments

1. Given the code in this repository, create a model to store a "Client", a client contains:
    * a client name
    * their address (as street name, suburb, postcode and state)
    * a contact name
    * an email address
    * a phone number
Notes: the most commonly queried fields are suburb, client name and email address. There should be no duplicate client names.

2. Write a view to create a new Client via a basic HTML form. Required fields for a client include:
    *  client name
    *  email address
    *  phone number


3. Using the view from 2. as a basis. Add another view that can update a given Client record.

4. Create a view to list all Client records, including a search form. The view must include the following:
    * a search by client name
    * a search by email address
    * a search by phone number
    * a search by client suburb
    * the ability to order by name, email address, phone number and suburb
    * each record should link to the update view from 3.
