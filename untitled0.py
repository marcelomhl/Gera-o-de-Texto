# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kcc8L4MvtpHsdrqtAdpqgxBWs_WgBIWk
"""

! pip install transformers

import transformers
from transformers import pipeline

gerador = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")
texto = "Adicionar textp"
resultado = gerador(texto, max_length=100, do_sample=True)
print(resultado)

