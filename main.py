import sympy
sympy.init_printing()

X_SYMBOL = sympy.symbols("x")

class Term:
    """
    A mathematical term containing zero, one or more integrals
    Integral placements are denoted by placeholder symbols:
    iota_0 to iota_i
    """
    symbolic: sympy.core.Expr
    placeholder_integrals: list

    def __init__(self, symbolic, placeholder_integrals):
        pass

class Integral(Term):
    """
    An indefinite integral
    """
    symbolic: sympy.core.Expr
    def __init__(self, symbolic, placeholder_integrals, integrand=X_SYMBOL):
        super().__init__(symbolic, placeholder_integrals)
        self.integrand = integrand

    def simp(self):
        self.symbolic = sympy.simplify(self.symbolic)

if __name__ == '__main__':
    pass