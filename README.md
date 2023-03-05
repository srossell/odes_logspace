# ODES with states in log space.

## Daniel Lee's idea

One trick that I haven't talked much about in public is running the ODE on the log scale, which requires a simple-ish transform of the ODE equations. And sometimes it helps.


## Biochem example
v1    v2
--> x -->

$v1 = a$

$ v2 = b \cdot x / (c + x)$

$\dot{x} = a - b \cdot x / (c + x)$

Translating to log space

$y = \ln(x)$ and x = e^{x}$

Then:

$\dot(x) = e^{x}\cdot \dot{y}$

and

$\dot{y} = \frac{a}{e^y} + \frac{b}{c + e^y}$

As an example, I chose $a = 1$; $b=1.5$ and $c = 0.314$. $a$ is givne, $b$ and $c$ are to be estimated.






