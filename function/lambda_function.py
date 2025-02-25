# from github import Github

def lambda_handler(event):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------'

    if event["input"] == "Hello":

        return "World"

    else:
