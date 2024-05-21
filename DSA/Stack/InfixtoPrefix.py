from  LinearStack import *

class Prefix:
    def isoperator(self, a):
        if(a=='+' or a=='-' or a=='/' or a=='*' or a=='^'):
            return True
        return False
    def precedence(self , a ):
        if(a=='^'):
            return 3
        elif(a=='*' or a=='/'):
            return 2
        elif(a=='+' or a=='-'):
            return 1
        else :
            return 0 
        return -1 
    def InfixtoPrefix(self , Infix):
        Infix = Infix[::-1]
        stack = LinearStack(len(Infix))
        ans = ""
        for i in range(len(Infix)):
            if(Infix[i]=='('):
                stack.push(Infix[i])
                print(1)
            elif(Infix[i]==')'):
                while(stack.top!='(' and not stack.IsEmpty()):
                    ans+=stack.pop()
                stack.pop()
                print(2)
            elif(self.isoperator(Infix[i])):
                x = stack.peek()
                if(stack.IsEmpty()):
                    stack.push(Infix[i])  
                elif(self.precedence(Infix[i])<=self.precedence(stack.peek()) and not stack.IsEmpty() ):
                    stack.push(Infix[i])                
                elif(self.precedence(Infix[i])>self.precedence(stack.peek()) and not stack.IsEmpty() ):
                    ans+=stack.pop()
                    stack.push(Infix[i])
                print(3)
            else :
                ans+=Infix[i]
                print(4)
        if(not stack.IsEmpty()):
            ans+=stack.pop()
            print(5)
        ans1 = ""
        for i in ans:
            if(i=='('):
                continue
            ans1+=i 
        ans1 = ans1[::-1]
        ans = ans[::-1]
        print("the prefix expression is " , ans1)

p = Prefix()
p.InfixtoPrefix(input("enter"))               
            
            


