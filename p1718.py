#__*__ coding:UTF-8 __*__

def Up(s):
	return s[0].upper()+s[1:].lower()

print map(Up,["jiaojinning","zhaolongfei"])

def prod(l):
	return reduce(lambda x,y:x*y,l)

l=[1,2,3]
print prod(l)
