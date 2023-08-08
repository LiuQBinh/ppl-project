# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_name.
    def visitClass_name(self, ctx:BKOOLParser.Class_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member_lists.
    def visitMember_lists(self, ctx:BKOOLParser.Member_listsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instructor.
    def visitInstructor(self, ctx:BKOOLParser.InstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methods.
    def visitMethods(self, ctx:BKOOLParser.MethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methods_name.
    def visitMethods_name(self, ctx:BKOOLParser.Methods_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methods_return_types.
    def visitMethods_return_types(self, ctx:BKOOLParser.Methods_return_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributes.
    def visitAttributes(self, ctx:BKOOLParser.AttributesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_props_kind.
    def visitClass_props_kind(self, ctx:BKOOLParser.Class_props_kindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt_list.
    def visitBlock_stmt_list(self, ctx:BKOOLParser.Block_stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#delc.
    def visitDelc(self, ctx:BKOOLParser.DelcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#cons_decl.
    def visitCons_decl(self, ctx:BKOOLParser.Cons_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#as_stmt.
    def visitAs_stmt(self, ctx:BKOOLParser.As_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#new_val_from_class_stmt.
    def visitNew_val_from_class_stmt(self, ctx:BKOOLParser.New_val_from_class_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:BKOOLParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#else_stmt.
    def visitElse_stmt(self, ctx:BKOOLParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#loop_for_stmt.
    def visitLoop_for_stmt(self, ctx:BKOOLParser.Loop_for_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invocation_stmt.
    def visitInvocation_stmt(self, ctx:BKOOLParser.Invocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invocation_stmt_params.
    def visitInvocation_stmt_params(self, ctx:BKOOLParser.Invocation_stmt_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#types.
    def visitTypes(self, ctx:BKOOLParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_type.
    def visitClass_type(self, ctx:BKOOLParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitive_Type.
    def visitPrimitive_Type(self, ctx:BKOOLParser.Primitive_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_Type.
    def visitArray_Type(self, ctx:BKOOLParser.Array_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_size.
    def visitArray_size(self, ctx:BKOOLParser.Array_sizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_list.
    def visitAttribute_list(self, ctx:BKOOLParser.Attribute_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attribute_name.
    def visitAttribute_name(self, ctx:BKOOLParser.Attribute_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_decl.
    def visitParam_decl(self, ctx:BKOOLParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#init_value.
    def visitInit_value(self, ctx:BKOOLParser.Init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx:BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#string_expr.
    def visitString_expr(self, ctx:BKOOLParser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#relational_expr.
    def visitRelational_expr(self, ctx:BKOOLParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#logical_expr.
    def visitLogical_expr(self, ctx:BKOOLParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#adding_expr.
    def visitAdding_expr(self, ctx:BKOOLParser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:BKOOLParser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#logical_not_expr.
    def visitLogical_not_expr(self, ctx:BKOOLParser.Logical_not_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#sign_expr.
    def visitSign_expr(self, ctx:BKOOLParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_expr.
    def visitIndex_expr(self, ctx:BKOOLParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_expr.
    def visitClass_expr(self, ctx:BKOOLParser.Class_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#piority_exp.
    def visitPiority_exp(self, ctx:BKOOLParser.Piority_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_exp.
    def visitArray_exp(self, ctx:BKOOLParser.Array_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#multi_ArrayLIT.
    def visitMulti_ArrayLIT(self, ctx:BKOOLParser.Multi_ArrayLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_list.
    def visitArray_list(self, ctx:BKOOLParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayLIT.
    def visitArrayLIT(self, ctx:BKOOLParser.ArrayLITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#element_list.
    def visitElement_list(self, ctx:BKOOLParser.Element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#elements.
    def visitElements(self, ctx:BKOOLParser.ElementsContext):
        return self.visitChildren(ctx)



del BKOOLParser