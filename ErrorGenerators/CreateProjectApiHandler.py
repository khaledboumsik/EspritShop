
from Utils.EmbededUrlVerification import vertify_embedded_url
def generate_add_project_error_message(about,degree,name,price,demo):
    confirmation = []
    error_message = ""
    if not about:
        confirmation.append("About")
    if not degree:
        confirmation.append("Degree")
    if not name:
        confirmation.append("Name")
    if not price:
        confirmation.append("Price")
    if not demo:
        confirmation.append("Demo")
    if confirmation:
        for mistake in confirmation:
            error_message += mistake + " is missing  | | "
    if (not isinstance(about,str)) or len(about)>2000:
        error_message+="About must be a string that is less than 2000 charcters | | "
    if not len(degree)<12:
        error_message+="Degree length must be under 12 charcters long preferably in the form of (1st dgree) (2nd degree)  | | "
    if not isinstance(name,str) and len(name)>200:
        error_message+="Name must be a string less than 200 charcters this should represent the project without much details" 
    if not isinstance(price,int) or len(str(price))>4:
        error_message+="Price must be a number that is less than or equal 4 digits long"
    if not isinstance(demo,str) or not vertify_embedded_url(demo):
        error_message+="Demo must be an imbeded url"

    return error_message