"""
Neural network script for Composite design pattern
"""
from abc import ABC
from collections.abc import Iterable
from typing import Any, Generator, Self


class Connectable(Iterable['Connectable'], ABC):
    """
    Connectable class based on Iterable and Abstract Base Class.
    """

    def __init__(self) -> None:
        self.inputs: list[Connectable] = []
        self.outputs: list[Connectable] = []

    def connect_to(self, other: 'Connectable') -> None:
        """
        Connect one object to another object.
        :param other: Other object to connect
        :type other: Connectable
        :return: None
        :rtype: NoneType
        """
        if self == other:
            return
        for s_obj in self:
            for o_obj in other:
                s_obj.outputs.append(other)
                o_obj.inputs.append(s_obj)


class Neuron(Connectable):
    """
    Neuron class that inherits from Connectable.
    """

    def __init__(self, name: str):
        super().__init__()
        self.name: str = name

    def __str__(self) -> str:
        return (
            f"{self.name} - {len(self.inputs)} inputs,"
            f" {len(self.outputs)}"
            f" outputs"
        )

    def __iter__(self) -> Generator[Self, Any, None]:
        yield self

    # def connect_to(self, other) -> None:
    #     """
    #     Connects the Neuron to another Neuron
    #     :param other: Other neuron object
    #     :type other: Neuron
    #     :return: None
    #     :rtype: NoneType
    #     """
    #     self.outputs.append(other)
    #     other.inputs.append(self)


class NeuronLayer(list[Any], Connectable):
    """
    Neuron layer class based on list of Neurons and Connectable.
    """

    def __init__(self, name: str, count: int):
        super().__init__()
        self.name: str = name
        for neuron in range(0, count):
            self.append(Neuron(f"{self.name}_{neuron}"))

    def __str__(self) -> str:
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":
    neuron1: Neuron = Neuron("N1")
    neuron2: Neuron = Neuron("N2")
    layer1: NeuronLayer = NeuronLayer("L1", 3)
    layer2: NeuronLayer = NeuronLayer("L2", 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)
