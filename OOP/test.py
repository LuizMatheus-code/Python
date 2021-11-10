from collection import Product
from collection import Person

if __name__ == "__main__":
    finn = Person('Finn, the human', 17)
    fern = Person('Fern, the Grass', 17)
    
    book = Product('Enchiridion', "100.60")
    
    print(book.price)
    print(type(book.price))
    print(book.name)