# Combining *args and **kwargs in the same function

#def my_function(*args, **kwargs):
    #print(args)      # Prints tuple of positional arguments
    #print(kwargs)    # Prints dictionary of keyword arguments

#my_function(10, True, 'abc', key = 20, name ='Bogdan')
# Positional args (10, True, 'abc') go into *args tuple
# Keyword args (key=20, name='Bogdan') go into **kwargs dictionary
# Order is important: positional arguments MUST come before keyword arguments





# Practice - Gathering positional arguments into *args tuple

#def send_email(to, subject, *args):
    # Required parameters: to, subject
    # *args captures additional positional arguments (CC recipients)
    #print(f"sending and email to: {to} ... ")
    #print(f"Email subject:{subject}")
    #print(f"Email cc:{args}")

   #print(args)  # Shows all extra positional arguments as a tuple

#send_email('test@test.com','Hello there!', 'adhafeez1@mail.com', 'someone@mail.com', 'sender12@mail.com')
# First 2 args go to 'to' and 'subject', rest go into *args tuple

#def send_email(to, subject, *args):
    #print(f"Sending email to: {to}")
    #print(f"Email subject: {subject}")

    #if args:  # Check if there are additional recipients
        #print("Additional recipients:")
        #for recipient in args:
           # print(recipient)  # Loop through each CC recipient

#send_email('test@test.com', 'Hello There!', 'other@test.com', 'someone@test.com')


# Practice - Combining *args and **kwargs for maximum flexibility

# Function that accepts:
# - 2 required parameters (to, subject)
# - Variable positional arguments for CC recipients (*args)
# - Variable keyword arguments for email metadata (**kwargs)
def send_email(to, subject, *args, **kwargs):
    # Print required parameters
    print(f"Sending email to: {to}")
    print(f"Email subject: {subject}")

    # Handle optional CC recipients from *args
    if args:
        print("Additional recipients:")
        for recipient in args:
            print(recipient)

    # Handle optional metadata from **kwargs (bcc, attachments, etc.)
    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}: {kwargs[key]}")

# Example 1: Only required parameters
send_email('test@test.com', 'Hello There!')
print('_______')

# Example 2: With additional CC recipients (positional args)
send_email('test@test.com', 'Hello There!','other@test.com', 'someone@test.com')
print('_______')

# Example 3: With keyword arguments only (no CC recipients)
send_email('test@test.com', 'Hello There!',  bcc = 'Adil@gmail.com', img='test.png')
print('_______')

# Example 4: With both CC recipients (*args) and metadata (**kwargs)
send_email('test@test.com', 'Hello There!','other@test.com', 'someone@test.com', 'other@test.com', 'someone@test.com', bcc = 'Adil@gmail.com', img='test.png')
print('_______')