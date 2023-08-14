# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3}")
        buf.write("\u021f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\3\2\6\2x\n\2\r\2\16\2y\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\3\3\3\7\3\u0086\n\3\f\3\16\3\u0089\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\5\5\u0092\n\5\3\6\3\6\3\6\5\6\u0097")
        buf.write("\n\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7\u00a1\n\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\5\t\u00aa\n\t\3\n\5\n\u00ad\n")
        buf.write("\n\3\n\5\n\u00b0\n\n\3\13\3\13\3\13\3\13\3\13\7\13\u00b7")
        buf.write("\n\13\f\13\16\13\u00ba\13\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00c2\n\f\3\f\3\f\3\r\3\r\3\r\5\r\u00c9\n\r\3\16")
        buf.write("\3\16\3\16\7\16\u00ce\n\16\f\16\16\16\u00d1\13\16\3\16")
        buf.write("\5\16\u00d4\n\16\3\17\3\17\5\17\u00d8\n\17\3\20\3\20\5")
        buf.write("\20\u00dc\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u00eb\n\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u00f4\n\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u00fc\n\25\3\25\3\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u010b")
        buf.write("\n\27\f\27\16\27\u010e\13\27\3\27\5\27\u0111\n\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0126\n\32\f")
        buf.write("\32\16\32\u0129\13\32\5\32\u012b\n\32\3\32\3\32\5\32\u012f")
        buf.write("\n\32\3\33\3\33\5\33\u0133\n\33\3\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\5\35\u013b\n\35\3\35\3\35\3\36\3\36\3\36\5\36")
        buf.write("\u0142\n\36\3\37\3\37\3 \3 \3!\3!\3!\5!\u014b\n!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3#\7#\u0154\n#\f#\16#\u0157\13#\3$\3$")
        buf.write("\3%\3%\3%\7%\u015e\n%\f%\16%\u0161\13%\3&\3&\3&\3&\3&")
        buf.write("\3&\5&\u0169\n&\3\'\3\'\3\'\5\'\u016e\n\'\3(\3(\3(\7(")
        buf.write("\u0173\n(\f(\16(\u0176\13(\3)\3)\3*\3*\3*\3*\3*\5*\u017f")
        buf.write("\n*\3+\3+\3+\3+\3+\5+\u0186\n+\3,\3,\3,\3,\3,\5,\u018d")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\7-\u0195\n-\f-\16-\u0198\13-\3.")
        buf.write("\3.\3.\3.\3.\3.\7.\u01a0\n.\f.\16.\u01a3\13.\3/\3/\3/")
        buf.write("\5/\u01a8\n/\3\60\3\60\3\60\5\60\u01ad\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\6\61\u01b7\n\61\r\61\16")
        buf.write("\61\u01b8\3\61\3\61\3\61\3\61\5\61\u01bf\n\61\3\61\5\61")
        buf.write("\u01c2\n\61\5\61\u01c4\n\61\7\61\u01c6\n\61\f\61\16\61")
        buf.write("\u01c9\13\61\3\62\3\62\3\62\3\62\5\62\u01cf\n\62\3\62")
        buf.write("\3\62\3\62\5\62\u01d4\n\62\3\63\3\63\3\63\3\63\3\63\5")
        buf.write("\63\u01db\n\63\3\64\3\64\3\64\3\64\7\64\u01e1\n\64\f\64")
        buf.write("\16\64\u01e4\13\64\3\64\3\64\3\64\5\64\u01e9\n\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u01f5")
        buf.write("\n\65\3\66\3\66\3\66\7\66\u01fa\n\66\f\66\16\66\u01fd")
        buf.write("\13\66\3\67\3\67\3\67\5\67\u0202\n\67\3\67\3\67\38\38")
        buf.write("\38\78\u0209\n8\f8\168\u020c\138\39\39\39\59\u0211\n9")
        buf.write("\39\39\3:\3:\3:\7:\u0218\n:\f:\16:\u021b\13:\3;\3;\3;")
        buf.write("\2\5XZ`<\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt\2\13\6")
        buf.write("\2\4\4\35\35!!KK\4\2\35\35!!\4\2\20\20\22\22\3\2\30\33")
        buf.write("\3\2\60\61\3\2*/\3\2()\3\2\"#\3\2$&\2\u022e\2w\3\2\2\2")
        buf.write("\4}\3\2\2\2\6\u008c\3\2\2\2\b\u0091\3\2\2\2\n\u0093\3")
        buf.write("\2\2\2\f\u009b\3\2\2\2\16\u00a5\3\2\2\2\20\u00a9\3\2\2")
        buf.write("\2\22\u00ac\3\2\2\2\24\u00b1\3\2\2\2\26\u00bd\3\2\2\2")
        buf.write("\30\u00c8\3\2\2\2\32\u00d3\3\2\2\2\34\u00d7\3\2\2\2\36")
        buf.write("\u00db\3\2\2\2 \u00dd\3\2\2\2\"\u00e1\3\2\2\2$\u00ea\3")
        buf.write("\2\2\2&\u00ec\3\2\2\2(\u00f7\3\2\2\2*\u00ff\3\2\2\2,\u010c")
        buf.write("\3\2\2\2.\u0112\3\2\2\2\60\u0115\3\2\2\2\62\u0120\3\2")
        buf.write("\2\2\64\u0132\3\2\2\2\66\u0134\3\2\2\28\u0137\3\2\2\2")
        buf.write(":\u0141\3\2\2\2<\u0143\3\2\2\2>\u0145\3\2\2\2@\u0147\3")
        buf.write("\2\2\2B\u014e\3\2\2\2D\u0150\3\2\2\2F\u0158\3\2\2\2H\u015a")
        buf.write("\3\2\2\2J\u0162\3\2\2\2L\u016d\3\2\2\2N\u016f\3\2\2\2")
        buf.write("P\u0177\3\2\2\2R\u017e\3\2\2\2T\u0185\3\2\2\2V\u018c\3")
        buf.write("\2\2\2X\u018e\3\2\2\2Z\u0199\3\2\2\2\\\u01a7\3\2\2\2^")
        buf.write("\u01ac\3\2\2\2`\u01ae\3\2\2\2b\u01d3\3\2\2\2d\u01da\3")
        buf.write("\2\2\2f\u01e8\3\2\2\2h\u01f4\3\2\2\2j\u01f6\3\2\2\2l\u01fe")
        buf.write("\3\2\2\2n\u0205\3\2\2\2p\u020d\3\2\2\2r\u0214\3\2\2\2")
        buf.write("t\u021c\3\2\2\2vx\5\4\3\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z{\3\2\2\2{|\7\2\2\3|\3\3\2\2\2}~\7\3\2\2")
        buf.write("~\u0081\5\6\4\2\177\u0080\7\5\2\2\u0080\u0082\5\6\4\2")
        buf.write("\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2")
        buf.write("\2\2\u0083\u0087\7u\2\2\u0084\u0086\5\b\5\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u008a\u008b\7v\2\2\u008b\5\3\2\2\2\u008c\u008d\t\2\2")
        buf.write("\2\u008d\7\3\2\2\2\u008e\u0092\5\24\13\2\u008f\u0092\5")
        buf.write("\f\7\2\u0090\u0092\5\n\6\2\u0091\u008e\3\2\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0091\u0090\3\2\2\2\u0092\t\3\2\2\2\u0093\u0094")
        buf.write("\5\6\4\2\u0094\u0096\7q\2\2\u0095\u0097\5H%\2\u0096\u0095")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\7r\2\2\u0099\u009a\5\32\16\2\u009a\13\3\2\2\2\u009b")
        buf.write("\u009c\5\22\n\2\u009c\u009d\5\20\t\2\u009d\u009e\5\16")
        buf.write("\b\2\u009e\u00a0\7q\2\2\u009f\u00a1\5H%\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\7r\2\2\u00a3\u00a4\5\32\16\2\u00a4\r\3\2\2\2\u00a5")
        buf.write("\u00a6\t\3\2\2\u00a6\17\3\2\2\2\u00a7\u00aa\5:\36\2\u00a8")
        buf.write("\u00aa\7\b\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2")
        buf.write("\u00aa\21\3\2\2\2\u00ab\u00ad\7\6\2\2\u00ac\u00ab\3\2")
        buf.write("\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00b0")
        buf.write("\7\7\2\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\23\3\2\2\2\u00b1\u00b2\5\22\n\2\u00b2\u00b3\5:\36\2\u00b3")
        buf.write("\u00b8\5\26\f\2\u00b4\u00b5\7y\2\2\u00b5\u00b7\5\26\f")
        buf.write("\2\u00b6\u00b4\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00bb\u00bc\7w\2\2\u00bc\25\3\2\2\2\u00bd")
        buf.write("\u00c1\7!\2\2\u00be\u00bf\7\64\2\2\u00bf\u00c2\7\17\2")
        buf.write("\2\u00c0\u00c2\7\17\2\2\u00c1\u00be\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\5\30\r\2\u00c4")
        buf.write("\27\3\2\2\2\u00c5\u00c9\5P)\2\u00c6\u00c9\5(\25\2\u00c7")
        buf.write("\u00c9\5\62\32\2\u00c8\u00c5\3\2\2\2\u00c8\u00c6\3\2\2")
        buf.write("\2\u00c8\u00c7\3\2\2\2\u00c9\31\3\2\2\2\u00ca\u00d4\5")
        buf.write("\34\17\2\u00cb\u00cf\7u\2\2\u00cc\u00ce\5\34\17\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d4\7v\2\2\u00d3\u00ca\3\2\2\2\u00d3\u00cb")
        buf.write("\3\2\2\2\u00d4\33\3\2\2\2\u00d5\u00d8\5$\23\2\u00d6\u00d8")
        buf.write("\5\36\20\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\35\3\2\2\2\u00d9\u00dc\5 \21\2\u00da\u00dc\5\"\22\2\u00db")
        buf.write("\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\37\3\2\2\2\u00dd")
        buf.write("\u00de\7\7\2\2\u00de\u00df\5H%\2\u00df\u00e0\7w\2\2\u00e0")
        buf.write("!\3\2\2\2\u00e1\u00e2\5H%\2\u00e2\u00e3\7w\2\2\u00e3#")
        buf.write("\3\2\2\2\u00e4\u00eb\5&\24\2\u00e5\u00eb\5*\26\2\u00e6")
        buf.write("\u00eb\5\60\31\2\u00e7\u00eb\5\66\34\2\u00e8\u00eb\58")
        buf.write("\35\2\u00e9\u00eb\5\62\32\2\u00ea\u00e4\3\2\2\2\u00ea")
        buf.write("\u00e5\3\2\2\2\u00ea\u00e6\3\2\2\2\u00ea\u00e7\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb%\3\2\2")
        buf.write("\2\u00ec\u00ed\5`\61\2\u00ed\u00ee\7\64\2\2\u00ee\u00ef")
        buf.write("\7\17\2\2\u00ef\u00f3\3\2\2\2\u00f0\u00f4\5P)\2\u00f1")
        buf.write("\u00f4\5(\25\2\u00f2\u00f4\5\62\32\2\u00f3\u00f0\3\2\2")
        buf.write("\2\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5\u00f6\7w\2\2\u00f6\'\3\2\2\2\u00f7\u00f8")
        buf.write("\7\t\2\2\u00f8\u00f9\5\6\4\2\u00f9\u00fb\7q\2\2\u00fa")
        buf.write("\u00fc\5N(\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fd\3\2\2\2\u00fd\u00fe\7r\2\2\u00fe)\3\2\2\2\u00ff")
        buf.write("\u0100\7\n\2\2\u0100\u0101\5P)\2\u0101\u0102\7\13\2\2")
        buf.write("\u0102\u0103\5\32\16\2\u0103\u0104\3\2\2\2\u0104\u0105")
        buf.write("\5,\27\2\u0105+\3\2\2\2\u0106\u0107\7\r\2\2\u0107\u0108")
        buf.write("\5P)\2\u0108\u0109\5\32\16\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u0106\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010f\u0111\5.\30\2\u0110\u010f\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111-\3\2\2\2\u0112\u0113\7\f\2\2\u0113\u0114")
        buf.write("\5\32\16\2\u0114/\3\2\2\2\u0115\u0116\7\16\2\2\u0116\u0117")
        buf.write("\7!\2\2\u0117\u0118\7\64\2\2\u0118\u0119\7\17\2\2\u0119")
        buf.write("\u011a\5P)\2\u011a\u011b\3\2\2\2\u011b\u011c\t\4\2\2\u011c")
        buf.write("\u011d\5P)\2\u011d\u011e\7\21\2\2\u011e\u011f\5\32\16")
        buf.write("\2\u011f\61\3\2\2\2\u0120\u0121\7!\2\2\u0121\u012a\7q")
        buf.write("\2\2\u0122\u0127\5\64\33\2\u0123\u0124\7y\2\2\u0124\u0126")
        buf.write("\5\64\33\2\u0125\u0123\3\2\2\2\u0126\u0129\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012b\3\2\2\2")
        buf.write("\u0129\u0127\3\2\2\2\u012a\u0122\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\7r\2\2\u012d\u012f")
        buf.write("\7w\2\2\u012e\u012d\3\2\2\2\u012e\u012f\3\2\2\2\u012f")
        buf.write("\63\3\2\2\2\u0130\u0133\5P)\2\u0131\u0133\5\62\32\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0131\3\2\2\2\u0133\65\3\2\2\2\u0134")
        buf.write("\u0135\7\23\2\2\u0135\u0136\7w\2\2\u0136\67\3\2\2\2\u0137")
        buf.write("\u013a\7\24\2\2\u0138\u013b\5P)\2\u0139\u013b\5\62\32")
        buf.write("\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7w\2\2\u013d")
        buf.write("9\3\2\2\2\u013e\u0142\5> \2\u013f\u0142\5@!\2\u0140\u0142")
        buf.write("\5<\37\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0141")
        buf.write("\u0140\3\2\2\2\u0142;\3\2\2\2\u0143\u0144\5\6\4\2\u0144")
        buf.write("=\3\2\2\2\u0145\u0146\t\5\2\2\u0146?\3\2\2\2\u0147\u0148")
        buf.write("\5> \2\u0148\u014a\7s\2\2\u0149\u014b\5B\"\2\u014a\u0149")
        buf.write("\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014d\7t\2\2\u014dA\3\2\2\2\u014e\u014f\78\2\2\u014f")
        buf.write("C\3\2\2\2\u0150\u0155\5F$\2\u0151\u0152\7y\2\2\u0152\u0154")
        buf.write("\5F$\2\u0153\u0151\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0156\3\2\2\2\u0156E\3\2\2\2\u0157\u0155")
        buf.write("\3\2\2\2\u0158\u0159\7!\2\2\u0159G\3\2\2\2\u015a\u015f")
        buf.write("\5J&\2\u015b\u015c\7y\2\2\u015c\u015e\5J&\2\u015d\u015b")
        buf.write("\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160I\3\2\2\2\u0161\u015f\3\2\2\2\u0162")
        buf.write("\u0163\5:\36\2\u0163\u0164\5j\66\2\u0164\u0168\3\2\2\2")
        buf.write("\u0165\u0166\7\64\2\2\u0166\u0167\7\17\2\2\u0167\u0169")
        buf.write("\5L\'\2\u0168\u0165\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("K\3\2\2\2\u016a\u016e\5P)\2\u016b\u016e\5(\25\2\u016c")
        buf.write("\u016e\5\62\32\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2")
        buf.write("\2\u016d\u016c\3\2\2\2\u016eM\3\2\2\2\u016f\u0174\5P)")
        buf.write("\2\u0170\u0171\7y\2\2\u0171\u0173\5P)\2\u0172\u0170\3")
        buf.write("\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175O\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178")
        buf.write("\5R*\2\u0178Q\3\2\2\2\u0179\u017a\5T+\2\u017a\u017b\t")
        buf.write("\6\2\2\u017b\u017c\5T+\2\u017c\u017f\3\2\2\2\u017d\u017f")
        buf.write("\5T+\2\u017e\u0179\3\2\2\2\u017e\u017d\3\2\2\2\u017fS")
        buf.write("\3\2\2\2\u0180\u0181\5V,\2\u0181\u0182\t\7\2\2\u0182\u0183")
        buf.write("\5V,\2\u0183\u0186\3\2\2\2\u0184\u0186\5V,\2\u0185\u0180")
        buf.write("\3\2\2\2\u0185\u0184\3\2\2\2\u0186U\3\2\2\2\u0187\u0188")
        buf.write("\5X-\2\u0188\u0189\t\b\2\2\u0189\u018a\5X-\2\u018a\u018d")
        buf.write("\3\2\2\2\u018b\u018d\5X-\2\u018c\u0187\3\2\2\2\u018c\u018b")
        buf.write("\3\2\2\2\u018dW\3\2\2\2\u018e\u018f\b-\1\2\u018f\u0190")
        buf.write("\5Z.\2\u0190\u0196\3\2\2\2\u0191\u0192\f\4\2\2\u0192\u0193")
        buf.write("\t\t\2\2\u0193\u0195\5Z.\2\u0194\u0191\3\2\2\2\u0195\u0198")
        buf.write("\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("Y\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\b.\1\2\u019a")
        buf.write("\u019b\5\\/\2\u019b\u01a1\3\2\2\2\u019c\u019d\f\4\2\2")
        buf.write("\u019d\u019e\t\n\2\2\u019e\u01a0\5\\/\2\u019f\u019c\3")
        buf.write("\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2[\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5")
        buf.write("\7\'\2\2\u01a5\u01a8\5\\/\2\u01a6\u01a8\5^\60\2\u01a7")
        buf.write("\u01a4\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8]\3\2\2\2\u01a9")
        buf.write("\u01aa\7#\2\2\u01aa\u01ad\5^\60\2\u01ab\u01ad\5`\61\2")
        buf.write("\u01ac\u01a9\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad_\3\2\2")
        buf.write("\2\u01ae\u01af\b\61\1\2\u01af\u01b0\5b\62\2\u01b0\u01c7")
        buf.write("\3\2\2\2\u01b1\u01c3\f\4\2\2\u01b2\u01b3\7s\2\2\u01b3")
        buf.write("\u01b4\5P)\2\u01b4\u01b5\7t\2\2\u01b5\u01b7\3\2\2\2\u01b6")
        buf.write("\u01b2\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6\3\2\2\2")
        buf.write("\u01b8\u01b9\3\2\2\2\u01b9\u01c4\3\2\2\2\u01ba\u01bb\7")
        buf.write("\62\2\2\u01bb\u01c1\5b\62\2\u01bc\u01be\7q\2\2\u01bd\u01bf")
        buf.write("\5N(\2\u01be\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0")
        buf.write("\3\2\2\2\u01c0\u01c2\7r\2\2\u01c1\u01bc\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01b6\3\2\2\2")
        buf.write("\u01c3\u01ba\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01b1\3")
        buf.write("\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8a\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cb")
        buf.write("\7R\2\2\u01cb\u01cc\5b\62\2\u01cc\u01ce\7q\2\2\u01cd\u01cf")
        buf.write("\5N(\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0\u01d1\7r\2\2\u01d1\u01d4\3\2\2\2\u01d2")
        buf.write("\u01d4\5d\63\2\u01d3\u01ca\3\2\2\2\u01d3\u01d2\3\2\2\2")
        buf.write("\u01d4c\3\2\2\2\u01d5\u01d6\7q\2\2\u01d6\u01d7\5P)\2\u01d7")
        buf.write("\u01d8\7r\2\2\u01d8\u01db\3\2\2\2\u01d9\u01db\5f\64\2")
        buf.write("\u01da\u01d5\3\2\2\2\u01da\u01d9\3\2\2\2\u01dbe\3\2\2")
        buf.write("\2\u01dc\u01dd\7u\2\2\u01dd\u01e2\5h\65\2\u01de\u01df")
        buf.write("\7y\2\2\u01df\u01e1\5h\65\2\u01e0\u01de\3\2\2\2\u01e1")
        buf.write("\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2")
        buf.write("\u01e3\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7")
        buf.write("v\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e9\5h\65\2\u01e8\u01dc")
        buf.write("\3\2\2\2\u01e8\u01e7\3\2\2\2\u01e9g\3\2\2\2\u01ea\u01f5")
        buf.write("\78\2\2\u01eb\u01f5\79\2\2\u01ec\u01f5\7\65\2\2\u01ed")
        buf.write("\u01f5\7\66\2\2\u01ee\u01f5\5p9\2\u01ef\u01f5\5l\67\2")
        buf.write("\u01f0\u01f5\7!\2\2\u01f1\u01f5\7 \2\2\u01f2\u01f5\5\6")
        buf.write("\4\2\u01f3\u01f5\7Y\2\2\u01f4\u01ea\3\2\2\2\u01f4\u01eb")
        buf.write("\3\2\2\2\u01f4\u01ec\3\2\2\2\u01f4\u01ed\3\2\2\2\u01f4")
        buf.write("\u01ee\3\2\2\2\u01f4\u01ef\3\2\2\2\u01f4\u01f0\3\2\2\2")
        buf.write("\u01f4\u01f1\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3\3")
        buf.write("\2\2\2\u01f5i\3\2\2\2\u01f6\u01fb\7!\2\2\u01f7\u01f8\7")
        buf.write("y\2\2\u01f8\u01fa\7!\2\2\u01f9\u01f7\3\2\2\2\u01fa\u01fd")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("k\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\7\34\2\2\u01ff")
        buf.write("\u0201\7q\2\2\u0200\u0202\5n8\2\u0201\u0200\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0204\7r\2\2")
        buf.write("\u0204m\3\2\2\2\u0205\u020a\5p9\2\u0206\u0207\7y\2\2\u0207")
        buf.write("\u0209\5p9\2\u0208\u0206\3\2\2\2\u0209\u020c\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020bo\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020e\7\34\2\2\u020e\u0210\7q\2\2")
        buf.write("\u020f\u0211\5r:\2\u0210\u020f\3\2\2\2\u0210\u0211\3\2")
        buf.write("\2\2\u0211\u0212\3\2\2\2\u0212\u0213\7r\2\2\u0213q\3\2")
        buf.write("\2\2\u0214\u0219\5t;\2\u0215\u0216\7y\2\2\u0216\u0218")
        buf.write("\5t;\2\u0217\u0215\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u0219\u021a\3\2\2\2\u021as\3\2\2\2\u021b\u0219")
        buf.write("\3\2\2\2\u021c\u021d\5P)\2\u021du\3\2\2\2:y\u0081\u0087")
        buf.write("\u0091\u0096\u00a0\u00a9\u00ac\u00af\u00b8\u00c1\u00c8")
        buf.write("\u00cf\u00d3\u00d7\u00db\u00ea\u00f3\u00fb\u010c\u0110")
        buf.write("\u0127\u012a\u012e\u0132\u013a\u0141\u014a\u0155\u015f")
        buf.write("\u0168\u016d\u0174\u017e\u0185\u018c\u0196\u01a1\u01a7")
        buf.write("\u01ac\u01b8\u01be\u01c1\u01c3\u01c7\u01ce\u01d3\u01da")
        buf.write("\u01e2\u01e8\u01f4\u01fb\u0201\u020a\u0210\u0219")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Program'", "'main'", "'extends'", "'break'", "'continue'", 
                     "'if'", "'elseif'", "'else'", "'for'", "'true'", "'false'", 
                     "'array'", "'in'", "'int'", "'float'", "'boolean'", 
                     "'return'", "'class'", "'Null'", "'val'", "'var'", 
                     "'self'", "'constructor'", "'destructor'", "'new'", 
                     "'By'", "'do'", "'string'", "'then'", "'void'", "'nil'", 
                     "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'='", "'>'", "'<'", "'>='", "'<='", 
                     "'==.'", "'+.'", "'^'", "'::'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "';'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "Class_word", "Prog_word", "Extends_word", 
                      "Static_word", "Final_word", "Void_word", "Keyword_new", 
                      "If_word", "Then_word", "Else_word", "Elseif_word", 
                      "For_word", "Assign_op", "To_word", "Do_word", "Down_to_word", 
                      "Break_word", "Return_word", "Comment_normal", "Comment_block", 
                      "Comment_sharp", "Bool_word", "Int_word", "Float_word", 
                      "Str_word", "Array_word", "Main_word", "Cons_word", 
                      "Dest_word", "Self_word", "ID", "Add", "Sub", "Mul", 
                      "Div", "Mod", "Not", "And", "Or", "Equal", "Diff", 
                      "Greater", "Lesser", "Greater_euqal", "Lesser_equal", 
                      "String_comp", "String_concat", "Member_access_in_ope", 
                      "Member_access_out", "Colon", "BOOLEANLIT", "STRINGLIT", 
                      "BLOCKCOMMENT", "INTLIT", "FLOATLIT", "PROGRAM", "MAIN", 
                      "EXTENDS", "BREAK", "CONT", "IF", "ELSEIF", "ELSE", 
                      "FOR", "BOOLTRUE", "BOOLFALSE", "ARRAY", "IN", "INT", 
                      "FLOAT", "BOOL", "RETURN", "CLASS", "NULL", "VAL", 
                      "VAR", "SELF", "CONS", "DEST", "KEYWORD_NEW", "BY", 
                      "DO", "STRING", "THEN", "VOID", "NIL", "THIS", "FINAL", 
                      "STATIC", "TO", "DOWNTO", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "FLOAT_DIVISION_OP", "MOD_OP", "NOT_OP", "AND_OP", 
                      "OR_OP", "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", 
                      "GREATER_OP", "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", 
                      "STRING_COMP_OP", "STRING_CONCAT_OP", "CONCATENATION_OP", 
                      "MEMBER_ACCESS_OUT", "LP", "RP", "LSB", "RSB", "LB", 
                      "RB", "SEMI", "DOT", "COMA", "COLON", "WS", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_name = 2
    RULE_member_lists = 3
    RULE_instructor = 4
    RULE_methods = 5
    RULE_methods_name = 6
    RULE_methods_return_types = 7
    RULE_class_props_kind = 8
    RULE_attributes = 9
    RULE_attribute_as = 10
    RULE_attribute_as_val = 11
    RULE_block_stmt = 12
    RULE_block_stmt_list = 13
    RULE_delc = 14
    RULE_cons_decl = 15
    RULE_var_decl = 16
    RULE_stmt = 17
    RULE_as_stmt = 18
    RULE_new_val_from_class_stmt = 19
    RULE_if_stmt = 20
    RULE_elseif_stmt = 21
    RULE_else_stmt = 22
    RULE_loop_for_stmt = 23
    RULE_invocation_stmt = 24
    RULE_invocation_stmt_params = 25
    RULE_break_stmt = 26
    RULE_return_stmt = 27
    RULE_types = 28
    RULE_class_type = 29
    RULE_primitive_Type = 30
    RULE_array_Type = 31
    RULE_array_size = 32
    RULE_attribute_list = 33
    RULE_attribute_name = 34
    RULE_paramlist = 35
    RULE_param_decl = 36
    RULE_init_value = 37
    RULE_expr_list = 38
    RULE_expr = 39
    RULE_string_expr = 40
    RULE_relational_expr = 41
    RULE_logical_expr = 42
    RULE_adding_expr = 43
    RULE_multiplying_expr = 44
    RULE_logical_not_expr = 45
    RULE_sign_expr = 46
    RULE_index_expr = 47
    RULE_class_expr = 48
    RULE_piority_exp = 49
    RULE_array_exp = 50
    RULE_operands = 51
    RULE_idlist = 52
    RULE_multi_ArrayLIT = 53
    RULE_array_list = 54
    RULE_arrayLIT = 55
    RULE_element_list = 56
    RULE_elements = 57

    ruleNames =  [ "program", "class_decl", "class_name", "member_lists", 
                   "instructor", "methods", "methods_name", "methods_return_types", 
                   "class_props_kind", "attributes", "attribute_as", "attribute_as_val", 
                   "block_stmt", "block_stmt_list", "delc", "cons_decl", 
                   "var_decl", "stmt", "as_stmt", "new_val_from_class_stmt", 
                   "if_stmt", "elseif_stmt", "else_stmt", "loop_for_stmt", 
                   "invocation_stmt", "invocation_stmt_params", "break_stmt", 
                   "return_stmt", "types", "class_type", "primitive_Type", 
                   "array_Type", "array_size", "attribute_list", "attribute_name", 
                   "paramlist", "param_decl", "init_value", "expr_list", 
                   "expr", "string_expr", "relational_expr", "logical_expr", 
                   "adding_expr", "multiplying_expr", "logical_not_expr", 
                   "sign_expr", "index_expr", "class_expr", "piority_exp", 
                   "array_exp", "operands", "idlist", "multi_ArrayLIT", 
                   "array_list", "arrayLIT", "element_list", "elements" ]

    EOF = Token.EOF
    Class_word=1
    Prog_word=2
    Extends_word=3
    Static_word=4
    Final_word=5
    Void_word=6
    Keyword_new=7
    If_word=8
    Then_word=9
    Else_word=10
    Elseif_word=11
    For_word=12
    Assign_op=13
    To_word=14
    Do_word=15
    Down_to_word=16
    Break_word=17
    Return_word=18
    Comment_normal=19
    Comment_block=20
    Comment_sharp=21
    Bool_word=22
    Int_word=23
    Float_word=24
    Str_word=25
    Array_word=26
    Main_word=27
    Cons_word=28
    Dest_word=29
    Self_word=30
    ID=31
    Add=32
    Sub=33
    Mul=34
    Div=35
    Mod=36
    Not=37
    And=38
    Or=39
    Equal=40
    Diff=41
    Greater=42
    Lesser=43
    Greater_euqal=44
    Lesser_equal=45
    String_comp=46
    String_concat=47
    Member_access_in_ope=48
    Member_access_out=49
    Colon=50
    BOOLEANLIT=51
    STRINGLIT=52
    BLOCKCOMMENT=53
    INTLIT=54
    FLOATLIT=55
    PROGRAM=56
    MAIN=57
    EXTENDS=58
    BREAK=59
    CONT=60
    IF=61
    ELSEIF=62
    ELSE=63
    FOR=64
    BOOLTRUE=65
    BOOLFALSE=66
    ARRAY=67
    IN=68
    INT=69
    FLOAT=70
    BOOL=71
    RETURN=72
    CLASS=73
    NULL=74
    VAL=75
    VAR=76
    SELF=77
    CONS=78
    DEST=79
    KEYWORD_NEW=80
    BY=81
    DO=82
    STRING=83
    THEN=84
    VOID=85
    NIL=86
    THIS=87
    FINAL=88
    STATIC=89
    TO=90
    DOWNTO=91
    ADD_OP=92
    SUB_OP=93
    MUL_OP=94
    FLOAT_DIVISION_OP=95
    MOD_OP=96
    NOT_OP=97
    AND_OP=98
    OR_OP=99
    EQUAL_OP=100
    NOT_EQUAL_OP=101
    ASSIGN_OP=102
    GREATER_OP=103
    LESS_OP=104
    GREATER_EQUAL_OP=105
    LESS_EQUAL_OP=106
    STRING_COMP_OP=107
    STRING_CONCAT_OP=108
    CONCATENATION_OP=109
    MEMBER_ACCESS_OUT=110
    LP=111
    RP=112
    LSB=113
    RSB=114
    LB=115
    RB=116
    SEMI=117
    DOT=118
    COMA=119
    COLON=120
    WS=121
    UNTERMINATED_COMMENT=122
    ERROR_CHAR=123

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.class_decl()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.Class_word):
                    break

            self.state = 121
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class_word(self):
            return self.getToken(BKOOLParser.Class_word, 0)

        def class_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_nameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_nameContext,i)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def Extends_word(self):
            return self.getToken(BKOOLParser.Extends_word, 0)

        def member_lists(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Member_listsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Member_listsContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKOOLParser.Class_word)
            self.state = 124
            self.class_name()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Extends_word:
                self.state = 125
                self.match(BKOOLParser.Extends_word)
                self.state = 126
                self.class_name()


            self.state = 129
            self.match(BKOOLParser.LB)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Static_word) | (1 << BKOOLParser.Final_word) | (1 << BKOOLParser.Void_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 130
                self.member_lists()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Prog_word(self):
            return self.getToken(BKOOLParser.Prog_word, 0)

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def Main_word(self):
            return self.getToken(BKOOLParser.Main_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = BKOOLParser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(BKOOLParser.AttributesContext,0)


        def methods(self):
            return self.getTypedRuleContext(BKOOLParser.MethodsContext,0)


        def instructor(self):
            return self.getTypedRuleContext(BKOOLParser.InstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member_lists

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_lists" ):
                return visitor.visitMember_lists(self)
            else:
                return visitor.visitChildren(self)




    def member_lists(self):

        localctx = BKOOLParser.Member_listsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_member_lists)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.attributes()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.methods()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.instructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructor" ):
                return visitor.visitInstructor(self)
            else:
                return visitor.visitChildren(self)




    def instructor(self):

        localctx = BKOOLParser.InstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.class_name()
            self.state = 146
            self.match(BKOOLParser.LP)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 147
                self.paramlist()


            self.state = 150
            self.match(BKOOLParser.RP)
            self.state = 151
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_props_kind(self):
            return self.getTypedRuleContext(BKOOLParser.Class_props_kindContext,0)


        def methods_return_types(self):
            return self.getTypedRuleContext(BKOOLParser.Methods_return_typesContext,0)


        def methods_name(self):
            return self.getTypedRuleContext(BKOOLParser.Methods_nameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods" ):
                return visitor.visitMethods(self)
            else:
                return visitor.visitChildren(self)




    def methods(self):

        localctx = BKOOLParser.MethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_methods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.class_props_kind()
            self.state = 154
            self.methods_return_types()
            self.state = 155
            self.methods_name()
            self.state = 156
            self.match(BKOOLParser.LP)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.ID))) != 0) or _la==BKOOLParser.CLASS:
                self.state = 157
                self.paramlist()


            self.state = 160
            self.match(BKOOLParser.RP)
            self.state = 161
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methods_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Main_word(self):
            return self.getToken(BKOOLParser.Main_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methods_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods_name" ):
                return visitor.visitMethods_name(self)
            else:
                return visitor.visitChildren(self)




    def methods_name(self):

        localctx = BKOOLParser.Methods_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_methods_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.Main_word or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methods_return_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def Void_word(self):
            return self.getToken(BKOOLParser.Void_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methods_return_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethods_return_types" ):
                return visitor.visitMethods_return_types(self)
            else:
                return visitor.visitChildren(self)




    def methods_return_types(self):

        localctx = BKOOLParser.Methods_return_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_methods_return_types)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Prog_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Main_word, BKOOLParser.ID, BKOOLParser.CLASS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.types()
                pass
            elif token in [BKOOLParser.Void_word]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(BKOOLParser.Void_word)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_props_kindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Static_word(self):
            return self.getToken(BKOOLParser.Static_word, 0)

        def Final_word(self):
            return self.getToken(BKOOLParser.Final_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_props_kind

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_props_kind" ):
                return visitor.visitClass_props_kind(self)
            else:
                return visitor.visitChildren(self)




    def class_props_kind(self):

        localctx = BKOOLParser.Class_props_kindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_class_props_kind)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Static_word:
                self.state = 169
                self.match(BKOOLParser.Static_word)


            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Final_word:
                self.state = 172
                self.match(BKOOLParser.Final_word)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_props_kind(self):
            return self.getTypedRuleContext(BKOOLParser.Class_props_kindContext,0)


        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def attribute_as(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Attribute_asContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Attribute_asContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = BKOOLParser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attributes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.class_props_kind()
            self.state = 176
            self.types()
            self.state = 177
            self.attribute_as()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 178
                self.match(BKOOLParser.COMA)
                self.state = 179
                self.attribute_as()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_asContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def attribute_as_val(self):
            return self.getTypedRuleContext(BKOOLParser.Attribute_as_valContext,0)


        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_as

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_as" ):
                return visitor.visitAttribute_as(self)
            else:
                return visitor.visitChildren(self)




    def attribute_as(self):

        localctx = BKOOLParser.Attribute_asContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_attribute_as)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKOOLParser.ID)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Colon]:
                self.state = 188
                self.match(BKOOLParser.Colon)
                self.state = 189
                self.match(BKOOLParser.Assign_op)
                pass
            elif token in [BKOOLParser.Assign_op]:
                self.state = 190
                self.match(BKOOLParser.Assign_op)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.attribute_as_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_as_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def new_val_from_class_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.New_val_from_class_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_as_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_as_val" ):
                return visitor.visitAttribute_as_val(self)
            else:
                return visitor.visitChildren(self)




    def attribute_as_val(self):

        localctx = BKOOLParser.Attribute_as_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attribute_as_val)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.new_val_from_class_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Block_stmt_listContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Block_stmt_listContext,i)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.block_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(BKOOLParser.LB)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Final_word) | (1 << BKOOLParser.If_word) | (1 << BKOOLParser.For_word) | (1 << BKOOLParser.Break_word) | (1 << BKOOLParser.Return_word) | (1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                    self.state = 202
                    self.block_stmt_list()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def delc(self):
            return self.getTypedRuleContext(BKOOLParser.DelcContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt_list" ):
                return visitor.visitBlock_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt_list(self):

        localctx = BKOOLParser.Block_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_block_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 211
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 212
                self.delc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cons_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Cons_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_delc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelc" ):
                return visitor.visitDelc(self)
            else:
                return visitor.visitChildren(self)




    def delc(self):

        localctx = BKOOLParser.DelcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_delc)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Final_word]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.cons_decl()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Bool_word, BKOOLParser.Int_word, BKOOLParser.Float_word, BKOOLParser.Str_word, BKOOLParser.Main_word, BKOOLParser.ID, BKOOLParser.CLASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.var_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cons_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Final_word(self):
            return self.getToken(BKOOLParser.Final_word, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_cons_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCons_decl" ):
                return visitor.visitCons_decl(self)
            else:
                return visitor.visitChildren(self)




    def cons_decl(self):

        localctx = BKOOLParser.Cons_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_cons_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BKOOLParser.Final_word)
            self.state = 220
            self.paramlist()
            self.state = 221
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.paramlist()
            self.state = 224
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def as_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.As_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def loop_for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Loop_for_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.as_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.loop_for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.break_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.return_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class As_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def new_val_from_class_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.New_val_from_class_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_as_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs_stmt" ):
                return visitor.visitAs_stmt(self)
            else:
                return visitor.visitChildren(self)




    def as_stmt(self):

        localctx = BKOOLParser.As_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_as_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.index_expr(0)

            self.state = 235
            self.match(BKOOLParser.Colon)
            self.state = 236
            self.match(BKOOLParser.Assign_op)
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 238
                self.expr()
                pass

            elif la_ == 2:
                self.state = 239
                self.new_val_from_class_stmt()
                pass

            elif la_ == 3:
                self.state = 240
                self.invocation_stmt()
                pass


            self.state = 243
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_val_from_class_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Keyword_new(self):
            return self.getToken(BKOOLParser.Keyword_new, 0)

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_new_val_from_class_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_val_from_class_stmt" ):
                return visitor.visitNew_val_from_class_stmt(self)
            else:
                return visitor.visitChildren(self)




    def new_val_from_class_stmt(self):

        localctx = BKOOLParser.New_val_from_class_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_new_val_from_class_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKOOLParser.Keyword_new)
            self.state = 246
            self.class_name()
            self.state = 247
            self.match(BKOOLParser.LP)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                self.state = 248
                self.expr_list()


            self.state = 251
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Elseif_stmtContext,0)


        def If_word(self):
            return self.getToken(BKOOLParser.If_word, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def Then_word(self):
            return self.getToken(BKOOLParser.Then_word, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(BKOOLParser.If_word)
            self.state = 254
            self.expr()
            self.state = 255
            self.match(BKOOLParser.Then_word)
            self.state = 256
            self.block_stmt()
            self.state = 258
            self.elseif_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Elseif_word(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.Elseif_word)
            else:
                return self.getToken(BKOOLParser.Elseif_word, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = BKOOLParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 260
                    self.match(BKOOLParser.Elseif_word)
                    self.state = 261
                    self.expr()
                    self.state = 262
                    self.block_stmt() 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 269
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else_word(self):
            return self.getToken(BKOOLParser.Else_word, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKOOLParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BKOOLParser.Else_word)
            self.state = 273
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_for_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def For_word(self):
            return self.getToken(BKOOLParser.For_word, 0)

        def Do_word(self):
            return self.getToken(BKOOLParser.Do_word, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def To_word(self):
            return self.getToken(BKOOLParser.To_word, 0)

        def Down_to_word(self):
            return self.getToken(BKOOLParser.Down_to_word, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_loop_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_for_stmt" ):
                return visitor.visitLoop_for_stmt(self)
            else:
                return visitor.visitChildren(self)




    def loop_for_stmt(self):

        localctx = BKOOLParser.Loop_for_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_loop_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(BKOOLParser.For_word)

            self.state = 276
            self.match(BKOOLParser.ID)
            self.state = 277
            self.match(BKOOLParser.Colon)
            self.state = 278
            self.match(BKOOLParser.Assign_op)
            self.state = 279
            self.expr()
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.To_word or _la==BKOOLParser.Down_to_word):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            self.state = 282
            self.expr()
            self.state = 283
            self.match(BKOOLParser.Do_word)
            self.state = 284
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def invocation_stmt_params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Invocation_stmt_paramsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Invocation_stmt_paramsContext,i)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_stmt" ):
                return visitor.visitInvocation_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invocation_stmt(self):

        localctx = BKOOLParser.Invocation_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_invocation_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BKOOLParser.ID)
            self.state = 287
            self.match(BKOOLParser.LP)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                self.state = 288
                self.invocation_stmt_params()
                self.state = 293
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMA:
                    self.state = 289
                    self.match(BKOOLParser.COMA)
                    self.state = 290
                    self.invocation_stmt_params()
                    self.state = 295
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 298
            self.match(BKOOLParser.RP)
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 299
                self.match(BKOOLParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stmt_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_stmt_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_stmt_params" ):
                return visitor.visitInvocation_stmt_params(self)
            else:
                return visitor.visitChildren(self)




    def invocation_stmt_params(self):

        localctx = BKOOLParser.Invocation_stmt_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_invocation_stmt_params)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break_word(self):
            return self.getToken(BKOOLParser.Break_word, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(BKOOLParser.Break_word)
            self.state = 307
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return_word(self):
            return self.getToken(BKOOLParser.Return_word, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKOOLParser.Return_word)
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 310
                self.expr()

            elif la_ == 2:
                self.state = 311
                self.invocation_stmt()


            self.state = 314
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def array_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_TypeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(BKOOLParser.Class_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = BKOOLParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_types)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.primitive_Type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.array_Type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.class_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = BKOOLParser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.class_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bool_word(self):
            return self.getToken(BKOOLParser.Bool_word, 0)

        def Int_word(self):
            return self.getToken(BKOOLParser.Int_word, 0)

        def Float_word(self):
            return self.getToken(BKOOLParser.Float_word, 0)

        def Str_word(self):
            return self.getToken(BKOOLParser.Str_word, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_Type" ):
                return visitor.visitPrimitive_Type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_Type(self):

        localctx = BKOOLParser.Primitive_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primitive_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Bool_word) | (1 << BKOOLParser.Int_word) | (1 << BKOOLParser.Float_word) | (1 << BKOOLParser.Str_word))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_Type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_TypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def array_size(self):
            return self.getTypedRuleContext(BKOOLParser.Array_sizeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_Type" ):
                return visitor.visitArray_Type(self)
            else:
                return visitor.visitChildren(self)




    def array_Type(self):

        localctx = BKOOLParser.Array_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_array_Type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.primitive_Type()
            self.state = 326
            self.match(BKOOLParser.LSB)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INTLIT:
                self.state = 327
                self.array_size()


            self.state = 330
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_sizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = BKOOLParser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(BKOOLParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Attribute_nameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Attribute_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_list" ):
                return visitor.visitAttribute_list(self)
            else:
                return visitor.visitChildren(self)




    def attribute_list(self):

        localctx = BKOOLParser.Attribute_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_attribute_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.attribute_name()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 335
                self.match(BKOOLParser.COMA)
                self.state = 336
                self.attribute_name()
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attribute_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = BKOOLParser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_attribute_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Param_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Param_declContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.param_decl()
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 345
                self.match(BKOOLParser.COMA)
                self.state = 346
                self.param_decl()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(BKOOLParser.TypesContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def Colon(self):
            return self.getToken(BKOOLParser.Colon, 0)

        def Assign_op(self):
            return self.getToken(BKOOLParser.Assign_op, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKOOLParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_decl" ):
                return visitor.visitParam_decl(self)
            else:
                return visitor.visitChildren(self)




    def param_decl(self):

        localctx = BKOOLParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.types()
            self.state = 353
            self.idlist()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Colon:
                self.state = 355
                self.match(BKOOLParser.Colon)
                self.state = 356
                self.match(BKOOLParser.Assign_op)
                self.state = 357
                self.init_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def new_val_from_class_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.New_val_from_class_stmtContext,0)


        def invocation_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = BKOOLParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 360
                self.expr()
                pass

            elif la_ == 2:
                self.state = 361
                self.new_val_from_class_stmt()
                pass

            elif la_ == 3:
                self.state = 362
                self.invocation_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = BKOOLParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr()
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 366
                self.match(BKOOLParser.COMA)
                self.state = 367
                self.expr()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(BKOOLParser.String_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Relational_exprContext,i)


        def String_comp(self):
            return self.getToken(BKOOLParser.String_comp, 0)

        def String_concat(self):
            return self.getToken(BKOOLParser.String_concat, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = BKOOLParser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_string_expr)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.relational_expr()
                self.state = 376
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.String_comp or _la==BKOOLParser.String_concat):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 377
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Logical_exprContext,i)


        def Equal(self):
            return self.getToken(BKOOLParser.Equal, 0)

        def Diff(self):
            return self.getToken(BKOOLParser.Diff, 0)

        def Greater(self):
            return self.getToken(BKOOLParser.Greater, 0)

        def Lesser(self):
            return self.getToken(BKOOLParser.Lesser, 0)

        def Greater_euqal(self):
            return self.getToken(BKOOLParser.Greater_euqal, 0)

        def Lesser_equal(self):
            return self.getToken(BKOOLParser.Lesser_equal, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = BKOOLParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 387
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.logical_expr()
                self.state = 383
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Equal) | (1 << BKOOLParser.Diff) | (1 << BKOOLParser.Greater) | (1 << BKOOLParser.Lesser) | (1 << BKOOLParser.Greater_euqal) | (1 << BKOOLParser.Lesser_equal))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 384
                self.logical_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 386
                self.logical_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Adding_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Adding_exprContext,i)


        def And(self):
            return self.getToken(BKOOLParser.And, 0)

        def Or(self):
            return self.getToken(BKOOLParser.Or, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)




    def logical_expr(self):

        localctx = BKOOLParser.Logical_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_logical_expr)
        self._la = 0 # Token type
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.adding_expr(0)
                self.state = 390
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.And or _la==BKOOLParser.Or):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 391
                self.adding_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.adding_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Adding_exprContext,0)


        def Add(self):
            return self.getToken(BKOOLParser.Add, 0)

        def Sub(self):
            return self.getToken(BKOOLParser.Sub, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 399
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 400
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.Add or _la==BKOOLParser.Sub):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 401
                    self.multiplying_expr(0) 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_not_exprContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Multiplying_exprContext,0)


        def Mul(self):
            return self.getToken(BKOOLParser.Mul, 0)

        def Div(self):
            return self.getToken(BKOOLParser.Div, 0)

        def Mod(self):
            return self.getToken(BKOOLParser.Mod, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.logical_not_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 410
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 411
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Mul) | (1 << BKOOLParser.Div) | (1 << BKOOLParser.Mod))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 412
                    self.logical_not_expr() 
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_not_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Not(self):
            return self.getToken(BKOOLParser.Not, 0)

        def logical_not_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Logical_not_exprContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_logical_not_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_not_expr" ):
                return visitor.visitLogical_not_expr(self)
            else:
                return visitor.visitChildren(self)




    def logical_not_expr(self):

        localctx = BKOOLParser.Logical_not_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_logical_not_expr)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKOOLParser.Not)
                self.state = 419
                self.logical_not_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.Sub, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Sub(self):
            return self.getToken(BKOOLParser.Sub, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sign_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = BKOOLParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_sign_expr)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.Sub]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(BKOOLParser.Sub)
                self.state = 424
                self.sign_expr()
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.KEYWORD_NEW, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.index_expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Class_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Index_exprContext,0)


        def Member_access_in_ope(self):
            return self.getToken(BKOOLParser.Member_access_in_ope, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LSB)
            else:
                return self.getToken(BKOOLParser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.RSB)
            else:
                return self.getToken(BKOOLParser.RSB, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)



    def index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.class_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 453
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 431
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 449
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKOOLParser.LSB]:
                        self.state = 436 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 432
                                self.match(BKOOLParser.LSB)
                                self.state = 433
                                self.expr()
                                self.state = 434
                                self.match(BKOOLParser.RSB)

                            else:
                                raise NoViableAltException(self)
                            self.state = 438 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                        pass
                    elif token in [BKOOLParser.Member_access_in_ope]:
                        self.state = 440
                        self.match(BKOOLParser.Member_access_in_ope)
                        self.state = 441
                        self.class_expr()
                        self.state = 447
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                        if la_ == 1:
                            self.state = 442
                            self.match(BKOOLParser.LP)
                            self.state = 444
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                                self.state = 443
                                self.expr_list()


                            self.state = 446
                            self.match(BKOOLParser.RP)


                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 455
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Class_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD_NEW(self):
            return self.getToken(BKOOLParser.KEYWORD_NEW, 0)

        def class_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Class_exprContext,0)


        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr_list(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_listContext,0)


        def piority_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Piority_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_expr" ):
                return visitor.visitClass_expr(self)
            else:
                return visitor.visitChildren(self)




    def class_expr(self):

        localctx = BKOOLParser.Class_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_class_expr)
        self._la = 0 # Token type
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.KEYWORD_NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(BKOOLParser.KEYWORD_NEW)
                self.state = 457
                self.class_expr()
                self.state = 458
                self.match(BKOOLParser.LP)
                self.state = 460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                    self.state = 459
                    self.expr_list()


                self.state = 462
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS, BKOOLParser.LP, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.piority_exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Piority_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def array_exp(self):
            return self.getTypedRuleContext(BKOOLParser.Array_expContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_piority_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPiority_exp" ):
                return visitor.visitPiority_exp(self)
            else:
                return visitor.visitChildren(self)




    def piority_exp(self):

        localctx = BKOOLParser.Piority_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_piority_exp)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(BKOOLParser.LP)
                self.state = 468
                self.expr()
                self.state = 469
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS, BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
                self.array_exp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def operands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.OperandsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.OperandsContext,i)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_exp" ):
                return visitor.visitArray_exp(self)
            else:
                return visitor.visitChildren(self)




    def array_exp(self):

        localctx = BKOOLParser.Array_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_exp)
        self._la = 0 # Token type
        try:
            self.state = 486
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(BKOOLParser.LB)
                self.state = 475
                self.operands()
                self.state = 480
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMA:
                    self.state = 476
                    self.match(BKOOLParser.COMA)
                    self.state = 477
                    self.operands()
                    self.state = 482
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 483
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.Prog_word, BKOOLParser.Array_word, BKOOLParser.Main_word, BKOOLParser.Self_word, BKOOLParser.ID, BKOOLParser.BOOLEANLIT, BKOOLParser.STRINGLIT, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.CLASS, BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(BKOOLParser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arrayLIT(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayLITContext,0)


        def multi_ArrayLIT(self):
            return self.getTypedRuleContext(BKOOLParser.Multi_ArrayLITContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def Self_word(self):
            return self.getToken(BKOOLParser.Self_word, 0)

        def class_name(self):
            return self.getTypedRuleContext(BKOOLParser.Class_nameContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_operands)
        try:
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.match(BKOOLParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.match(BKOOLParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 490
                self.match(BKOOLParser.BOOLEANLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 491
                self.match(BKOOLParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 492
                self.arrayLIT()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 493
                self.multi_ArrayLIT()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 494
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 495
                self.match(BKOOLParser.Self_word)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 496
                self.class_name()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 497
                self.match(BKOOLParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_idlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(BKOOLParser.ID)
            self.state = 505
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 501
                    self.match(BKOOLParser.COMA)
                    self.state = 502
                    self.match(BKOOLParser.ID) 
                self.state = 507
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array_word(self):
            return self.getToken(BKOOLParser.Array_word, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_multi_ArrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_ArrayLIT" ):
                return visitor.visitMulti_ArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def multi_ArrayLIT(self):

        localctx = BKOOLParser.Multi_ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_multi_ArrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(BKOOLParser.Array_word)
            self.state = 509
            self.match(BKOOLParser.LP)
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.Array_word:
                self.state = 510
                self.array_list()


            self.state = 513
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayLIT(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ArrayLITContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ArrayLITContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.arrayLIT()
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 516
                self.match(BKOOLParser.COMA)
                self.state = 517
                self.arrayLIT()
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLITContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Array_word(self):
            return self.getToken(BKOOLParser.Array_word, 0)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def element_list(self):
            return self.getTypedRuleContext(BKOOLParser.Element_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayLIT

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLIT" ):
                return visitor.visitArrayLIT(self)
            else:
                return visitor.visitChildren(self)




    def arrayLIT(self):

        localctx = BKOOLParser.ArrayLITContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_arrayLIT)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(BKOOLParser.Array_word)
            self.state = 524
            self.match(BKOOLParser.LP)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.Prog_word) | (1 << BKOOLParser.Array_word) | (1 << BKOOLParser.Main_word) | (1 << BKOOLParser.Self_word) | (1 << BKOOLParser.ID) | (1 << BKOOLParser.Sub) | (1 << BKOOLParser.Not) | (1 << BKOOLParser.BOOLEANLIT) | (1 << BKOOLParser.STRINGLIT) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (BKOOLParser.CLASS - 73)) | (1 << (BKOOLParser.KEYWORD_NEW - 73)) | (1 << (BKOOLParser.THIS - 73)) | (1 << (BKOOLParser.LP - 73)) | (1 << (BKOOLParser.LB - 73)))) != 0):
                self.state = 525
                self.element_list()


            self.state = 528
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ElementsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ElementsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMA)
            else:
                return self.getToken(BKOOLParser.COMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = BKOOLParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.elements()
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMA:
                self.state = 531
                self.match(BKOOLParser.COMA)
                self.state = 532
                self.elements()
                self.state = 537
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = BKOOLParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[43] = self.adding_expr_sempred
        self._predicates[44] = self.multiplying_expr_sempred
        self._predicates[47] = self.index_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def index_expr_sempred(self, localctx:Index_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




