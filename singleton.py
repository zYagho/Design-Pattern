class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
    
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

"""
    Podemos ver que a classe SingletonMeta é a classe que identifica e controla as instâncias que serão criadas
    dessa forma, garantindo que apenas uma instância dessa classe exista ao mesmo tempo.
"""
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
            Á lógica de negócio ficaria aqui.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")