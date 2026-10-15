from agents import function_tool

@function_tool

def calculator(a:float,b:float, operation:str)->float:
    if operation == 'add':
        return a+b
    if operation == 'sub':
        return a-b
    if operation == 'mul':
        return a*b
    if operation == 'divide':
        return a/b

    raise ValueError("Invlaid Error")

@function_tool

def get_user_data(key: str)-> str:
    data = {
        "name":"Shivam Kumar",
        "company": "RoboSiddhi",
        "Age": 22
    }

    return data.get(key,"Value not found")


@function_tool

def currency_calculator(num:float,currency:str)-> float:
    if currency=="Dollar":
        return num*100
    if currency == "Euro":
        return num*106

    raise ValueError("Invaild Error")