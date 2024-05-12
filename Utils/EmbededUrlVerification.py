
import re

def vertify_embedded_url(email):
    """this function verifies the structure of the email adress"""   
    pattern = r'<iframe .*?src="(.*?)".*?>'
    
    # Check if the provided email matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False
