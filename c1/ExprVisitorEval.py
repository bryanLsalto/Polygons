import sys
sys.path.append(('../'))
from polygons import ConvexPolygon as cp
import random
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):
    """Consta de tres grandes funciones para cada tipo de lexico,
    visitRoot, el encargado de devolver el resultado con los estandares marcados.
    visitExpr, el encargado de distinguir las diferentes operaciones unitarias
    o de .
    visitOper. Encargado de las operaciones que requieren recursividad."""

    def __init__(self):
        self.items = {}
        self.calc = cp([(0, 0), (0, 1), (1, 1)])

    def visitRoot(self, ctx: ExprParser.RootContext):
        """Retorna el resultado de los comandos en formato texto,
        con tres decimales
        """
        n = next(ctx.getChildren())
        a = self.visit(n)
        if isinstance(a, list):
            sol = " "
            sol += f'{a[0][0]:.3f}'
            sol += ' '
            sol += f'{a[0][1]:.3f}'

            for i in range(1, len(a)-1):
                sol += ' '
                sol += f'{a[i][0]:.3f}'
                sol += ' '
                sol += f'{a[i][1]:.3f}'
            return sol

        elif isinstance(a, bool):
            if not a:
                return "no"
            else:
                return "yes"
        elif isinstance(a, float):
            return f'{a:.3f}'
        elif isinstance(a, tuple):
            return f'{a[0]:.3f}' + ' ' + f'{a[1]:.3f}'
        elif a is not None:
            return a

    def visitExpr(self, ctx: ExprParser.ExprContext):
        """Lee una expresión dependiendo de la comanda devuelde un valor o otro,
        Aqui nuestro interprete tiene sus funciones bases, si se realizan
        coresponde a otra visit, concretamente al Oper"""
        g = ctx.getChildren()
        l = [next(g) for i in range(ctx.getChildCount())]

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "PRINT"):
                a = l[1].getText()
                if a[0] == '"':
                    res = a.replace('"', '')
                    return res
                else:
                    return self.visit(l[1])

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "AREA"):
            a = self.visit(l[1])
            (x, y) = self.calc.cal_area_centroide(a)
            return x

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "COLOR"):
            exists = self.items.get(l[1].getText(), False)
            if not exists:
                print("No existe!!!!")
            else:
                numeros = l[4].getText()
                numeros = numeros.replace(',', '')
                numeros = numeros.split()

                a = self.items[l[1].getText()]
                a.set_color(int(float(numeros[0])*255), int(float(numeros[1])*255), int(float(numeros[2])*255))
                self.items[l[1].getText()] = a

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "PERIMETER"):
            a = self.visit(l[1])
            return self.calc.cal_perimetro(a)

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "VERTICES"):
            a = self.visit(l[1])
            return len(a) - 1

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "CENTROID"):
            a = self.visit(l[1])
            (x, y) = self.calc.cal_area_centroide(a)
            return y

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "EQUAL"):
            a = self.visit(l[1])
            b = self.visit(l[3])
            return a == b

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "INSIDE"):
            a = self.visit(l[1])
            b = self.visit(l[3])
            if len(a) == 1:
                return self.calc.inside(a[0], b)
            else:
                return self.calc.polygon_inside(a, b)

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "DRAW"):
            name = l[1].getText()
            name = name.replace('"', '')
            P = []
            C = []

            nombres = ""
            for i in range(3, len(l)):
                nombres += l[i].getText()
            nombres = nombres.split(',')
            for i in nombres:
                P.append(self.items[i].get_puntosal())
                C.append(self.items[i].get_color())
            self.calc.drawpolygon(name, P, C)

        if (ExprParser.symbolicNames[l[0].getSymbol().type] == "LINE_COMMENT"):
                return None

        if l[1].getText() == ":=":
            a = self.visit(l[2])
            if a[0] == a[len(a)-1]:
                a.pop()
            res = cp(a)
            self.items[l[0].getText()] = res

    def visitOper(self, ctx: ExprParser.OperContext):
        """Encargado de devolver el polygono dado una id, de pasar un vector en
        formato string a una lista de puntos, y de calcular las operaciones de
        interseccion, unio, boundinBox, random entre otras."""
        g = ctx.getChildren()
        l = [next(g) for i in range(ctx.getChildCount())]
        if len(l) == 1:
            a = self.items.get(l[0].getText(), False)
            if not a:
                print("No existe la variable " + l[0].getText())
            else:
                sol = self.items[l[0].getText()]
                res = sol.get_puntosal()
                return res

        if len(l) == 2:
            if(l[0].getText() == '#'):
                a = self.visit(l[1])
                return self.calc.get_boundingbox(a)
            elif l[0].getText() == '!':
                num = int(l[1].getText())
                punts = []
                for i in range(num):
                    a = random.random()
                    b = random.random()
                    punts.append((a, b))
                poly = cp(punts)
                sol = poly.get_puntosal()
                return sol
            else:
                text = l[1].getText()
                text = text.replace(']', '')
                text = text.split()
                vol = []
                for i in range(0, len(text), 2):
                    vol.append((float(text[i]), float(text[i+1])))
                a = cp(vol)
                return a.get_puntosal()

        if len(l) == 3:
            if l[0].getText() == '(':
                return self.visit(l[1])
            elif ExprParser.symbolicNames[l[1].getSymbol().type] == "INTERSECT":
                a = self.visit(l[0])
                b = self.visit(l[2])
                print(a)
                print(b)
                x = self.calc.intersection(a, b)
                print(x)
                return x
            elif ExprParser.symbolicNames[l[1].getSymbol().type] == "UNION":
                a = self.visit(l[0])
                b = self.visit(l[2])
                return self.calc.union(a, b)
            if l[0].getText() == '[':
                text = l[1].getText()
                x = text.split()
                for i in range(0, len(x), 2):
                    x = float(text[i])
                    y = float(text[i+1])
                sol.append((x, y))
                return cp(sol).get_puntosal()
