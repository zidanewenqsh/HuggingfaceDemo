#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from transformers import pipeline
translator = pipeline("translation_en_to_fr")
result = translator("Hugging Face is a great company")[0]['translation_text']
print(result)
