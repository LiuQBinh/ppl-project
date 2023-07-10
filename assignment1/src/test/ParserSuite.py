import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #Test Class decl
    # def test_class_decl1(self):
    #     input = """class Shape {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,801))
    # def test_class_decl2(self):
    #     input = """
    #         class Shape1 {}
    #         class Shape2 {}
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,802))
    # def test_class_decl_1method(self):
    #     input = """
    #         class Shape1 {
    #             getArea() {
    #                 return self.length * self.width;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,803))
    # def test_class_decl_1method_1atrribute(self):
    #     input = """
    #         class Shape1 {
    #             static final int numOfShape = 0;
    #             getArea() {
    #                 return self.length * self.width;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,804))
    # def test_class_decl_final_method(self):
    #     input = """
    #         class Shape1 {
    #             final float getArea() {
    #                 return this.length*this.width;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,805))
    # def test_class_decl_static_method(self):
    #     input = """
    #         class Shape1 {
    #             static float getArea() {
    #                 return this.length*this.width;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,806))
    # def test_class_decl_static_1atrribute(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,807))
    # def test_class_decl_static_2atrribute(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int color = 0;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,808))
    # def test_class_decl_static_final_atrribute(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,809))
    # def test_class_decl_static_final_atrribute_error(self):
    #     input = """
    #         class Shape {
    #             final static int numOfShape = 0;
    #         }
    #     """
    #     expect = "Error on line 3 col 22: static"
    #     self.assertTrue(TestParser.test(input,expect,810))
    # def test_class_decl_method_attribute(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #                 return this.length*this.width;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,811))
    # def test_class_decl_method_with_loop(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #               for i:=2232 to 12121 do {
    #                   a := 1;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,812))
    # def test_class_decl_method_with_loop_downto(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   a := 1;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,813))
    # def test_class_decl_method_with_loop_downto_if_inside(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
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
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,814))
    # def test_class_decl_method_with_loop_downto_if_outside(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #               if a > 2 then {
    #                   a := 111;
    #               }
    #               for i:=2232 downto 12121 do {
    #                   a := 1;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,815))
    #     def test_class_decl_method_with_loop_downto_inside_if(self):
    #         input = """
    #             class Shape {
    #                 static final int numOfShape = 0;
    #                 static float getArea() {
    #                   if a > 2 then {
    #                       a := 111;
    #                       for i:=2232 downto 12121 do {
    #                           a := 1;
    #                       }
    #                   }
    #                 }
    #             }
    #         """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 816))
    #     def test_class_decl_method_with_loop_downto_inside_if2(self):
    #         input = """
    #             class Shape {
    #                 static final int numOfShape = 0;
    #                 static float getArea() {
    #                     if a > 2 then {
    #                         a := 111;
    #                         for i:=2232 downto 12121 do {
    #                             a := 1;
    #                             if a > 2 then {
    #                                 a := 111;
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 817))
    #     def test_class_decl_method_with_loop_downto_inside_if2(self):
    #         input = """
    #             class Shape {
    #                 static final int numOfShape = 0;
    #                 static float getArea() {
    #                     if a > 2 then {
    #                         a := 111;
    #                         for i:=2232 downto 12121 do {
    #                             a := 1;
    #                             if a > 2 then {
    #                                 a := 111;
    #                             }
    #                         }
    #                     }
    #                 }
    #                 static float getArea2() {
    #                     if a > 2 then {
    #                         a := 111;
    #                         for i:=2232 downto 12121 do {
    #                             a := 1;
    #                             if a > 2 then {
    #                                 a := 111;
    #                             }
    #                         }
    #                     }
    #                 }
    #             }
    #         """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 818))

    # def test_class_decl_method_with_declare_var(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #                 int a := 1;
    #                 if a > 2 then {
    #                     a := 111;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 819))
    # def test_class_decl_method_with_declare_var_in_if(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static float getArea() {
    #                 if a > 2 then {
    #                     int a := 1;
    #                     a := 111;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 820))
    # def test_class_decl_2method_2atribute(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 if a > 2 then {
    #                     int a := 1;
    #                     a := 111;
    #                 }
    #             }
    #             static float getArea2() {
    #                 if a > 2 then {
    #                     int a := 1;
    #                     a := 111;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 821))
    # def test_if_else_invocation_and_loop_in_block(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 } else {
    #                     for i:=2232 to 12121 do {
    #                         sqrt(this.length + this.width);
    #                     }
    #                     return;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 822))
    # def test_if_else_invocation_and_loop(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               if(i > 2) then {
    #                   sqrt(sqrt(this.length + this.width));
    #               } else {
    #                   for i:=2232 to 12121 do {
    #                       sqrt(this.length + this.width);
    #                   }
    #                   return;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 823))
    # def test_if_else_invocation(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                if(i > 2) then {
    #                    sqrt(sqrt(this.length + this.width));
    #                } else {
    #                    return;
    #                }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 824))
    # def test_if_else_invocation_and_loop(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 } else {
    #                     for i:=2232 to 12121 do {
    #                         sqrt(this.length + this.width);
    #                     }
    #                     return;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 825))
    # def test_if_invocation(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 826))
    # def test_nested_invocation(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 sqrt(sqrt(this.length + this.width));
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 827))
    # def test_loop_and_invocation(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 for i:=2232 to 12121 do {
    #                     sqrt(this.length + this.width);
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 828))
    # def test_declare_var_boolean_array_and_comment_1_err(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   / variable a
    #                   boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "Error on line 6 col 22: /"
    #     self.assertTrue(TestParser.test(input, expect, 829))
    # def test_declare_var_boolean_array_and_comment_3_error(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   /* variable a
    #                   boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "Error on line 6 col 22: /"
    #     self.assertTrue(TestParser.test(input, expect, 830))
    # def test_declare_var_boolean_array_and_comment_3(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 /* variable a */
    #                 boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 831))
    # def test_declare_var_boolean_array_and_comment_2(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 # variable a
    #                 boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 832))
    # def test_declare_var_boolean_array_and_comment_1(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 // variable a
    #                 boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 833))
    # def test_declare_var_boolean_array(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 boolean[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 834))
    # def test_declare_var_boolean(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 boolean a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 835))
    # def test_assign_from_new_val_class_with_no_params(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 a := new Shape();
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 836))
    # def test_assign_from_new_val_class(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 a := new Shape(1, 2);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 837))
    # def test_new_val_from_class(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 new Shape(1, 2);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 838))
    # def test_invoke_function(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                sqrt(this.length + this.width);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 839))
    # def test_return_invoke_function(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                return sqrt(this.length + this.width);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 840))
    # def test_return_complex_expression(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                return ((a + b + c) / (a * b * c)) + ((a + b + c) / (a * b * c));
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 841))
    # def test_return_normal(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                return 1;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 842))
    # def test_complex_expression(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                a := ((a + b + c) / (a * b * c)) + ((a + b + c) / (a * b * c));
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 843))
    # def test_declare_list_variable_int_array_and_loop_if(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   if(i > 2) then {
    #                       for i:=2232 to 12121 do {
    #                           int[] a, b, c, d, e;
    #                       }
    #                   }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 844))
    # def test_declare_list_variable_int_array_and_loop(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   for i:=2232 to 12121 do {
    #                       int[] a, b, c, d, e;
    #                   }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 845))
    # def test_declare_list_variable_int_array(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 int a, b, c, d, e;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 846))
    # def test_declare_list_variable_string_array(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 string[] a, b, c, d, e;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 847))
    # def test_declare_list_variable_float(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 float[] a, b, c, d, e;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 848))
    # def test_declare_list_variable_int(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 int a, b, c, d, e;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 849))
    # def test_declare_list_variable_string(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 string a, b, c, d, e;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 850))
    # def test_concat_string_2(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                a := "abc" + 123;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 851))
    # def test_concat_string_1(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                a := "abc" + "def";
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 852))
    # def test_declare_variable_array_float(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                float[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 853))
    # def test_declare_variable_array_int(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                int[] a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 854))
    # def test_declare_variable_float(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                float a;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 855))
    # def test_assign_variable_8(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                a:= c * (e + f) + 100 / 100101101010;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 856))
    # def test_assign_variable_7(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a: = c * (e + f) + 100;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 857))
    # def test_assign_variable_6(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c * (e + f);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 858))
    # def test_assign_variable_5(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c - d - e - f;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 859))
    # def test_assign_variable_4(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c % d % e % f;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 860))
    # def test_assign_variable_3(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c / d / e / f;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 861))
    # def test_assign_variable_2(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c + d + e + f;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 862))
    # def test_assign_variable_1(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               a:= c * d * e * f;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 863))
    # def test_for_and_return_and_if_elseif_else_block_list(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   for i:=2232 downto 12121 do {
    #                       if a > 2 then {
    #                           a := 111;
    #                       } elseif a < -1 {
    #                           a := 000;
    #                       } else {
    #                           a := 222;
    #                       }
    #                       id.write(aa);
    #                       return;
    #                   }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 864))
    # def test_for_and_return_and_if_elseif_else_block_and_comment(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                   # for i:=2232 downto 12121 do {
    #                   #     if a > 2 then {
    #                   #         a := 111;
    #                   #     } elseif a < -1 {
    #                   #         a := 000;
    #                   #     } else {
    #                   #         a := 222;
    #                   #     }
    #                   #     id.write(aa);
    #                   #     return;
    #                   # }
    #                   for i:=2232 downto 12121 do {
    #                       if a > 2 then {
    #                           a := 111;
    #                       } elseif a < -1 {
    #                           a := 000;
    #                       } else {
    #                           a := 222;
    #                       }
    #                       id.write(aa);
    #                       return;
    #                   }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 865))
    # def test_for_and_return_and_if_elseif_else2(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   if a > 2 then {
    #                       a := 111;
    #                   } elseif a < -1 {
    #                       a := 000;
    #                   } else {
    #                       a := 222;
    #                   }
    #                   id.write(aa);
    #               }
    #               return;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 866))
    # def test_for_and_return_and_if_else(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   if a > 2 then {
    #                       a := 111;
    #                   } else {
    #                       a := 000;
    #                   }
    #                   id.write(aa);
    #                   return;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 867))
    # def test_for_and_return_and_if(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   if a > 2 then {
    #                       a := 111;
    #                   }
    #                   id.write(aa);
    #                   return;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 868))
    # def test_for_and_return(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   id.write(aa);
    #                   return;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 869))
    # def test_for_and_break(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   id.write(aa);
    #                   break;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 870))
    # def test_invocation(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 id.write(aa);
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 871))
    # def test_else_if_for(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               for i:=2232 downto 12121 do {
    #                   if a > 2 then {
    #                       a := 111;
    #                   } elseif a < -1 {
    #                       a := 000;
    #                   } else {
    #                       a := 222;
    #                   }
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 872))
    # def test_else_if_error(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               if a > 2 then {
    #                   a := 111;
    #               } elseif a < -1 then {
    #                   a := 000;
    #               } else then {
    #                   a := 222;
    #               }
    #             }
    #         }
    #     """
    #     expect = "Error on line 8 col 34: then"
    #     self.assertTrue(TestParser.test(input, expect, 873))
    # def test_else(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #               if a > 2 then {
    #                   a := 111;
    #               } else {
    #                   a := 222;
    #               }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 874))
    # def test_for_if(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
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
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 875))
    # def test_for_loop_2(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 for i:=2232 downto 12121 do {
    #                     a := 1;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 876))
    # def test_for_loop_1(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 for i:=2232 to 12121 do {
    #                     a := 1;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 877))
    # def test_for_2loop_1(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 for i:=2232 to 12121 do {
    #                     a := 1;
    #                 }
    #                 for i:=2232 to 12121 do {
    #                     a := 1;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 878))
    # def test_for_2loop_1_error(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static final int numOfShape2 = 0;
    #             static float getArea() {
    #                 for i:=2232 to 12121 do {
    #                     a := 1;
    #                 }
    #                 for i:=2232 to 12121 do {
    #                     a := 1
    #                 }
    #             }
    #         }
    #     """
    #     expect = "Error on line 11 col 20: }"
    #     self.assertTrue(TestParser.test(input, expect, 879))
    # def test_declare_class_with_method_final_static_2_error(self):
    #     input = """
    #         class Shape {
    #             static final int numOfShape = 0;
    #             static finaaaaaaaal int numOfShape2 = 0;
    #         }
    #     """
    #     expect = "Error on line 4 col 23: finaaaaaaaal"
    #     self.assertTrue(TestParser.test(input, expect, 880))
    # def test_declare_class_with_method_final_static_error(self):
    #     input = """
    #         class Shape {
    #             return this.length*this.width
    #         }
    #     """
    #     expect = "Error on line 3 col 16: return"
    #     self.assertTrue(TestParser.test(input, expect, 881))
    # def test_declare_class_with_method_static(self):
    #     input = """
    #         class Shape {
    #           static float getArea() {
    #               return this.length*this.width;
    #           }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 882))
    # def test_declare_class_with_method_final_error(self):
    #     input = """
    #         class Shape {
    #           final float getArea() {
    #               return this.length*this.width
    #           }
    #         }
    #     """
    #     expect = "Error on line 5 col 14: }"
    #     self.assertTrue(TestParser.test(input, expect, 883))

    def test_declare_class_with_method_normal(self):
        input = """
            class Shape {
              float getArea() {
                  return this.length*this.width
              }
            }
        """
        expect = "Error on line 5 col 14: }"
        self.assertTrue(TestParser.test(input, expect, 884))
    def test_declare_class_with_attributes_static_and_final(self):
        input = """
            class Shape {
              static final int numOfShape = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 885))
    def test_declare_class_with_attributes_final(self):
        input = """
            class Shape {
              final int numOfShape = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 886))
    def test_declare_class_with_attributes_static(self):
        input = """
            class Shape {
              static int numOfShape = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 887))
    def test_declare_class_with_attributes(self):
        input = """
            class Shape {
              int numOfShape = 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 888))
    def test_declare_class(self):
        input = """
            class Shape {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 889))
    def test_declare_class_extends(self):
        input = """
            class Shape extends A {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 889))
    def test_logic_exp_4(self):
        input = """
            class Shape {
                static float getArea() {
                    return ((1 + 2 + 3 + 4 + 5 + 6) * abcbcbcbcbcbcbbc) / 999;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 890))
    def test_logic_exp_3(self):
        input = """
            class Shape {
                static float getArea() {
                    return ((1 + 2 + 3 + 4 + 5 + 6) * 23456) / 999;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 890))
    def test_logic_exp_2(self):
        input = """
            class Shape {
                static float getArea() {
                    return (100 > 222) || ((100 <= 222) && (100 <= 222));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 890))
    def test_logic_exp_1(self):
        input = """
            class Shape {
                static float getArea() {
                    return (100 > 222) || (100 <= 222);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 890))
    def test_negative_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return -1217892178;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 891))
    def test_negative_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return --1217892178;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 892))
    def test_member_access(self):
        input = """
            class Shape {
                static float getArea() {
                    return a.b[cccc];
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 893))
    def test_larger_equal_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc >= def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 894))
    def test_smaller_equal_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc <= def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 894))
    def test_larger_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc > def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 895))
    def test_div_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc % def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 896))
    def test_time_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc * def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 897))
    def test_divide_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc / def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 898))
    def test_adding_number(self):
        input = """
            class Shape {
                static float getArea() {
                    return abc + def;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 899))
    def test_array(self):
        input = """
            class Shape {
                static float getArea() {
                    return array(array(1, 2), array(3, 4));
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 8999))
