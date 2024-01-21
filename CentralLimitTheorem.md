The question being asked is "to show that the Binomial and Normal distributions converge in the large N limit." I had troubles plotting both on top of each other so these are the results I got.
Essentially, this quetion is asking to visually prove the Central Limit Theorem, in layman's terms, that the more independent random variables that are added, the closer the distribution comes to a Normal distribution regardless of original distribution.
To prove this I took these steps:
- I created a list of number of samples to run ranging from smaller to larger (1, 5, 10, 100)
- I created an empty list of means to append the results of our loop to so we could plot them
- Using a loop, we generated 1 then 5 then 10 then 100 numbers in the range 0-100
- We then took their means and appended them to the empty list, so each loop was individually stored
- We then plotted the resulting histogram for each of these samples with the title being the number of samples
- As you can see, the larger the number of samples (n), the closer the distribution resembles a normal distribution.
