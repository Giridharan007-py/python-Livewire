# WRITE A PROGRAM TO CHECK A VALID EMAIL ID USING FUNCTION

e_mail=input("Enter your E-mail id:")
check=input("Enter the check ststement:")
def email():
    if("@" in e_mail):
        if("." in e_mail):
            if("gmail" in e_mail):
                if("com" or "in" in e_mail):
                    print("✅ Valid email address")
                else:
                    print("❌ Invalid email address")
            else:
                print("Please enter the valid E-MAIL ID")
        else:
            print("Please enter the valid E-MAIL ID")
    else:
        print("Please enter the valid E-MAIL ID")
if(check=="email"):
    email()

# giridharan088@gmail.com

                                                                                                                                                                                                                                                        

























