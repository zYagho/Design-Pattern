import json
from typing import Dict


class Flyweight():
    """
    O Flyweight armazena uma parte comum do estado (também chamada de estado intrínseco)
    que pertence a várias entidades de negócios reais. O Flyweight
    aceita o restante do estado (estado extrínseco, único para cada entidade) via
    seus parâmetros de método.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Exibindo estado compartilhado ({s}) e único ({u}) estado.", end="")


class FlyweightFactory():
    """
    A fábrica de Flyweights cria e gerencia os objetos Flyweight. Ela garante
    que os flyweights sejam compartilhados corretamente. Quando o cliente solicita um flyweight,
    a fábrica retorna uma instância existente ou cria uma nova, se ela
    ainda não existir.
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Retorna o hash de string de um Flyweight para um estado dado.
        """

        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Retorna um Flyweight existente com um estado dado ou cria um novo.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Não encontrei um flyweight, criando um novo.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reutilizando flyweight existente.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Eu tenho {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str,
    brand: str, model: str, color: str
) -> None:
    print("\n\nCliente: Adicionando um carro ao banco de dados.")
    flyweight = factory.get_flyweight([brand, model, color])
    # O código do cliente armazena ou calcula o estado extrínseco e o passa
    # para os métodos do flyweight.
    flyweight.operation([plates, owner])


if __name__ == "__main__":
    """
    O código do cliente geralmente cria um monte de flyweights pré-populados na
    fase de inicialização da aplicação.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "rosa"],
        ["Mercedes Benz", "C300", "preto"],
        ["Mercedes Benz", "C500", "vermelho"],
        ["BMW", "M5", "vermelho"],
        ["BMW", "X6", "branco"],
    ])

    factory.list_flyweights()

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "vermelho")

    add_car_to_police_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "vermelho")

    print("\n")

    factory.list_flyweights()
