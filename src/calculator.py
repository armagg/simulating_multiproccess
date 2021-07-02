import pandas as pd
import numpy as np
from .consts import const


## time-dependent RungeKutta 4th order

def RungeKutta (f,arr,t,func_n):#f is the vector field function: arraydot=f(array), array is the vector (x,y,z)
    k1=f(arr,t,func_n)*const.dt
    k2=f(arr+0.5*k1,t+0.5*const.dt,func_n)*const.dt
    k3=f(arr+0.5*k2,t+0.5*const.dt,func_n)*const.dt
    k4=f(arr+k3,t+const.dt,func_n)*const.dt
    return (k1+2*k2+2*k3+k4)/6

def Lorenz(a,t,func_n): # 'a' is the array of system state, i.e (x,y,z), func_n: 0 == funcya, 1 == funcyc
    x = a[0]
    y = a[1]
    z= a[2]
    r=24.4+np.sin(const.w*t)
    xdot = const.sigma*(y-x)
    ydot = const.funcy[func_n](x,y,z,r)
    zdot= x*y-const.b*z
    return np.array([xdot,ydot,zdot])

def z_fixed(t):
    return 23.4 + np.sin(const.w*t)


def check_func(arr_z,tl,tf):
    for i in range(3800):
        if (np.abs(arr_z[int((tf-i)*1000)] - z_fixed(tl-i)) > const.check_radius):
            return 1
    return 0

def simulate(x0,y0,z0,func_n):
    
    
    time=np.arange(0,const.tfinal+const.dt/2,const.dt)
        
    xs=np.zeros(np.size(time),dtype=float)
    ys=np.zeros(np.size(time),dtype=float)
    zs=np.zeros(np.size(time),dtype=float)
        

    
    check = 1
    i = 0
    
    while(check==1):
        
        
        x_save = np.zeros(0,dtype=float)
        y_save = np.zeros(0,dtype=float)
        z_save = np.zeros(0,dtype=float)
        z_fix = np.zeros(0,dtype=float)
        t_save = np.zeros(0)
        
        if(i==0):
            
            xs[0]=x0
            ys[0]=y0
            zs[0]=z0
            helping=np.array([x0,y0,z0])
            
        else:
            
            xs[0]=xs[-1]
            ys[0]=ys[-1]
            zs[0]=zs[-1]
            helping=np.array([xs[-1],ys[-1],zs[-1]]) 
            
            
        
        for tt in range(0,const.n):
            if(tt%1000==0):
                x_save = np.append(x_save,xs[tt])
                y_save = np.append(y_save,ys[tt])
                z_save = np.append(z_save,zs[tt])
                z_fix = np.append(z_fix,z_fixed(time[tt]))
                t_save = np.append(t_save,time[tt])
            
            helping+=RungeKutta(Lorenz,helping,time[tt],func_n)
            xs[tt+1]=helping[0]
            ys[tt+1]=helping[1]
            zs[tt+1]=helping[2]
            
        
        difference = z_save - z_fix    
            
        save=np.transpose(np.array([t_save,x_save,y_save,z_save,z_fix,difference]))
        df = pd.DataFrame(save,columns=['time','x','y','z','z_fixed','difference'])
        df.to_csv('(x0,y0,z0)=(%.2f,%.2f,%.2f),eq%s.csv'%(x0,y0,z0,const.funcylabel[func_n]),mode='a',header=(i==0),index=False)
        
        check = check_func(zs,time[tt+1],const.tfinal)
        i += 1
        
        time = time + const.tfinal
        
        if (i>2):
            break
        
    if (xs[-1]>0):
        end = 1
    else:
        end = 0
    
        
    df2 = pd.DataFrame(np.array([end]),columns=['end'])
    df2.to_csv('results/(x0,y0,z0)=(%.2f,%.2f,%.2f),eq%s_check.csv'%(x0,y0,z0,const.funcylabel[func_n]),mode='a',header=True)

   