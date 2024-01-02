import time
ask = input("Code or Decode >> ").lower()

if 'decode' in ask:
    string = input("Enter the code >> ")
    values = string.split(" ")
    decoad = "" 
    for extract in values:
            decoad += f"{chr(int(extract))}"
    print('Decoading....')
    time.sleep(3)
    print(decoad)
        
elif "code" in ask:
    number = input('Write here >> ')   
    converting = ''
    for list in number:
        converting += f"{ord(str(list))} "
    print('Coading....')
    time.sleep(2)
    print(f">> {converting}")
        
else:
    print('Invalid prompt')