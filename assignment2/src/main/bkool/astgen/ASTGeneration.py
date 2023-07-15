from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return program([self.visit(x) for x in ctx.class_decl()])

    def visitClassdecl(self,ctx:BKOOLParser.Class_declContext):
        return ClassDecl(Id(ctx.ID().getText()),[self.visit(x) for x in ctx.memdecl()])

    def visitMemdecl(self,ctx:BKOOLParser.Member_listsContext):
        return AttributeDecl(Instance(),VarDecl(Id(ctx.ID().getText()),self.visit(ctx.bkooltype())))

    def visitBkooltype(self,ctx:BKOOLParser.Primitive_TypeContext):
        return IntType() if ctx.INTTYPE() else VoidType()
        

    
