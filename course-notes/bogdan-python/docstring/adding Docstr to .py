def send_email(to, subject, *args, **kwargs):
    """
    Send email to different recipients

    :param str to: Recipient Address
    :param  str subject: Email Subject
    :param str args: Additional Recipient
    :param str kwargs: Additional details
    return None:
    """
    print(f"Sending an email to : {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional Recipients:")
        for recipient in args:
            print(recipient)
    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}:{kwargs[key]}")


send_email('test@test.com,', 'Hello There!')
print("_______")
send_email('test@test.com', 'Hello There!', 'other@test.com', 'someone@gmail.com')
print("_______")
send_email('test@test.com','Hello There!', bcc='bogdan@gmail.com', img='test.png')
print("_______")
(send_email('adil.mail.com', 'This is not spam', 'sus@mail.com', 'mail2@mail.com', bcc='ian@gmail.com', img='image.png'))
