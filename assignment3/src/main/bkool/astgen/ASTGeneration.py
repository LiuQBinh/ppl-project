from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from dataclasses import dataclass
import collections.abc
from abc import ABC


class InitValue(Type):
    def __str__(self):
        return "InitValue"


@dataclass
class IndexExpr():
    data: str
    props: str

    def __str__(self):
        a = self.data
        b = self.props
        return "IndexExpr(" + str(self.data) + "," + str(self.props) + ")"

    def __str__(self):
        a = self.data
        b = self.props
        if isinstance(b, CallExpr):
            return "IndexExpr(" + str(self.data) + ',' + b.data.data.__str__() + ")"
        return "IndexExpr(" + self.data + ',' + self.props + ")"


class ASTGeneration(BKOOLVisitor):
    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.class_decl()])

    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        return ClassDecl(self.visit(ctx.class_name(0)), [self.visit(x) for x in ctx.member_lists()])

    # Visit a parse tree produced by BKOOLParser#class_name.
    def visitClass_name(self, ctx: BKOOLParser.Class_nameContext):
        # class_name = ID | Prog_word | CLASS | Main_word
        ID = ctx.ID()
        Prog_word = ctx.Prog_word()
        CLASS = ctx.CLASS()
        Main_word = ctx.Main_word()

        class_name = ''
        if ID is not None:
            class_name = ID.getText()
        if Prog_word is not None:
            class_name = Prog_word.getText()
        if CLASS is not None:
            class_name = CLASS.getText()
        if Main_word is not None:
            class_name = Main_word.getText()
        return Id(class_name)

    # Visit a parse tree produced by BKOOLParser#member_lists.
    def visitMember_lists(self, ctx: BKOOLParser.Member_listsContext):
        if ctx.attributes() is not None:
            return self.visit(ctx.attributes())

        if ctx.methods() is not None:
            return self.visit(ctx.methods())

        if ctx.instructor() is not None:
            return AttributeDecl(Instance(), VarDecl(Id(ctx.attributes().idlist().getText()), IntType()))

    # Visit a parse tree produced by BKOOLParser#instructor.
    def visitInstructor(self, ctx: BKOOLParser.InstructorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#methods.
    def visitMethods(self, ctx: BKOOLParser.MethodsContext):
        return MethodDecl(
            self.visit(ctx.class_props_kind()),
            self.visit(ctx.methods_name()),
            self.visit(ctx.paramlist()) if ctx.paramlist() is not None else [],
            self.visit(ctx.methods_return_types()),
            self.visit(ctx.block_stmt()),
        )

    # Visit a parse tree produced by BKOOLParser#methods_name.
    def visitMethods_name(self, ctx: BKOOLParser.Methods_nameContext):
        return Id(ctx.getText())

    # Visit a parse tree produced by BKOOLParser#methods_return_types.
    def visitMethods_return_types(self, ctx: BKOOLParser.Methods_return_typesContext):
        if ctx.types() is not None:
            return self.visit(ctx.types())
        if ctx.Void_word() is not None:
            return VoidType()

    # Visit a parse tree produced by BKOOLParser#attributes.
    def visitAttributes(self, ctx: BKOOLParser.AttributesContext):
        class_props_kind = ctx.class_props_kind()

        if class_props_kind.Static_word() is not None:
            decl = [
                str(ConstDecl(
                    str(Id(attribute_as.ID().getText())),
                    self.visit(ctx.types()),
                    self.visit(attribute_as.attribute_as_val()) if attribute_as.attribute_as_val() is not None else None,
                )) for attribute_as in ctx.attribute_as()
            ]
            kind = Static()
        else:
            decl = (
                str(VarDecl(
                    str(Id(attribute_as.ID().getText())),
                    self.visit(ctx.types()),
                    self.visit(attribute_as.attribute_as_val()) if attribute_as.attribute_as_val() is not None else None,
                )) for attribute_as in ctx.attribute_as()
            )
            kind = Instance()

        return [(AttributeDecl(str(kind), d)) for d in decl]

    # Visit a parse tree produced by BKOOLParser#class_props_kind.
    def visitClass_props_kind(self, ctx: BKOOLParser.Class_props_kindContext):
        if ctx.Static_word() is not None:
            return Static()
        return str(Instance())

    # Visit a parse tree produced by BKOOLParser#attribute_as.
    def visitAttribute_as(self, ctx: BKOOLParser.Attribute_asContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#attribute_as_val.
    def visitAttribute_as_val(self, ctx: BKOOLParser.Attribute_as_valContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        delc = []
        stmt = []
        for block in ctx.block_stmt_list():
            if block.delc() is not None:
                delc.append(block.delc())
            if block.stmt() is not None:
                stmt.append(block.stmt())

        return Block([self.visit(x) for x in delc], [self.visit(x) for x in stmt])

    # Visit a parse tree produced by BKOOLParser#block_stmt_list.
    def visitBlock_stmt_list(self, ctx: BKOOLParser.Block_stmt_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#delc.
    def visitDelc(self, ctx: BKOOLParser.DelcContext):
        if ctx.cons_decl() is not None:
            return self.visit(ctx.cons_decl())
        if ctx.var_decl() is not None:
            return self.visit(ctx.var_decl())

    # Visit a parse tree produced by BKOOLParser#var_cons_decl.
    def visitCons_decl(self, ctx: BKOOLParser.Cons_declContext):
        array_param_decl = ctx.paramlist().param_decl()
        return [
            ConstDecl(
                Id(param_decl.idlist().getText()),
                str(self.visit(array_param_decl[0].types())),
                self.visit(param_decl.init_value()) if param_decl.init_value() is not None else 'None'
            )
            for param_decl in array_param_decl
        ]

    # Visit a parse tree produced by BKOOLParser#var_cons_list.
    def visitVar_decl(self, ctx: BKOOLParser.Var_declContext):
        array_param_decl = ctx.paramlist().param_decl()

        return [
            VarDecl(
                Id(param_decl.idlist().getText()),
                str(self.visit(array_param_decl[0].types())),
                self.visit(param_decl.init_value()) if param_decl.init_value() is not None else 'None'
            )
            for param_decl in array_param_decl
        ]

    # Visit a parse tree produced by BKOOLParser#var_cons_name.
    def visitInit_value(self, ctx: BKOOLParser.Init_valueContext):
        return ctx.getText()

    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        if ctx.as_stmt() is not None:
            return self.visitChildren(ctx)

        if ctx.if_stmt() is not None:
            return self.visitChildren(ctx)

        if ctx.loop_for_stmt() is not None:
            return self.visitChildren(ctx)

        if ctx.break_stmt() is not None:
            return self.visitChildren(ctx)

        if ctx.return_stmt() is not None:
            return self.visitChildren(ctx)

        if ctx.getRuleIndex() is not None:
            return self.visitChildren(ctx)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#invoke_stmt.
    def visitInvoke_stmt(self, ctx:BKOOLParser.Invoke_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#as_stmt.
    def visitAs_stmt(self, ctx: BKOOLParser.As_stmtContext):
        rightExpr = None
        expr = ctx.expr()
        if expr is not None:
            rightExpr = expr
        new_val_from_class_stmt = ctx.new_val_from_class_stmt()
        if new_val_from_class_stmt is not None:
            rightExpr = new_val_from_class_stmt

        return Assign(self.visit(ctx.index_expr()), self.visit(rightExpr))

    # Visit a parse tree produced by BKOOLParser#new_val_from_class_stmt.
    def visitNew_val_from_class_stmt(self, ctx: BKOOLParser.New_val_from_class_stmtContext):
        return NewExpr(
            Id(ctx.class_name().getText()),
            [(self.visit(x)) for x in ctx.expr_list().expr()]
        )

    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        return If(
            self.visit(ctx.expr()),
            self.visit(ctx.block_stmt()),
            self.visit(ctx.elseif_stmt()),
        )

    # Visit a parse tree produced by BKOOLParser#elseif_stmt.
    def visitElseif_stmt(self, ctx: BKOOLParser.Elseif_stmtContext):
        expr = ctx.expr()
        else_stmt = ctx.else_stmt()
        if len(expr) == 0:
            return self.visit(ctx.else_stmt()) if (else_stmt is not None) else None

        return If(
            [(self.visit(x)) for x in ctx.expr()],
            [(self.visit(x)) for x in ctx.block_stmt()],
            self.visit(ctx.else_stmt()) if (else_stmt is not None) else None,
        )

    # Visit a parse tree produced by BKOOLParser#else_stmt.
    def visitElse_stmt(self, ctx: BKOOLParser.Else_stmtContext):
        return self.visit(ctx.block_stmt())

    # Visit a parse tree produced by BKOOLParser#loop_for_stmt.
    def visitLoop_for_stmt(self, ctx: BKOOLParser.Loop_for_stmtContext):
        expr = ctx.expr()
        return For(
            Id(ctx.ID().getText()),
            self.visit(expr[0]),
            self.visit(expr[1]),
            ctx.To_word() is not None,
            self.visit(ctx.block_stmt()),
        )

    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        expr = ctx.expr()
        return Return(self.visit(expr) if expr is not None else None)

    # Visit a parse tree produced by BKOOLParser#types.
    def visitTypes(self, ctx: BKOOLParser.TypesContext):
        if ctx.primitive_Type() is not None:
            return self.visit(ctx.primitive_Type())
        if ctx.array_Type() is not None:
            return self.visit(ctx.array_Type())
        return self.visit(ctx.class_type())

    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx: BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#primitive_Type.
    def visitPrimitive_Type(self, ctx: BKOOLParser.Primitive_TypeContext):
        if ctx.Float_word() is not None:
            return str(FloatType())
        if ctx.Bool_word() is not None:
            return str(BoolType())
        if ctx.Str_word() is not None:
            return str(StringType())
        if ctx.Int_word() is not None:
            return str(IntType())

    # Visit a parse tree produced by BKOOLParser#array_Type.
    def visitArray_Type(self, ctx: BKOOLParser.Array_TypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#array_size.
    def visitArray_size(self, ctx: BKOOLParser.Array_sizeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#attribute_list.
    def visitAttribute_list(self, ctx: BKOOLParser.Attribute_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#attribute_name.
    def visitAttribute_name(self, ctx: BKOOLParser.Attribute_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx: BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#param_decl.
    def visitParam_decl(self, ctx: BKOOLParser.Param_declContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#init_value.
    def visitInit_value(self, ctx: BKOOLParser.Init_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx: BKOOLParser.Expr_listContext):
        # return [Expr(self.visit(x)) for x in ctx.class_decl()]
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        return self.visit(ctx.string_expr())

    # Visit a parse tree produced by BKOOLParser#string_expr.
    def visitString_expr(self, ctx: BKOOLParser.String_exprContext):
        relational_expr = ctx.relational_expr()
        if isinstance(relational_expr, BKOOLParser.Relational_exprContext):
            return self.visit(relational_expr)
        if relational_expr.__len__() == 1:
            return self.visit(relational_expr[0])
        str = ''
        for re in relational_expr:
            str = str + re.getText()
        return StringLiteral(str)

    # Visit a parse tree produced by BKOOLParser#relational_expr.
    def visitRelational_expr(self, ctx: BKOOLParser.Relational_exprContext):
        relational_expr = ctx.logical_expr()
        if isinstance(relational_expr, BKOOLParser.Logical_exprContext):
            return self.visit(relational_expr)
        if relational_expr.__len__() == 1:
            return self.visit(relational_expr[0])
        ope = ''
        if ctx.Equal() is not None:
            ope = '=='
        if ctx.Diff() is not None:
            ope = '!='
        if ctx.Greater() is not None:
            ope = '>'
        if ctx.Lesser() is not None:
            ope = '<'
        if ctx.Greater_euqal() is not None:
            ope = '>='
        if ctx.Lesser_equal() is not None:
            ope = '<='
        return BinaryOp(ope, self.visit(relational_expr[0]), self.visit(relational_expr[1]))

    # Visit a parse tree produced by BKOOLParser#logical_expr.
    def visitLogical_expr(self, ctx: BKOOLParser.Logical_exprContext):
        adding_expr = ctx.adding_expr()
        if isinstance(adding_expr, BKOOLParser.Adding_exprContext):
            return self.visit(adding_expr)
        if adding_expr.__len__() == 1:
            return self.visit(adding_expr[0])
        ope = ''
        if ctx.And() is not None:
            ope = '&&'
        if ctx.Or() is not None:
            ope = '||'
        return BooleanLiteral(self.visit(adding_expr[0]) + ope + self.visit(adding_expr[1]))

    # Visit a parse tree produced by BKOOLParser#adding_expr.
    def visitAdding_expr(self, ctx: BKOOLParser.Adding_exprContext):
        adding_expr = ctx.adding_expr()
        if adding_expr is not None:
            ope = ''
            if ctx.Add() is not None:
                ope = '+'
            if ctx.Sub() is not None:
                ope = '-'
            return BinaryOp(ope, self.visit(adding_expr), self.visit(ctx.multiplying_expr()))
        return self.visit(ctx.multiplying_expr())

    # Visit a parse tree produced by BKOOLParser#multiplying_expr.
    def visitMultiplying_expr(self, ctx: BKOOLParser.Multiplying_exprContext):
        multiplying_expr = ctx.multiplying_expr()
        if multiplying_expr is not None:
            ope = ''
            if ctx.Mul() is not None:
                ope = '*'
            if ctx.Div() is not None:
                ope = '/'
            if ctx.Mod() is not None:
                ope = '%'
            return BinaryOp(ope, self.visit(multiplying_expr), self.visit(ctx.logical_not_expr()))
        return self.visit(ctx.logical_not_expr())

    # Visit a parse tree produced by BKOOLParser#logical_not_expr.
    def visitLogical_not_expr(self, ctx: BKOOLParser.Logical_not_exprContext):
        logical_not_expr = ctx.logical_not_expr()
        if logical_not_expr is not None:
            return UnaryOp('!', self.visit(logical_not_expr))
        return self.visit(ctx.sign_expr())

    # Visit a parse tree produced by BKOOLParser#sign_expr.
    def visitSign_expr(self, ctx: BKOOLParser.Sign_exprContext):
        sign_expr = ctx.sign_expr()
        if sign_expr is not None:
            return UnaryOp('-', self.visit(sign_expr))
        return self.visit(ctx.index_expr())

    # Visit a parse tree produced by BKOOLParser#index_expr.
    def visitIndex_expr(self, ctx: BKOOLParser.Index_exprContext):
        index_expr = ctx.index_expr()
        if index_expr is not None:
            expr = ctx.expr()
            if len(expr) > 0:
                return FieldAccess(self.visit(index_expr), self.visit(expr[0]))

            LP = ctx.LP()
            if LP is not None:
                expr_list = ctx.expr_list()
                expr = expr_list.expr() if expr_list is not None else []
                return CallExpr(
                    self.visit(index_expr),
                    self.visit(ctx.class_expr()),
                    [self.visit(x) for x in expr]
                )
            return FieldAccess(self.visit(index_expr), self.visit(ctx.class_expr()))

        return self.visit(ctx.class_expr())

    # Visit a parse tree produced by BKOOLParser#class_expr.
    def visitClass_expr(self, ctx: BKOOLParser.Class_exprContext):
        # class_expr = ctx.class_expr()
        # if class_expr is not None:
        #     return NewExpr()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#piority_exp.
    def visitPiority_exp(self, ctx: BKOOLParser.Piority_expContext):
        expr = ctx.expr()
        if expr is not None:
            return self.visit(expr)

        return self.visit(ctx.array_exp())

    # Visit a parse tree produced by BKOOLParser#array_exp.
    def visitArray_exp(self, ctx: BKOOLParser.Array_expContext):
        operands = ctx.operands()
        if len(operands) > 1:
            return ArrayLiteral([self.visit(x) for x in operands])
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        if ctx.INTLIT() is not None:
            return IntLiteral(int(ctx.getText()))

        if ctx.FLOATLIT() is not None:
            return FloatLiteral(ctx.getText())

        if ctx.BOOLEANLIT() is not None:
            return BooleanLiteral(ctx.getText())

        if ctx.STRINGLIT() is not None:
            return StringLiteral(ctx.getText())

        arrayLIT = ctx.arrayLIT()
        if arrayLIT is not None:
            elements = arrayLIT.element_list().elements()
            return [self.visit(x) for x in elements]

        if ctx.multi_ArrayLIT() is not None:
            return self.visitChildren(ctx.array_list())

        if ctx.ID() is not None:
            return Id(ctx.getText())

        if ctx.Self_word() is not None:
            return SelfLiteral()

        if ctx.class_name() is not None:
            return Id(ctx.getText())

        if ctx.THIS() is not None:
            return SelfLiteral()

    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx: BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#multi_ArrayLIT.
    def visitMulti_ArrayLIT(self, ctx: BKOOLParser.Multi_ArrayLITContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#array_list.
    def visitArray_list(self, ctx: BKOOLParser.Array_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#arrayLIT.
    def visitArrayLIT(self, ctx: BKOOLParser.ArrayLITContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#element_list.
    def visitElement_list(self, ctx: BKOOLParser.Element_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#elements.
    def visitElements(self, ctx: BKOOLParser.ElementsContext):
        return self.visitChildren(ctx)
