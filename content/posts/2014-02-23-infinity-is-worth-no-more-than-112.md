---
title: Infinity Is Worth No More Than -1/12
author: Markus Shepherd
type: post
date: 2014-02-23T10:38:53+00:00
url: /2014/02/infinity-is-worth-no-more-than-112/
categories:
  - Feature
tags:
  - Infinity
  - Series
---

On 16 January 1913, a confused manuscript reached the famous mathematician G. H. Hardy in Cambridge. Other researchers have received similar letters before, and rejected it due to the seemingly incoherent formulae mixed with trivial mathematical results. Professional mathematicians are used to receiving manuscripts by amateurs who believe to have solved famous problems, but this particularly odd scribble caught the eye:

\\[ 1+2+3+4+5+6+\ldots+\infty=-\frac{1}{12} \\]

Did this amateur mathematician really think that the sum of all natural numbers, a value that will exceed any given boundary at some point, will wind up being a negative fraction? M. J. M. Hill of the University College, London, simply responded that the author must have fallen victim to the pitfalls of divergent series and referred him to a standard textbook on the topic.

So, was this really just the work of a lunatic? Well, recently, the [New York Times](http://www.nytimes.com/2014/02/04/science/in-the-end-it-all-adds-up-to.html) covered the topic, linking a [video](http://www.numberphile.com/videos/analytical_continuation1.html) in which two physicists explain the importance of this result in modern string theory. While many physicists may not be too far from lunatics, these two make a pretty strong argument in this case:<!-- more -->

We will start with a different sum \\(S_1\\) which just adds ones and subtracts them again:

\\[ S_1=1-1+1-1+1-1\pm\ldots \\]

What's the value of this infinite sum? If you stop at an odd position, you will get \\(1\\), but if you move on to next even position, it will be back to \\(0\\). This will continue for ever and ever, so the value of the sum will alternate between \\(0\\) and \\(1\\). It seems like these two values fight to dominate the sum, but the answer is surprisingly Solomonian: \\(\frac{1}{2}\\). Here's why: We subtract the sum from \\(1\\) and see what happens:

\\[ \begin{align}1-S_1&=1-(1-1+1-1+1-1\pm\ldots)\nonumber\\&=1-1+1-1+1-1+1\mp\ldots\nonumber\end{align} \\]

But this is just the original sum again! Hence, we just found the simple relationship

\\[ 1-S_1=S_1 \\]

which we can solve easily to \\(S_1=\frac{1}{2}\\). ((For the record, this sum is also know as [Grandi's series](http://en.wikipedia.org/wiki/Grandi%27s_series).)) If you think this was weird, just wait for it.

Next, we'll look at a sum that also involves all natural numbers, but we use them alternating as in \\(S_1\\). This sum is

\\[ S_2=1-2+3-4+5-6\pm\ldots \\]

What we will do now is add the sum to itself, obtaining \\(2S_2\\). But when we add the two, we will shift the second sum by one position. See what happens:

\\[ \begin{align}2S_2&=1-2+3-4+5-6\pm\ldots\nonumber\\&\qquad+1-2+3-4+5\mp\ldots\nonumber\\&=1-1+1-1+1-1+1\mp\ldots\nonumber\end{align} \\]

At this point you probably scream out: But that's just \\(S_1\\) again! Just like magic, we ended up with a value that we already know:

\\[ 2S_2=S_1=\frac{1}{2} \\]

which directly yields \\(S_2=\frac{1}{4}\\). Cool! Now, we're only one step away from unraveling the mystery sum. What we do now is subtract our new friend \\(S_2\\) from our original sum which we shall call for short \\(S=1+2+3+4+\ldots\\):

\\[ \begin{align}S-S_2&=1+2+3+4+5+ 6+7+ 8+\ldots\nonumber\\&\,-1+2-3+4-5+ 6-7+ 8\mp\ldots\nonumber\\&=0+4+0+8+0+12+0+16+\ldots\nonumber\end{align} \\]

So we end up with \\(4+8+12+16+\ldots\\) We notice that all summands are a multiple of \\(4\\), so we can take that out of the sum, and obtain:

\\[ S-S_2=4(1+2+3+4+5+\ldots) \\]

Another moment to exclaim: We got back to \\(S\\[  Also, remember that we know  \\]S_2\\) to have the value \\(\frac{1}{4}\\). Putting all things together, this yields

\\[ S-\frac{1}{4}=4S \\]

Exercising our rusty algebra a little, we finally arrive at

\\[ S=1+2+3+4+5+6+\ldots=-\frac{1}{12}. \\]

It may be madness, but there's a system behind it!

Now, the trained mathematicians or other sceptical minds may have impatiently waited to destroy my little show by pointing out the obvious mistake in this chain of arguments. Strictly, that is _analytically_, speaking, none of these sums converge, so me treating them as numbers and manipulating the equations as though they were numbers indeed is pretty much cheating. But rearranging (infinite) sums _formally_ and neglecting the question of convergence is a surprisingly powerful and useful tool. One particular master of this craft was Leonard Euler who by these means solved the famous [Basel problem](http://localhost:8885/riemannhypothesis.info/2017/05/the-prime-bet/)

\\[ \sum_{n\ge1}\frac{1}{n^2}=1+\frac{1}{4}+\frac{1}{9}+\frac{1}{16}+\frac{1}{25}+\ldots=\frac{\pi^2}{6}. \\]

This proves that sometimes the restraints of convergence are too tight and formal manipulations can lead to interesting and useful results. Indeed, Euler himself is credited ((This is somewhat [controversial](http://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF#History), but given his other work entirely possible.)) with finding the result that all natural numbers sum up to \\(-\frac{1}{12}\\).

This is all fair enough, but how is some formal manipulation relevant to the prime numbers and the rest of this blog? As always, it comes down to the \\(\zeta\\)-function. Remember the definition:

\\[ \zeta(s)=\sum_{n\ge1}n^{-s}. \\]

This converges for \\(\Re s>1\\) and hence gives meaningful results only in this domain. But this is largely due to the singularity of \\(\zeta(s)\\) at \\(s=1\\) where the defining series boils down to the harmonic series. Let's forget convergence for a second, and just plug \\(s=-1\\) into the definition of \\(\zeta(s)\\). What we get is

\\[ \zeta(-1)=\sum_{n\ge1}n^{-(-1)}=1+2+3+4+5+\ldots \\]

I hope by now your excitement to rediscover our mystery sum has not eased up but intensified: \\(\zeta(-1)=S\\). Euler couldn't get past the singularity in the \\(\zeta\\)-function as he only considered real values for \\(s\\), but Riemann could! Extending the domain to complex numbers, he was able to circumvent the singularity and attach a meaningful value to \\(\zeta(-1)\\). So now, it's time to go back to the [functional equation](http://www.riemannhypothesis.info/?p=93)

\\[ \zeta(1-s)=2^{1-s}\pi^{-s}\cos(\pi s/2)\Pi(s-1)\zeta(s). \\]

Setting \\(s=2\\), we obtain our ominous \\(\zeta(-1)\\) on the left hand side. What do we get on the right? Well, \\(2^{-1}\pi^{-2}\\) are just constants, \\(\cos(\pi)\\) is \\(-1\\), and \\(\Pi(1)\\) is \\(1! \\) or simply \\(1\\). We're left with \\(\zeta(2)\\) which happens to be the series over the reciprocals of all square numbers. Wait, didn't we see this just now? Yes, that's the famous Basel problem! What Euler calculated was nothing but the value of \\(\zeta(2)\\). Combining all this, we arrive at

\\[ \zeta(-1)=\frac{1}{2}\cdot\pi^{-2}\cdot(-1)\cdot1\cdot\frac{\pi^2}{6}=-\frac{1}{12}. \\]

I'll give you a moment to breathe in the full beauty of mathematics.

Done?

We started out with a seemingly non-sense question about the sum of all natural numbers, came up with a downright insane answer, and ended up combining various deep results to give a real meaning to all this madness. Mathematics at its best.

By the way, the "lunatic" who sent the letter to Hardy was no one less than Srinivasa Ramanujan who is now widely regarded as one of mathematics' greatest genii. Whoever remembers M. J. M. Hill?
