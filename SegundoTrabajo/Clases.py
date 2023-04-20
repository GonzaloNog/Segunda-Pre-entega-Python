class user:
    def __init__(self,name,lastname,password,email,phone,id):
        #metodos privados 
        self.__id = id
        self.__email = email
        self.__password = password
        #metodos publicos
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.favorites = set()

    #set y get metodos privados
    def getPassword(self):
        return self.__password
    def setPassword(self, password):
        self.__password = password
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    #el id va a ser la clave de identificacion del usuario no se va a poder cambiar
    def getId(self):
        return self.__id

    def addFavorite(self,idProducto):
        self.favorites.add(idProducto)

    def displayCompleteInformation(self):
        print(f'name: {self.name}\nlastname: {self.lastname}\nemail: {self.__email}\npassword: {self.__password}\nphone: {self.phone}\n id: {self.__id}')
    def __str__(self):
        return f'name: {self.name}\nlastname: {self.lastname}\nphone: {self.phone}'

class item():
    def __init__(self,title,categoria,precio,idUser,idProducto,paused = False):
        self.__idProducto = idProducto
        self.__userId = idUser
        self.title = title
        self.categoria = categoria
        self.precio = precio
        self.paused = paused

    #Get
    def getIdProducto(self):
        return self.__idProducto
    def getIdUser(self):
        return self.__userId

class seller(user):
    def __init__(self, name, lastname, password, email, phone,id):
        super().__init__(name, lastname, password, email, phone, id)
        self.__sold = 0
        self.items = set()
        self.reputation = 'neutral'
        self.__points = 5
    
    def newItem(self, idItem):
        self.items.add(idItem)
    def getItemList(self):
        return self.items
    def reputationChange(self, num):
        self.__points = self.__points + num
        if(self.__points > 10):
            self.reputation = 'positive'
        elif(self.__points > 0):
            self.reputation = 'neutral'
        else:
            self.reputation = 'negative'

    def newSold(self):
        self.__sold = self.__sold + 1
    def getSold(self):
        return self.__sold

    def displayCompleteInformation(self):
        print(f'name: {self.name}\nlastname: {self.lastname}\nemail: {self.__email}\npassword: {self.__password}\nphone: {self.phone}\n id: {self.__id}\nsold :{self.sold}\ncant items: {len(self.items)}\nreputation :{self.reputation}')
    def __str__(self):
        return f'name: {self.name}\nlastname: {self.lastname}\nphone: {self.phone}\nsold :{self.sold}\ncant items: {len(self.items)}\nreputation :{self.reputation}'

        
    



