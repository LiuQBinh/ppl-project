/**
*   Student's Name: Luu Quoc Binh
*   Student's ID: 2033009
**/

grammar BKOOL;
@lexer::header {
    from lexererr import *
}

options{
	language=Python3;
}
program: (class_decl+ EOF); // the ID for cheat bkel
// ---------------------------------- MY PATH START
// class declaration _ start
class_decl: Class_word class_name (Extends_word class_name)? LB member_lists* RB;
class_name: ID | Prog_word | CLASS | Main_word;
//Ex:
//   class Rectangle extends Shape {
//       float length, width = 2.2222;
//       float height = 2.2222;
//       boolean isHaveBackground = false;
//       float getArea() {
//           return this.length*this.width;
//       }
//   }
Class_word: CLASS;
Prog_word: PROGRAM;
Extends_word: EXTENDS;
member_lists: attributes | methods | instructor;
instructor: class_name LP (paramlist)? RP block_stmt;
methods: class_props_kind methods_return_types methods_name LP (paramlist)? RP block_stmt;
methods_name: (ID|Main_word);
methods_return_types: types|Void_word;

class_props_kind: (Static_word)? (Final_word)?;
attributes: class_props_kind types attribute_as (COMA attribute_as)* SEMI;
attribute_as: ID ((Colon Assign_op)|Assign_op) attribute_as_val;
attribute_as_val: expr|new_val_from_class_stmt|invocation_stmt;

// class declaration _ end

//-------------------------------------------------------
//This is praser rules for block stmts
block_stmt: (block_stmt_list) | (LB block_stmt_list* RB);
block_stmt_list: (stmt | delc); //including stmts and variables/constants declaration

//Rules for variables/constants
delc: cons_decl | var_decl;
cons_decl: Final_word paramlist SEMI;
var_decl: paramlist SEMI;
Static_word: STATIC;
Final_word: FINAL;
Void_word: VOID;

//All type of stmts
stmt: as_stmt | if_stmt | loop_for_stmt | break_stmt | return_stmt | invocation_stmt;
as_stmt: index_expr (Colon Assign_op) (expr|new_val_from_class_stmt|invocation_stmt) SEMI; // Assignmet stmt
new_val_from_class_stmt: Keyword_new class_name LP expr_list? RP;
Keyword_new: KEYWORD_NEW;

//If stmt
if_stmt: (If_word expr Then_word block_stmt) elseif_stmt;
elseif_stmt: (Elseif_word  expr block_stmt)* else_stmt?;
else_stmt: (Else_word block_stmt);
If_word: IF;
Then_word: THEN;
Else_word: ELSE;
Elseif_word: ELSEIF;

//Loop (For) stmt
loop_for_stmt: For_word (ID Colon Assign_op expr) (To_word|Down_to_word) (expr) Do_word block_stmt;
For_word: FOR;
Assign_op: ASSIGN_OP;
To_word: TO;
Do_word: DO;
Down_to_word: DOWNTO;

//Instance/static (member_access_in/member_access_out) method invocation
invocation_stmt: ID LP (invocation_stmt_params (COMA invocation_stmt_params)*)? RP SEMI?;
invocation_stmt_params: expr|invocation_stmt;

//Look at the names => rules
break_stmt: Break_word SEMI;
Break_word: BREAK;

// RETURN STMT
return_stmt: Return_word (expr|invocation_stmt)? SEMI;
Return_word: RETURN;
//-------------------------------------------------------



// comments - start
Comment_normal:  '//' ~( '\r' | '\n' )* -> skip;
// Ex:
// //This is a line comment so // has no meaning here
Comment_block: '/*' .*? '*/' -> skip;
// Ex:
// /* This is a block comment so /* has no meaning here */
Comment_sharp:  '#' ~( '\r' | '\n' )* -> skip;
// Ex:
// #This is a line comment so # has no meaning here
// comments _ end

// Keywords - start
//keywords: BOOLEANLIT | BREAK | CLASS | CONT | DO
//         | EXTENDS | FLOAT | IF | INT | NEW | STRING
//         | THEN | FOR | RETURN | BOOLTRUE | BOOLFALSE | VOID
//         | NIL | THIS | FINAL | STATIC | TO | DOWNTO;
/*
    boolean break class continue do else
    extends float if int new string
    then for return true false void
    nil this final static to downto
*/
// Keywords _ end

