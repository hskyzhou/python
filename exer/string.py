s='spam'
print(s)
s=s+'SPAM!'
print(s)
s= s[:4] + "Burger" +s[-1]
print(s)
s='splot'
s.replace('pl', 'pamal')
print(s)
s='this is %d %s bird!' % (1, 'dead')
print(s)
s='this is {0} {1} bird!'.format(1,'dead')
print(s)
s='spammy'
print(s)
s=s[:3]+'xx'+s[:5]
print(s)
s='spammy'
print(s)
s=s.replace('mm','xx')
print(s)
s='aa$bb$cc$dd'
print(s)
s=s.replace('$','spam')
print(s)
s='spammy'
print(s)
l=list(s)
print(l)
l[3]='x'
l[4]='x'
print(l)
s=''.join(l)
print(s)
reply="""
Greetings...
Hello %(name)s
your age squared is %(age)s
"""
values={'name':'bob','age':40}
print(reply % values)
