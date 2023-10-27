#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from transformers import pipeline
generator = pipeline("text-generation")
result = generator("Once upon a time")[0]['generated_text']
print(result)
