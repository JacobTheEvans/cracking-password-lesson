import requests
#import requests because posts are much easier then in urllib2

def attemptLogin(username, password):
    #Make a post request to the server and pass in the arguments as a dict
    r = requests.post("http://localhost:9000", data={"username": username, "password": password})
    #The text resposne from the server
    response = r.text
    #The http response Code
    code = r.status_code
    
    if(code != 200):
        print("Failed login attempt")
        print(response)
        return False
    else:
        print(response)
        print("Username was " + username + " and password was " + password)
        return True


#Every time they want to try the password they will call a function like attemptLogin
#If it is the correct username and password it will return True

#Fail
attemptLogin("mike", "tcfs")
#Fail
attemptLogin("mike", "kit1")
#Pass
attemptLogin("mike", "du42")
