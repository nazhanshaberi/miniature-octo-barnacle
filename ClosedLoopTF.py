#group 1: Question 1(b)
# A control system for positioning the head of a laser printer has the closed loop transfer function:
# !pip install control 

import matplotlib.pyplot as plt
import control

a=10  #Value for a
b=50  #value for b
sys1 = control.tf(20*b,[1,20+a,b+20*a,20*b])
print('3rd order system transfer function T1(s)=',sys1)
sys2=control.tf(b,[1,a,b])
print('2nd order system transfer funtion T2(s)',sys2)

value = sys1.pole()
list_of_poles = [pole.round(2) for pole in value]
print('poles',list_of_poles)

y1=control.step_response(sys1)
y2=control.step_response(sys2)
plt.plot(y1[0],y1[1],'r--', label='3rd order actual system')
plt.plot(y2[0],y2[1],'g', label='2nd order approximation system')
plt.legend()
plt.grid()
plt.xlabel('time (s)')
plt.ylabel('step response y(t)')
plt.title('step response comparison of 3rd and 2nd order system')
plt.show()
