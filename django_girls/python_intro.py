'''def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hi('Ola')

def hi(name):
    print('Hi ' + name + '!')

hi("Kate")
'''

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Kate']
for name in girls:
    hi(name)
    print('Next girl')

? sort