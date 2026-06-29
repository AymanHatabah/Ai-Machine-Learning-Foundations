def main():
    print("\t My calculator")
    while True:
        try:
            expression=input("").strip()
            #flag
            success=False
            for op in ["+","-","/","*"]:
                if op in expression:
                    operator=op
                    num1,num2=expression.split(operator)
                    num1=float(num1.strip())
                    num2=float(num2.strip())
                    
                    print(f"result={calculate(operator,num1,num2)}")
                    success=True
                    break
                    
                
            if success:
                break
             
            
        except ValueError:
            pass
        except ZeroDivisionError:
            pass    
def calculate(op,n1,n2):
  result=0
  if op=="+":
      result=n1+n2
      return result
  elif op=="-":
      result=n1-n2
      return result
  elif op=="*":
      result=n1*n2
      return f"{result:.4f}" if result >1000 else result
  elif op=="/":
      result=n1/n2
      return f"{result:.4f}"
    

      
    


main()