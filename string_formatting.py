person = {'name': 'Ram', 'Age':23}
sentence = ' My name is ' + person['name'] + ' and I am ' + str(person['Age']) + ' years old. '
print(sentence)
'''
its not a good way to write strings so string fomatting is required.

'''

formatted_sentence = 'My name is {} and I am {} years old'.format(person['name'],person['Age'])
print("formatted_string",formatted_sentence)
#one more example

tag = 'h1'
text = 'this is a headline'
sentence = '<{0}> {1} </{0}>'.format(tag,text)
print(sentence)