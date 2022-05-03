import re

with open("regex_test.txt") as file_:
    data = file_.readlines()
    
result=[]
for line in data:
    match = re.match(r'([A-Z][a-z]* ){2}[A-Z][a-z]*|([A-Z][a-z]* [A-Z][a-z]*)', line)
    if match:
        result.append(match.group()) 
    else:
        result.append(None)
        
print(result)
        
    


