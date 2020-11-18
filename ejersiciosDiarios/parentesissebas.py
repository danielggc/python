
def side_brackets(brackets, n):
    for b in generate_brackets(n):
        yield brackets+b
        yield b+brackets
def inner_brackets(start_bracket, end_bracket, n):
    for brackets in generate_brackets(n):
        yield start_bracket+brackets+end_bracket
def generate_brackets(n):
    mem = set()    
    if n==0: return []
    elif n==1: return ["()"]
    if n>0:
        [mem.add(s) for s in side_brackets("()",n-1) ]
        [mem.add(i) for i in inner_brackets("(", ")", n-1)]
        
        return list(mem)
    
  
print(generate_brackets(4))
