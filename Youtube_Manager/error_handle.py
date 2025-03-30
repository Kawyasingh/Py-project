file  open('youtube.txt','w')

try:
    file.write('coffee and code')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('coffee and python')