names = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

print({name: len(name) for name in names})

print([name.upper() for name in names])

print([name + "a" for name in names])

print([name.lower() + "@email.com" for name in names])
