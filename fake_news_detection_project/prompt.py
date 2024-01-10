for i in range():
    data = datas["Title"][i]
    test = input_1.format(data)
    
    text = [{"role": "system", "content": ""},
        {"role": "user", "content": test},
        {"role": "assistant", "content": "Select T of F"}]


    request_data = {
        'messages': text,
        'topP': 0.8,
        'topK': 1,
        'maxTokens': 256,
        'temperature': 0.3,
        'repeatPenalty': 5.0,
        'stopBefore': [],
        'includeAiFilters': True
        }
    model.execute(request_data)
