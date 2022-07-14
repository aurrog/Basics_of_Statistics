import math

mean = 20
n = 64
x_sample = 18.5
sd = 4

h0 = "mean = 20"
h1 = "mean!= 20"

# if p > 0,05:
#    h0 = True
# if p < 0.05:
#    h1 = True

se = sd / math.sqrt(n)

z = (x_sample - mean) / se
print(z)
