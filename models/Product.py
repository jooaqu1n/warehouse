class Product:

    def __init__(self, id: int, name: str):
        self.__id: int = id
        self.__name: str = name

    def getId(self) -> int:
        return self.__id

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name: str = name

    def getDescription(self) -> str:
        return self.__description

    def setDescription(self, description: str) -> None:
        self.__description: str = description

    def getCost(self) -> float:
        return self.__cost

    def setCost(self, cost: float) -> None:
        self.__cost: float = cost

    def getPrice(self) -> float:
        return self.__price

    def setPrice(self, price: float) -> None:
        self.__price: float = price

    def getCategory(self) -> float:
        return self.__category

    def setCategory(self, category: float) -> None:
        self.__category: int = category

    def __repr__(self) -> str:
        return f'Product<{self.__id} | {self.__name} | {self.__description} | {self.__cost} | {self.__price} | {self.__category}>'    
