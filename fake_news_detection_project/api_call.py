class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id
        self.result_record = []
        self.tf = ["T","F","True"]
        
    # T,F 만 가져오기
    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            
        }

        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-002',
                   headers=headers, json=completion_request, stream=True) as r:
            
            for line in r.iter_lines():
                if line:
                    # JSON 문자열을 파싱하여 JSON 객체로 변환
                    json_response = json.loads(line.decode("utf-8"))

                   
            
                    try:
                        result_value = json_response.get("result").get('message').get('content')
                        result_value_string = str(result_value)
                        #finder_t = result_value_string.find("True")
                        #finder_true = result_value_string.find("T")
                        #finder_f = result_value_string.find("F")
                        #finder_false = result_value_string.find("False")
                        if re.search("T", result_value_string, re.IGNORECASE):
                                self.result_record.append("T")
                                
                        elif re.search("F", result_value_string, re.IGNORECASE):
                                self.result_record.append("F")
                                
                        elif re.search("True", result_value_string, re.IGNORECASE):
                                self.result_record.append("True")
                        elif re.search("False", result_value_string, re.IGNORECASE):
                                self.result_record.append("False")
                                
                        else:
                            self.result_record.append("None")
                                
                    except Exception as e:
                        
                        pass
                    
                    print("Result Record:", self.result_record)    
                
                



model = CompletionExecutor(
        host='https://clovastudio.stream.ntruss.com',
        api_key='NTA0MjU2MWZlZTcxNDJiYwbOU8C6YbcVmMu3aJBaodXwTgCAnS+V+oXnSuwCtbKLN3LGgyX6qZKRjDa6KFZA1v3Zqd1MSu5eZqRrJG+H40TJMLQpspIYkr+cZumPv6f6fzOXbE/aV5ACWluGzXSz2BHvuB6G/IGxbsRBezRrDVO8rtZAaVJ0eKN9oXT12Zt/StJg/Je49/Nt9rUujbNrp3hjbIOPyYsKNtEyyFyTxTA=',
        api_key_primary_val='ECs0liU07FEavC33v8Jz8Xwpf8WRBa5Pz34T4LHr',
        request_id='7e1509ee7dc74447891950462bac9f8c'
    )