from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class InitValue(Type):
    def __str__(self):
        return "InitValue"


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
        init_value = ctx.operands().getText() if ctx.operands() is not None else 'None'
        return AttributeDecl(
            Instance(),
            VarDecl(
                Id(ctx.idlist().getText()),
                self.visit(ctx.types()),
                init_value
            )
        )

    # Visit a parse tree produced by BKOOLParser#class_props_kind.
    def visitClass_props_kind(self, ctx: BKOOLParser.Class_props_kindContext):
        static = 'static' if Static() is not None else ''
        final = 'final' if ctx.Final_word() is not None else ''
        kind = final + static
        return 'normal' if kind == '' else kind

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
    def visitDelc(self, ctx:BKOOLParser.DelcContext):
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#as_stmt.
    def visitAs_stmt(self, ctx: BKOOLParser.As_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#new_val_from_class_stmt.
    def visitNew_val_from_class_stmt(self, ctx: BKOOLParser.New_val_from_class_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#loop_for_stmt.
    def visitLoop_for_stmt(self, ctx: BKOOLParser.Loop_for_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#invocation_stmt.
    def visitInvocation_stmt(self, ctx: BKOOLParser.Invocation_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)

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
            return FloatType()
        if ctx.Bool_word() is not None:
            return BoolType()
        if ctx.Str_word() is not None:
            return StringType()
        if ctx.Int_word() is not None:
            return IntType()

    # Visit a parse tree produced by BKOOLParser#array_Type.
    def visitArray_Type(self, ctx: BKOOLParser.Array_TypeContext):
        arr_size = ctx.array_size().getText() if ctx.array_size() is not None else 'None'
        return ArrayType(self.visit(ctx.primitive_Type()), arr_size)

    # Visit a parse tree produced by BKOOLParser#array_size.
    # def visitArray_size(self, ctx:BKOOLParser.Array_sizeContext):
    #     return self.visitChildren(ctx)

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

    # Visit a parse tree produced by BKOOLParser#expr_list.
    def visitExpr_list(self, ctx: BKOOLParser.Expr_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx: BKOOLParser.ExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#string_expr.
    def visitString_expr(self, ctx: BKOOLParser.String_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#relational_expr.
    def visitRelational_expr(self, ctx: BKOOLParser.Relational_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#logical_expr.
    def visitLogical_expr(self, ctx: BKOOLParser.Logical_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#adding_expr.
    def visitAdding_expr(self, ctx: BKOOLParser.Adding_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#multiplying_expr.
    def visitMultiplying_expr(self, ctx: BKOOLParser.Multiplying_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#logical_not_expr.
    def visitLogical_not_expr(self, ctx: BKOOLParser.Logical_not_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#sign_expr.
    def visitSign_expr(self, ctx: BKOOLParser.Sign_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#index_expr.
    def visitIndex_expr(self, ctx: BKOOLParser.Index_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#member_access_in.
    def visitMember_access_in(self, ctx: BKOOLParser.Member_access_inContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#member_access_out.
    def visitMember_access_out(self, ctx: BKOOLParser.Member_access_outContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#class_expr.
    def visitClass_expr(self, ctx: BKOOLParser.Class_exprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#piority_exp.
    def visitPiority_exp(self, ctx: BKOOLParser.Piority_expContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx: BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)

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
