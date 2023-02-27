import requests
import webbrowser

class WebexSession:

    def __init__(self, clientId:str, redirectURI:str):
        self.responseType = "code"
        self.clientId= clientId
        self.scope = "" 
        self.state =""
        self.webexURL = "https://webexapis.com/"
        self.sessionState = "NOT_STARTED"
        self.redirectURI = redirectURI


    def startSession(self):
        authURL = self.webexURL + "v1/authorize"
        
        # open the browser
        webbrowser.get('firefox').open_new_tab(authURL)
        

    def stopSession(self):
        authURL




'''
Class WebexCalling
A class containing methods for issueing api calls for Webex Calling

API Response Code
Code	Status	        Description
200	    OK	            Successful request with body content.
201	    Created	        The request has succeeded and has led to the creation of a resource.
202	    Accepted        The request has been accepted for processing.
204	    No Content	    Successful request without body content.
400	    Bad Request	    The request was invalid or cannot be otherwise served. An accompanying error message will explain further.
401	    Unauthorized	Authentication credentials were missing or incorrect.
403	    Forbidden	    The request is understood, but it has been refused or access is not allowed.
404	    Not Found	    The URI requested is invalid or the resource requested, such as a user, does not exist. Also returned when the requested format is not supported by the requested method.
405	    Method Not      Allowed	The request was made to a resource using an HTTP request method that is not supported.
409	    Conflict	    The request could not be processed because it conflicts with some established rule of the system. For example, a person may not be added to a room more than once.
410	    Gone	        The requested resource is no longer available.
415	    Unsupported     Media Type	The request was made to a resource without specifying a media type or used a media type that is not supported.
423	    Locked	        The requested resource is temporarily unavailable. A Retry-After header may be present that specifies how many seconds you need to wait before attempting the request again.
428	    Precondition    Required	File(s) cannot be scanned for malware and need to be force downloaded.
429	    Too Many Requests	Too many requests have been sent in a given amount of time and the request has been rate limited. A Retry-After header should be present that specifies how many seconds you need to wait before a successful request can be made.
500	    Internal Server Error	Something went wrong on the server. If the issue persists, feel free to contact the Webex Developer Support team.
502	    Bad Gateway	    The server received an invalid response from an upstream server while processing the request. Try again later.
503	    Service Unavailable	Server is overloaded with requests. Try again later.
504	    Gateway Timeout	An upstream server failed to respond on time. If your query uses max parameter, please try to reduce it.
'''
class WebexCalling:

    '''
    CONSTRUCTOR
    ' takes a webex
    ' 
    '''
    def __init__(self, session) -> None:
        self.session = session

        if session != "RUNNING":
            self.session.startSession()

    '''
    ' Call(destination)
    ' https://developer.webex.com/docs/api/v1/call-controls/dial
    ' destination - number to dial
    ' returns - http response with callId and callSessionId
    '''
    def Call(self,destination:str):
        apiCallURL = self.WebURL + "/v1/telephony/calls/dial"
        body = {"destination": destination}

        return requests.post(apiCallURL,json=body)
    
    '''
    ' Answer(callId)
    ' https://developer.webex.com/docs/api/v1/call-controls/answer
    ' callId - The call identifier of the call to be answered.
    ' returns - http response
    '''
    def Answer(self,callId):
        apiCallURL = self.WebURL + "/v1/telephony/calls/answer"
        body = {"callId": callId}

        return requests.post(apiCallURL,json=body)