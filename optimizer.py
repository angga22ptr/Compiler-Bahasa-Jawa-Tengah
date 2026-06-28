"""
====================================================
OPTIMIZER
Compiler Bahasa Jawa Tengah
====================================================

Optimizer bertugas menyederhanakan AST
agar proses eksekusi menjadi lebih efisien.

Optimasi yang digunakan:
- Constant Folding
"""

from ast_node import Node


class Optimizer:

    def optimize(self, node):

        if node is None:
            return None

        # Optimasi child terlebih dahulu
        node.kiri = self.optimize(node.kiri)
        node.kanan = self.optimize(node.kanan)

        # =====================================
        # Constant Folding
        # =====================================

        if node.tipe in ("PLUS", "MINUS", "MULTIPLY", "DIVIDE"):

            if (
                node.kiri is not None
                and node.kanan is not None
                and node.kiri.tipe == "NUMBER"
                and node.kanan.tipe == "NUMBER"
            ):

                kiri = node.kiri.nilai
                kanan = node.kanan.nilai

                if node.tipe == "PLUS":
                    hasil = kiri + kanan

                elif node.tipe == "MINUS":
                    hasil = kiri - kanan

                elif node.tipe == "MULTIPLY":
                    hasil = kiri * kanan

                elif node.tipe == "DIVIDE":
                    hasil = kiri / kanan

                return Node("NUMBER", hasil)

        return node