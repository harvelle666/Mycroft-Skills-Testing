import requests

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill


class LoginSkill ( MycroftSkill ):
    def __init__(self):
        super(LoginSkill, self).__init__(name="LoginSkill")
    
    def initialize(self):
        
        login_intent = IntentBuilder("LoginIntent"). \
            require("UsernameKeyword").build()
        self.register_intent(login_intent, self.handle_login_intent)

    def handle_login_intent ( self , message ):
        uname = message.data.get ( "UsernameKeyword" )
        try:
            response = self.find_and_query (uname)
            self.speak_dialog ( "login" , data=response )
        except Exception as e:
            self.log.exception ( e )
            self.speak_dialog ( "not.found")

    def find_and_query(uname):
        url = "url_here"
        headers = {'Content-Type': 'application/json'}
        data = {'key1': 'value1' , 'key2': 'value2' , 'key3': 'value3' , 'key4': 'value4'
                'key5': 'value5'}
        response = requests.post ( url , data , headers )
        finalresponse = response.json ( )
        username = finalresponse[ 'data' ][ 0 ][ 'dsm_name' ]
        return username

    def stop ( self ):
            pass

    def create_skill ( ):
        return LoginSkill ( )



