#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sentiment Analysis
"""
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", revision="af0f99b")
result = classifier("I love programming")[0]
print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