//Types in d96 include: primitive types (int, float, bool, string), array and object(class)
types: primitive_Type | array_Type | class_type;
class_type: class_name;
primitive_Type: Bool_word | Int_word | Float_word | Str_word;
Bool_word: BOOL;
Int_word: INT;
Float_word: FLOAT;
Str_word: STRING;
//array_Type: Array_word LSB (element_type COMA array_size)? RSB;
array_Type: primitive_Type LSB (array_size)? RSB;
Array_word: ARRAY;
array_size: INTLIT;
Main_word: MAIN;
Cons_word: CONS;
Dest_word: DEST;

//This is attribute declaration, which include Types
attribute_list: attribute_name (COMA attribute_name)*;
attribute_name: ID;


//Loop (Foreach) stmt
//loop_foreach_stmt: Foreach_word LP ID In_word expr '..' expr (By_word expr)? RP block_stmt;
//Foreach_word: FOREACH;
//In_word: IN;
//By_word: BY;


//Rules for variables/constants
paramlist: param_decl (COMA param_decl)*;
param_decl: (types idlist) (Colon Assign_op init_value)?;
init_value: (expr|new_val_from_class_stmt|invocation_stmt);

//Rules for expressions, very complicated
expr_list: expr (COMA expr)*;

expr: string_expr;

string_expr: relational_expr (String_comp | String_concat) relational_expr
| relational_expr;

relational_expr: logical_expr (Equal | Diff | Greater | Lesser | Greater_euqal | Lesser_equal) logical_expr
| logical_expr;

logical_expr: adding_expr (And | Or) adding_expr
| adding_expr;

adding_expr: adding_expr (Add | Sub) multiplying_expr
| multiplying_expr;

multiplying_expr: multiplying_expr (Mul | Div | Mod) logical_not_expr
| logical_not_expr;

logical_not_expr: Not logical_not_expr
| sign_expr;

sign_expr: Sub sign_expr
| index_expr;

index_expr: index_expr
            (
                (LSB expr RSB)+|
                Member_access_in_ope class_expr (LP expr_list? RP)?
            )
| class_expr;

//member_access_in: member_access_in Member_access_in_ope class_expr (LP expr_list? RP)?
//| class_expr;

// member_access_out: class_expr Member_access_out class_expr (LP expr_list? RP)?
// | class_expr;

class_expr: KEYWORD_NEW class_expr LP expr_list? RP
| piority_exp;

piority_exp: LP expr RP
| array_exp;

array_exp: LB operands (COMA operands)* RB
    | operands;

operands: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT | arrayLIT | multi_ArrayLIT | ID | Self_word | class_name | THIS;
Self_word: SELF;


// identifier - start
ID: NORM_ID | SPEC_ID;
idlist: ID (COMA ID)*;
fragment NORM_ID: [a-zA-Z_][a-zA-Z0-9_]*;
fragment SPEC_ID: '$'[a-zA-Z0-9_]+;
// identifier _ end

Add: ADD_OP;
Sub: SUB_OP;
Mul: MUL_OP;
Div: FLOAT_DIVISION_OP;
Mod: MOD_OP;
Not: NOT_OP;
And: AND_OP;
Or: OR_OP;
Equal: EQUAL_OP;
Diff: NOT_EQUAL_OP;
Greater: GREATER_OP;
Lesser: LESS_OP;
Greater_euqal: GREATER_EQUAL_OP;
Lesser_equal: LESS_EQUAL_OP;
String_comp: STRING_COMP_OP;
String_concat: STRING_CONCAT_OP;
Member_access_in_ope: DOT;
Member_access_out: MEMBER_ACCESS_OUT;
Colon: COLON;



