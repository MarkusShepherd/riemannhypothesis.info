---
title: If One at a Time is too Difficult, Try All at Once!
author: Markus Shepherd
type: post
date: 2014-12-27T12:00:16+00:00
url: /2014/12/if-one-at-a-time-is-too-difficult-try-all-at-once/
categories:
  - Feature
tags:
  - Analysis
  - Asymptotics
  - Combinatorics
  - Coursera
  - Derbyshire
  - Dirichlet
  - du Sautoy
  - Number theory
  - Riemann
---

In the past months, I spent as much time as I had on taking online courses at [Coursera](https://www.coursera.org/). One particularly interesting course, both from a mathematical and computational point of view, is [Analytic Combinatorics](https://www.coursera.org/course/ac) which applies combinatorics (i.e., the art of counting) to the analysis of algorithms by finding formulae, exact or asymptotic, for their running time.

It is notoriously difficult to find exact formulae for general combinatorial constructs. Typically, we want to know how many objects, e.g., trees, permutations, sequences, with certain properties there are of a given size. Famously, the number of binary trees (and about a million other constructions) is governed by the [Catalan numbers](https://en.wikipedia.org/wiki/Catalan_number)

\\[ C_n = \frac{1}{n+1}{2n\choose n}. \\]

<!-- more -->

How do we get to this result?[^catalan] We could start to construct small examples. How many trees are there of size 1? How many of size 2? 3, 4, 5? This will get tedious very soon, may not help you with finding a formula if the behaviour does not match any of the known sequences, or may even mislead if the beginning of the sequence is very different from the asymptotic behaviour.

You may be tempted to think of constructing a general formula like this: here we have \\(n\\) nodes, how many trees can I build from these? In some cases, this approach actually works, e.g., for permutations, but it soon reaches its limits. Working example by example, number by number, won't get us very far. But working on all examples _simultaneously_ will!

What I mean by this is that we find a general recipe to construct our object of interest, usually from smaller parts we already understand, i.e., atoms and smaller sub-structures. This is particularly natural for recursively defined structures like trees. Now, you have _all_ the objects at your disposal. The trick is to encode them all together in one function -- the _generating_ function.

In the case of combinatorial objects, we define a polynomial series of the form

\\[ A(x)=\sum_{n=0}^\infty a_n x^n, \\]

where the \\(a_n\\) are the quantities we're interested in, i.e., \\(a_n\\) is the number of object of size \\(n\\). Once we understand the resulting function[^convergence] \\(A(x)\\), we can simply extract the coefficient of \\(x^n\\) to recover \\(a_n\\). This may sound pretty circular since we need the \\(a_n\\) to define the function in the first place, but the recursive constructions I mentioned before lead to functional equations that allow us to easily retrieve the function \\(A(x)\\) (i.e., write down a nice, closed form of the function). Once we have that, we can recover the coefficients by applying techniques like comparing it to other well-understood functions, calculating the Taylor coefficients, or finding asymptotic expressions for the coefficients.

You may now be enchanted by the magic powers of analytic combinatorics, but may ask: what does this again have to do with primes? In fact, _analytic_ number theory owes its name to the exact same reason as _analytic_ combinatorics: we take stubborn and hard to handle discrete objects (e.g., primes or trees), throw them all together into one nice function (e.g., the zeta function or a generating function), and -- voilà! -- finally, we have a handle on those objects by applying all these wonderful analytical[^analytical] tools we developed over the centuries. It's as though we smooth out the erratic behaviour of these discrete[^discrete] structures by zooming out of the nitty-gritty details and taking a look at the big picture.

As Marcus du Sautoy[^sautoy] puts it more poetically:

> The zeta function provided Riemann with a looking-glass in which the primes appeared transformed. As in _Alice in Wonderland_, Riemann's paper sucked mathematicians from their familiar world of numbers through a rabbit hole into a new and often counterintuitive mathematical land.

John Derbyshire[^derbyshire] calls it "the great fusion": the discrete and the continuous worlds, that for centuries have been thought as being completely independent, "counting and measuring", "numbers _staccato_ and numbers _legato_", come together in an unexpected harmony. For me, this is what makes the beauty of mathematics: even the most harmless problems require the full power of our mind and imagination to come up with new and creative concepts. Only the brightest mathematicians will pioneer new techniques like Bernhard Riemann did.[^fusion] But by following their footsteps, we may hope to breathe some of the inspiration they exhale.

[^catalan]: The exact result depends on what exactly the question is, e.g., if you count internal nodes, external nodes, only full trees, etc. Either way, the Catalan numbers are a recurring theme. Here, we don't care about the details, but just the general idea.
[^convergence]: Of course, if we want to apply analytical tools, we need this series to converge, which isn't guaranteed at all. If it doesn't, we can usually make it converge by applying weights, e.g., inverses of factorials like in the definition of the exponential function.
[^analytical]: At this point, I fully got confused between _analytic_ and _analytical_. A quick internet search indicates that there is simply no difference. However, I didn't find a single mention of analytic_al_ number theory. Still, I somehow feel that _analytical_ tools sound better than _analytic_ tools. English is such a confusing language!
[^discrete]: Luckily, the distinction between _discrete_ and _discreet_ is an easy one!
[^sautoy]: In [_The Music of the Primes_](https://www.amazon.co.uk/gp/product/1841155802/ref=as_li_tf_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=1841155802&linkCode=as2&tag=riemannhypo-21), chapter 3.
[^derbyshire]: In [_Prime Obsession_](https://www.amazon.co.uk/gp/product/0452285259/ref=as_li_tf_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=0452285259&linkCode=as2&tag=riemannhypo-21), chapter 6.
[^fusion]: Derbyshire rightfully attributes "the great fusion" to Peter Gustav Lejeune Dirichlet who first used analytical methods to prove his famous [theorem on arithmetic progressions](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions), but it was Riemann who brought the subject to its full powers by leaving the known waters of the real numbers and set sail for the complex numbers.
