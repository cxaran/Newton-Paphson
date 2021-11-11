import sympy as sym
import random

def newton(f, df, x0, tol, n, max, rts):
    if n > max:
        return rts
    if abs(f(x0)) < tol:
        xn = float("{:.4f}".format(x0))
        r = random.uniform(-df(x0), df(x0))
        if xn not in rts:
            return newton(f, df, x0 * r, tol, n+1, max, [*rts, xn] ) 
        else:
            return newton(f, df, x0 * r, tol, n+1, max, rts)
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol, n+1, max, rts)    


stf= input('f(x)=') #Enter your funtion here, test (x**5)+(5*x**4)+(6*x**3)+(6*x**2)+(5*x)+1
stdf = str(sym.diff(stf)) #Derivative
print('f´(x)='+stdf)

f = lambda x: eval(stf) # Funtion
df = lambda x: eval(stdf) # Funtion Derivative

# newton( funtion, derivative, start value, max iterations, roots )
roots = newton(f, df, 0, 10E-8, 0, 500, [])

print(roots)# real roots, with the test suggested  [-0.2679, -3.7321, -1.0]