# Is This Normal?

I saw [this article](https://timdellinger.substack.com/p/hey-wait-is-employee-performance) on Hacker News -- it's mainly about pay scales and performance and, you know, tedious real-world stuff[^1]. It got me wondering about whether I could wave my hands at the real world with a not-entirely-outlandish assumptions and end up with a Pareto distribution.

[^1]: Saying that, if you want to pay me to do real-world stuff, I'm available for consulting work. Email [colin@colinbeveridge.co.uk](mailto:colin@colinbeveridge.co.uk).

So: I assumed that there's a firm with 1000 employees, and every person in the universe has a fixed performance rate drawn from \( N(100,10^2)\)[^2], and this number is known for everyone. Every year, the firm fires its 100 worst-performing employees, and runs a hiring process: they get 1000 applicants, and hire the 100 best of them.

[^2]: No special reason to pick those parameters other than to keep the numbers nice.

Starting with 1000 normally-distributed employees and running the routine for 100 years (the employees live until they're fired, of course), we get this as the mean performance of the 900 surviving workers: 

![Plot of mean surviving worker productivity over the first glorious century](fig0.png)

... which is roughly what I'd expect, the mean rises very sharply at first, but with diminishing returns over time. 

What do the surviving employees look like after 100 years, apart from grizzled and slightly terrified of what happens when they *do* eventually leave? Here's a (slightly funky) CDF plot with a log-scale on the y-axis[^3]:

![Reverse log-scale CDF of employee productivity](fig1.png)

If the resulting distribution is Pareto, this line should be approximately straight. I'd call that plausible, at least! Incidentally, 20% of the employees are below the blue line. 80% of the performance scale is to the right of the orange line, which also fits with the folk-wisdom Pareto distribution.

[^3]: You would usually expect a CDF to start from the lowest values and move to the highest. Doing it backwards is what gives a good log fit.

To finish: I note that I haven't found (or looked for) any evidence that the distribution isn't lognormal -- I think I'd expect a curve in that case. 
