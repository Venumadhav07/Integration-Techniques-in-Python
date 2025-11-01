def f(x,n):
    return 2*(x**n)

a=1
b=6

for n in [1,2,3,4,5,6]:
    I_mid=(b-a)*f((a+b)/2,n)
    I_trap=(b-a)*(f(a,n)+f(b,n))/2
    I_simp=(b-a)*(f(a,n)+f(b,n)+4*f((a+b)/2,n))/6

    I_exact=2*(b**(n+1)-a**(n+1))/n+1

    print(f"\n For n=  {n}: ")
    print(f"\n Midpoint Rule = {I_mid}:")
    print(f"\n Trapezoidal Rule = {I_trap}: ")
    print(f"\n Simpsons Rule = {I_simp}: ")
    print(f"\n Exact Value for Comparison = {I_exact}:")
    print("\n +++++++++  Next Iteration  ++++++++++")