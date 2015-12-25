from payemoi.services import payutc

def get_new_transactions_info(request):
    cli = payutc.Client()
    cli.loginApp()
    print cli.call("USERRIGHT", "getAllFundations")
    return {}