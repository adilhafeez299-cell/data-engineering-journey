#def my_function(*args, **kwargs):
    #print(args)
    #print(kwargs)

#my_function(10, True, 'abc', key = 20, name ='Bogdan')
# gives tuple of args
# gives dictionary of keyword arguments
# order of the arguments is important





# practice - gathering all keyword arguments into the **args tuple

#def send_email(to, subject, *args):
    #print(f"sending and email to: {to} ... ")
    #print(f"Email subject:{subject}")
    #print(f"Email cc:{args}")

   #print(args)

#send_email('test@test.com','Hello there!', 'adhafeez1@mail.com', 'someone@mail.com', 'sender12@mail.com')

#def send_email(to, subject, *args):
    #print(f"Sending email to: {to}")
    #print(f"Email subject: {subject}")

    #if args:
        #print("Additional recipients:")
        #for recipient in args:
           # print(recipient)

#send_email('test@test.com', 'Hello There!', 'other@test.com', 'someone@test.com')


# practice - gathering all keyword arguments into the **kwargs dictionary

def send_email(to, subject, *args, **kwargs):
    print(f"Sending email to: {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients:")
        for recipient in args:
            print(recipient)

    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}: {kwargs[key]}")


send_email('test@test.com', 'Hello There!')
print('_______')

send_email('test@test.com', 'Hello There!','other@test.com', 'someone@test.com')
print('_______')

send_email('test@test.com', 'Hello There!',  bcc = 'Adil@gmail.com', img='test.png')
print('_______')

send_email('test@test.com', 'Hello There!','other@test.com', 'someone@test.com', 'other@test.com', 'someone@test.com', bcc = 'Adil@gmail.com', img='test.png')
print('_______')