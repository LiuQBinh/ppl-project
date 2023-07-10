import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # def test_comment_1(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             // comment line
    #         """,
    #         """<EOF>""",
    #         901
    #     ))
    # def test_comment_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             # comment line
    #         """,
    #         """<EOF>""",
    #         902
    #     ))
    # def test_comment_3(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             /* comment line */
    #         """,
    #         """<EOF>""",
    #         903
    #     ))
    # def test_comment_4(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             /*
    #                 comment line
    #                 comment line
    #                 comment line
    #                 comment line
    #                 comment line
    #                 comment line
    #             */
    #         """,
    #         """<EOF>""",
    #         904
    #     ))
    # def test_id(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             id
    #         """,
    #         """id,<EOF>""",
    #         905
    #     ))
    # def test_list_id(self):
    #     self.assertTrue(TestLexer.test(
    #         """id1,id2""",
    #         """id1,,,id2,<EOF>""",
    #         906
    #     ))
    # def test_float(self):
    #     self.assertTrue(TestLexer.test(
    #         """a := 22233333e44534.34344e334343""",
    #         """a,:,=,22233333e44534,.,34344e334343,<EOF>""",
    #         907
    #     ))
    # def test_int(self):
    #     self.assertTrue(TestLexer.test(
    #         """a := 22233333e44534""",
    #         """a,:,=,22233333e44534,<EOF>""",
    #         908
    #     ))
    # def test_int_without_e(self):
    #     self.assertTrue(TestLexer.test(
    #         """a := 2223333344534""",
    #         """a,:,=,2223333344534,<EOF>""",
    #         910
    #     ))
    # def test_float_without_e(self):
    #     self.assertTrue(TestLexer.test(
    #         """a := 2223333344534.1111""",
    #         """a,:,=,2223333344534.1111,<EOF>""",
    #         911
    #     ))
    # def test_float_without_e(self):
    #     self.assertTrue(TestLexer.test(
    #         """a := 2223333344534.1111""",
    #         """a,:,=,2223333344534.1111,<EOF>""",
    #         912
    #     ))
    # def test_array_lexer(self):
    #     self.assertTrue(TestLexer.test(
    #         """array(array(1, 2), array(3, 4))""",
    #         """array,(,array,(,1,,,2,),,,array,(,3,,,4,),),<EOF>""",
    #         913
    #     ))
    # def test_adding_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc + def""",
    #         """abc,+,def,<EOF>""",
    #         914
    #     ))
    # def test_divide_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc / def""",
    #         """abc,/,def,<EOF>""",
    #         915
    #     ))
    # def test_time_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc * def""",
    #         """abc,*,def,<EOF>""",
    #         916
    #     ))
    # def test_div_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc % def""",
    #         """abc,%,def,<EOF>""",
    #         917
    #     ))
    # def test_larger_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc > def""",
    #         """abc,>,def,<EOF>""",
    #         918
    #     ))
    # def test_smaller_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc < def""",
    #         """abc,<,def,<EOF>""",
    #         919
    #     ))
    # def test_smaller_equal_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc <= def""",
    #         """abc,<=,def,<EOF>""",
    #         920
    #     ))
    # def test_larger_equal_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """abc >= def""",
    #         """abc,>=,def,<EOF>""",
    #         921
    #     ))
    # def test_member_access(self):
    #     self.assertTrue(TestLexer.test(
    #         """a.b.c""",
    #         """a,.,b,.,c,<EOF>""",
    #         922
    #     ))
    # def test_member_access(self):
    #     self.assertTrue(TestLexer.test(
    #         """a.b[cccc]""",
    #         """a,.,b,[,cccc,],<EOF>""",
    #         923
    #     ))
    # def test_negative_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """--1217892178""",
    #         """-,1217892178,<EOF>""",
    #         924
    #     ))
    # def test_negative_number(self):
    #     self.assertTrue(TestLexer.test(
    #         """-1217892178""",
    #         """-,1217892178,<EOF>""",
    #         925
    #     ))
    # def test_logic_exp_1(self):
    #     self.assertTrue(TestLexer.test(
    #         """(100 > 222) || (100 <= 222)""",
    #         """(,100,>,222,),||,(,100,<=,222,),<EOF>""",
    #         926
    #     ))
    # def test_logic_exp_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """(100 > 222) || ((100 <= 222) && (100 <= 222))""",
    #         """(,100,>,222,),||,(,(,100,<=,222,),&&,(,100,<=,222,),),<EOF>""",
    #         927
    #     ))
    # def test_logic_exp_3(self):
    #     self.assertTrue(TestLexer.test(
    #         """((1 + 2 + 3 + 4 + 5 + 6) * 23456) / 999""",
    #         """(,(,1,+,2,+,3,+,4,+,5,+,6,),*,23456,),/,999,<EOF>""",
    #         928
    #     ))
    # def test_logic_exp_4(self):
    #     self.assertTrue(TestLexer.test(
    #         """((1 + 2 + 3 + 4 + 5 + 6) * abcbcbcbcbcbcbbc) / 999""",
    #         """(,(,1,+,2,+,3,+,4,+,5,+,6,),*,abcbcbcbcbcbcbbc,),/,999,<EOF>""",
    #         929
    #     ))
    # def test_declare_class(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #         class Rectangle {
    #             float getArea() {
    #                 return this.length*this.width;
    #             }
    #         }
    #         """,
    #         """class,Rectangle,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         930
    #     ))
    # def test_declare_class_with_attributes(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Shape {
    #                 int numOfShape = 0;
    #             }
    #         """,
    #         """class,Shape,{,int,numOfShape,=,0,;,},<EOF>""",
    #         931
    #     ))
    # def test_declare_class_with_attributes_final(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Shape {
    #                 final int numOfShape = 0;
    #             }
    #         """,
    #         """class,Shape,{,final,int,numOfShape,=,0,;,},<EOF>""",
    #         932
    #     ))
    # def test_declare_class_with_attributes_final(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Shape {
    #                 final int numOfShape = 0;
    #             }
    #         """,
    #         """class,Shape,{,final,int,numOfShape,=,0,;,},<EOF>""",
    #         933
    #     ))
    #
    # def test_declare_class_with_attributes_static_and_final(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Shape {
    #                 static final int numOfShape = 0;
    #             }
    #         """,
    #         """class,Shape,{,static,final,int,numOfShape,=,0,;,},<EOF>""",
    #         934
    #     ))
    #
    # def test_declare_class_with_attributes_static_and_final_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Shape {
    #                 static final int numOfShape = 0;
    #                 static final int numOfShape = 0;
    #             }
    #         """,
    #         """class,Shape,{,static,final,int,numOfShape,=,0,;,static,final,int,numOfShape,=,0,;,},<EOF>""",
    #         935
    #     ))
    #
    # def test_declare_class_with_method(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Rectangle {
    #                 float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """,
    #         """class,Rectangle,{,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         936
    #     ))
    #
    # def test_declare_class_with_method_final(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Rectangle {
    #                 final float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """,
    #         """class,Rectangle,{,final,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         937
    #     ))
    #
    # def test_declare_class_with_method_static(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Rectangle {
    #                 static float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """,
    #         """class,Rectangle,{,static,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         938
    #     ))
    #
    # def test_declare_class_with_method_final_static(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Rectangle {
    #                 static final float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """,
    #         """class,Rectangle,{,static,final,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         939
    #     ))
    #
    # def test_declare_class_with_method_final_static_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             class Rectangle {
    #                 static final float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #             class Rectangle2 {
    #                 static final float getArea() {
    #                     return this.length*this.width;
    #                 }
    #             }
    #         """,
    #         """class,Rectangle,{,static,final,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},class,Rectangle2,{,static,final,float,getArea,(,),{,return,this,.,length,*,this,.,width,;,},},<EOF>""",
    #         940
    #     ))
    #
    # def test_for_loop_1(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 to 12121 do {
    #                 a := 1;
    #             }
    #         """,
    #         """for,i,:,=,2232,to,12121,do,{,a,:,=,1,;,},<EOF>""",
    #         941
    #     ))
    # def test_for_loop_2(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 a := 1;
    #             }
    #         """,
    #         """for,i,:,=,2232,to,12121,do,{,a,:,=,1,;,},<EOF>""",
    #         942
    #     ))
    # def test_for_if(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 a := 1;
    #                 if a > 2 then {
    #                     a := 111;
    #                 }
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,a,:,=,1,;,if,a,>,2,then,{,a,:,=,111,;,},},<EOF>""",
    #         943
    #     ))
    # def test_else(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             if a > 2 then {
    #                 a := 111;
    #             } else then {
    #                 a := 222;
    #             }
    #         """,
    #         """if,a,>,2,then,{,a,:,=,111,;,},else,then,{,a,:,=,222,;,},<EOF>""",
    #         944
    #     ))
    # def test_else_if(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             if a > 2 then {
    #                 a := 111;
    #             } elseif a < -1 then {
    #                 a := 000;
    #             } else then {
    #                 a := 222;
    #             }
    #         """,
    #         """if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,then,{,a,:,=,000,;,},else,then,{,a,:,=,222,;,},<EOF>""",
    #         945
    #     ))
    # def test_else_if_for(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 if a > 2 then {
    #                     a := 111;
    #                 } elseif a < -1 {
    #                     a := 000;
    #                 } else {
    #                     a := 222;
    #                 }
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},},<EOF>""",
    #         947
    #     ))
    # def test_invocation(self):
    #     self.assertTrue(TestLexer.test(
    #         """id.write(aa);""",
    #         """id,.,write,(,aa,),;,<EOF>""",
    #         948
    #     ))
    # def test_for_and_break(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 id.write(aa);
    #                 break;
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,id,.,write,(,aa,),;,break,;,},<EOF>""",
    #         949
    #     ))
    # def test_for_and_return(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 id.write(aa);
    #                 return;
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,id,.,write,(,aa,),;,return,;,},<EOF>""",
    #         950
    #     ))
    # def test_for_and_return_and_if(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 if a > 2 then {
    #                     a := 111;
    #                 }
    #                 id.write(aa);
    #                 return;
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},id,.,write,(,aa,),;,return,;,},<EOF>""",
    #         951
    #     ))
    # def test_for_and_return_and_if_else(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 if a > 2 then {
    #                     a := 111;
    #                 } else {
    #                     a := 000;
    #                 }
    #                 id.write(aa);
    #                 return;
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},else,{,a,:,=,000,;,},id,.,write,(,aa,),;,return,;,},<EOF>""",
    #         952
    #     ))
    # def test_for_and_return_and_if_elseif_else(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             for i:=2232 downto 12121 do {
    #                 if a > 2 then {
    #                     a := 111;
    #                 } elseif a < -1 {
    #                     a := 000;
    #                 } else {
    #                     a := 222;
    #                 }
    #                 id.write(aa);
    #                 return;
    #             }
    #         """,
    #         """for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},id,.,write,(,aa,),;,return,;,},<EOF>""",
    #         953
    #     ))
    # def test_for_and_return_and_if_elseif_else_block(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             {
    #                 for i:=2232 downto 12121 do {
    #                     if a > 2 then {
    #                         a := 111;
    #                     } elseif a < -1 {
    #                         a := 000;
    #                     } else {
    #                         a := 222;
    #                     }
    #                     id.write(aa);
    #                     return;
    #                 }
    #             }
    #         """,
    #         """{,for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},id,.,write,(,aa,),;,return,;,},},<EOF>""",
    #         954
    #     ))
    # def test_for_and_return_and_if_elseif_else_block_list(self):
    #     self.assertTrue(TestLexer.test(
    #         """
    #             {
    #                 for i:=2232 downto 12121 do {
    #                     if a > 2 then {
    #                         a := 111;
    #                     } elseif a < -1 {
    #                         a := 000;
    #                     } else {
    #                         a := 222;
    #                     }
    #                     id.write(aa);
    #                     return;
    #                 }
    #             }
    #             {
    #                 for i:=2232 downto 12121 do {
    #                     if a > 2 then {
    #                         a := 111;
    #                     } elseif a < -1 {
    #                         a := 000;
    #                     } else {
    #                         a := 222;
    #                     }
    #                     id.write(aa);
    #                     return;
    #                 }
    #             }
    #             {
    #                 for i:=2232 downto 12121 do {
    #                     if a > 2 then {
    #                         a := 111;
    #                     } elseif a < -1 {
    #                         a := 000;
    #                     } else {
    #                         a := 222;
    #                     }
    #                     id.write(aa);
    #                     return;
    #                 }
    #             }
    #         """,
    #         """{,for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},id,.,write,(,aa,),;,return,;,},},{,for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},id,.,write,(,aa,),;,return,;,},},{,for,i,:,=,2232,downto,12121,do,{,if,a,>,2,then,{,a,:,=,111,;,},elseif,a,<,-,1,{,a,:,=,000,;,},else,{,a,:,=,222,;,},id,.,write,(,aa,),;,return,;,},},<EOF>""",
    #         954
    #     ))
    #     def test_assign_variable_1(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c * d * e * f
    #             """,
    #             """a,:,=,c,*,d,*,e,*,f,<EOF>""",
    #             955
    #         ))
    #     def test_assign_variable_2(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c + d + e + f
    #             """,
    #             """a,:,=,c,+,d,+,e,+,f,<EOF>""",
    #             956
    #         ))
    #     def test_assign_variable_3(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c / d / e / f
    #             """,
    #             """a,:,=,c,/,d,/,e,/,f,<EOF>""",
    #             957
    #         ))
    #     def test_assign_variable_4(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c % d % e % f
    #             """,
    #             """a,:,=,c,%,d,%,e,%,f,<EOF>""",
    #             958
    #         ))
    #     def test_assign_variable_5(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c - d - e - f
    #             """,
    #             """a,:,=,c,%,d,%,e,%,f,<EOF>""",
    #             959
    #         ))
    #     def test_assign_variable_6(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c * (e + f)
    #             """,
    #             """a,:,=,c,%,d,%,e,%,f,<EOF>""",
    #             960
    #         ))
    #     def test_assign_variable_7(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a: = c * (e + f) + 100
    #             """,
    #             """a,:,=,c,*,(,e,+,f,),+,100,<EOF>""",
    #             961
    #         ))
    #     def test_assign_variable_8(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 a:= c * (e + f) + 100 / 100101101010
    #             """,
    #             """a,:,=,c,*,(,e,+,f,),+,100,/,100101101010,<EOF>""",
    #             962
    #         ))
    #     def test_declare_variable_float(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 float a;
    #             """,
    #             """float,a,;,<EOF>""",
    #             963
    #         ))
    #     def test_declare_variable_array_int(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 int[] a;
    #             """,
    #             """int,[,],a,;,<EOF>""",
    #             964
    #         ))
    #     def test_declare_variable_array_float(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 float[] a;
    #             """,
    #             """float,[,],a,;,<EOF>""",
    #             965
    #         ))
    #     def test_declare_variable_array_string(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 string[] a;
    #             """,
    #             """string,[,],a,;,<EOF>""",
    #             966
    #         ))
    #     def test_concat_string_1(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 "abc" + "def"
    #             """,
    #             """abc,+,def,<EOF>""",
    #             967
    #         ))
    #     def test_concat_string_2(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 "abc" + 123
    #             """,
    #             """abc,+,123,<EOF>""",
    #             968
    #         ))
    #     def test_concat_string_2(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 "abc" + 123
    #             """,
    #             """abc,+,123,<EOF>""",
    #             969
    #         ))
    #     def test_declare_list_variable_string(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 string a, b, c, d, e;
    #             """,
    #             """string,a,,,b,,,c,,,d,,,e,;,<EOF>""",
    #             970
    #         ))
    #     def test_declare_list_variable_int(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 int a, b, c, d, e;
    #             """,
    #             """int,a,,,b,,,c,,,d,,,e,;,<EOF>""",
    #             971
    #         ))
    #     def test_declare_list_variable_float(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 float[] a, b, c, d, e;
    #             """,
    #             """float,[,],a,,,b,,,c,,,d,,,e,;,<EOF>""",
    #             972
    #         ))
    #     def test_declare_list_variable_string_array(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 string[] a, b, c, d, e;
    #             """,
    #             """string,[,],a,,,b,,,c,,,d,,,e,;,<EOF>""",
    #             973
    #         ))
    #     def test_declare_list_variable_int_array(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 int a, b, c, d, e;
    #             """,
    #             """int,a,,,b,,,c,,,d,,,e,;,<EOF>""",
    #             974
    #         ))
    #     def test_declare_list_variable_int_array_and_loop(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 for i:=2232 to 12121 do {
    #                     int[] a, b, c, d, e;
    #                 }
    #             """,
    #             """for,i,:,=,2232,to,12121,do,{,int,[,],a,,,b,,,c,,,d,,,e,;,},<EOF>""",
    #             975
    #         ))
    #     def test_declare_list_variable_int_array_and_loop_if(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 if(i > 2) then {
    #                     for i:=2232 to 12121 do {
    #                         int[] a, b, c, d, e;
    #                     }
    #                 }
    #             """,
    #             """if,(,i,>,2,),then,{,for,i,:,=,2232,to,12121,do,{,int,[,],a,,,b,,,c,,,d,,,e,;,},},<EOF>""",
    #             976
    #         ))
    #     def test_complex_expression(self):
    #         self.assertTrue(TestLexer.test(
    #             """((a + b + c) / (a * b * c)) + ((a + b + c) / (a * b * c))""",
    #             """(,(,a,+,b,+,c,),/,(,a,*,b,*,c,),),+,(,(,a,+,b,+,c,),/,(,a,*,b,*,c,),),<EOF>""",
    #             977
    #         ))
    #     def test_return_normal(self):
    #         self.assertTrue(TestLexer.test(
    #             """return 1;""",
    #             """return,1,;,<EOF>""",
    #             978
    #         ))
    #     def test_return_complex_expression(self):
    #         self.assertTrue(TestLexer.test(
    #             """return ((a + b + c) / (a * b * c)) + ((a + b + c) / (a * b * c));""",
    #             """return,(,(,a,+,b,+,c,),/,(,a,*,b,*,c,),),+,(,(,a,+,b,+,c,),/,(,a,*,b,*,c,),),;,<EOF>""",
    #             979
    #         ))
    #     def test_return_invoke_function(self):
    #         self.assertTrue(TestLexer.test(
    #             """return sqrt(this.length + this.width);""",
    #             """return,sqrt,(,this,.,length,+,this,.,width,),;,<EOF>""",
    #             980
    #         ))
    #     def test_invoke_function(self):
    #         self.assertTrue(TestLexer.test(
    #             """sqrt(this.length + this.width);""",
    #             """return,sqrt,(,this,.,length,+,this,.,width,),;,<EOF>""",
    #             981
    #         ))
    #     def test_new_val_from_class(self):
    #         self.assertTrue(TestLexer.test(
    #             """new Shape(1, 2);""",
    #             """new,Shape,(,1,,,2,),;,<EOF>""",
    #             982
    #         ))
    #     def test_assign_from_new_val_class(self):
    #         self.assertTrue(TestLexer.test(
    #             """a := new Shape(1, 2);""",
    #             """a,:,=,new,Shape,(,1,,,2,),;,<EOF>""",
    #             983
    #         ))
    #     def test_assign_from_new_val_class_with_no_params(self):
    #         self.assertTrue(TestLexer.test(
    #             """a := new Shape();""",
    #             """a,:,=,new,Shape,(,),;,<EOF>""",
    #             984
    #         ))
    #     def test_declare_var_boolean(self):
    #         self.assertTrue(TestLexer.test(
    #             """boolean a;""",
    #             """boolean,a,;,<EOF>""",
    #             985
    #         ))
    #     def test_declare_var_boolean_array(self):
    #         self.assertTrue(TestLexer.test(
    #             """boolean[] a;""",
    #             """boolean,[,],a,;,<EOF>""",
    #             986
    #         ))
    #     def test_declare_var_boolean_array_and_comment_1(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 // variable a
    #                 boolean[] a;
    #             """,
    #             """boolean,[,],a,;,<EOF>""",
    #             987
    #         ))
    #     def test_declare_var_boolean_array_and_comment_2(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 # variable a
    #                 boolean[] a;
    #             """,
    #             """boolean,[,],a,;,<EOF>""",
    #             988
    #         ))
    #     def test_declare_var_boolean_array_and_comment_3(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 /* variable a */
    #                 boolean[] a;
    #             """,
    #             """boolean,[,],a,;,<EOF>""",
    #             989
    #         ))
    #     def test_declare_var_boolean_array_and_comment_3_error(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 /* variable a
    #                 boolean[] a;
    #             """,
    #             """/,*,variable,a,boolean,[,],a,;,<EOF>""",
    #             990
    #         ))
    #     def test_declare_var_boolean_array_and_comment_1_err(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 / variable a
    #                 boolean[] a;
    #             """,
    #             """/,variable,a,boolean,[,],a,;,<EOF>""",
    #             991
    #         ))
    #     def test_declare_var_boolean_array_and_comment_1_err(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 / variable a
    #                 boolean[] a;
    #             """,
    #             """/,variable,a,boolean,[,],a,;,<EOF>""",
    #             992
    #         ))
    #     def test_loop_and_invocation(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 for i:=2232 to 12121 do {
    #                     sqrt(this.length + this.width);
    #                 }
    #             """,
    #             """for,i,:,=,2232,to,12121,do,{,sqrt,(,this,.,length,+,this,.,width,),;,},<EOF>""",
    #             993
    #         ))
    #     def test_nested_invocation(self):
    #         self.assertTrue(TestLexer.test(
    #             """sqrt(sqrt(this.length + this.width));""",
    #             """sqrt,(,sqrt,(,this,.,length,+,this,.,width,),),;,<EOF>""",
    #             995
    #         ))
    #     def test_if_invocation(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 }
    #             """,
    #             """if,(,i,>,2,),then,{,sqrt,(,sqrt,(,this,.,length,+,this,.,width,),),;,},<EOF>""",
    #             996
    #         ))
    #     def test_if_else_invocation(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 } else {
    #                     return;
    #                 }
    #             """,
    #             """if,(,i,>,2,),then,{,sqrt,(,sqrt,(,this,.,length,+,this,.,width,),),;,},else,{,return,;,},<EOF>""",
    #             997
    #         ))
    #     def test_if_else_invocation_and_loop(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 if(i > 2) then {
    #                     sqrt(sqrt(this.length + this.width));
    #                 } else {
    #                     for i:=2232 to 12121 do {
    #                         sqrt(this.length + this.width);
    #                     }
    #                     return;
    #                 }
    #             """,
    #             """if,(,i,>,2,),then,{,sqrt,(,sqrt,(,this,.,length,+,this,.,width,),),;,},else,{,for,i,:,=,2232,to,12121,do,{,sqrt,(,this,.,length,+,this,.,width,),;,},return,;,},<EOF>""",
    #             998
    #         ))
    #     def test_if_else_invocation_and_loop_in_block(self):
    #         self.assertTrue(TestLexer.test(
    #             """
    #                 {
    #                     if(i > 2) then {
    #                         sqrt(sqrt(this.length + this.width));
    #                     } else {
    #                         for i:=2232 to 12121 do {
    #                             sqrt(this.length + this.width);
    #                         }
    #                         return;
    #                     }
    #                 }
    #             """,
    #             """{,if,(,i,>,2,),then,{,sqrt,(,sqrt,(,this,.,length,+,this,.,width,),),;,},else,{,for,i,:,=,2232,to,12121,do,{,sqrt,(,this,.,length,+,this,.,width,),;,},return,;,},},<EOF>""",
    #             999
    #         ))
        def test_if_invocation(self):
            TestLexer.test(
                """abc?svn""",
                """abc,<EOF>""",
                1000
            )
