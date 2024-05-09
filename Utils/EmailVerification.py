import re

def vertify_email(email):
    """this function verifies the structure of the email adress"""   
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Check if the provided email matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False
