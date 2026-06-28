"""
====================================================
SEMANTIC ANALYSIS
Compiler Bahasa Jawa Tengah
====================================================

Semantic Analysis bertugas memeriksa apakah
program memiliki makna yang benar.

Yang diperiksa:
1. Variabel harus sudah dideklarasikan.
2. Assignment disimpan ke tabel simbol.
3. Pembagian dengan nol.
"""

from ast_node import Node


class SemanticAnalyzer:

    def __init__(self):

        # Symbol Table
        self.simbol = {}

    # ==========================================

    def analyze(self, node):

        if node is None:
            return

        # --------------------------------------
        # NUMBER
        # --------------------------------------

        if node.tipe == "NUMBER":
            return

        # --------------------------------------
        # IDENTIFIER
        # --------------------------------------

        if node.tipe == "IDENTIFIER":

            if node.nilai not in self.simbol:

                raise Exception(
                    f"Variabel '{node.nilai}' belum dideklarasikan."
                )

            return

        # --------------------------------------
        # ASSIGN
        # --------------------------------------

        if node.tipe == "ASSIGN":

            self.analyze(node.kiri)

            self.simbol[node.nilai] = True

            return

        # --------------------------------------
        # CETAK
        # --------------------------------------

        if node.tipe == "CETAK":

            self.analyze(node.kiri)

            return

        # --------------------------------------
        # Operator
        # --------------------------------------

        self.analyze(node.kiri)
        self.analyze(node.kanan)

        # Pembagian dengan nol
        if node.tipe == "DIVIDE":

            if (
                node.kanan is not None
                and node.kanan.tipe == "NUMBER"
                and node.kanan.nilai == 0
            ):

                raise Exception(
                    "Tidak boleh membagi dengan nol."
                )