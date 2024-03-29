"""
 * @author nhphung
"""
from AST import *
from Visitor import *
# from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

class Decl(AST):
    __metaclass__ = ABCMeta
    pass

class StoreDecl(Decl):
    __metaclass__ = ABCMeta
    pass

class ConstDecl(StoreDecl):
    constant: Id
    constType: Type
    value: Expr

    def __str__(self):
        return "ConstDecl(" + str(self.constant) + "," + str(self.constType) + "," + str(self.value) + ")"

class StaticChecker(BaseVisitor):
    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        return [self.visit(x, c) for x in ast.decl]

    def visitClassDecl(self, ast, c):
        if ast.parentname:
            if not ast.parentname.name in map(lambda x: x.name, c):
                raise Undeclared(Class(), ast.parentname.name)
        return list(map(lambda x: self.visit(x, c), ast.memlist))




