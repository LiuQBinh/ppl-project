# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


    from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2|")
        buf.write("\u036d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4")
        buf.write("p\tp\4q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4")
        buf.write("y\ty\4z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080")
        buf.write("\t\u0080\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083")
        buf.write("\4\u0084\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087")
        buf.write("\t\u0087\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u013c\n\23\f\23\16\23\u013f\13\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u0147\n\24\f\24\16\24\u014a")
        buf.write("\13\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\7\25\u0153\n")
        buf.write("\25\f\25\16\25\u0156\13\25\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\5\37\u016e\n\37\3 \3 \7")
        buf.write(" \u0172\n \f \16 \u0175\13 \3!\3!\6!\u0179\n!\r!\16!\u017a")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u01a5\n")
        buf.write("\65\3\66\3\66\3\66\7\66\u01aa\n\66\f\66\16\66\u01ad\13")
        buf.write("\66\3\66\3\66\3\66\3\66\7\66\u01b3\n\66\f\66\16\66\u01b6")
        buf.write("\13\66\3\66\3\66\7\66\u01ba\n\66\f\66\16\66\u01bd\13\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\38\58\u01ca")
        buf.write("\n8\39\39\39\39\39\39\39\39\39\59\u01d5\n9\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3=\7=\u01e7\n=\f=\16")
        buf.write("=\u01ea\13=\3=\3=\3=\3=\3=\3>\3>\3>\3>\5>\u01f5\n>\3>")
        buf.write("\3>\3?\3?\3?\3?\3?\3?\5?\u01ff\n?\3?\3?\3@\3@\3A\3A\5")
        buf.write("A\u0207\nA\3A\6A\u020a\nA\rA\16A\u020b\3B\3B\7B\u0210")
        buf.write("\nB\fB\16B\u0213\13B\3C\3C\3C\7C\u0218\nC\fC\16C\u021b")
        buf.write("\13C\3C\5C\u021e\nC\3C\6C\u0221\nC\rC\16C\u0222\7C\u0225")
        buf.write("\nC\fC\16C\u0228\13C\5C\u022a\nC\3D\3D\3D\7D\u022f\nD")
        buf.write("\fD\16D\u0232\13D\3E\3E\3E\3E\7E\u0238\nE\fE\16E\u023b")
        buf.write("\13E\3F\3F\3F\3F\7F\u0241\nF\fF\16F\u0244\13F\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3")
        buf.write("I\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3K\3K\3L\3L\3")
        buf.write("L\3M\3M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3P\3")
        buf.write("P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3")
        buf.write("S\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3W\3W\3W\3W\3W\3W\3W\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3]\3]\3")
        buf.write("]\3]\3]\3]\3]\3]\3]\3]\3]\3]\3^\3^\3^\3^\3^\3^\3^\3^\3")
        buf.write("^\3^\3^\3_\3_\3_\3_\3`\3`\3`\3a\3a\3a\3b\3b\3b\3b\3b\3")
        buf.write("b\3b\3c\3c\3c\3c\3c\3d\3d\3d\3d\3d\3e\3e\3e\3e\3f\3f\3")
        buf.write("f\3f\3f\3g\3g\3g\3g\3g\3g\3h\3h\3h\3h\3h\3h\3h\3i\3i\3")
        buf.write("i\3j\3j\3j\3j\3j\3j\3j\3k\3k\3l\3l\3m\3m\3n\3n\3o\3o\3")
        buf.write("p\3p\3q\3q\3q\3r\3r\3r\3s\3s\3s\3t\3t\3t\3u\3u\3v\3v\3")
        buf.write("w\3w\3x\3x\3x\3y\3y\3y\3z\3z\3z\3z\3{\3{\3{\3|\3|\3}\3")
        buf.write("}\3}\3~\3~\3\177\3\177\3\u0080\3\u0080\3\u0081\3\u0081")
        buf.write("\3\u0082\3\u0082\3\u0083\3\u0083\3\u0084\3\u0084\3\u0085")
        buf.write("\3\u0085\3\u0086\3\u0086\3\u0087\3\u0087\3\u0088\6\u0088")
        buf.write("\u0359\n\u0088\r\u0088\16\u0088\u035a\3\u0088\3\u0088")
        buf.write("\3\u0089\3\u0089\3\u0089\3\u0089\7\u0089\u0363\n\u0089")
        buf.write("\f\u0089\16\u0089\u0366\13\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\3\u008a\3\u008a\3\u008a\5\u0148\u01e8\u0364\2\u008b\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?\2A\2C!E\"G#I$K%M&O\'")
        buf.write("Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\2o\2q\2s\2u")
        buf.write("\2w\2y\66{\67}8\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d9\u008f:\u0091;\u0093<\u0095=\u0097")
        buf.write(">\u0099?\u009b@\u009dA\u009fB\u00a1C\u00a3D\u00a5E\u00a7")
        buf.write("F\u00a9G\u00abH\u00adI\u00afJ\u00b1K\u00b3L\u00b5M\u00b7")
        buf.write("N\u00b9O\u00bbP\u00bdQ\u00bfR\u00c1S\u00c3T\u00c5U\u00c7")
        buf.write("V\u00c9W\u00cbX\u00cdY\u00cfZ\u00d1[\u00d3\\\u00d5]\u00d7")
        buf.write("^\u00d9_\u00db`\u00dda\u00dfb\u00e1c\u00e3d\u00e5e\u00e7")
        buf.write("f\u00e9g\u00ebh\u00edi\u00efj\u00f1k\u00f3l\u00f5m\u00f7")
        buf.write("n\u00f9o\u00fbp\u00fdq\u00ffr\u0101s\u0103t\u0105u\u0107")
        buf.write("v\u0109w\u010bx\u010dy\u010fz\u0111{\u0113|\3\2\25\4\2")
        buf.write("\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\3\2$$\t\2))^^ddh")
        buf.write("hppttvv\5\2\62;CHch\4\2GGgg\4\2--//\3\2\62;\3\2\63;\3")
        buf.write("\2\629\4\2\629aa\4\2ZZzz\4\2\62;CH\5\2\62;CHaa\4\2DDd")
        buf.write("d\3\2\62\63\4\2\62\63aa\5\2\n\f\16\17\"\"\2\u0381\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2C\3\2\2\2\2")
        buf.write("E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write("\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2")
        buf.write("\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd")
        buf.write("\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2")
        buf.write("\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db")
        buf.write("\3\2\2\2\2\u00dd\3\2\2\2\2\u00df\3\2\2\2\2\u00e1\3\2\2")
        buf.write("\2\2\u00e3\3\2\2\2\2\u00e5\3\2\2\2\2\u00e7\3\2\2\2\2\u00e9")
        buf.write("\3\2\2\2\2\u00eb\3\2\2\2\2\u00ed\3\2\2\2\2\u00ef\3\2\2")
        buf.write("\2\2\u00f1\3\2\2\2\2\u00f3\3\2\2\2\2\u00f5\3\2\2\2\2\u00f7")
        buf.write("\3\2\2\2\2\u00f9\3\2\2\2\2\u00fb\3\2\2\2\2\u00fd\3\2\2")
        buf.write("\2\2\u00ff\3\2\2\2\2\u0101\3\2\2\2\2\u0103\3\2\2\2\2\u0105")
        buf.write("\3\2\2\2\2\u0107\3\2\2\2\2\u0109\3\2\2\2\2\u010b\3\2\2")
        buf.write("\2\2\u010d\3\2\2\2\2\u010f\3\2\2\2\2\u0111\3\2\2\2\2\u0113")
        buf.write("\3\2\2\2\3\u0115\3\2\2\2\5\u0117\3\2\2\2\7\u0119\3\2\2")
        buf.write("\2\t\u011b\3\2\2\2\13\u011d\3\2\2\2\r\u011f\3\2\2\2\17")
        buf.write("\u0121\3\2\2\2\21\u0123\3\2\2\2\23\u0125\3\2\2\2\25\u0127")
        buf.write("\3\2\2\2\27\u0129\3\2\2\2\31\u012b\3\2\2\2\33\u012d\3")
        buf.write("\2\2\2\35\u012f\3\2\2\2\37\u0131\3\2\2\2!\u0133\3\2\2")
        buf.write("\2#\u0135\3\2\2\2%\u0137\3\2\2\2\'\u0142\3\2\2\2)\u0150")
        buf.write("\3\2\2\2+\u0159\3\2\2\2-\u015b\3\2\2\2/\u015d\3\2\2\2")
        buf.write("\61\u015f\3\2\2\2\63\u0161\3\2\2\2\65\u0163\3\2\2\2\67")
        buf.write("\u0165\3\2\2\29\u0167\3\2\2\2;\u0169\3\2\2\2=\u016d\3")
        buf.write("\2\2\2?\u016f\3\2\2\2A\u0176\3\2\2\2C\u017c\3\2\2\2E\u017e")
        buf.write("\3\2\2\2G\u0180\3\2\2\2I\u0182\3\2\2\2K\u0184\3\2\2\2")
        buf.write("M\u0186\3\2\2\2O\u0188\3\2\2\2Q\u018a\3\2\2\2S\u018c\3")
        buf.write("\2\2\2U\u018e\3\2\2\2W\u0190\3\2\2\2Y\u0192\3\2\2\2[\u0194")
        buf.write("\3\2\2\2]\u0196\3\2\2\2_\u0198\3\2\2\2a\u019a\3\2\2\2")
        buf.write("c\u019c\3\2\2\2e\u019e\3\2\2\2g\u01a0\3\2\2\2i\u01a4\3")
        buf.write("\2\2\2k\u01a6\3\2\2\2m\u01c1\3\2\2\2o\u01c9\3\2\2\2q\u01d4")
        buf.write("\3\2\2\2s\u01d6\3\2\2\2u\u01dd\3\2\2\2w\u01df\3\2\2\2")
        buf.write("y\u01e2\3\2\2\2{\u01f4\3\2\2\2}\u01f8\3\2\2\2\177\u0202")
        buf.write("\3\2\2\2\u0081\u0204\3\2\2\2\u0083\u020d\3\2\2\2\u0085")
        buf.write("\u0229\3\2\2\2\u0087\u022b\3\2\2\2\u0089\u0233\3\2\2\2")
        buf.write("\u008b\u023c\3\2\2\2\u008d\u0245\3\2\2\2\u008f\u024d\3")
        buf.write("\2\2\2\u0091\u0252\3\2\2\2\u0093\u025a\3\2\2\2\u0095\u0260")
        buf.write("\3\2\2\2\u0097\u0269\3\2\2\2\u0099\u026c\3\2\2\2\u009b")
        buf.write("\u0273\3\2\2\2\u009d\u0278\3\2\2\2\u009f\u027c\3\2\2\2")
        buf.write("\u00a1\u0281\3\2\2\2\u00a3\u0287\3\2\2\2\u00a5\u028d\3")
        buf.write("\2\2\2\u00a7\u0290\3\2\2\2\u00a9\u0294\3\2\2\2\u00ab\u029a")
        buf.write("\3\2\2\2\u00ad\u02a2\3\2\2\2\u00af\u02a9\3\2\2\2\u00b1")
        buf.write("\u02af\3\2\2\2\u00b3\u02b4\3\2\2\2\u00b5\u02b8\3\2\2\2")
        buf.write("\u00b7\u02bc\3\2\2\2\u00b9\u02c1\3\2\2\2\u00bb\u02cd\3")
        buf.write("\2\2\2\u00bd\u02d8\3\2\2\2\u00bf\u02dc\3\2\2\2\u00c1\u02df")
        buf.write("\3\2\2\2\u00c3\u02e2\3\2\2\2\u00c5\u02e9\3\2\2\2\u00c7")
        buf.write("\u02ee\3\2\2\2\u00c9\u02f3\3\2\2\2\u00cb\u02f7\3\2\2\2")
        buf.write("\u00cd\u02fc\3\2\2\2\u00cf\u0302\3\2\2\2\u00d1\u0309\3")
        buf.write("\2\2\2\u00d3\u030c\3\2\2\2\u00d5\u0313\3\2\2\2\u00d7\u0315")
        buf.write("\3\2\2\2\u00d9\u0317\3\2\2\2\u00db\u0319\3\2\2\2\u00dd")
        buf.write("\u031b\3\2\2\2\u00df\u031d\3\2\2\2\u00e1\u031f\3\2\2\2")
        buf.write("\u00e3\u0322\3\2\2\2\u00e5\u0325\3\2\2\2\u00e7\u0328\3")
        buf.write("\2\2\2\u00e9\u032b\3\2\2\2\u00eb\u032d\3\2\2\2\u00ed\u032f")
        buf.write("\3\2\2\2\u00ef\u0331\3\2\2\2\u00f1\u0334\3\2\2\2\u00f3")
        buf.write("\u0337\3\2\2\2\u00f5\u033b\3\2\2\2\u00f7\u033e\3\2\2\2")
        buf.write("\u00f9\u0340\3\2\2\2\u00fb\u0343\3\2\2\2\u00fd\u0345\3")
        buf.write("\2\2\2\u00ff\u0347\3\2\2\2\u0101\u0349\3\2\2\2\u0103\u034b")
        buf.write("\3\2\2\2\u0105\u034d\3\2\2\2\u0107\u034f\3\2\2\2\u0109")
        buf.write("\u0351\3\2\2\2\u010b\u0353\3\2\2\2\u010d\u0355\3\2\2\2")
        buf.write("\u010f\u0358\3\2\2\2\u0111\u035e\3\2\2\2\u0113\u036a\3")
        buf.write("\2\2\2\u0115\u0116\5\u00afX\2\u0116\4\3\2\2\2\u0117\u0118")
        buf.write("\5\u008dG\2\u0118\6\3\2\2\2\u0119\u011a\5\u0091I\2\u011a")
        buf.write("\b\3\2\2\2\u011b\u011c\5\u00cfh\2\u011c\n\3\2\2\2\u011d")
        buf.write("\u011e\5\u00cdg\2\u011e\f\3\2\2\2\u011f\u0120\5\u00c7")
        buf.write("d\2\u0120\16\3\2\2\2\u0121\u0122\5\u00b5[\2\u0122\20\3")
        buf.write("\2\2\2\u0123\u0124\5\u00b3Z\2\u0124\22\3\2\2\2\u0125\u0126")
        buf.write("\5\u0097L\2\u0126\24\3\2\2\2\u0127\u0128\5\u00c5c\2\u0128")
        buf.write("\26\3\2\2\2\u0129\u012a\5\u009bN\2\u012a\30\3\2\2\2\u012b")
        buf.write("\u012c\5\u0099M\2\u012c\32\3\2\2\2\u012d\u012e\5\u009d")
        buf.write("O\2\u012e\34\3\2\2\2\u012f\u0130\5\u00e9u\2\u0130\36\3")
        buf.write("\2\2\2\u0131\u0132\5\u00d1i\2\u0132 \3\2\2\2\u0133\u0134")
        buf.write("\5\u00c1a\2\u0134\"\3\2\2\2\u0135\u0136\5\u0093J\2\u0136")
        buf.write("$\3\2\2\2\u0137\u0138\7\61\2\2\u0138\u0139\7\61\2\2\u0139")
        buf.write("\u013d\3\2\2\2\u013a\u013c\n\2\2\2\u013b\u013a\3\2\2\2")
        buf.write("\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3")
        buf.write("\2\2\2\u013e\u0140\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141")
        buf.write("\b\23\2\2\u0141&\3\2\2\2\u0142\u0143\7\61\2\2\u0143\u0144")
        buf.write("\7,\2\2\u0144\u0148\3\2\2\2\u0145\u0147\13\2\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0149\u014b\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014b\u014c\7,\2\2\u014c\u014d\7\61\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u014f\b\24\2\2\u014f(\3\2\2\2\u0150\u0154")
        buf.write("\7%\2\2\u0151\u0153\n\2\2\2\u0152\u0151\3\2\2\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2")
        buf.write("\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0157\u0158\b")
        buf.write("\25\2\2\u0158*\3\2\2\2\u0159\u015a\5\u00abV\2\u015a,\3")
        buf.write("\2\2\2\u015b\u015c\5\u00a7T\2\u015c.\3\2\2\2\u015d\u015e")
        buf.write("\5\u00a9U\2\u015e\60\3\2\2\2\u015f\u0160\5\u00c3b\2\u0160")
        buf.write("\62\3\2\2\2\u0161\u0162\5\u00a3R\2\u0162\64\3\2\2\2\u0163")
        buf.write("\u0164\5\u008fH\2\u0164\66\3\2\2\2\u0165\u0166\5\u00b9")
        buf.write("]\2\u01668\3\2\2\2\u0167\u0168\5\u00bb^\2\u0168:\3\2\2")
        buf.write("\2\u0169\u016a\5\u00b7\\\2\u016a<\3\2\2\2\u016b\u016e")
        buf.write("\5? \2\u016c\u016e\5A!\2\u016d\u016b\3\2\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016e>\3\2\2\2\u016f\u0173\t\3\2\2\u0170\u0172")
        buf.write("\t\4\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174@\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u0178\7&\2\2\u0177\u0179\t\4\2\2")
        buf.write("\u0178\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017a\u017b\3\2\2\2\u017bB\3\2\2\2\u017c\u017d")
        buf.write("\5\u00d5k\2\u017dD\3\2\2\2\u017e\u017f\5\u00d7l\2\u017f")
        buf.write("F\3\2\2\2\u0180\u0181\5\u00d9m\2\u0181H\3\2\2\2\u0182")
        buf.write("\u0183\5\u00dbn\2\u0183J\3\2\2\2\u0184\u0185\5\u00ddo")
        buf.write("\2\u0185L\3\2\2\2\u0186\u0187\5\u00dfp\2\u0187N\3\2\2")
        buf.write("\2\u0188\u0189\5\u00e1q\2\u0189P\3\2\2\2\u018a\u018b\5")
        buf.write("\u00e3r\2\u018bR\3\2\2\2\u018c\u018d\5\u00e5s\2\u018d")
        buf.write("T\3\2\2\2\u018e\u018f\5\u00e7t\2\u018fV\3\2\2\2\u0190")
        buf.write("\u0191\5\u00ebv\2\u0191X\3\2\2\2\u0192\u0193\5\u00edw")
        buf.write("\2\u0193Z\3\2\2\2\u0194\u0195\5\u00efx\2\u0195\\\3\2\2")
        buf.write("\2\u0196\u0197\5\u00f1y\2\u0197^\3\2\2\2\u0198\u0199\5")
        buf.write("\u00f3z\2\u0199`\3\2\2\2\u019a\u019b\5\u00f5{\2\u019b")
        buf.write("b\3\2\2\2\u019c\u019d\5\u0109\u0085\2\u019dd\3\2\2\2\u019e")
        buf.write("\u019f\5\u00f9}\2\u019ff\3\2\2\2\u01a0\u01a1\5\u010d\u0087")
        buf.write("\2\u01a1h\3\2\2\2\u01a2\u01a5\5\u009fP\2\u01a3\u01a5\5")
        buf.write("\u00a1Q\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("j\3\2\2\2\u01a6\u01ab\7$\2\2\u01a7\u01a8\7)\2\2\u01a8")
        buf.write("\u01aa\7$\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ad\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01b4\3")
        buf.write("\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b3\5m\67\2\u01af\u01b3")
        buf.write("\n\5\2\2\u01b0\u01b1\7)\2\2\u01b1\u01b3\7$\2\2\u01b2\u01ae")
        buf.write("\3\2\2\2\u01b2\u01af\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01bb\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7\u01b8\7")
        buf.write(")\2\2\u01b8\u01ba\7$\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01bf\7$\2\2")
        buf.write("\u01bf\u01c0\b\66\3\2\u01c0l\3\2\2\2\u01c1\u01c2\7^\2")
        buf.write("\2\u01c2\u01c3\t\6\2\2\u01c3n\3\2\2\2\u01c4\u01c5\7^\2")
        buf.write("\2\u01c5\u01ca\n\6\2\2\u01c6\u01ca\5s:\2\u01c7\u01ca\5")
        buf.write("q9\2\u01c8\u01ca\5w<\2\u01c9\u01c4\3\2\2\2\u01c9\u01c6")
        buf.write("\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("p\3\2\2\2\u01cb\u01cc\7^\2\2\u01cc\u01cd\4\62\65\2\u01cd")
        buf.write("\u01ce\4\629\2\u01ce\u01d5\4\629\2\u01cf\u01d0\7^\2\2")
        buf.write("\u01d0\u01d1\4\629\2\u01d1\u01d5\4\629\2\u01d2\u01d3\7")
        buf.write("^\2\2\u01d3\u01d5\4\629\2\u01d4\u01cb\3\2\2\2\u01d4\u01cf")
        buf.write("\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5r\3\2\2\2\u01d6\u01d7")
        buf.write("\7^\2\2\u01d7\u01d8\7w\2\2\u01d8\u01d9\5u;\2\u01d9\u01da")
        buf.write("\5u;\2\u01da\u01db\5u;\2\u01db\u01dc\5u;\2\u01dct\3\2")
        buf.write("\2\2\u01dd\u01de\t\7\2\2\u01dev\3\2\2\2\u01df\u01e0\7")
        buf.write("^\2\2\u01e0\u01e1\7j\2\2\u01e1x\3\2\2\2\u01e2\u01e3\7")
        buf.write("%\2\2\u01e3\u01e4\7%\2\2\u01e4\u01e8\3\2\2\2\u01e5\u01e7")
        buf.write("\13\2\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\3\2\2\2")
        buf.write("\u01ea\u01e8\3\2\2\2\u01eb\u01ec\7%\2\2\u01ec\u01ed\7")
        buf.write("%\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\b=\2\2\u01efz\3")
        buf.write("\2\2\2\u01f0\u01f5\5\u0085C\2\u01f1\u01f5\5\u0087D\2\u01f2")
        buf.write("\u01f5\5\u0089E\2\u01f3\u01f5\5\u008bF\2\u01f4\u01f0\3")
        buf.write("\2\2\2\u01f4\u01f1\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\b>\4\2\u01f7")
        buf.write("|\3\2\2\2\u01f8\u01fe\5\177@\2\u01f9\u01ff\5\u0083B\2")
        buf.write("\u01fa\u01ff\5\u0081A\2\u01fb\u01fc\5\u0083B\2\u01fc\u01fd")
        buf.write("\5\u0081A\2\u01fd\u01ff\3\2\2\2\u01fe\u01f9\3\2\2\2\u01fe")
        buf.write("\u01fa\3\2\2\2\u01fe\u01fb\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0201\b?\5\2\u0201~\3\2\2\2\u0202\u0203\5\u0085")
        buf.write("C\2\u0203\u0080\3\2\2\2\u0204\u0206\t\b\2\2\u0205\u0207")
        buf.write("\t\t\2\2\u0206\u0205\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0209\3\2\2\2\u0208\u020a\t\n\2\2\u0209\u0208\3\2\2\2")
        buf.write("\u020a\u020b\3\2\2\2\u020b\u0209\3\2\2\2\u020b\u020c\3")
        buf.write("\2\2\2\u020c\u0082\3\2\2\2\u020d\u0211\5\u0109\u0085\2")
        buf.write("\u020e\u0210\t\n\2\2\u020f\u020e\3\2\2\2\u0210\u0213\3")
        buf.write("\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0084")
        buf.write("\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u022a\7\62\2\2\u0215")
        buf.write("\u0226\t\13\2\2\u0216\u0218\t\n\2\2\u0217\u0216\3\2\2")
        buf.write("\2\u0218\u021b\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021c")
        buf.write("\u021e\7a\2\2\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u0220\3\2\2\2\u021f\u0221\t\n\2\2\u0220\u021f\3")
        buf.write("\2\2\2\u0221\u0222\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0219\3\2\2\2\u0225")
        buf.write("\u0228\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2")
        buf.write("\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u0214\3")
        buf.write("\2\2\2\u0229\u0215\3\2\2\2\u022a\u0086\3\2\2\2\u022b\u022c")
        buf.write("\7\62\2\2\u022c\u0230\t\f\2\2\u022d\u022f\t\r\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0088\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0234\7\62\2\2\u0234\u0235\t\16\2\2\u0235")
        buf.write("\u0239\t\17\2\2\u0236\u0238\t\20\2\2\u0237\u0236\3\2\2")
        buf.write("\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a")
        buf.write("\3\2\2\2\u023a\u008a\3\2\2\2\u023b\u0239\3\2\2\2\u023c")
        buf.write("\u023d\7\62\2\2\u023d\u023e\t\21\2\2\u023e\u0242\t\22")
        buf.write("\2\2\u023f\u0241\t\23\2\2\u0240\u023f\3\2\2\2\u0241\u0244")
        buf.write("\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243")
        buf.write("\u008c\3\2\2\2\u0244\u0242\3\2\2\2\u0245\u0246\7R\2\2")
        buf.write("\u0246\u0247\7t\2\2\u0247\u0248\7q\2\2\u0248\u0249\7i")
        buf.write("\2\2\u0249\u024a\7t\2\2\u024a\u024b\7c\2\2\u024b\u024c")
        buf.write("\7o\2\2\u024c\u008e\3\2\2\2\u024d\u024e\7o\2\2\u024e\u024f")
        buf.write("\7c\2\2\u024f\u0250\7k\2\2\u0250\u0251\7p\2\2\u0251\u0090")
        buf.write("\3\2\2\2\u0252\u0253\7g\2\2\u0253\u0254\7z\2\2\u0254\u0255")
        buf.write("\7v\2\2\u0255\u0256\7g\2\2\u0256\u0257\7p\2\2\u0257\u0258")
        buf.write("\7f\2\2\u0258\u0259\7u\2\2\u0259\u0092\3\2\2\2\u025a\u025b")
        buf.write("\7d\2\2\u025b\u025c\7t\2\2\u025c\u025d\7g\2\2\u025d\u025e")
        buf.write("\7c\2\2\u025e\u025f\7m\2\2\u025f\u0094\3\2\2\2\u0260\u0261")
        buf.write("\7e\2\2\u0261\u0262\7q\2\2\u0262\u0263\7p\2\2\u0263\u0264")
        buf.write("\7v\2\2\u0264\u0265\7k\2\2\u0265\u0266\7p\2\2\u0266\u0267")
        buf.write("\7w\2\2\u0267\u0268\7g\2\2\u0268\u0096\3\2\2\2\u0269\u026a")
        buf.write("\7k\2\2\u026a\u026b\7h\2\2\u026b\u0098\3\2\2\2\u026c\u026d")
        buf.write("\7g\2\2\u026d\u026e\7n\2\2\u026e\u026f\7u\2\2\u026f\u0270")
        buf.write("\7g\2\2\u0270\u0271\7k\2\2\u0271\u0272\7h\2\2\u0272\u009a")
        buf.write("\3\2\2\2\u0273\u0274\7g\2\2\u0274\u0275\7n\2\2\u0275\u0276")
        buf.write("\7u\2\2\u0276\u0277\7g\2\2\u0277\u009c\3\2\2\2\u0278\u0279")
        buf.write("\7h\2\2\u0279\u027a\7q\2\2\u027a\u027b\7t\2\2\u027b\u009e")
        buf.write("\3\2\2\2\u027c\u027d\7v\2\2\u027d\u027e\7t\2\2\u027e\u027f")
        buf.write("\7w\2\2\u027f\u0280\7g\2\2\u0280\u00a0\3\2\2\2\u0281\u0282")
        buf.write("\7h\2\2\u0282\u0283\7c\2\2\u0283\u0284\7n\2\2\u0284\u0285")
        buf.write("\7u\2\2\u0285\u0286\7g\2\2\u0286\u00a2\3\2\2\2\u0287\u0288")
        buf.write("\7c\2\2\u0288\u0289\7t\2\2\u0289\u028a\7t\2\2\u028a\u028b")
        buf.write("\7c\2\2\u028b\u028c\7{\2\2\u028c\u00a4\3\2\2\2\u028d\u028e")
        buf.write("\7k\2\2\u028e\u028f\7p\2\2\u028f\u00a6\3\2\2\2\u0290\u0291")
        buf.write("\7k\2\2\u0291\u0292\7p\2\2\u0292\u0293\7v\2\2\u0293\u00a8")
        buf.write("\3\2\2\2\u0294\u0295\7h\2\2\u0295\u0296\7n\2\2\u0296\u0297")
        buf.write("\7q\2\2\u0297\u0298\7c\2\2\u0298\u0299\7v\2\2\u0299\u00aa")
        buf.write("\3\2\2\2\u029a\u029b\7d\2\2\u029b\u029c\7q\2\2\u029c\u029d")
        buf.write("\7q\2\2\u029d\u029e\7n\2\2\u029e\u029f\7g\2\2\u029f\u02a0")
        buf.write("\7c\2\2\u02a0\u02a1\7p\2\2\u02a1\u00ac\3\2\2\2\u02a2\u02a3")
        buf.write("\7t\2\2\u02a3\u02a4\7g\2\2\u02a4\u02a5\7v\2\2\u02a5\u02a6")
        buf.write("\7w\2\2\u02a6\u02a7\7t\2\2\u02a7\u02a8\7p\2\2\u02a8\u00ae")
        buf.write("\3\2\2\2\u02a9\u02aa\7e\2\2\u02aa\u02ab\7n\2\2\u02ab\u02ac")
        buf.write("\7c\2\2\u02ac\u02ad\7u\2\2\u02ad\u02ae\7u\2\2\u02ae\u00b0")
        buf.write("\3\2\2\2\u02af\u02b0\7P\2\2\u02b0\u02b1\7w\2\2\u02b1\u02b2")
        buf.write("\7n\2\2\u02b2\u02b3\7n\2\2\u02b3\u00b2\3\2\2\2\u02b4\u02b5")
        buf.write("\7x\2\2\u02b5\u02b6\7c\2\2\u02b6\u02b7\7n\2\2\u02b7\u00b4")
        buf.write("\3\2\2\2\u02b8\u02b9\7x\2\2\u02b9\u02ba\7c\2\2\u02ba\u02bb")
        buf.write("\7t\2\2\u02bb\u00b6\3\2\2\2\u02bc\u02bd\7u\2\2\u02bd\u02be")
        buf.write("\7g\2\2\u02be\u02bf\7n\2\2\u02bf\u02c0\7h\2\2\u02c0\u00b8")
        buf.write("\3\2\2\2\u02c1\u02c2\7e\2\2\u02c2\u02c3\7q\2\2\u02c3\u02c4")
        buf.write("\7p\2\2\u02c4\u02c5\7u\2\2\u02c5\u02c6\7v\2\2\u02c6\u02c7")
        buf.write("\7t\2\2\u02c7\u02c8\7w\2\2\u02c8\u02c9\7e\2\2\u02c9\u02ca")
        buf.write("\7v\2\2\u02ca\u02cb\7q\2\2\u02cb\u02cc\7t\2\2\u02cc\u00ba")
        buf.write("\3\2\2\2\u02cd\u02ce\7f\2\2\u02ce\u02cf\7g\2\2\u02cf\u02d0")
        buf.write("\7u\2\2\u02d0\u02d1\7v\2\2\u02d1\u02d2\7t\2\2\u02d2\u02d3")
        buf.write("\7w\2\2\u02d3\u02d4\7e\2\2\u02d4\u02d5\7v\2\2\u02d5\u02d6")
        buf.write("\7q\2\2\u02d6\u02d7\7t\2\2\u02d7\u00bc\3\2\2\2\u02d8\u02d9")
        buf.write("\7p\2\2\u02d9\u02da\7g\2\2\u02da\u02db\7y\2\2\u02db\u00be")
        buf.write("\3\2\2\2\u02dc\u02dd\7D\2\2\u02dd\u02de\7{\2\2\u02de\u00c0")
        buf.write("\3\2\2\2\u02df\u02e0\7f\2\2\u02e0\u02e1\7q\2\2\u02e1\u00c2")
        buf.write("\3\2\2\2\u02e2\u02e3\7u\2\2\u02e3\u02e4\7v\2\2\u02e4\u02e5")
        buf.write("\7t\2\2\u02e5\u02e6\7k\2\2\u02e6\u02e7\7p\2\2\u02e7\u02e8")
        buf.write("\7i\2\2\u02e8\u00c4\3\2\2\2\u02e9\u02ea\7v\2\2\u02ea\u02eb")
        buf.write("\7j\2\2\u02eb\u02ec\7g\2\2\u02ec\u02ed\7p\2\2\u02ed\u00c6")
        buf.write("\3\2\2\2\u02ee\u02ef\7x\2\2\u02ef\u02f0\7q\2\2\u02f0\u02f1")
        buf.write("\7k\2\2\u02f1\u02f2\7f\2\2\u02f2\u00c8\3\2\2\2\u02f3\u02f4")
        buf.write("\7p\2\2\u02f4\u02f5\7k\2\2\u02f5\u02f6\7n\2\2\u02f6\u00ca")
        buf.write("\3\2\2\2\u02f7\u02f8\7v\2\2\u02f8\u02f9\7j\2\2\u02f9\u02fa")
        buf.write("\7k\2\2\u02fa\u02fb\7u\2\2\u02fb\u00cc\3\2\2\2\u02fc\u02fd")
        buf.write("\7h\2\2\u02fd\u02fe\7k\2\2\u02fe\u02ff\7p\2\2\u02ff\u0300")
        buf.write("\7c\2\2\u0300\u0301\7n\2\2\u0301\u00ce\3\2\2\2\u0302\u0303")
        buf.write("\7u\2\2\u0303\u0304\7v\2\2\u0304\u0305\7c\2\2\u0305\u0306")
        buf.write("\7v\2\2\u0306\u0307\7k\2\2\u0307\u0308\7e\2\2\u0308\u00d0")
        buf.write("\3\2\2\2\u0309\u030a\7v\2\2\u030a\u030b\7q\2\2\u030b\u00d2")
        buf.write("\3\2\2\2\u030c\u030d\7f\2\2\u030d\u030e\7q\2\2\u030e\u030f")
        buf.write("\7y\2\2\u030f\u0310\7p\2\2\u0310\u0311\7v\2\2\u0311\u0312")
        buf.write("\7q\2\2\u0312\u00d4\3\2\2\2\u0313\u0314\7-\2\2\u0314\u00d6")
        buf.write("\3\2\2\2\u0315\u0316\7/\2\2\u0316\u00d8\3\2\2\2\u0317")
        buf.write("\u0318\7,\2\2\u0318\u00da\3\2\2\2\u0319\u031a\7\61\2\2")
        buf.write("\u031a\u00dc\3\2\2\2\u031b\u031c\7\'\2\2\u031c\u00de\3")
        buf.write("\2\2\2\u031d\u031e\7#\2\2\u031e\u00e0\3\2\2\2\u031f\u0320")
        buf.write("\7(\2\2\u0320\u0321\7(\2\2\u0321\u00e2\3\2\2\2\u0322\u0323")
        buf.write("\7~\2\2\u0323\u0324\7~\2\2\u0324\u00e4\3\2\2\2\u0325\u0326")
        buf.write("\7?\2\2\u0326\u0327\7?\2\2\u0327\u00e6\3\2\2\2\u0328\u0329")
        buf.write("\7#\2\2\u0329\u032a\7?\2\2\u032a\u00e8\3\2\2\2\u032b\u032c")
        buf.write("\7?\2\2\u032c\u00ea\3\2\2\2\u032d\u032e\7@\2\2\u032e\u00ec")
        buf.write("\3\2\2\2\u032f\u0330\7>\2\2\u0330\u00ee\3\2\2\2\u0331")
        buf.write("\u0332\7@\2\2\u0332\u0333\7?\2\2\u0333\u00f0\3\2\2\2\u0334")
        buf.write("\u0335\7>\2\2\u0335\u0336\7?\2\2\u0336\u00f2\3\2\2\2\u0337")
        buf.write("\u0338\7?\2\2\u0338\u0339\7?\2\2\u0339\u033a\7\60\2\2")
        buf.write("\u033a\u00f4\3\2\2\2\u033b\u033c\7-\2\2\u033c\u033d\7")
        buf.write("\60\2\2\u033d\u00f6\3\2\2\2\u033e\u033f\7`\2\2\u033f\u00f8")
        buf.write("\3\2\2\2\u0340\u0341\7<\2\2\u0341\u0342\7<\2\2\u0342\u00fa")
        buf.write("\3\2\2\2\u0343\u0344\7*\2\2\u0344\u00fc\3\2\2\2\u0345")
        buf.write("\u0346\7+\2\2\u0346\u00fe\3\2\2\2\u0347\u0348\7]\2\2\u0348")
        buf.write("\u0100\3\2\2\2\u0349\u034a\7_\2\2\u034a\u0102\3\2\2\2")
        buf.write("\u034b\u034c\7}\2\2\u034c\u0104\3\2\2\2\u034d\u034e\7")
        buf.write("\177\2\2\u034e\u0106\3\2\2\2\u034f\u0350\7=\2\2\u0350")
        buf.write("\u0108\3\2\2\2\u0351\u0352\7\60\2\2\u0352\u010a\3\2\2")
        buf.write("\2\u0353\u0354\7.\2\2\u0354\u010c\3\2\2\2\u0355\u0356")
        buf.write("\7<\2\2\u0356\u010e\3\2\2\2\u0357\u0359\t\24\2\2\u0358")
        buf.write("\u0357\3\2\2\2\u0359\u035a\3\2\2\2\u035a\u0358\3\2\2\2")
        buf.write("\u035a\u035b\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u035d\b")
        buf.write("\u0088\2\2\u035d\u0110\3\2\2\2\u035e\u035f\7%\2\2\u035f")
        buf.write("\u0360\7%\2\2\u0360\u0364\3\2\2\2\u0361\u0363\13\2\2\2")
        buf.write("\u0362\u0361\3\2\2\2\u0363\u0366\3\2\2\2\u0364\u0365\3")
        buf.write("\2\2\2\u0364\u0362\3\2\2\2\u0365\u0367\3\2\2\2\u0366\u0364")
        buf.write("\3\2\2\2\u0367\u0368\7\2\2\3\u0368\u0369\b\u0089\6\2\u0369")
        buf.write("\u0112\3\2\2\2\u036a\u036b\13\2\2\2\u036b\u036c\b\u008a")
        buf.write("\7\2\u036c\u0114\3\2\2\2 \2\u013d\u0148\u0154\u016d\u0173")
        buf.write("\u017a\u01a4\u01ab\u01b2\u01b4\u01bb\u01c9\u01d4\u01e8")
        buf.write("\u01f4\u01fe\u0206\u020b\u0211\u0219\u021d\u0222\u0226")
        buf.write("\u0229\u0230\u0239\u0242\u035a\u0364\b\b\2\2\3\66\2\3")
        buf.write(">\3\3?\4\3\u0089\5\3\u008a\6")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Class_word = 1
    Prog_word = 2
    Extends_word = 3
    Static_word = 4
    Final_word = 5
    Void_word = 6
    Var_word = 7
    Val_word = 8
    If_word = 9
    Then_word = 10
    Else_word = 11
    Elseif_word = 12
    For_word = 13
    Assign_op = 14
    To_word = 15
    Do_word = 16
    Break_word = 17
    Comment_normal = 18
    Comment_block = 19
    Comment_sharp = 20
    Bool_word = 21
    Int_word = 22
    Float_word = 23
    Str_word = 24
    Array_word = 25
    Main_word = 26
    Cons_word = 27
    Dest_word = 28
    Self_word = 29
    ID = 30
    Add = 31
    Sub = 32
    Mul = 33
    Div = 34
    Mod = 35
    Not = 36
    And = 37
    Or = 38
    Equal = 39
    Diff = 40
    Greater = 41
    Lesser = 42
    Greater_euqal = 43
    Lesser_equal = 44
    String_comp = 45
    String_concat = 46
    Member_access_in = 47
    Member_access_out = 48
    Colon = 49
    BOOLEANLIT = 50
    STRINGLIT = 51
    BLOCKCOMMENT = 52
    INTLIT = 53
    FLOATLIT = 54
    PROGRAM = 55
    MAIN = 56
    EXTENDS = 57
    BREAK = 58
    CONT = 59
    IF = 60
    ELSEIF = 61
    ELSE = 62
    FOR = 63
    BOOLTRUE = 64
    BOOLFALSE = 65
    ARRAY = 66
    IN = 67
    INT = 68
    FLOAT = 69
    BOOL = 70
    RETURN = 71
    CLASS = 72
    NULL = 73
    VAL = 74
    VAR = 75
    SELF = 76
    CONS = 77
    DEST = 78
    KEYWORD_NEW = 79
    BY = 80
    DO = 81
    STRING = 82
    THEN = 83
    VOID = 84
    NIL = 85
    THIS = 86
    FINAL = 87
    STATIC = 88
    TO = 89
    DOWNTO = 90
    ADD_OP = 91
    SUB_OP = 92
    MUL_OP = 93
    FLOAT_DIVISION_OP = 94
    MOD_OP = 95
    NOT_OP = 96
    AND_OP = 97
    OR_OP = 98
    EQUAL_OP = 99
    NOT_EQUAL_OP = 100
    ASSIGN_OP = 101
    GREATER_OP = 102
    LESS_OP = 103
    GREATER_EQUAL_OP = 104
    LESS_EQUAL_OP = 105
    STRING_COMP_OP = 106
    STRING_CONCAT_OP = 107
    CONCATENATION_OP = 108
    MEMBER_ACCESS_OUT = 109
    LP = 110
    RP = 111
    LSB = 112
    RSB = 113
    LB = 114
    RB = 115
    SEMI = 116
    DOT = 117
    COMA = 118
    COLON = 119
    WS = 120
    UNTERMINATED_COMMENT = 121
    ERROR_CHAR = 122

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Program'", "'main'", "'extends'", "'break'", "'continue'", 
            "'if'", "'elseif'", "'else'", "'for'", "'true'", "'false'", 
            "'array'", "'in'", "'int'", "'float'", "'boolean'", "'return'", 
            "'class'", "'Null'", "'val'", "'var'", "'self'", "'constructor'", 
            "'destructor'", "'new'", "'By'", "'do'", "'string'", "'then'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'='", "'>'", "'<'", "'>='", "'<='", 
            "'==.'", "'+.'", "'^'", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "';'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "Class_word", "Prog_word", "Extends_word", "Static_word", "Final_word", 
            "Void_word", "Var_word", "Val_word", "If_word", "Then_word", 
            "Else_word", "Elseif_word", "For_word", "Assign_op", "To_word", 
            "Do_word", "Break_word", "Comment_normal", "Comment_block", 
            "Comment_sharp", "Bool_word", "Int_word", "Float_word", "Str_word", 
            "Array_word", "Main_word", "Cons_word", "Dest_word", "Self_word", 
            "ID", "Add", "Sub", "Mul", "Div", "Mod", "Not", "And", "Or", 
            "Equal", "Diff", "Greater", "Lesser", "Greater_euqal", "Lesser_equal", 
            "String_comp", "String_concat", "Member_access_in", "Member_access_out", 
            "Colon", "BOOLEANLIT", "STRINGLIT", "BLOCKCOMMENT", "INTLIT", 
            "FLOATLIT", "PROGRAM", "MAIN", "EXTENDS", "BREAK", "CONT", "IF", 
            "ELSEIF", "ELSE", "FOR", "BOOLTRUE", "BOOLFALSE", "ARRAY", "IN", 
            "INT", "FLOAT", "BOOL", "RETURN", "CLASS", "NULL", "VAL", "VAR", 
            "SELF", "CONS", "DEST", "KEYWORD_NEW", "BY", "DO", "STRING", 
            "THEN", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
            "ADD_OP", "SUB_OP", "MUL_OP", "FLOAT_DIVISION_OP", "MOD_OP", 
            "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", 
            "GREATER_OP", "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", 
            "STRING_COMP_OP", "STRING_CONCAT_OP", "CONCATENATION_OP", "MEMBER_ACCESS_OUT", 
            "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", 
            "COLON", "WS", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "Class_word", "Prog_word", "Extends_word", "Static_word", 
                  "Final_word", "Void_word", "Var_word", "Val_word", "If_word", 
                  "Then_word", "Else_word", "Elseif_word", "For_word", "Assign_op", 
                  "To_word", "Do_word", "Break_word", "Comment_normal", 
                  "Comment_block", "Comment_sharp", "Bool_word", "Int_word", 
                  "Float_word", "Str_word", "Array_word", "Main_word", "Cons_word", 
                  "Dest_word", "Self_word", "ID", "NORM_ID", "SPEC_ID", 
                  "Add", "Sub", "Mul", "Div", "Mod", "Not", "And", "Or", 
                  "Equal", "Diff", "Greater", "Lesser", "Greater_euqal", 
                  "Lesser_equal", "String_comp", "String_concat", "Member_access_in", 
                  "Member_access_out", "Colon", "BOOLEANLIT", "STRINGLIT", 
                  "ESC_SEQ", "ILL_ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC", 
                  "HEX_DIGIT", "UNKNOW_ESC", "BLOCKCOMMENT", "INTLIT", "FLOATLIT", 
                  "INTERGER_PART", "EXPONENT", "FRACTION", "DECIMAL", "OCTAL", 
                  "HEX", "BIN", "PROGRAM", "MAIN", "EXTENDS", "BREAK", "CONT", 
                  "IF", "ELSEIF", "ELSE", "FOR", "BOOLTRUE", "BOOLFALSE", 
                  "ARRAY", "IN", "INT", "FLOAT", "BOOL", "RETURN", "CLASS", 
                  "NULL", "VAL", "VAR", "SELF", "CONS", "DEST", "KEYWORD_NEW", 
                  "BY", "DO", "STRING", "THEN", "VOID", "NIL", "THIS", "FINAL", 
                  "STATIC", "TO", "DOWNTO", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "FLOAT_DIVISION_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", 
                  "EQUAL_OP", "NOT_EQUAL_OP", "ASSIGN_OP", "GREATER_OP", 
                  "LESS_OP", "GREATER_EQUAL_OP", "LESS_EQUAL_OP", "STRING_COMP_OP", 
                  "STRING_CONCAT_OP", "CONCATENATION_OP", "MEMBER_ACCESS_OUT", 
                  "LP", "RP", "LSB", "RSB", "LB", "RB", "SEMI", "DOT", "COMA", 
                  "COLON", "WS", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[52] = self.STRINGLIT_action 
            actions[60] = self.INTLIT_action 
            actions[61] = self.FLOATLIT_action 
            actions[135] = self.UNTERMINATED_COMMENT_action 
            actions[136] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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

     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_','')

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text.replace('_','')
            	##print("Float: ", self.text)

     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UnterminatedComment(self.text) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                from lexererr import ErrorToken
                raise ErrorToken(self.text)

     


