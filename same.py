# 1) Read the entire line once:
line = input().strip()  
#    e.g. "b1=[blue,white] b2=[green,white] b3=[red,green,blue,white]"

# 2) Split it on spaces into exactly three parts:
parts = line.split()  
#    parts == ["b1=[blue,white]", "b2=[green,white]", "b3=[red,green,blue,white]"]

# 3) parse_bucket() pulls the stuff between [ and ] and splits on commas:
def parse_bucket(spec):
    start = spec.find('[')
    end   = spec.find(']')
    return spec[start+1:end].split(',') if start!=-1 and end!=-1 else []

b1 = parse_bucket(parts[0])
b2 = parse_bucket(parts[1])
b3 = parse_bucket(parts[2])

# 4) Find intersection of b1 & b2, then remove any in b3:
result = [c for c in b1 if c in b2 and c not in b3]

# 5) Print the result or “none”:
print(','.join(result) if result else 'none')

