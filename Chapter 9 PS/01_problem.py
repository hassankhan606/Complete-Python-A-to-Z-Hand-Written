f = open("poem.txt" , "r")
content= f.read()
if ("Twinkle" in content):
    print("Twinkle is present in poem")
f.close()
    