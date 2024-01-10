for i in range():
    if model.result_record[i] == "T":
        model.result_record[i] = "True"
    elif model.result_record[i] == "F":
        model.result_record[i] = "False"
    elif model.result_record[i] == "None":
        model.result_record[i] = "Fail"