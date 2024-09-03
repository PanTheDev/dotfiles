from __future__ import annotations

from common.expressions.operators import Operator
from pydantic import BaseModel

from panoplie.common.expressions.values import Value


class Expression(BaseModel):
    left_operand: Value | Expression
    operator: Operator
    right_operand: Value | Expression

    @classmethod
    def from_string(cls, expression_string: str) -> Expression:
        pass

    def evaluate(self) -> Value:
        pass

    def __bool__(self) -> bool:
        return bool(self.evaluate())
