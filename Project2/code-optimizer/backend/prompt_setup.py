"""
Exected once at app startup to register prompts.: executed only once at startup
"""

import logging
from langfuse import Langfuse
logger = logging.getLogger(__name__)
lf = Langfuse()

import os
model = os.getenv['AZURE_DEPLOYMENT']

def _ensure_prompt(name:str,prompt:str,model:str,temperature=0.2):
    if lf.get_prompt(name, raise_if_not_found=False):
        logger.debug("Prompt %s already exists",name)
        return
    lf.create_prompt(name=name, promtp=prompt,
                     config={"model":model,"temperature":temperature},
                     labels=['production'])
    logger.info("Prompt %s created",name)


def register_prompt_once():
    _ensure_prompt("input_guardrail","")
    _ensure_prompt("output_guardrail","")
    _ensure_prompt("optimize-code","")
