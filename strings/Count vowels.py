s="hello"
count=0
for i in range(5):
    ch=s[i]
    if ch in "aeiou":
      count+=1
print(count)
