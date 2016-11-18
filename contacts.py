class Contact(object):
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name= first_name
        self.last_name=last_name
        self.mobile=mobile
        self.email=email

    def send_text(self, message):    
        print "To: %s - %s" % (self.mobile, message)

    def send_email(self, message):
        print "To: %s - %s" % (self.email, message)  

  
def contact_list(contact):
    contact_list = [] 
    contact_list.append(contact)
    return contact_list

    

def main():
    contact_diana = Contact("Diana", "Banana", "415-555-5555", "email@email.com")
    the_message = "Hello! How are you?"
# contact_list = []
    my_list = contact_list(contact_diana)
    # print contact_list
    print my_list[0].__dict__
    


if __name__ == '__main__':
    main()
 