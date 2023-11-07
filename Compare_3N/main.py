i=1
while i<10:
 tmp_nmb=input("please,introduce an integer number")
 if(tmp_nmb.isdigit()== True):
    number1=int(tmp_nmb)
 else:
    exit()
 tmp_nmb=input("please,introduce an integer number")
 if(tmp_nmb.isdigit()== True):
    number2=int(tmp_nmb)
 else:
    exit()
 tmp_nmb=input("please,introduce an integer number")
 if(tmp_nmb.isdigit()== True):
    number3=int(tmp_nmb)
 else:
    exit()
 if number1>number2:
  if number1>number3:
     print(f"The higher number is the 1st : {number1}")
  else:
     print(f"The higher number is the 3rd : {number3}")
 else:
    if number2>number3:
      print(f"The higher number is the 2nd : {number2}")
    else:
      print(f"The higher number is the 3rd : {number3}")
 i=i+1
