
def exponent(x:float):
    counter=1
    stage_1=1
    stage_2=1
    sum=0
    while True:  
        stage_1=stage_1*x
        stage_2=stage_2*counter
        stage_3=stage_1/stage_2
        sum=sum+stage_3       
        counter=counter+1
        if stage_3<0.00001:
            exp=sum+1
            break
    return (exp)

def Ln(x:float):
    if x<=0:
        return(0.0)
    y0=x-1.0
    y1=y0+2*((x-exponent(y0))/(x+exponent(y0)))        
    while (y0-y1>0.001)or(y1-y0>0.001):
        y0=y1
        y1=y0+2*((x-exponent(y0))/(x+exponent(y0))) 
    return (y1)

def XtimesY(x:float,y:float):
   # ans=exponent(y*Ln(x))
   if y<0:
       return 0.0
   if x<=0:
       if y % 2 == 0:
           return exponent(y*Ln(-x))
       else:
           return -exponent(y*Ln(-x))
   else:
         return exponent(y*Ln(x))
         
    
##B
def sqrt(x:float,y:float):
    if x>=0 and y>=0:
        return XtimesY(x=y, y=1/x)
    if x<=0 and y>=0:
        return 1/XtimesY(x=y,y=-1/x)
    if x>=0 and y<=0:
        if x%2.0==0:
            return 0
        else:
            return XtimesY(x=y, y=1/x)
    if x<=0 and y<=0:
        if x%2.0==0:
            return 0
        else:
              return 1/XtimesY(x=y,y=-1/x)
    
def calculate(x:float):
    num1=exponent(x)
    num2=XtimesY(7,x)
    num3=XtimesY(x, -1)
    num4=sqrt(x, x)
    return num1*num2*num3*num4


    
   

        
        
        
        
        
    

    

