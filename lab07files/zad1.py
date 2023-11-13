import argparse
import sympy
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
from sympy.parsing.sympy_parser import parse_expr


parser=argparse.ArgumentParser(description="Newton Method")
parser.add_argument('polynomial',action='store',type=str,help='Polynomial without space variable as x')
parser.add_argument('-x0','--xstart',dest='x0',action='store',type=float,default=0.0,help='Starting point')
parser.add_argument('-m','--steps',dest='steps',action='store',type=int,default=100,help='Number steps of Newton Method')
parser.add_argument('-e','--epsilon',dest='epsilon',action='store',type=float,default=10e-6,help='Acceptable error to 0')

args=parser.parse_args()

transformations = (standard_transformations +
    (implicit_multiplication_application,))

parsed=parse_expr(args.polynomial, transformations=transformations)
steps=args.steps
epsilon=args.epsilon
x_prev=args.x0

def newtons_method(x_prev,f,epsilon,max_iterations):
    derivative = f.diff('x')
    for i in range(max_iterations):
        y = f.subs('x',x_prev)
        der_at_point=derivative.subs('x', x_prev)
        if abs(der_at_point) < 1e-10:
            print("Derivative too close to zero. Newton's method cannot proceed.")
            return None
        x1 = x_prev - y / der_at_point      
        if abs(x1 - x_prev) <= epsilon:
            return x_prev
        x_prev = x1
     
    return x_prev


print(newtons_method(x_prev,parsed,epsilon,steps))

