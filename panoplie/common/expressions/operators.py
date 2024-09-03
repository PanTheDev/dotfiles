from abc import ABC, abstractmethod

from common.expressions.values import Number, Value


OperatorPrecedence = [[], [], []]


class Operator(ABC):
    @staticmethod
    @abstractmethod
    def __call__(left_operand: Value, right_operand: Value) -> Value:
        pass


class GreaterThan(Operator):
    def __call__(left_operand: Value, right_operand: Value) -> bool:
        if isinstance(left_operand, Number) and isinstance(right_operand, Number):
            return left_operand > right_operand
        raise NotImplementedError()


class LesserThan(Operator):
    def __call__(left_operand: Value, right_operand: Value) -> bool:
        if isinstance(left_operand, Number) and isinstance(right_operand, Number):
            return left_operand < right_operand
        raise NotImplementedError()


class Equals(Operator):
    def __call__(left_operand: Value, right_operand: Value) -> bool:
        if isinstance(left_operand, Number) and isinstance(right_operand, Number):
            return left_operand == right_operand
        raise NotImplementedError()


class NotEquals(Operator):
    def __call__(left_operand: Value, right_operand: Value) -> bool:
        if isinstance(left_operand, Number) and isinstance(right_operand, Number):
            return left_operand != right_operand
        raise NotImplementedError()


class In(Operator):
    def __call__(left_operand: Value, right_operand: Value) -> bool:
        if not isinstance(right_operand, list):
            raise Exception()  # TODO
        return left_operand in right_operand


class Matches(Operator):
    raise NotImplementedError()


class And(Operator):
    raise NotImplementedError()


class Or(Operator):
    raise NotImplementedError()
