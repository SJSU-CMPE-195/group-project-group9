from ollama import chat
from ollama import ChatResponse

# specify the string from the file.
str = "The mitochondria is the powerhouse of the cell."
# Sends the chat reponse (from the Ollama github) 
response: ChatResponse = chat(model='qwen3.5:cloud', messages=[
   {
       'role': 'user',
       'content': 'From training data, can you give a website with more info and relevant text from it, (PLEASE FOLLOW FORMAT) please structure the prompt with sections link: and text:' + str,
   },

])

# response.message.content has the response from the model.
promptResponse = response.message.content

# store the length of the starting strings
linkLen = len("link: ")
textLen = len("text: ")
# Used to detect error.
err=False

linkInd = promptResponse.find("link: ")
textInd = promptResponse.find("text: ")
# this stores the index after the space, so it is where the data start. For example, 
# "link: " starts at 0 0+6 = 6, this is the index after the space where the url is. 
linkEnd = linkInd + linkLen
textEnd = textInd + textLen

# this gets the substrings, the link goes from the linkEnd to that the start  of text excluding.
linkStr = promptResponse[linkEnd:textInd]
textStr = promptResponse[textEnd:]

#Checks for errors.
if(linkStr == -1):
   print("link was not found: ")
   err = True
if(textInd == -1):
   print("text was not found")
   err = True
if(err == False):
   print(linkStr)
   print(textStr)
