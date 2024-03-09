# -*- coding: utf-8 -*-
"""ASR project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t9q9Yf_x-IaollVsmkt4sGg4RNUfoTXX
"""

!pip install transformers

from transformers import pipeline

asr = pipeline("automatic-speech-recognition")
rec = asr("test.mp3")
print(rec)