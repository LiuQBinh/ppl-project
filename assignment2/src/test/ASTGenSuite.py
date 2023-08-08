import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: class main {} """
    #     input = """class main {}"""
    #     expect = str(Program([ClassDecl(Id("main"),[])]))
    #     self.assertTrue(TestAST.test(input,expect,300))

    # def test_class_with_one_decl_program(self):
    #     """More complex program"""
    #     input = """class test {
    #         Shape a, b;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("test"),[AttributeDecl(Instance(),VarDecl(Id("a,b"),ClassType('Shape')))])]))
    #     self.assertTrue(TestAST.test(input,expect,301))

    # def test_class_with_two_decl_program(self):
    #     """More complex program"""
    #     input = """class main {
    #         int a;
    #         int b;
    #     }"""
    #     expect = str(Program([ClassDecl(Id("main"),
    #         [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
    #          AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
    #     self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_methods(self):
        """More complex program"""
        input = """class Shape {
            static float getArea() {
                sqrt(this.length + this.width);
            }
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
   