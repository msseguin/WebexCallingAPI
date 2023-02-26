import requests

class WebexSession():

    def __init__(self, clientId:str, redirectURI:str):
        self.responseType = "code"
        self.clientId= clientId
        self.scope = "" 
        self.state =""
        self.webexURL = "https://webexapis.com/"
        self.sessionState = "NOT_STARTED"


    def startSession(self):
        authURL = self.webexURL + "v1/auth"

        


class WebexCalling():

    def __init__(self, session) -> None:
        self.session = session

        if session != "RUNNING":
            self.session.startSession()

    def Call(self,destination:str):
        apiCallURL = self.WebURL + "/v1/telephony/call/dial"
        body = {"destination": destination}

        return requests.post(apiCallURL,json=body)


