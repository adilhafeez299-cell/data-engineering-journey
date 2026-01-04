def is_user_authenticated():
    return True

def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        print("user is authenticated")
        if is_user_authenticated():
            return fn(*args, **kwargs)
        else:
            raise Exception("user is not authenticated")


    return wrapper

@check_user_auth
def do_sensitive_job():
    #only perform this job if user is authenticated
    print("Performing sensitive job")

do_sensitive_job()
