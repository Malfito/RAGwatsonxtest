import os
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM

def get_granite_llm():
    wxa_url = os.getenv("WXA_URL")
    wxa_key = os.getenv("WXA_API_KEY")
    project_id = os.getenv("WXA_PROJECT_ID")

    model = Model(
        model_id="ibm/granite-13b-instruct-v2",
        params={GenParams.DECODING_METHOD: DecodingMethods.GREEDY, GenParams.MIN_NEW_TOKENS: 1, GenParams.MAX_NEW_TOKENS: 200},
        credentials={"url": wxa_url, "apikey": wxa_key},
        project_id=project_id
    )
    return WatsonxLLM(model=model)
