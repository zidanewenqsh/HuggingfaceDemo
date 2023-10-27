#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("Hugging Face is a company that specializes in NLP.")[0]['summary_text']
print(result)
