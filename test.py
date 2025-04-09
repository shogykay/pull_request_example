import json
import requests
from config import getConfig
from local_or_global_search_delegation import classify_query_llm
def graph_rag(question):
    search = classify_query_llm(question)
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': getConfig()['GraphRag']["ApiKey"]
    }

    payload = {
        'index_name': 'eva_graphrag_210', 
        # 'index_name': 'test_20_doc',
        'query': question
    }

    json_payload = json.dumps(payload)
    
    if search == "Global":
        response = requests.post(getConfig()['GraphRag']["Url_global"], headers=headers, data=json_payload)
    else:
        response = requests.post(getConfig()['GraphRag']["Url_local"], headers=headers, data=json_payload)

    # return json.loads(response.content.decode("utf-8"))['result']
    return json.loads(response.content)