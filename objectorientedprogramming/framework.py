


class Framework:

    name:str

    language:str

    architecture:str

    def __init__(self,name,language,architecture):
    

        self.name = name

        self.language = language

        self.architecture = architecture

    def display(self):

        print(self.name,self.language,self.architecture)


django = Framework()

asp = Framework()

asp.set_framework("asp.net","c#","mvc")

django.set_framework("django","python","mvt")

angular = Framework()

angular.set_framework("angular","typescript","component")

django.display()

angular.display()

asp.display()

