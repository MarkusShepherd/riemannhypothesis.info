---
title: Euler Product Revisited
author: Markus Shepherd
type: post
date: 2013-10-06T22:24:34+00:00
url: /2013/10/euler-product-revisited/
categories:
  - Euler product
tags:
  - Euler
  - Product
  - Series
---

From the [previous]({{<ref "posts/2013-09-29-in-the-beginning-there-was-eulers-formula.md">}}) post we know that the harmless looking series \\(\sum n^{-s}\\) can be extended to the product \\(\prod (1-p^{-s})^{-1}\\). At first sight, this does not seem terribly helpful, and it actually makes the rather easy series more complicated. So what's the big deal?

It's what has actually been suppressed in the above notation: The sequences we run through. The series runs over all natural numbers (or positive integers, if you prefer), the product runs through all prime numbers. Now, that's cool, isn't it? We found a series over the natural numbers that, as we will see later, defines a well-behaved function which is accessible to all the nice methods modern mathematics can offer, and related it to the prime numbers.

In other words: Riemann's \\(\zeta\\)-function encodes the mysteries of the primes.<!-- more -->

If you are still not convinced, just remember the following: Primes have been studied for two millennia ((citation needed)) and rather little was (and still is) known. They are defined in the simplest terms, and the smartest minds have dealt with them, yet still they seemed to remain an invulnerable fortress. Now and again, one of these smart minds has got a glimpse through a window, but no more. It's presumptuous to claim that Riemann has conquered the fortress, but at least he has found a way how to assault it. Proving the Riemann Hypothesis would mean executing the final blow and taking residence in the prime fortress.

But back to the Euler product. The proof using the sieve of Eratosthenes dates back to Euler himself and couldn't be clearer and more insightful. Still, I'd like to take a look at a more technical proof, partly because it is a great practice in dealing with sums, partly because the Euler product is so immensely important that it's worth dwelling a little on it.

The careful reader will observe that plugging \\(s=1\\) into \\(\zeta(s)\\) yields \\(\sum 1/n\\) which is known as the [harmonic series](http://en.wikipedia.org/wiki/Harmonic_series_(mathematics)), one of the most fundamental series in mathematics, and usually the first example of a divergent series. The second proof makes use of the second of the three most important series in mathematics (the other one being the [exponential series](http://en.wikipedia.org/wiki/Exponential_function), with an honorary mention of the [Dirichlet series](http://en.wikipedia.org/wiki/Dirichlet_series) as the Riemann \\(\zeta\\)-function is a special case of it). So, we need to remember the formula for the [geometric series](http://en.wikipedia.org/wiki/Geometric_series):

\\[ \sum_{n\ge0}\alpha^n=(1-\alpha)^{-1}, \\]

where \\(|\alpha|<1\\). Now, as long as \\(\Re s>1\\), we have \\(|p^{-s}|<1\\) for any prime \\(p\\), so can expand the Euler product (yes, we kind of move backwards) to

\\[ \prod_p (1-p^{-s})^{-1}=\prod_p\sum_{n\ge0}p^{-ns}. \\]

Again, instead of an infinite product, we now have an infinite product of infinite series --  doesn't look easier at all. But let's just write out a few of these terms:

\\[ (1^{-s}+2^{-s}+2^{-2s}+2^{-3s}+\ldots)(1^{-s}+3^{-s}+3^{-2s}+3^{-3s}+\ldots)(1^{-s}+5^{-s}+5^{-2s}+5^{-3s}+\ldots)(1^{-s}+7^{-s}+7^{-2s}+7^{-3s}+\ldots)\cdots \\]

Expanding the product just means picking one summand from each factor at a time, and then sum up all the possible combinations. If I always pick the first summand, I certainly get

\\[ 1^{-s}\cdot1^{-s}\cdot1^{-s}\cdot1^{-s}\cdots=1^{-s}=1. \\]

OK, not too spectacular. Now, we pick the second summand of the first factor, and \\(1\\) everywhere else. This yields

\\[ 2^{-s}\cdot1^{-s}\cdot1^{-s}\cdot1^{-s}\cdots=2^{-s}. \\]

I think it is clear enough that I can obtain in similar ways a summand \\(p^{-s}\\) for every prime \\(p\\) by picking the second summand of the respective factor, and \\(1\\) otherwise. What else would I get? Can I get, say, \\(12^{-s}\\). Sure I can! I just pick the third summand of the first factor and the second summand of the second factor, and \\(1\\) otherwise. We get

\\[ 2^{-2s}\cdot3^{-s}\cdot1^{-s}\cdot1^{-s}\cdots=(2^2\cdot3)^{-s}=12^{-s}. \\]

I hope by now it is clear that we will get this way a summand \\(n^{-s}\\) for every natural number \\(n\\) when expending the product. On the other hand, the [fundamental theorem of arithmetic](http://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic) asserts that each natural number has a unique factorisation into prime powers, which means in our case that we will have each summand \\(n^{-s}\\) once _and once only_. Hence we can conclude

\\[ \prod_p (1-p^{-s})^{-1}=\prod_p\sum_{n\ge1}p^{-ns}=\sum_{n\ge1}n^{-s}, \\]

which we knew all along, but have now proved in a different way. Before, I claimed that the Euler product would encode the prime mystery, now I can claim that it encodes the fundamental theorem of arithmetic -- which is cool, since this theorem really is the reason why we got into primes in the first place.
