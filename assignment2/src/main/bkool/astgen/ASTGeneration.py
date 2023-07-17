from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        print(ctx.class_decl)
        return Program([self.visit(x) for x in ctx.class_decl()])

    def visitClass_decl(self, ctx: BKOOLParser.Class_declContext):
        # class_name = ID | Prog_word | CLASS | Main_word
        ID = ctx.class_name(0).ID()
        Prog_word = ctx.class_name(0).Prog_word()
        CLASS = ctx.class_name(0).CLASS()
        Main_word = ctx.class_name(0).Main_word()

        class_name = ''
        if ID is not None:
            class_name = ID.getText()
        if Prog_word is not None:
            class_name = Prog_word.getText()
        if CLASS is not None:
            class_name = CLASS.getText()
        if Main_word is not None:
            class_name = Main_word.getText()
        return ClassDecl(Id(class_name), [self.visit(x) for x in ctx.member_lists()])

    def visitMember_lists(self, ctx: BKOOLParser.Member_listsContext):
        if ctx.attributes() is not None:
            init_value = ctx.attributes().operands().getText() if ctx.attributes().operands() is not None else ''
            return AttributeDecl(
                Instance(),
                VarDecl(
                    Id(ctx.attributes().idlist().getText()),
                    self.visit(ctx.attributes().types()),
                    init_value
                )
            )

        if ctx.methods() is not None:
            return self.visit(ctx.methods())

        if ctx.instructor() is not None:
            return AttributeDecl(Instance(), VarDecl(Id(ctx.attributes().idlist().getText()), IntType()))

    # Visit a parse tree produced by BKOOLParser#methods.
    def visitMethods(self, ctx:BKOOLParser.MethodsContext):
        return MethodDecl(
            self.visit(ctx.class_props_kind()),
            Id(ctx.methods_name().getText()),
            self.visit(ctx.paramlist()),
            self.visit(ctx.methods_return_types()),
            Block(self.visit(ctx.block_stmt())),
        )

    def visitClass_props_kind(self, ctx:BKOOLParser.Class_props_kindContext):
        static = 'static' if Static() is not None else ''
        final = 'final' if ctx.Final_word() is not None else ''
        kind = final + static
        return 'normal' if kind == '' else kind
    def visitTypes(self, ctx:BKOOLParser.TypesContext):
        if ctx.primitive_Type() is not None:
            return self.visit(ctx.primitive_Type())
        if ctx.array_Type() is not None:
            return self.visit(ctx.array_Type())
        if ctx.class_type() is not None:
            return self.visit(ctx.class_type())

    def visitMethods_return_types(self, ctx:BKOOLParser.Methods_return_typesContext):
        if ctx.types() is not None:
            return self.visit(ctx.types())
        if ctx.Void_word() is not None:
            return VoidType()

    def visitPrimitive_Type(self, ctx:BKOOLParser.Primitive_TypeContext):
        if ctx.Float_word() is not None:
            return FloatType()
        if ctx.Bool_word() is not None:
            return BoolType()
        if ctx.Str_word() is not None:
            return StringType()
        if ctx.Int_word() is not None:
            return IntType()

    def visitArray_Type(self, ctx:BKOOLParser.Array_TypeContext):
        return ArrayType(self.visit(ctx.primitive_Type()), ctx.array_size().INTLIT().getText())

    def visitClass_name(self, ctx:BKOOLParser.Class_nameContext):
        return ClassType(ctx.getText())

    # def visitBkooltype(self, ctx: BKOOLParser.BkooltypeContext):
    #     return IntType() if ctx.INTTYPE() else VoidType()
