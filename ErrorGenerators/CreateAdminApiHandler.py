
from Utils.EmailVerification import vertify_email
def generate_add_admin_error_message(email,Login,password,phoneNumber,status):
    confirmation = []
    error_message = ""
    if not email:
        confirmation.append("Email")
    if not Login:
        confirmation.append("Login")
    if not password:
        confirmation.append("Password")
    if not phoneNumber:
        confirmation.append("PhoneNumber")
    if not status:
        confirmation.append("Status")
    if confirmation:
        for mistake in confirmation:
            error_message += mistake + " is missing  | | "
    if (not vertify_email(email)) or len(email)>100:
        print(email,vertify_email(email))
        error_message+="Email must be valid and it's length dosent go over 100 letters | | "
    if not isinstance(phoneNumber,int) or len(str(phoneNumber))>12:
        error_message+="PhoneNumber must be composed of only numbers and dosent go over 12 number  | | "
    if len(password)<10:
        error_message+="Password must be at least 10 chacters long"
    if status not in [1,0]:
        error_message+="Status must be an int of either 1 or 0"
    return error_message