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

    # def test_class_decl_method_with_loop_downto(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
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
    #                                 False,
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
    #     self.assertTrue(TestAST.test(input, expect, 310))

    # def test_class_decl_method_with_loop_downto_if_inside(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   a := 1;
    #                   if a > 2 then {
    #                       a := 111;
    #                   }
    #               }
    #             }
    #         }
    #     """
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
    #                         Block(
    #                             [],
    #                             [
    #                                 For(
    #                                     Id('i'),
    #                                     IntLiteral(2232),
    #                                     IntLiteral(12121),
    #                                     False,
    #                                     Block(
    #                                         [],
    #                                         [
    #                                             Assign(Id('a'),IntLiteral(1)),
    #                                             If(
    #                                                 BinaryOp('>',Id('a'),IntLiteral(2)),
    #                                                 Block([],[Assign(Id('a'),IntLiteral(111))])
    #                                             )
    #                                         ]
    #                                     )
    #                                 )
    #                             ]
    #                         )
    #                     )
    #                 ]
    #             )
    #         ]
    #     ))
    #     self.assertTrue(TestAST.test(input, expect, 311))

    # def test_class_decl_attr(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float length, width = pi[121];
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(Id('Shape'),[['AttributeDecl(Static,ConstDecl(Id(length),FloatType,None))', 'AttributeDecl(Static,ConstDecl(Id(width),FloatType,FieldAccess(Id(pi),IntLit(121))))']])]))
    #     self.assertTrue(TestAST.test(input, expect, 312))
    #
    # def test_class_decl_attr2(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float length = 222, width = pi[121];
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(Id('Shape'),[[AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))]])]))
    #     self.assertTrue(TestAST.test(input, expect, 313))

    # def test_class_decl_attr3(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float length = 222, width = pi[121];
    #             static float length = 222, width = pi[121];
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(Id('Shape'),[
    #             [AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))],
    #             [AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))],
    #         ])]))
    #     self.assertTrue(TestAST.test(input, expect, 314))

    # def test_class_decl_attr3(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static float length = 222, width = pi[121];
    #             static float length2 = 3;
    #             static float length3 = 4;
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(Id('Shape'),[
    #             [AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))],
    #             [AttributeDecl('Static',str(ConstDecl(Id('length2'),FloatType(),IntLiteral(3))))],
    #             [AttributeDecl('Static',str(ConstDecl(Id('length3'),FloatType(),IntLiteral(4))))],
    #         ])]))
    #     self.assertTrue(TestAST.test(input, expect, 315))

    # def test_assign_variable_3(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c / d / e / f;
    #             }
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(
    #             Id('Shape'),
    #             [
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape),IntType,IntLit(0))')],
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape2),IntType,IntLit(0))')],
    #                 MethodDecl(
    #                     Static(),
    #                     Id('getArea'),
    #                     [],
    #                     FloatType(),
    #                     Block(
    #                         [],
    #                         [
    #                             Assign(
    #                                 Id('a'),
    #                                 BinaryOp(
    #                                     '/',
    #                                     BinaryOp(
    #                                         '/',
    #                                         BinaryOp('/', Id('c'), Id('d')),
    #                                         Id('e')
    #                                     ),
    #                                     Id('f')
    #                                 )
    #                             )
    #                         ]
    #                     )
    #                 )])])
    #
    #     )
    #     self.assertTrue(TestAST.test(input, expect, 316))

    # def test_assign_variable_2(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c + d + e + f;
    #             }
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(
    #             Id('Shape'),
    #             [
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape),IntType,IntLit(0))')],
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape2),IntType,IntLit(0))')],
    #                 MethodDecl(
    #                     Static(),
    #                     Id('getArea'),
    #                     [],
    #                     FloatType(),
    #                     Block(
    #                         [],
    #                         [
    #                             Assign(
    #                                 Id('a'),
    #                                 BinaryOp(
    #                                     '+',
    #                                     BinaryOp(
    #                                         '+',
    #                                         BinaryOp('+', Id('c'), Id('d')),
    #                                         Id('e')
    #                                     ),
    #                                     Id('f')
    #                                 )
    #                             )
    #                         ]
    #                     )
    #                 )])])
    #
    #     )
    #     self.assertTrue(TestAST.test(input, expect, 317))

    # def test_assign_variable_1(self):
    #     """Simple program: class main {} """
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c * d * e * f;
    #             }
    #         }
    #     """
    #     expect = str(
    #         Program([ClassDecl(
    #             Id('Shape'),
    #             [
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape),IntType,IntLit(0))')],
    #                 [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape2),IntType,IntLit(0))')],
    #                 MethodDecl(
    #                     Static(),
    #                     Id('getArea'),
    #                     [],
    #                     FloatType(),
    #                     Block(
    #                         [],
    #                         [
    #                             Assign(
    #                                 Id('a'),
    #                                 BinaryOp(
    #                                     '*',
    #                                     BinaryOp(
    #                                         '*',
    #                                         BinaryOp('*', Id('c'), Id('d')),
    #                                         Id('e')
    #                                     ),
    #                                     Id('f')
    #                                 )
    #                             )
    #                         ]
    #                     )
    #                 )])])
    #
    #     )
    #     self.assertTrue(TestAST.test(input, expect, 318))

    def test_for_and_return_and_if_elseif_else_block_list(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int numOfShape2 = 0;
                static float getArea() {
                      for i:=2232 downto 12121 do {
                          if a > 2 then {
                              a := 111;
                          } elseif a < -1 {
                              a := 000;
                          } else {
                              a := 222;
                          }
                          id.write(aa);
                          return;
                      }
                }
            }
        """
        expect = str(
            Program([ClassDecl(
                Id('Shape'),
                [
                    [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape),IntType,IntLit(0))')],
                    [AttributeDecl(kind='Static', decl='ConstDecl(Id(numOfShape2),IntType,IntLit(0))')],
                    MethodDecl(
                        Static(),
                        Id('getArea'),
                        [],
                        FloatType(),
                        Block(
                            [],
                            [
                                Assign(
                                    Id('a'),
                                    BinaryOp(
                                        '*',
                                        BinaryOp(
                                            '*',
                                            BinaryOp('*', Id('c'), Id('d')),
                                            Id('e')
                                        ),
                                        Id('f')
                                    )
                                )
                            ]
                        )
                    )])])

        )
        self.assertTrue(TestAST.test(input, expect, 318))
