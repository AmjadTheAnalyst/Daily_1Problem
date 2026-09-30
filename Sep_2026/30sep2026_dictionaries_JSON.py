a = {"name": "Bob", "role": "Agent"}
for element in a:
    print(element)

'''4. Dynamic Presence Check (Level: Medium)
The Scenario: You receive a raw response dictionary from an LLM API:
ai_response = {"action": "search", "query": "Python tutorials"}
The Task: Write a validation step using an if statement to check if the key "destination" is inside the dictionary. 
If it is missing, print a meaningful error message telling the user exactly what is missing.
'''

ai_response = {"action": "search", "query": "Python tutorials"}
#"destination"
if "destination" not in ai_response.keys():
        print('The information regarding destination is missing')

keys_list = ["username", "email", "id"]
values_list = ["ai_dev", "dev@agent.ai", 404]


