def main ():
    fruits =input("Enter the fruit name ")
    fruits = fruits.upper()
    check_calorie(fruits)

def check_calorie(f):
    FDA = {"APPLE":150 , "BANANA":120 ,"ORNAGE":120 , "MANGO" : 239 }
    if f in FDA:
        print(f"Caloreies {FDA[f]}" )

main()