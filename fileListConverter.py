fileobj=open("LangChainQAgpt/langChainTEXTtest.txt")
lines=[]
for line in fileobj:
    lines.append(line.strip())
print(lines)