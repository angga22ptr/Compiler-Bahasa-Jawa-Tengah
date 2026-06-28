"""
====================================================
MAIN PROGRAM
Compiler Bahasa Jawa Tengah
====================================================

Menghubungkan seluruh tahap compiler:

1. Lexer
2. Parser
3. AST
4. Semantic Analysis
5. Optimizer
6. Code Generator
"""


from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from optimizer import Optimizer
from code_generator import CodeGenerator
from visual import VisualAST


print("=" * 50)
print("     COMPILER BAHASA JAWA TENGAH")
print("=" * 50)

print("Nama  : Angga Saputra")
print("NIM   : 231011403177")
print("Ruang : 06 TPLP 023")

print("=" * 50)


kode = input("\nMasukkan program : ")


try:

    # ===============================
    # LEXER
    # ===============================

    print("\n===== HASIL LEXER =====")

    lexer = Lexer(kode)

    token = lexer.tokenize()


    terjemahan = {

        "CETAK": "CETAK",

    "NUMBER": "ANGKA",

    "PLUS": "TAMBAH",

    "MINUS": "KURANG",

    "MULTIPLY": "KALI",

    "DIVIDE": "BAGI",

    "LPAREN": "KURUNG_BUKA",

    "RPAREN": "KURUNG_TUTUP",

    "IDENTIFIER": "JENENG",

    "ASSIGN": "NEMPEL",

    "EOF": "SELESAI"

    }


    for tipe, nilai in token:

        nama = terjemahan.get(tipe, tipe)

        print(f"({nama}, {nilai})")



    # ===============================
    # PARSER + AST
    # ===============================

    parser = Parser(token)

    pohon = parser.parse()


    print("\n===== ABSTRACT SYNTAX TREE =====")


    visual = VisualAST()

    visual.tampilkan(pohon)



    # ===============================
    # SEMANTIC
    # ===============================

    print("\n===== SEMANTIC ANALYSIS =====")


    semantic = SemanticAnalyzer()

    semantic.analyze(pohon)


    print("Program valid.")



    # ===============================
    # OPTIMIZER
    # ===============================

    print("\n===== OPTIMIZER =====")


    optimizer = Optimizer()

    pohon_baru = optimizer.optimize(pohon)


    print("Optimasi berhasil.")



    # ===============================
    # CODE GENERATOR
    # ===============================

    print("\n===== CODE GENERATOR =====")


    generator = CodeGenerator()

    hasil = generator.generate(pohon_baru)


    for kode in hasil:

        print(kode)



except Exception as error:


    print("\nTerjadi kesalahan:")

    print(error)