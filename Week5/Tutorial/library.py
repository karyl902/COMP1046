class person:
    def __init__(self,forenames: str,surnames: str):
        self.forenames = forenames #given names
        self.surnames = surnames #family names
        pass
    
    @property
    def furenames(self):
            return self.__forenames

    @forenames.setter
    def forenames(self,forenames):
        self.__forenames = forenames
        pass

    @surnames
    def surnames(self):
        return self.__surnames
    @surnames.setter
    def surnames(self,surnames):
        self.__surnames = surnames
        pass
    pass


    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,title):
        self.__title = title
        pass
    pass