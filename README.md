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
the equation `record_distance = press_time · (race_time - press_time)`,
but I solved anyway part 1 by brute force.

And in fact in part 2 I solved the equation.
