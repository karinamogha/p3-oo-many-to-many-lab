from datetime import datetime

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  

    def contracts(self):
        return self._contracts

    def authors(self):

        return [contract.author for contract in self._contracts]

    def add_contract(self, contract):
        self._contracts.append(contract) 

class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  

    def contracts(self):
        return self._contracts

    def books(self):
      
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)  
        return contract

    def total_royalties(self):
        # Return the total royalties for this author from all contracts
        return sum(contract.royalties for contract in self._contracts)

class Contract:
    all = []  

    def __init__(self, author, book, date, royalties):
     
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("Book must be of type Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  

        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
      
        target_date = datetime.strptime(date, "%d/%m/%Y")
        

        filtered = [contract for contract in cls.all if datetime.strptime(contract.date, "%d/%m/%Y") == target_date]
        
  
        return sorted(filtered, key=lambda contract: datetime.strptime(contract.date, "%d/%m/%Y"))






