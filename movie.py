#film nesneleri
class Movie:
    __name = None
    __imbdpuan = None
    __director = None
    __scriptwriter = None
    __subject = None
    __players = None
    __banner = None
    __fragment = None

    #kurucu metot
    def __init__(self, name = None, imdbpuan = None, director = None, scriptwriter = None, subject = None, players = None, banner = None, fragment = None):
        self.__name = name
        self.__imbdpuan = imdbpuan
        self.__director = director
        self.__scriptwriter = scriptwriter
        self.__subject = subject
        self.__players = players
        self.__banner = banner
        self.__fragment = fragment

    #private elemanlar için get ve set metotları
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_imbdpuan(self):
        return self.__imbdpuan

    def set_imbdpuan(self, imbdpuan):
        self.__imbdpuan = imbdpuan
    
    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    def get_scriptwriter(self):
        return self.__scriptwriter

    def set_scriptwriter(self, scriptwriter):
        self.__scriptwriter = scriptwriter

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject
    
    def get_players(self):
        return self.__players

    def set_players(self, players):
        self.__players = players

    def get_banner(self):
        return self.__banner

    def set_banner(self, banner):
        self.__banner = banner

    def get_fragment(self):
        return self.__fragment

    def set_fragment(self, fragment):
        self.__fragment = fragment    