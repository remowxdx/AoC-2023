# Advent of code 2023


## Day 1

Whoa! About 40 minutes for the first problem...

OK, I lost about 20 minutes to understand that my script downloaded the
input of the last year.

And some time again to find that a digit written in letters could be
repeated more than one time.


## Day 2

... Not enough free time to also write comments ...


## Day 3

... Not enough free time to also write comments ...


## Day 4

Like last year, I really have to find a faster way to parse the input.
All those `split` are not good!

Anyway I solved the problem without much problems, once the script
ran without error, the solution was right.


## Day 5

Part 1 a little complex but not too much.

Part 2 complex in a way that I don't like, but solved anyway:
kept track of start and end of every range, splitting ranges
when going from one category to the next.

I had location 0 as the minimum location, because of a off-by-one
error. Corrected the next day.


## Day 6

Easy enough problem. I suspected that in part 2 you had to solve,
the equation $record\_distance = press\_time · (race\_time - press\_time)$,
but I solved anyway part 1 by brute force.

For the second part, I had to solve the equation

$$r = p (t-p)$$

$$r = pt - p^2$$

$$p^2-pt+r=0$$

$$x_{1,2} = {t \pm \sqrt{t^2-4r} \over 2}$$

$$x_2 -x_1 = \sqrt{t^2-4r}$$

to not have to wait too much time (this just to see how
github renders math).


## Day 7

Interesting poker problem... did find it too much difficult.
Found a relatively simple way to rank the `type` of the hand.
That helped for part 2.


## Day 8

This is the type of probelms that I like...

First part easily done in 12 minutes.

Second part... I tried solved it assuming that every cycle could
also pass thru many "Z" nodes and that the first nodes
could also not be touched in subsequent cycles.

Next time I'll just try with the least common multiple
of the first time a "Z" node is touched.

Anyway if multiple "Z" nodes are touched, my solution
still doesn't work.


## Day 9

Ahhh, I like it when there is a clean, simple recursive
solution! And that solution works!


## Day 10

This has been a long day...
Nearly two hours to solve!

Part 1 more or less straightforward, just create a grid with every cell
having the cells that are connected to it, and explore the loop from the
two sides until they encounter.

In part 2 I remade the grid with "bigger resolution": every cell is transformed
in 9 new cells, for example an "L" cell will be:

```
      .|.
 L -> .L-
      ...
```

That way I can flood the outside and then count what is not outside and
on the loop.


## Day 11

Luckily in part 1 I abstracted the universe with a width, height and
a set with the coordinates of the galaxies.

This way the second part was really easy to solve, I only needed
to add more line in the shift dictionaries.


## Day 12

Part 1 done with too much effort... I have not found a fast way
to solve this problem.
The second part I was too tired to do it...
On the 13th I found a somewhat faster way, but it's
still too slow. I let the computer work all the night,
but still didn't terminate the computation.

On day 17 I revisited the problem, changing my approach:
instead of recursing on every "?", I splitted the record on the
"."'s end multiplied the ways for every chunk.
Still it wasn't fast enough, but adding a cache on the
chunks I got a good enough speed. Now it takes about 20 seconds
on my computer.



## Day 13

I liked this problem, even though I struggled with off by one
errors.


## Day 14

First part approachable, done with string manipulation.

Then I redid everything with dict of stones, that took some time.

But that solves part 2 in short time.


## Day 15

This is the implementation of a hashmap, but in python there
already is an hashmap.


## Day 16

I continued to have the same (false) result, until I noticed that a 
beam reflection rule was wrong.

Then everything was right and easy!


## Day 17

Oh, more than two hours... and it takes some time to find the
path.
I should have taken a different approach:
instead of going step by step, add to the blocks to
visit directly the blocks at the end of the
allowed straight paths.

Maybe later, if I have the time.


## Day 18

I liked this problem, first part solved like day 10, by
flooding the exterior.

For part 2 I had to rethink the way.
I thought that if I add the blocks on the left
and subtract block on the right of trenches going
down and viceversa of trenches going up,
I count twice the block on the inside.

```

out  in->                    <-in   out
---v+++++++#++++       +++#+++++++^----
---v+++++++#++++  and  +++#+++++++^----
---v+++++++#++++       +++#+++++++^----

            ===#2222222#====
            ===#2222222#====
            ===#2222222#====
```


## Day 19

Long problem to solve, and also if you don't read accurately,
it will never work!
It took me too much time to find that the parts can be rated
from **1** to 4000, and **not** from **0** to 4000.
