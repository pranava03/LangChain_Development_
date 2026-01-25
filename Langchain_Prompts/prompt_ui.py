from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import load_prompt
import streamlit as st

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import settings

llm   = HuggingFaceEndpoint(repo_id = 'HuggingFaceH4/zephyr-7b-beta', task = 'text-generation', huggingfacehub_api_token = settings.huggingfacehub_access_token)
model = ChatHuggingFace(llm = llm)

st.header("Langchain Research Tool")

paper_input  = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input  = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("prompt_template.json")

if st.button('summarize'):
    chain  = template | model
    result = chain.invoke({'paper_input' : paper_input, 'style_input' : style_input, 'length_input' : length_input})
    st.write(result.content)