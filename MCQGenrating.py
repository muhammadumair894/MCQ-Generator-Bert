from summarizer import Summarizer

f = open("egypt.txt","r")
full_text = f.read()

model = Summarizer()
result = model(full_text, min_length=60, max_length = 500 , ratio = 0.4)

summarized_text = ''.join(result)
print (summarized_text)