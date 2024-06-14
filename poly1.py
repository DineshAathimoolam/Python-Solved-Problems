class India():
    def capital(self):
        print('New Delhi is the Capital of India')

    def language(self):
        print('Hindi is the popular Language in india')

    def type(self):
        print('India is one of the Developing Country in the World')

class USA():
    def capital(self):
        print('Washington is the Capital of USA')

    def language(self):
        print('English is the popular Language in USA')

    def type(self):
        print('USA is one of the Developed Country in the World')

obj_India=India()
obj_USA=USA()
for country in(obj_India,obj_USA):
    country.capital()
    country.language()
    country.type()