/////////////////// Lexer Rules//////////////////////
//For Boolean literal
BOOLEANLIT: BOOLTRUE | BOOLFALSE;
//For string litteral
STRINGLIT:  '"' ('\'"')* ( ESC_SEQ | ~["] | ('\'"'))* ('\'"')* '"' //'"' ( ESC_SEQ | (~[\\"]) | ('\'"'))* '"'
{
	s = ""
	check = False;
	for i in range(len(self.text)):
		s += self.text[i]
		a = ''
		if(i == len(self.text)-1): a = ''
		else: a = self.text[i+1]
		b = ((a != 'b') and  (a != 'f') and  (a != 'r') and  (a != 'n') and  (a != 't') and (a != '\'') and  (a != '"') and (a != '\\'))
		if(self.text[i] == '\\' and b == True):
			s += self.text[i+1]
			check = True
			break;
	if(check == True):
		self.text = s
		self.text = self.text[1:]
		raise IllegalEscape(self.text)
	else:
		self.text = s
		self.text = self.text[1:-1]
};
//fragment for string literals
fragment ESC_SEQ: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment ILL_ESC_SEQ: ('\\' ~([bfnrt\\] | '\'') ) | UNICODE_ESC | OCTAL_ESC | UNKNOW_ESC;
fragment OCTAL_ESC:   '\\' ('0'..'3') ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7') ('0'..'7')
    |   '\\' ('0'..'7');
fragment UNICODE_ESC:   '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT ;
fragment HEX_DIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;
fragment UNKNOW_ESC: '\\' 'h';

//Block comment
BLOCKCOMMENT: '##' .*? '##' -> skip;


//Describe Interger Literal
INTLIT: (DECIMAL | OCTAL | HEX | BIN)
{
	self.text = self.text.replace('_','')
};
//For Floating point number
FLOATLIT: INTERGER_PART (FRACTION  | EXPONENT | FRACTION EXPONENT)
{
	self.text = self.text.replace('_','')
	##print("Float: ", self.text)
};
fragment INTERGER_PART: DECIMAL;
fragment EXPONENT: [eE] [+-]? [0-9]+;
fragment FRACTION: DOT [0-9]*;
fragment DECIMAL: ('0') | ([1-9]([0-9]*'_'?[0-9]+)*);
fragment OCTAL: '0'[0-7][0-7_]*;
fragment HEX: '0'[xX][A-F0-9][A-F0-9_]*;
fragment BIN: '0'[bB][01][01_]*;


PROGRAM: 'Program';
MAIN: 'main';
EXTENDS: 'extends';

//These are for Keywords
BREAK: 'break';
CONT: 'continue';
IF: 'if';
ELSEIF: 'elseif';
ELSE: 'else';
FOR: 'for';
//FOREACH: 'foreach';
BOOLTRUE: 'true';
BOOLFALSE: 'false';
ARRAY: 'array';
IN: 'in';
INT: 'int';
FLOAT: 'float';
BOOL: 'boolean';
RETURN: 'return';
CLASS: 'class';
NULL: 'Null';
VAL: 'val';
VAR: 'var';
SELF: 'self';
CONS: 'constructor';
DEST: 'destructor';
KEYWORD_NEW: 'new';
BY: 'By';
DO: 'do';
STRING: 'string';
THEN: 'then';
VOID: 'void';
NIL: 'nil';
THIS: 'this';
FINAL: 'final';
STATIC: 'static';
TO: 'to';
DOWNTO: 'downto';
//Total Keywords available
//fragment KEYWORD: BREAK | CONT | IF | ELSEIF | ELSE |
//| FOR | BOOLTRUE | BOOLFALSE | ARRAY | IN |
//| INT | FLOAT | BOOL | STRING | RETURN |
//| NULL | CLASS | VAL | VAR |
//| CONS | DEST | KEYWORD_NEW | BY ;

//This is not lexer rules!!!
// For arrays in array
multi_ArrayLIT: Array_word LP array_list? RP;
array_list: arrayLIT (COMA arrayLIT)*;
// For indexed array
arrayLIT: Array_word LP element_list? RP;
element_list: elements (COMA elements)*;
elements: expr;
//This is not lexer rules!!!

//These tokens for operators
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
//INTERGER_DIVISION_OP: '\\';
FLOAT_DIVISION_OP: '/';
MOD_OP: '%';
NOT_OP: '!';
AND_OP: '&&';
OR_OP: '||';
EQUAL_OP: '==';
NOT_EQUAL_OP: '!=';
ASSIGN_OP: '=';
GREATER_OP: '>';
LESS_OP: '<';
GREATER_EQUAL_OP: '>=';
LESS_EQUAL_OP: '<=';
STRING_COMP_OP: '==.';
STRING_CONCAT_OP: '+.';
CONCATENATION_OP: '^';
//MEMBER_ACCESS_IN: '.'; //Can be presented by dot in Special Character
MEMBER_ACCESS_OUT: '::';

//These tokens for Special Character
LP: '(';
RP: ')';

LSB: '[';
RSB: ']';

LB: '{';
RB: '}';

SEMI: ';';

DOT: '.';

COMA: ',';

COLON: ':';

WS: [ \t\b\f\r\n]+ -> skip; // skip blanks, tabs, backspaces, form feed, carriage return, newline

UNTERMINATED_COMMENT: '##' .*? EOF { raise UnterminatedComment(self.text) }; //This is removed from assignment requirement
ERROR_CHAR: . {
    from lexererr import ErrorToken
    raise ErrorToken(self.text)
};
// ---------------------------------- MY PATH END