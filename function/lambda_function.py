# from github import Github

def lambda_handler(event):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------')
    print(f"Received event: {event}")
    try:
        if "input" not in event:
            raise ValueError("Missing 'input' in event")
        if event["input"] == "Hello":
            return "World"
        if event["input"] == "Hi":
            return "World"
        else:
            raise ValueError("Invalid input")
    except Exception as e:
        print(f"Error: {e}")
        raise e
