import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class main {}"""
    #     expect = str(Program([ClassDecl(Id('main'),[])]))
    #     self.assertTrue(TestAST.test(input,expect,301))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class test {
    #         Shape a, b;
    #     }"""
    #     expect = str(Program([
    #         ClassDecl(
    #             Id('test'),
    #             [
    #                 AttributeDecl(
    #                     Instance(),
    #                     [
    #                         VarDecl(Id('a'), Id('Shape'), NullLiteral()),
    #                         VarDecl(Id('b'), Id('Shape'), NullLiteral())
    #                     ]
    #                 )
    #             ]
    #         )
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,301))

    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         static int a;
    #         int b;
    #     }"""
    #     expect = str(Program([
    #         ClassDecl(
    #             Id('main'),
    #             [
    #                 AttributeDecl(
    #                     Static(),
    #                     [
    #                         ConstDecl(Id('a'), str(IntType()), None)
    #                     ]
    #                 ),
    #                 AttributeDecl(
    #                     Instance(),
    #                     [
    #                         VarDecl(Id('b'), str(IntType()), None)
    #                     ]
    #                 )
    #             ]
    #         )
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,302))

    # def test_class_with_methods(self):
    #     """More complex program"""
    #     input = """class Shape {
    #         static float getArea() {
    #             if(i > 2) then {
    #                 return sqrt(this.length + this.width, 2);
    #             }
    #             else {
    #                 return sqrt(this.length + this.width, 2);
    #             }
    #         }
    #     }"""
    #     expect = str(
    #         Program(
    #             [
    #                 ClassDecl(
    #                     Id('Shape'),
    #                     [
    #                         MethodDecl(
    #                             'static',
    #                             Id('getArea'),
    #                             [],
    #                             FloatType(),
    #                             Block(
    #                                 [],
    #                                 [
    #                                     If(
    #                                         BinaryOp('>', Id('i'), IntLiteral(2)),
    #                                         Block(
    #                                             [],
    #                                             [
    #                                                 Return(CallExpr(
    #                                                     Id('sqrt'),
    #                                                     NullLiteral(),
    #                                                     [
    #                                                         BinaryOp('+', FieldAccess(Id('this'), Id('length')),FieldAccess(Id('this'), Id('width'))),
    #                                                         IntLiteral(2)
    #                                                     ]
    #                                                 ))
    #                                             ]
    #                                         ),
    #                                         Block(
    #                                             [],
    #                                             [
    #                                                 Return(CallExpr(
    #                                                     Id('sqrt'),
    #                                                     NullLiteral(),
    #                                                     [
    #                                                         BinaryOp('+', FieldAccess(Id('this'), Id('length')),FieldAccess(Id('this'), Id('width'))),
    #                                                         IntLiteral(2)
    #                                                     ]
    #                                                 ))
    #                                             ]
    #                                         )
    #                                     )
    #                                 ]
    #                             )
    #                         )])]))
    #     self.assertTrue(TestAST.test(input,expect,303))

    # def test_program_2class(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class main {}
    #         class main2 {}
    #     """
    #     expect = str(Program([
    #         ClassDecl(Id('main'),[]),
    #         ClassDecl(Id('main2'),[]),
    #     ]))
    #     self.assertTrue(TestAST.test(input,expect,304))

    # def test_class_decl_final_method(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape1 {
    #             final float getArea() {
    #                 return this.length*this.width;
    #             }
    #         }
    #     """
    #     expect = str(
    #         Program([
    #             ClassDecl(
    #                 Id('Shape1'),
    #                 [
    #                     MethodDecl(
    #                         Instance(),
    #                         Id('getArea'),
    #                         [],
    #                         FloatType(),
    #                         Block(
    #                             [],
    #                             [
    #                                 Return(
    #                                     BinaryOp(
    #                                         '*',
    #                                         FieldAccess(Id('this'),Id('length')),
    #                                         FieldAccess(Id('this'),Id('width'))
    #                                     ))
    #                             ]))
    #                 ])]))
    #     self.assertTrue(TestAST.test(input,expect,305))

    # def test_class_decl_static_1atrribute(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static int numOfShape = 0;
    #         }
    #     """
    #     expect = str(Program([
    #         ClassDecl(
    #             Id('Shape'),
    #             [
    #                 AttributeDecl(
    #                     Static(),
    #                     [
    #                         ConstDecl(
    #                             Id('numOfShape'),
    #                             'IntType',
    #                             IntLiteral(0)
    #                         )
    #                     ]
    #                 )
    #             ])]))
    #     self.assertTrue(TestAST.test(input,expect,306))

    # def test_class_decl_static_2atrribute(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int color = 0;
    #         }
    #     """
    #     expect = str(Program(
    #         [
    #             ClassDecl(
    #                 Id('Shape'),
    #                 [
    #                     AttributeDecl(
    #                         Static(),
    #                         [
    #                             ConstDecl(constant=Id(name='numOfShape'), constType='IntType', value=IntLiteral(value=0))
    #                         ]
    #                     ),
    #                     AttributeDecl(
    #                         Static(),
    #                         [ConstDecl(constant=Id(name='color'), constType='IntType', value=IntLiteral(value=0))]
    #                     )]
    #             )
    #         ]))
    #     self.assertTrue(TestAST.test(input, expect, 307))

    # def test_class_decl_method_attribute(self):
    #     """Simple program: class main {} """
    #     input = """
    #             class Shape {
    #                 static float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """
    #     expect = str(Program(
    #         [
    #             ClassDecl(
    #                 Id('Shape'),
    #                 [
    #                     MethodDecl(
    #                         Static(),
    #                         Id('getArea'),
    #                         [],
    #                         FloatType(),
    #                         Block([],
    #                               [
    #                                   Return(
    #                                     BinaryOp(
    #                                         '*',
    #                                         FieldAccess(Id('this'), Id('length')),
    #                                         FieldAccess(Id('this'), Id('width')))
    #                                   )
    #                               ]))
    #                 ])
    #         ]))
    #     self.assertTrue(TestAST.test(input, expect, 308))

    # def test_class_decl_method_with_loop(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float getArea() {
    #               for i:=2232 to 12121 do {
    #                   a := 1;
    #               }
    #             }
    #         }
    #     """
    #     expect = str(Program([
    #         ClassDecl(
    #             Id('Shape'),
    #             [
    #                 MethodDecl(
    #                     Static(),
    #                     Id('getArea'),
    #                     [],
    #                     FloatType(),
    #                     Block(
    #                         [],
    #                         [
    #                             For(
    #                                 Id('i'),
    #                                 IntLiteral(2232),
    #                                 IntLiteral(12121),
    #                                 True,
    #                                 Block(
    #                                     [],
    #                                     [
    #                                         Assign(Id('a'),IntLiteral(1))
    #                                     ]
    #                                 )
    #                             )
    #                         ]
    #                     )
    #                 )]
    #         )
    #     ]))
    #     self.assertTrue(TestAST.test(input, expect, 309))

    def test_class_decl_method_with_loop_downto(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float getArea() {
                  for i:=2232 downto 12121 do {
                      a := 1;
                  }
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id('Shape'),
                [
                    MethodDecl(
                        Static(),
                        Id('getArea'),
                        [],
                        FloatType(),
                        Block(
                            [],
                            [
                                For(
                                    Id('i'),
                                    IntLiteral(2232),
                                    IntLiteral(12121),
                                    False,
                                    Block(
                                        [],
                                        [
                                            Assign(Id('a'),IntLiteral(1))
                                        ]
                                    )
                                )
                            ]
                        )
                    )]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 310))
