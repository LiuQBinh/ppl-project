import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class test {
            Shape a, b;
        }"""
        expect = str(Program([ClassDecl(Id('test'),[[AttributeDecl(kind='Instance', decl='VarDecl(Id(a),Id(Shape))'), AttributeDecl(kind='Instance', decl='VarDecl(Id(b),Id(Shape))')]])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            static int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id(test),[[AttributeDecl(kind='Instance', decl='VarDecl(Id(a),Id(Shape))'), AttributeDecl(kind='Instance', decl='VarDecl(Id(b),Id(Shape))')]])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_methods(self):
        """More complex program"""
        input = """class Shape {
            static float getArea() {
                if(i > 2) then {
                    return sqrt(this.length + this.width, 2);
                }
                else {
                    return sqrt(this.length + this.width, 2);
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id(Shape),[MethodDecl(Static,Id(getArea),[],FloatType,Block([],[If(BinaryOp(>,Id(i),IntLiteral(2)),Block([],[Return(Id(sqrt)),None,None,None,None,None,None,None]),Block([],[Return(Id(sqrt)),None,None,None,None,None,None,None]))]))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_program_2class(self):
        """Simple program: class main {} """
        input = """
            class main {}
            class main2 {}
        """
        expect = str(Program([
            ClassDecl(Id('main'),[]),
            ClassDecl(Id('main2'),[]),
        ]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_class_decl_final_method(self):
        """Simple program: class main {} """
        input = """
            class Shape1 {
                final float getArea() {
                    return this.length*this.width;
                }
            }
        """
        expect = str(
            Program([
                ClassDecl(
                    Id('Shape1'),
                    [
                        MethodDecl(
                            Instance(),
                            Id('getArea'),
                            [],
                            FloatType(),
                            Block(
                                [],
                                [
                                    Return(
                                        BinaryOp(
                                            '*',
                                            FieldAccess(Id('this'),Id('length')),
                                            FieldAccess(Id('this'),Id('width'))
                                        ))
                                ]))
                    ])]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_class_decl_static_1atrribute(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static int numOfShape = 0;
            }
        """
        expect = str(Program([
            ClassDecl(
                Id('Shape'),
                [
                    AttributeDecl(
                        Static(),
                        [
                            ConstDecl(
                                Id('numOfShape'),
                                'IntType',
                                IntLiteral(0)
                            )
                        ]
                    )
                ])]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_class_decl_static_2atrribute(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int color = 0;
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape'), constType='IntType', value=IntLiteral(value=0)))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='color'), constType='IntType', value=IntLiteral(value=0)))]])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_class_decl_method_attribute(self):
        """Simple program: class main {} """
        input = """
                class Shape {
                    static float getArea() {
                        return this.length*this.width;
                    }
                }
            """
        expect = str(Program(
            [
                ClassDecl(
                    Id('Shape'),
                    [
                        MethodDecl(
                            Static(),
                            Id('getArea'),
                            [],
                            FloatType(),
                            Block([],
                                  [
                                      Return(
                                        BinaryOp(
                                            '*',
                                            FieldAccess(Id('this'), Id('length')),
                                            FieldAccess(Id('this'), Id('width')))
                                      )
                                  ]))
                    ])
            ]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_class_decl_method_with_loop(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float getArea() {
                  for i:=2232 to 12121 do {
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
                                    True,
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
        self.assertTrue(TestAST.test(input, expect, 309))

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

    def test_class_decl_method_with_loop_downto_if_inside(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float getArea() {
                  for i:=2232 downto 12121 do {
                      a := 1;
                      if a > 2 then {
                          a := 111;
                      }
                  }
                }
            }
        """
        expect = str(Program(
            [
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
                                                Assign(Id('a'),IntLiteral(1)),
                                                If(
                                                    BinaryOp('>',Id('a'),IntLiteral(2)),
                                                    Block([],[Assign(Id('a'),IntLiteral(111))])
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        ))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_class_decl_attr(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float length, width = pi[121];
            }
        """
        expect = str(
            Program(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='length'), constType='FloatType', value=None)), AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='width'), constType='FloatType', value=FieldAccess(obj=Id(name='pi'), fieldname=IntLiteral(value=121))))]])])))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_class_decl_attr2(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float length = 222, width = pi[121];
            }
        """
        expect = str(
            Program(Program([ClassDecl(Id(Shape),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='length'), constType='FloatType', value=IntLiteral(value=222))), AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='width'), constType='FloatType', value=FieldAccess(obj=Id(name='pi'), fieldname=IntLiteral(value=121))))]])])))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_class_decl_attr3(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float length = 222, width = pi[121];
                static float length = 222, width = pi[121];
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'),[
                [AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))],
                [AttributeDecl('Static',str(ConstDecl(Id('length'),FloatType(),IntLiteral(222)))), AttributeDecl('Static',str(ConstDecl(Id('width'),FloatType(),FieldAccess(Id('pi'),IntLiteral(121)))))],
            ])]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_class_decl_attr3(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static float length = 222, width = pi[121];
                static float length2 = 3;
                static float length3 = 4;
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='length'), constType='FloatType', value=IntLiteral(value=222))), AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='width'), constType='FloatType', value=FieldAccess(obj=Id(name='pi'), fieldname=IntLiteral(value=121))))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='length2'), constType='FloatType', value=IntLiteral(value=3)))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='length3'), constType='FloatType', value=IntLiteral(value=4)))]])]))
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_assign_variable_3(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int numOfShape2 = 0;
                static float getArea() {
                  a:= c / d / e / f;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape'), constType='IntType', value=IntLiteral(value=0)))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape2'), constType='IntType', value=IntLiteral(value=0)))],MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[Assign(Id('a'),BinaryOp('/',BinaryOp('/',BinaryOp('/',Id('c'),Id('d')),Id('e')),Id('f')))]))])]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_assign_variable_2(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int numOfShape2 = 0;
                static float getArea() {
                  a:= c + d + e + f;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape'), constType='IntType', value=IntLiteral(value=0)))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape2'), constType='IntType', value=IntLiteral(value=0)))],MethodDecl(Static(),Id(getArea),[],FloatType(),Block([],[Assign(Id('a'),BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('c'),Id('d')),Id('e')),Id('f')))]))])]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_assign_variable_1(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int numOfShape2 = 0;
                static float getArea() {
                  a:= c * d * e * f;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape'), constType='IntType', value=IntLiteral(value=0)))],[AttributeDecl(kind='Static', decl=ConstDecl(constant=Id(name='numOfShape2'), constType='IntType', value=IntLiteral(value=0)))],MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[Assign(Id('a'),BinaryOp('*',BinaryOp('*',BinaryOp('*',Id('c'),Id('d')),Id('e')),Id('f')))]))])]))
        self.assertTrue(TestAST.test(input, expect, 318))

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
            Program([
                ClassDecl(
                    Id('Shape'),
                    [
                        [AttributeDecl(
                            kind='Static',
                            decl=ConstDecl(
                                constant=Id(name='numOfShape'),
                                constType='IntType',
                                value=IntLiteral(value=0)))
                        ], [
                        AttributeDecl(
                            kind='Static',
                            decl=ConstDecl(
                                constant=Id(name='numOfShape2'),
                                constType='IntType',
                                value=IntLiteral(value=0)
                            )
                        )
                    ],
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
                                                If(
                                                    BinaryOp('>',
                                                             Id('a'),
                                                             IntLiteral(2)
                                                             ),
                                                    Block(
                                                        [],
                                                        [
                                                            Assign(
                                                                Id('a'),
                                                                IntLiteral(111)
                                                            )
                                                        ]
                                                    ),
                                                    If(
                                                        [
                                                            BinaryOp(op='<', left=Id(name='a'),
                                                                     right=UnaryOp(op='-', body=IntLiteral(value=1)))
                                                        ],
                                                        [
                                                            Block(decl=[],
                                                                  stmt=[
                                                                      Assign(lhs=Id(name='a'), exp=IntLiteral(value=0))
                                                                  ])
                                                        ],
                                                        Block(
                                                            [],
                                                            [
                                                                Assign(Id('a'), IntLiteral(222))
                                                            ])
                                                    )
                                                ),
                                                None,
                                                Return(None)
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
            )

        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_for_and_return_and_if_elseif_else_block_list(self):
        """Simple program: class main {} """
        input = """
            class Shape {
                static final int numOfShape = 0;
                static final int numOfShape2 = 0;
                static float getArea() {
                      for i:=2232 to 12121 do {
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
            Program([
                ClassDecl(
                    Id('Shape'),
                    [
                        [AttributeDecl(
                            kind='Static',
                            decl=ConstDecl(
                                constant=Id(name='numOfShape'),
                                constType='IntType',
                                value=IntLiteral(value=0)))
                        ], [
                        AttributeDecl(
                            kind='Static',
                            decl=ConstDecl(
                                constant=Id(name='numOfShape2'),
                                constType='IntType',
                                value=IntLiteral(value=0)
                            )
                        )
                    ],
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
                                        True,
                                        Block(
                                            [],
                                            [
                                                If(
                                                    BinaryOp('>',
                                                             Id('a'),
                                                             IntLiteral(2)
                                                             ),
                                                    Block(
                                                        [],
                                                        [
                                                            Assign(
                                                                Id('a'),
                                                                IntLiteral(111)
                                                            )
                                                        ]
                                                    ),
                                                    If(
                                                        [
                                                            BinaryOp(op='<', left=Id(name='a'),
                                                                     right=UnaryOp(op='-', body=IntLiteral(value=1)))
                                                        ],
                                                        [
                                                            Block(decl=[],
                                                                  stmt=[
                                                                      Assign(lhs=Id(name='a'), exp=IntLiteral(value=0))
                                                                  ])
                                                        ],
                                                        Block(
                                                            [],
                                                            [
                                                                Assign(Id('a'), IntLiteral(222))
                                                            ])
                                                    )
                                                ),
                                                None,
                                                Return(None)
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
            )

        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_return_in_for(self):
        input = """
            class Shape {
                static float getArea() {
                    for i:=2232 to 12121 do {
                        return;
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
                            [], [
                                For(Id('i'), IntLiteral(2232), IntLiteral(12121), True, Block([], [Return(None)]))])
                    )]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_return_in_for_downto(self):
        input = """
            class Shape {
                static float getArea() {
                    for i:=2232 downto 12121 do {
                        return;
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
                            [], [
                                For(Id('i'), IntLiteral(2232), IntLiteral(12121), False, Block([], [Return(None)]))])
                    )]
            )
        ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_if_return_in_for(self):
        input = """
            class Shape {
                static float getArea() {
                    for i:=2232 to 12121 do {
                        if i > 1 then {
                            return;
                        }
                    }
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id('Shape'),
                [MethodDecl(
                    Static(),
                    Id('getArea'),
                    [],
                    FloatType(),
                    Block(
                        [], [
                            For(Id('i'),
                                IntLiteral(2232),
                                IntLiteral(12121),
                                True,
                                Block(
                                    [],
                                    [If(BinaryOp('>', Id('i'), IntLiteral(1)), Block([], [Return(None)]))]
                                ))
                        ]
                    ))
                ]
            )])
        )
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_if_return_in_for_downto(self):
        input = """
            class Shape {
                static float getArea() {
                    for i:=2232 downto 12121 do {
                        if i > 1 then {
                            return;
                        }
                    }
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id('Shape'),
                [MethodDecl(
                    Static(),
                    Id('getArea'),
                    [],
                    FloatType(),
                    Block(
                        [], [
                            For(Id('i'),
                                IntLiteral(2232),
                                IntLiteral(12121),
                                False,
                                Block(
                                    [],
                                    [If(BinaryOp('>', Id('i'), IntLiteral(1)), Block([], [Return(None)]))]
                                ))
                        ]
                    ))
                ]
            )])
        )
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_if_return_relation(self):
        input = """
            class Shape {
                static float getArea() {
                    return a > 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('>', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_if_return_relation_2(self):
        input = """
            class Shape {
                static float getArea() {
                    return a < 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('<', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_if_return_relation_3(self):
        input = """
            class Shape {
                static float getArea() {
                    return a == 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('==', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_if_return_relation_4(self):
        input = """
            class Shape {
                static float getArea() {
                    return a >= 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('>=', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_if_return_relation_5(self):
        input = """
            class Shape {
                static float getArea() {
                    return a <= 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('<=', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_if_return_relation_6(self):
        input = """
            class Shape {
                static float getArea() {
                    return a != 2;
                }
            }
        """
        expect = str(
            Program([ClassDecl(Id('Shape'), [MethodDecl(Static(), Id('getArea'), [], FloatType(),
                                                        Block([], [Return(BinaryOp('!=', Id('a'), IntLiteral(2)))]))])])
        )
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_if_return(self):
        input = """
            class Shape {
                static float getArea() {
                if a != 2 then
                    return a != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('!=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_if_return_2(self):
        input = """
            class Shape {
                static float getArea() {
                if a > 2 then
                    return a != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('>',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_if_return_3(self):
        input = """
            class Shape {
                static float getArea() {
                if a < 2 then
                    return a != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('<',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_if_return_4(self):
        input = """
            class Shape {
                static float getArea() {
                if a >= 2 then
                    return a != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('>=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_if_return_5(self):
        input = """
            class Shape {
                static float getArea() {
                if a <= 2 then
                    return a != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('<=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_if_else_return_1(self):
        input = """
            class Shape {
                static float getArea() {
                    if a <= 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
    ClassDecl(
        Id('Shape'),
        [MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('<=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]),Block([],[Return(BinaryOp('==',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_if_else_return_2(self):
        input = """
            class Shape {
                static float getArea() {
                    if a == 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
    ClassDecl(
        Id('Shape'),
        [MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('==',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]),Block([],[Return(BinaryOp('==',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_if_else_return_3(self):
        input = """
            class Shape {
                static float getArea() {
                    if a <= 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
    ClassDecl(
        Id('Shape'),
        [MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('<=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]),Block([],[Return(BinaryOp('==',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_if_else_return_4(self):
        input = """
            class Shape {
                static float getArea() {
                    if a >= 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
    ClassDecl(
        Id('Shape'),
        [MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('>=',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]),Block([],[Return(BinaryOp('==',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_if_else_return_4(self):
        input = """
            class Shape {
                static float getArea() {
                    if a > 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
    ClassDecl(
        Id('Shape'),
        [MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([],[If(BinaryOp('>',Id('a'),IntLiteral(2)),Block([],[Return(BinaryOp('!=',Id('a'),IntLiteral(2)))]),Block([],[Return(BinaryOp('==',Id('a'),IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_if_else_return_4(self):
        input = """
            class Shape {
                static float getArea() {
                    if a < 2 then {
                        return a != 2;
                    } else {
                        return a == 2;
                    }
                }
            }
        """
        expect = str(Program([
            ClassDecl(
                Id('Shape'),
                [MethodDecl(Static(), Id('getArea'), [], FloatType(), Block([], [
                    If(BinaryOp('<', Id('a'), IntLiteral(2)),
                       Block([], [Return(BinaryOp('!=', Id('a'), IntLiteral(2)))]),
                       Block([], [Return(BinaryOp('==', Id('a'), IntLiteral(2)))]))]))])]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_declare_const(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value='None')]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_declare(self):
        input = """
            class Shape {
                static float getArea() {
                    int a;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit='None')]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_declar_with_init_value(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=IntLiteral(value=2))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_const_declare_with_init_value(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=IntLiteral(value=2))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_const_declare_with_init_value_boolean(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = false;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BooleanLiteral(value='false'))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_const_declare_with_init_value_boolean_2(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = true;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BooleanLiteral(value='true'))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_const_declare_with_init_value_boolean_3(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b > 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_const_declare_with_init_value_boolean_4(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b < 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_const_declare_with_init_value_boolean_5(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b <= 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='<=', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_const_declare_with_init_value_boolean_6(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b == 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='==', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_const_declare_with_init_value_boolean_7(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b == 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='==', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_const_declare_with_init_value_boolean_8(self):
        input = """
            class Shape {
                static float getArea() {
                    final int a = b != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[ConstDecl(constant=Id(name='a'), constType='IntType', value=BinaryOp(op='!=', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_var_declare_with_init_value_boolean_8(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b != 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='!=', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_adding_expr(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b + 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_adding_expr2(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b + 1) + 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 355))



    def test_adding_expr2(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b + 1) + (b + 2);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=2))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_adding_expr3(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b + 1) + (b + 2) + (b + 3);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=2))), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=3))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 357))


    def test_adding_expr4(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b + 1) + (b + 2) + ((b + 3) + (b + 4));
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=2))), right=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=3)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=4)))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 358))


    def test_adding_expr4(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b + 1) + (b + 2) + ((b + 3) + (b + 4));
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=2))), right=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=3)), right=BinaryOp(op='+', left=Id(name='b'), right=IntLiteral(value=4)))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_multi_expr(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b * 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_multi_expr_2(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b * 2 + 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_multi_expr_3(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b * 2 + 1) + 3;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)), right=IntLiteral(value=3)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 362))


    def test_multi_expr_4(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b * 2 + 1) + (b + 3.14 + 2);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=BinaryOp(op='+', left=Id(name='b'), right=FloatLiteral(value='3.14')), right=IntLiteral(value=2))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_multi_expr_5(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b % 2 + 1) + (b / 3.14 + 2);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='%', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)), right=BinaryOp(op='+', left=BinaryOp(op='/', left=Id(name='b'), right=FloatLiteral(value='3.14')), right=IntLiteral(value=2))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_multi_expr_6(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = ((b % 2 + 1) + (b * 3.14 / 2)) / 3;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='/', left=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='%', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)), right=BinaryOp(op='/', left=BinaryOp(op='*', left=Id(name='b'), right=FloatLiteral(value='3.14')), right=IntLiteral(value=2))), right=IntLiteral(value=3)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_multi_expr_7(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = ((b % 2 + 1) + (b * 3.14 / 2)) / 3;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='/', left=BinaryOp(op='+', left=BinaryOp(op='+', left=BinaryOp(op='%', left=Id(name='b'), right=IntLiteral(value=2)), right=IntLiteral(value=1)), right=BinaryOp(op='/', left=BinaryOp(op='*', left=Id(name='b'), right=FloatLiteral(value='3.14')), right=IntLiteral(value=2))), right=IntLiteral(value=3)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_multi_expr_8(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b * 1 / 2 % 3 + 4;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='+', left=BinaryOp(op='%', left=BinaryOp(op='/', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=1)), right=IntLiteral(value=2)), right=IntLiteral(value=3)), right=IntLiteral(value=4)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_multi_expr_9(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = (b * 1 / 2 % 3 + 4) - 2 * (b * 1 / 2 % 3 + 4);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='-', left=BinaryOp(op='+', left=BinaryOp(op='%', left=BinaryOp(op='/', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=1)), right=IntLiteral(value=2)), right=IntLiteral(value=3)), right=IntLiteral(value=4)), right=BinaryOp(op='*', left=IntLiteral(value=2), right=BinaryOp(op='+', left=BinaryOp(op='%', left=BinaryOp(op='/', left=BinaryOp(op='*', left=Id(name='b'), right=IntLiteral(value=1)), right=IntLiteral(value=2)), right=IntLiteral(value=3)), right=IntLiteral(value=4)))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_multi_expr_10(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = a % b % c % d % e % f;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=Id(name='a'), right=Id(name='b')), right=Id(name='c')), right=Id(name='d')), right=Id(name='e')), right=Id(name='f')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_multi_expr_11(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = ((a % b % c) % d) % e % f;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=BinaryOp(op='%', left=Id(name='a'), right=Id(name='b')), right=Id(name='c')), right=Id(name='d')), right=Id(name='e')), right=Id(name='f')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_multi_expr_12(self):
        input = """
            class Shape {
                static float getArea() {
                    int a = b > 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],FloatType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_multi_expr_12(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = b > 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_boolean_expr(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b > 2) && true;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BooleanLiteral(value='true')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_boolean_expr_2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b > 2) && true;
                    boolean a = (b > 2) && false;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BooleanLiteral(value='true')))],[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BooleanLiteral(value='false')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_boolean_expr_3(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b > 2) && true;
                    boolean a = (b > 2) && false;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BooleanLiteral(value='true')))],[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BooleanLiteral(value='false')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_boolean_expr_4(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b > 2) && (b < 100);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_boolean_expr_5(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b < 2) && (b < 100) && false;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=BooleanLiteral(value='false')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_boolean_expr_6(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b < 2) && (b < 100) && true;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='&&', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=BooleanLiteral(value='true')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_boolean_expr_7(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b < 2) && (b < 100) || a;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='||', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=Id(name='a')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_boolean_expr_8(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (b < 2) && (b < 100) || a || c < 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='<', left=BinaryOp(op='||', left=BinaryOp(op='||', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=Id(name='a')), right=Id(name='c')), right=IntLiteral(value=1)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_boolean_expr_9(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = ((b < 2) && (b < 100) || a || c < 1) || false;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='||', left=BinaryOp(op='<', left=BinaryOp(op='||', left=BinaryOp(op='||', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=Id(name='a')), right=Id(name='c')), right=IntLiteral(value=1)), right=BooleanLiteral(value='false')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_logical_not_expr(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = -(b > 2);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=UnaryOp(op='-', body=BinaryOp(op='>', left=Id(name='b'), right=IntLiteral(value=2))))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 382))


    def test_logical_not_expr2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = -((b < 2) && (b < 100) || a || c < 1) || false);
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='||', left=UnaryOp(op='-', body=BinaryOp(op='<', left=BinaryOp(op='||', left=BinaryOp(op='||', left=BinaryOp(op='&&', left=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=2)), right=BinaryOp(op='<', left=Id(name='b'), right=IntLiteral(value=100))), right=Id(name='a')), right=Id(name='c')), right=IntLiteral(value=1))), right=BooleanLiteral(value='false')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_index_expr(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = a.b.c;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=FieldAccess(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), fieldname=Id(name='c')))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_index_expr2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = a.b.c();
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=CallExpr(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), method=Id(name='c'), param=[]))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_index_expr3(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = a[b].c();
                    boolean a = a[b].c();
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=CallExpr(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), method=Id(name='c'), param=[]))],[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=CallExpr(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), method=Id(name='c'), param=[]))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_index_expr3(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = (a[b].c()) + 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='+', left=CallExpr(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), method=Id(name='c'), param=[]), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_index_expr3(self):
        input = """
            class Shape {
                static boolean getArea() {
                    boolean a = ((a[b].c()) + 2) > 2;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='BoolType', varInit=BinaryOp(op='>', left=BinaryOp(op='+', left=CallExpr(obj=FieldAccess(obj=Id(name='a'), fieldname=Id(name='b')), method=Id(name='c'), param=[]), right=IntLiteral(value=2)), right=IntLiteral(value=2)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_assign_integer(self):
        input = """
            class Shape {
                static boolean getArea() {
                    int a = 2e333333;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=FloatLiteral(value='2e333333'))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_assign_integer2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=FloatLiteral(value='2e333333'))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_assign_integer2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([[VarDecl(variable=Id(name='a'), varType='IntType', varInit=BinaryOp(op='*', left=FloatLiteral(value='2e333333'), right=IntLiteral(value=1)))]],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_comment_line(self):
        input = """
            class Shape {
                static boolean getArea() {
                    // int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_comment_line2(self):
        input = """
            class Shape {
                static boolean getArea() {
                    // int a = 2e333333 * 1;
                    // int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 394))


    def test_comment_line3(self):
        input = """
            class Shape {
                static boolean getArea() {
                    # int a = 2e333333 * 1;
                    # int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_comment_line4(self):
        input = """
            class Shape {
                static boolean getArea() {
                    // int a = 2e333333 * 1;
                    // int a = 2e333333 * 1;
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_comment_line5(self):
        input = """
            class Shape {
                static boolean getArea() {
                    /* int a = 2e333333 * 1;
                     int a = 2e333333 * 1; */
                }
            }
        """
        expect = str(Program([ClassDecl(Id('Shape'),[MethodDecl(Static(),Id('getArea'),[],BoolType(),Block([],[]))])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_empty_class(self):
        input = """
            class Shape {}
        """
        expect = str(Program([ClassDecl(Id('Shape'),[])]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_empty_class2(self):
        input = """
            class Shape {}
            class Square extends Shape {}
        """
        expect = str(Program([ClassDecl(Id('Shape'),[]),ClassDecl(Id('Square'),[])]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_empty_class3(self):
        input = """
            class Shape {}
            class Square extends Shape {}
            class Triangle extends Shape {}
        """
        expect = str(Program([ClassDecl(Id('Shape'),[]),ClassDecl(Id('Square'),[]),ClassDecl(Id('Triangle'),[])]))
        self.assertTrue(TestAST.test(input, expect, 400))