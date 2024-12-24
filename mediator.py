from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    """
    A interface Mediator declara um método usado pelos componentes para notificar o mediador sobre vários eventos. 
    O mediador pode reagir a esses eventos e passar a execução para outros componentes.
    """
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("O Mediator reage ao evento A e desencadeia as seguintes operações:")
            self._component2.do_c()
        elif event == "D":
            print("O Mediator reage ao evento D e desencadeia as seguintes operações:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    O Componente Base fornece a funcionalidade básica de armazenar uma instância do mediador 
    dentro dos objetos dos componentes.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("O Componente 1 executa A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("O Componente 1 executa B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("O Componente 2 executa C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("O Componente 2 executa D.")
        self.mediator.notify(self, "D")



if __name__ == "__main__":
    # O código do cliente.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)

    print("O cliente dispara a operação A.")
    c1.do_a()

    print("\n", end="")

    print("O cliente dispara a operação D.")
    c2.do_d()