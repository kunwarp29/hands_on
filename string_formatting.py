person = {'name': 'Ram', 'Age':23}
sentence = ' My name is ' + person['name'] + ' and I am ' + str(person['Age']) + ' years old. '
print(sentence)
'''
its not a good way to write strings so string fomatting is required.

'''

formatted_sentence = 'My name is {} and I am {} years old'.format(person['name'],person['Age'])
#other way to write the string is
formatted_sentence_other = 'My name is {0[name]} and I am {1[Age]} years old'.format(person,person)
#one more way of doing so
formatted_sentence_other2 = 'My name is {name} and I am {Age} years old'.format(**person)


print("formatted_string: ",formatted_sentence)
print("formatted_string_other: ",formatted_sentence_other)
print("formatted_string_other2: ",formatted_sentence_other2)


#one more example

tag = 'h1'
text = 'this is a headline'
sentence = '<{0}> {1} </{0}>'.format(tag,text)  #index pass in the placeholder
print(sentence)
'''-------------------------------------------------------------------------------------------------------------------------------'''

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Ramesh','33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print("class_string: ",sentence)


for i in range(1,11):
    sentence = 'the value is {}'.format(i)
    print(sentence)

for i in range(1,11):
    sentence = 'the value is {:03}'.format(i)       #padding of zero and 3 digit places.
    print(sentence)    