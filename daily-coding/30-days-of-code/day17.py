#Write your code here
class Calculator:
    def power(self,base,exp):
        solution = None
        if (base < 0) or (exp < 0):
            solution = "n and p should be non-negative"
        else:
            solution = base**exp
        return solution
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
