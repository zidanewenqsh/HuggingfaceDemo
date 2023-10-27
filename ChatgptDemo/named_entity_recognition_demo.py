#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from transformers import pipeline
ner = pipeline("ner")
result = ner("Hugging Face is a company based in New York.")
print(result)
