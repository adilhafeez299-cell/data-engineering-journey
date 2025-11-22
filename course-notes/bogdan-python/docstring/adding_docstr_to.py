# Adding Docstrings to functions - comprehensive example with *args and **kwargs

def send_email(to, subject, *args, **kwargs):
    """
    Send email to different recipients with optional CC and metadata

    :param str to: Primary recipient email address
    :param str subject: Email subject line
    :param str args: Additional recipient email addresses (CC)
    :param str kwargs: Additional email details (bcc, attachments, etc.)
    :return None: This function doesn't return anything, just prints
    """
    # Print primary recipient and subject
    print(f"Sending an email to : {to}")
    print(f"Email subject: {subject}")

    # If there are additional recipients in *args, print them
    if args:
        print("Additional Recipients:")
        for recipient in args:
            print(recipient)

    # If there are keyword arguments (metadata), print them
    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}:{kwargs[key]}")

# Example 1: Send email with only required parameters
send_email('test@test.com,', 'Hello There!')
print("_______")

# Example 2: Send email with additional CC recipients (*args)
send_email('test@test.com', 'Hello There!', 'other@test.com', 'someone@gmail.com')
print("_______")

# Example 3: Send email with metadata only (**kwargs)
send_email('test@test.com','Hello There!', bcc='bogdan@gmail.com', img='test.png')
print("_______")

# Example 4: Send email with both CC recipients and metadata
send_email('adil.mail.com', 'This is not spam', 'sus@mail.com', 'mail2@mail.com', bcc='ian@gmail.com', img='image.png')
