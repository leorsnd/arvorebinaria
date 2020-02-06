class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    
    def imprime(self):
        if self.left:
            self.left.imprime()
        print(self.key, end=" ")
        if self.right:
            self.right.imprime()
            
    
    def __insere(self, key):
        if self.key is None:
            self.key = key
            return True
        else:
            if key < self.key:
                if self.left:
                    return self.left.__insere(key)
                else:
                    self.left = Node(key)
                    return True
            elif key > self.key:
                if self.right:
                    return self.right.__insere(key)
                else:
                    self.right = Node(key)
                    return True
            else:
                return False
    
    def insere_no(self, key):
        if self.__insere(key):
            print("Chave inserida")
        else:
            print("Chave nao inserida")
    
    def __pesquisa(self, key):
        if self.key is None:
            return False
        else:
            if key < self.key:
                if self.left:
                    return self.left.__pesquisa(key)
            elif key > self.key:
                if self.right:
                    return self.right.__pesquisa(key)
            else:
                return True
    
    def pesquisa(self, key):
        if self.__pesquisa(key):
            print("Chave presente")
        else:
            print("Chave ausente")
