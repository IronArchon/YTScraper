def mandelbrot(z): # you have a point called z in the complex plane
    z = (z * z) + 1 # where z not is z1 squared plus c
    print (z)
    return z


value = 1 # starting from mandelbrot point z (1 in this instance)
for i in range(10): # returning the first 10 entries of this mandelbrot set
    value = mandelbrot(value) # set the value as the mandelbrot value returns the computed value
