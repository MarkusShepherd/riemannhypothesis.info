---
title: From Zeta to J and Back (And Yet Again Back)
author: Markus Shepherd
type: post
date: 2014-04-06T14:13:42+00:00
url: /2014/04/from-zeta-to-j-and-back-and-yet-again-back/
categories:
  - Euler product
tags:
  - Euler
  - Functions
  - Fundamental Theorem
  - Golden Key
  - Logarithm
  - Newton
---

We know a lot about the [\\(\zeta\\) and \\(\xi\\)-functions]({{<ref "posts/2013-12-01-more-symmetry-and-another-product.md">}}), we've learnt all about the different [prime counting functions]({{<ref "posts/2014-01-12-counting-primes-functionally.md">}}), most notably \\(J(x)\\), so it's high time we found a connection between the two. Probably not too surprisingly, the crucial link is our good friend, the Euler product

\\[ \zeta(s)=\prod_{p}(1-p^{-s})^{-1}. \\]

What we want to develop now is a version of this product that will suit us to find a formula that magically can count primes. (Remember that the Euler product is an [analytical version of the fundamental theorem of arithmetic]({{<ref "posts/2013-10-31-perfect-symmetry.md">}}), so this is a natural starting point for our search.)

<!-- more -->

The only trouble is that we have a product, but analysis is all about _series_. Luckily, we have another good and reliable friend that can transform a product into a sum: the logarithm. So, by taking \\(\log\\) on both sides, we obtain something easier to handle:

\\[ \log\zeta(s)=-\sum_p\log(1-p^{-s}). \\]

The cool bit is that there is a classical result that gives us a series expression for \\(\log(1-x)\\). This dates back to Isaac Newton and goes as follows:

\\[ \log(1-x)=-\sum_{n\ge1}\frac{1}{n}x^n, \\]

which immediately allows us to substitute the inner term:

\\[ \log\zeta(s)=\sum_p\sum_{n\ge1}\frac{1}{n}p^{-ns}. \\]

With some technical acrobatics we can convince ourselves that the series are sufficiently well behaved, such that we can swap the order of summation and write instead

\\[ \log\zeta(s)=\sum_{n\ge1}\sum_p\frac{1}{n}p^{-ns}. \\]

Granted, this doesn't look any easier or even friendly than our nice, familiar Euler product, but remember the slightly esoteric function we defined to count prime powers:

\\[ J(x)=\sum_{n\ge1}\sum_{p^n\le x}\frac{1}{n}. \\]

As you see, the only real differences are that the innermost sum is truncated at \\(p^n\le x\\), and the additional factor \\(p^{-ns}\\) in the sum. We will handle both issues by introducing analysis' killer feature: integrals. If you just exercise a little basic calculus, it's easy to see that \\(p^{-ns}\\) can be expressed as

\\[ p^{-ns}=s\int_{p^n}^\infty x^{-s-1} dx. \\]

(Just notice that the antiderivative of \\(x^{-s-1}\\) is \\(\frac{1}{-s}x^{-s}\\) which is zero at infinity since we assume here \\(\Re s>1\\).) Now, let's plug this into our expression above:

\\[ \log\zeta(s)=\sum_{n\ge1}\sum_p\frac{1}{n}s\int_{p^n}^\infty x^{-s-1} dx. \\]

Yes, I know this looks even messier than before, but bare with me, it's worth it and will become clearer shortly. What we want to do next is drag the integral sign out of the sums. This is no problem in principal since integration is "transparent" under addition, but we have to keep two things in mind: First, since we talk about infinite sums, caution is in order to ensure convergence, and second, the range of integration depends on the variables we're summing over, so we need to think how this range may change. As usual, we don't pay too much attention to the question of convergence, but are just happy for others to take care of the technicalities.

The second point, however, needs some thinking. The easiest way to find the right boundaries for integration and summation is to consider the different ranges and formulate common constraints. In this case we sum over all \\(n\ge1\\) (this will remain unchanged), all primes \\(p\\), and integrate over all \\(x\ge p^n\\). So, if we want to take the integral out of the sums and make the range independent of \\(p\\) and \\(n\\), we extend it to \\(0\le x\le\infty\\), but need to add the restriction \\(p^n\le x\\) then to the summation over the primes \\(p\\). That's it! We obtain:

\\[ \log\zeta(s)=s\int_{0}^\infty\left(\sum_{n\ge1}\sum_{p^n\le x}\frac{1}{n}\right)x^{-s-1} dx. \\]

I've already put the parentheses in the right place, so we only need to compare this to our definition above, and notice with a sign of relieve that things start to look prettier:

\\[ \log\zeta(s)=s\int_{0}^\infty J(x)x^{-s-1} dx. \\]

John Derbyshire dubbed this formula the _Calculus Version of the Golden Key_, his nickname to the Euler product. He also gave a little more (graphical) intuition behind the deduction of the formula in chapter 19.V-VI of his book.

 You may still not be convinced that any of this is useful. After all, we didn't get anything other than an expression for \\(\log\zeta(s)\\) that not only contains a formula we can hardly control, but on top of it all is even hidden away in an integral. But just as we recovered \\(\mu(n)\\) from the definition of \\(J(x)\\) through a clever trick known as Möbius-inversion, we can now recover \\(J(x)\\) from the formula we found through an even more powerful tool called Fourier-inversion. Again, this would not only deserve its own article, but rather its own blog. Instead, I will just present you the result that we obtain by applying a little Fourier-magic to the _Golden Key_:

\\[ J(x)=\frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}\log\zeta(s)x^s\frac{ds}{s}, \\]

where \\(a\\) is any real number with \\(a>1\\). Now, recall that we can express \\(\zeta(s)\\) as a product over its zeros (which means we have a series expression for \\(\log\zeta(s)\\)), and hence we will be able to express \\(J(x)\\) as a sum over the legendary \\(\zeta\\)-zeros. Further, we can calculate \\(\pi(x)\\) from \\(J(x)\\) (in fact, these behave the same asymptotically), and so we can exactly (mind, these are strict equalities, not only approximations) count the primes by virtue of calculating the zeros.

These stubborn, erratic creatures that we call primes are thereby completely determined by the zeros of Riemann's \\(\zeta\\)-function. This is what makes the Riemann Hypothesis so powerful and surprising: Primes are volatile and unpredictable, but they obey the law of the zeros, and if Riemann was right, these zeros fall all on one single straight line, out of all possible places in the critical strip. Bernhard Riemann brought order to the chaos that governed the prime research for two millennia!
