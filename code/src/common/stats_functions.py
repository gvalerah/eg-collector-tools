# Statistical Agnostic Functions and Classes
# ==========================================

import math

class RunningStats:
    """
    Here is a literal pure Python translation of the Welford's algorithm implementation from http://www.johndcook.com/standard_deviation.html:
    https://github.com/liyanage/python-modules/blob/master/running_stats.py
    Modified by Gerardo L Valera 2019
    
    Usage: 
    
    rs = RunningStats()
    rs.push(17.0)
    rs.push(19.0)
    rs.push(24.0)

    mean = rs.mean()
    variance = rs.variance()
    stdev = rs.standard_deviation()
    min = rs.min()
    max = rs.max()
    N = rs.n
    """


    def __init__(self):
        self.n = 0
        self.old_m = 0
        self.new_m = 0
        self.old_s = 0
        self.new_s = 0
        self.min_ = 0
        self.max_ = 0

    def clear(self):
        self.n = 0

    def push(self, x):
        self.n += 1

        if self.n == 1:
            self.old_m = self.new_m = x
            self.old_s = 0
            self.min_ = x
            self.max_ = x
        else:
            self.new_m = self.old_m + (x - self.old_m) / self.n
            self.new_s = self.old_s + (x - self.old_m) * (x - self.new_m)

            self.old_m = self.new_m
            self.old_s = self.new_s
            self.min_ = x if x < self.min_ else self.min_
            self.max_ = x if x > self.max_ else self.max_

    def mean(self):
        return self.new_m if self.n else 0.0

    def variance(self):
        return self.new_s / (self.n - 1) if self.n > 1 else 0.0

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def min(self):
        return self.min_ if self.n else 0.0

    def max(self):
        return self.max_ if self.n else 0.0
        
class Regression_Line():
    sumx=0
    sumy=0
    sum_x2=0
    sum_y2=0
    sum_prod_xy=0
    meanx=0
    meany=0
    n=0
    x=None
    y=None
    covariance_xy=0
    variance_x=0
    variance_y=0
    line_yx_a=0
    line_yx_b=0
    line_xy_a=0
    line_xy_b=0
    
    def __init__(self,y,x=None):
        self.x=x
        self.y=y
        self.n=len(y)
        if x is None:
            self.x=[]
            for i in range(0,self.n):
                self.x.append(i)
        # Normalize vectors to floats in order to standarize calculations
        for i in range(len(self.y)):
            self.y[i]=float(self.y[i])
        for i in range(len(self.x)):
            self.x[i]=float(self.x[i])
                

        for i in range(0,self.n):
            self.sumx += self.x[i]
            self.sumy += self.y[i]
            self.sum_x2 += self.x[i]*self.x[i]
            self.sum_y2 += self.y[i]*self.y[i]
            self.sum_prod_xy += self.x[i]*self.y[i]
    
        if self.n > 0:
            self.meanx=self.sumx/self.n
            self.meany=self.sumy/self.n 
            self.covariance_xy=(self.sum_prod_xy/self.n)-(self.meanx*self.meany)

            self.variance_x=(self.sum_x2/self.n)-(self.meanx*self.meanx)
            self.variance_y=(self.sum_y2/self.n)-(self.meany*self.meany)

        if self.variance_x > 0:
            self.line_yx_a=self.covariance_xy/self.variance_x
            self.line_yx_b=self.meany-(self.covariance_xy*self.meanx/self.variance_x)

        if self.variance_y > 0:
            self.line_xy_a=self.covariance_xy/self.variance_y
            self.line_xy_b=self.meanx-(self.covariance_xy*self.meany/self.variance_y)
   
        
    def get_y(self,x):
        return self.line_yx_a*x+self.line_yx_b

    def get_x(self,y):
        return self.line_xy_a*y+self.line_xy_b
        
    def get_yx_coeficients(self):
        return (self.line_yx_a,+self.line_yx_b)

    def get_xy_coeficients(self):
        return (self.line_xy_a,+self.line_xy_b)
        
            
    def estimate_y(self,From,To=None):
        if To is None:
            To=From
        result=[]
        for x in range(From,To+1):
            result.append(self.line_yx_a*x+self.line_yx_b)    
        return result
        
