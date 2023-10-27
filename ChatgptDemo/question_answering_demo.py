#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from transformers import pipeline
qa = pipeline("question-answering")
result = qa(question="What is Hugging Face?", context="Hugging Face is a company that specializes in NLP.")
print(result['answer'])

