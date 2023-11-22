from typing import Callable, Type

dependencies_container: dict[Type | Callable, Callable] = {}


def add_factory_to_mapper(class_: Type | Callable):
    def _add_factory_to_mapper(func: Callable):
        dependencies_container[class_] = func
        return func
    return _add_factory_to_mapper

