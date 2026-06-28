"""
====================================================
CODE GENERATOR
Compiler Bahasa Jawa Tengah
====================================================

Code Generator bertugas mengubah AST
menjadi pseudo assembly.
"""

class CodeGenerator:

    def generate(self, node):

        hasil = []

        self.visit(node, hasil)

        return hasil

    # ==========================================

    def visit(self, node, hasil):

        if node is None:
            return

        # --------------------------------------
        # NUMBER
        # --------------------------------------

        if node.tipe == "NUMBER":

            hasil.append(f"PUSH {node.nilai}")

            return

        # --------------------------------------
        # IDENTIFIER
        # --------------------------------------

        if node.tipe == "IDENTIFIER":

            hasil.append(f"LOAD {node.nilai}")

            return

        # --------------------------------------
        # ASSIGN
        # --------------------------------------

        if node.tipe == "ASSIGN":

            self.visit(node.kiri, hasil)

            hasil.append(f"STORE {node.nilai}")

            return

        # --------------------------------------
        # CETAK
        # --------------------------------------

        if node.tipe == "CETAK":

            self.visit(node.kiri, hasil)

            hasil.append("PRINT")

            return

        # --------------------------------------
        # OPERATOR
        # --------------------------------------

        self.visit(node.kiri, hasil)

        self.visit(node.kanan, hasil)

        if node.tipe == "PLUS":
            hasil.append("ADD")

        elif node.tipe == "MINUS":
            hasil.append("SUB")

        elif node.tipe == "MULTIPLY":
            hasil.append("MUL")

        elif node.tipe == "DIVIDE":
            hasil.append("DIV")