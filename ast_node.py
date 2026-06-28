
"""
====================================================
AST (Abstract Syntax Tree)
Compiler Bahasa Jawa Tengah
====================================================

File ini digunakan untuk membangun struktur
Abstract Syntax Tree (AST).

AST merupakan representasi program dalam bentuk
pohon yang akan digunakan pada proses:

1. Semantic Analysis
2. Optimizer
3. Code Generator
"""


class Node:

    def __init__(self, tipe, nilai=None, kiri=None, kanan=None):

        # Jenis node
        self.tipe = tipe

        # Nilai node
        self.nilai = nilai

        # Child kiri
        self.kiri = kiri

        # Child kanan
        self.kanan = kanan

    def __repr__(self):
        return f"Node({self.tipe}, {self.nilai})"
