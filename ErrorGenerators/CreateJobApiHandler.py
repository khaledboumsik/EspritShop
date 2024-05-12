from Utils.EmailVerification import vertify_email
def generate_add_job_error_message(ClientID,ProjectID,ResponsableID,BuyTaskOnly,FastDelivery,Customization,PrivateSession):
    confirmation = []
    error_message = ""
    if not ClientID:
        confirmation.append("ClientID")
    if not ProjectID:
        confirmation.append("ProjectID")
    if not ResponsableID:
        confirmation.append("ResponsableID")
    if not BuyTaskOnly and BuyTaskOnly!=0:
        confirmation.append("BuyTaskOnly")
    if not Customization:
        confirmation.append("Customization")
    if not FastDelivery and FastDelivery!=0:
        confirmation.append("FastDelivery")
    if not PrivateSession and PrivateSession!=0:
        confirmation.append("PrivateSession")
    if confirmation:
        for mistake in confirmation:
            error_message += mistake + " is missing  | | "
    if not isinstance(ClientID,int) or len(str(ClientID))>12:
        error_message+="ClientID must be 12 or less length integer | | "
    if not isinstance(ProjectID,int) or len(str(ProjectID))>12:
        error_message+="ProjectID must be 12 or less length integer | | "
    if not isinstance(ResponsableID,int) or len(str(ResponsableID))>12:
        error_message+="ResponsableID must be 12 or less length integer | | "
    if BuyTaskOnly not in [1,0]:
        error_message+="BuyTaskOnly should be either 1 or 0"
    if FastDelivery not in [1,0]:
        error_message+="FastDelivery should be either 1 or 0"
    if PrivateSession not in [1,0]:
        error_message+="PrivateSession should be either 1 or 0"
    if not  isinstance(Customization,str) or len(Customization)>2000:
        error_message+="Customization must be a string that is of 2000 length of less"
    return error_message