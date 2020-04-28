---
title: Integral Madness
author: Markus Shepherd
type: post
date: 2014-04-13T15:25:54+00:00
url: /2014/04/integral-madness/
categories:
  - "Riemann's Paper"
tags:
  - Calculus
  - Euler
  - Gauss
  - Legendre
  - Riemann
  - Zeros
---

We've seen the calculus version

$$!J(x)=\frac{1}{2\pi i}\int_{a-i\infty}^{a+i\infty}\log\zeta(s)x^s\frac{\mathrm{d}s}{s},$$

of the Euler product, and we know how to express $$\xi(s)$$ as a product over its roots

$$!\xi(s)=\xi(0)\prod_\varrho\left(1-\frac{s}{\varrho}\right),$$

where

$$!\begin{align}\xi(s)&=\frac{1}{2}\pi^{-s/2}s(s-1)\Pi(s/2-1)\zeta(s)\nonumber\\&=\pi^{-s/2}(s-1)\Pi(s/2)\zeta(s).\nonumber\end{align}$$

High time we put everything together -- the reward will be the long expected _explicit formula_ for counting primes!<!-- more -->

First, let's bring the two formulae for $$\xi(s)$$ together and rearrange them such that we obtain a formula for $$\zeta(s)$$:

$$!\zeta(s)=\xi(0)\prod_\varrho\left(1-\frac{s}{\varrho}\right)\pi^{s/2}(s-1)^{-1}\Pi(s/2)^{-1}.$$

Before we proceed, let's get rid of this unnecessarily complicated factor $$\xi(0)$$. Using the formula above, this is

$$!\xi(0)=\pi^{-0/2}(0-1)\Pi(0/2)\zeta(0)=-\zeta(0).$$

The value of $$\zeta(0)$$ can be obtained in a similar fashion to [that of $$\zeta(-1)$$](http://www.riemannhypothesis.info/2014/02/infinity-is-worth-no-more-than-112/) by interpreting it as the sum

$$!\zeta(0)=\sum n^{-0}=1+1+1+1+1+\ldots,$$

which winds up to be, somewhat surprisingly, $$-\frac{1}{2}$$, giving us $$\xi(0)=\frac{1}{2}$$.

In our formula for $$J(x)$$, we have $$\log\zeta(s)$$, so it appears wise to take logarithms of both sides. Remembering  that the logarithm translates products into sums we obtain

$$!\log\zeta(s)=-\log2+\sum_\varrho\log\left(1-\frac{s}{\varrho}\right)+\frac{s}{2}\log\pi-\log(s-1)-\log\Pi(s/2).$$

If you're scared by this expression, remember that we need to plug it into our integral to get back to $$J(x)$$. Prime research is only for the valiant. But before we can do this, we first need to transform the integral slightly (through partial integration) to

$$!J(x)=-\frac{1}{2\pi i}\frac{1}{\log x}\int_{a-i\infty}^{a+i\infty}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{\log\zeta(s)}{s}\right)x^s\,\mathrm{d}s.$$

Now we can substitute the term $$\log\zeta(s)$$ by the above sum. Luckily, both differentiation and integration are transparent to addition, hence we can handle five (slightly) less intimidating integrals instead of one monster integral.

The derivation of these terms fill the better part of the second half in Riemann's paper, so I'm not gonna give a full account of the intricate arguments required to arrive at the final terms, but will instead be satisfied with a few remarks on each of them.

Let's start with the easiest one as an appetiser. The term $$\frac{s}{2}\log\pi$$ will simplify to $$\frac{1}{2}\log\pi$$ when divided by $$s$$, and then vanish completely when differentiated with respect to $$s$$. Nice! Unfortunately, the other terms won't behave nearly half as nicely as this one.

Another one, however, is still reasonably well behaved. The term $$-\log2$$ when plugged into the integral, gives us

$$!\frac{1}{2\pi i}\frac{1}{\log x}\int_{a-i\infty}^{a+i\infty}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{\log2}{s}\right)x^s\,\mathrm{d}s.$$

If you follow all steps through, this all just boils down to $$\log2$$ -- not too bad either.

OK, now let's roll up our sleeves, and get on with the real troublemakers. The next term we consider is $$-\log(s-1)$$ which yields the integral

$$!\frac{1}{2\pi i}\frac{1}{\log x}\int_{a-i\infty}^{a+i\infty}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{\log(s-1)}{s}\right)x^s\,\mathrm{d}s.$$

This integral is by no means easily simplified, so I'll just present you with the final version which is ((You may -- rightfully -- remark that during integration, the integrand 1/log t is undefined for t = 1 since log 1 = 0, and we cannot divide by zero. But rest assured that this is just another technicality that's easily circumvented. In fact, it's never quite sure which version an author works with: the integral that starts at 0 or the one that starts at 2. However, these two just differ by an additive constant, which is completely negligible when it comes to the asymptotic behaviour.))

$$!\int_0^x\frac{\mathrm{d}t}{\log t}=\mathrm{Li}(x).$$

The function $$\mathrm{Li}(x)$$ is also called the _logarithmic integral_, and will turn out to be the main term in our formula for $$J(x)$$, and a great approximation for the number of primes less than $$x$$ in general. I've [mentioned it before](http://localhost:8885/riemannhypothesis.info/2013/11/are-primes-independent/), and interpreted there $$1/\log t$$ as the density of the primes "near" $$t$$. This means we need to sum, or rather integrate, along all values of $$t$$ to obtain the total number of primes. Those working with (continuous) probabilities will be familiar with the concept.

All these words just to avoid admitting that I won't work out more details about the derivation of the main term at this point. Luckily, we still have more work to do anyway. Next, let's look at the sum over the roots $$\sum\log\left(1-\frac{s}{\varrho}\right)$$. The tricky bit here is that we would like to take the sum out of differentiation and integration, but this is not so straightforward since the sum only converges conditionally and hence care needs to be taken when interchanging limits. So, we are grateful to all the smart minds who did the hard work for us, and go on exchanging the order to obtain

$$!-\sum_\varrho\frac{1}{2\pi i}\frac{1}{\log x}\int_{a-i\infty}^{a+i\infty}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{\log(1-s/\varrho)}{s}\right)x^s\,\mathrm{d}s.$$

I hope you see the resemblance to the expression above that led to the main term, so we will  expect a similar result. The main difference is that, as noted, the convergence of the sum is only conditional, and hence the order in which the zeros are summed does matter. So, which is the right order?

Remember that zeros come in "pairs of pairs" since $$\xi(x)$$ has two symmetries. First, it is symmetrical along the real axis, that is $$\xi(s)=\xi(\overline{s})$$, where $$\overline{s}$$ is the complex conjugate which is nothing but the mirror image along the real axis. Since every single zeros that's been found is of the form $$\varrho=\frac{1}{2}+ti$$, where $$t$$ is a real number, this means that every zeros has a "twin" $$\overline{\varrho}=\frac{1}{2}-ti$$.

But there is another symmetry, the symmetry along the critical line $$\Re s=\frac{1}{2}$$. The function $$\xi(s)$$ has been defined such that $$\xi(1-s)=\xi(s)$$. This means that for every zero $$\varrho$$ we have another zero $$1-\varrho$$. For a zero $$\varrho=\frac{1}{2}+ti$$ on the critical line, this is actually the same "twin" $$1-\frac{1}{2}-ti=\frac{1}{2}-ti=\overline{\varrho}$$, but if there's any zero off the magical line, this will yield a total of three distinct other zeros associated with $$\varrho$$, which are $$\overline{\varrho}$$, $$1-\varrho$$, and $$1-\overline{\varrho}$$.

Back to our original topic, we wanted to find the right order of summation. When it comes to summing real values, usually the right thing to do is to sum in increasing order. Unfortunately, the zeros are complex and hence have no natural order. However, we know they are condensed to the critical strip, and we will just sum them up according to their imaginary part. But that's not enough -- we will also need to pair each zero $$\varrho$$ with one of it's "twins". It turns out the right one is $$1-\varrho$$, the mirror image with respect to the point $$s=\frac{1}{2}$$.

All this combined with some more careful analysis, we arrive at the penultimate term in our expression for $$J(x)$$:

$$!-\sum_{\Im\varrho>0}\left(\mathrm{Li}(x^\varrho)+\mathrm{Li}(x^{1-\varrho})\right).$$

This leaves the term $$-\log\Pi(s/2)$$ and the corresponding integral

$$!\frac{1}{2\pi i}\frac{1}{\log x}\int_{a-i\infty}^{a+i\infty}\frac{\mathrm{d}}{\mathrm{d}s}\left(\frac{\log\Pi(s/2)}{s}\right)x^s\,\mathrm{d}s.$$

There's a series for $$\Pi(s)$$ that translates this integral into a series of integrals, each one similar to the ones we have seen before. Summing these up again, we arrive at the final term

$$!\int_x^\infty\frac{\mathrm{d}t}{t(t^2-1)\log t}.$$

This may look scarier than it is, particularly since this integral grows small very quickly and will thus be asymptotically negligible.

It's high time we wrapped up things and take a look at the result of all this madness:

$$!J(x)=\mathrm{Li}(x)-\sum_{\Im\varrho>0}\left(\mathrm{Li}(x^\varrho)+\mathrm{Li}(x^{1-\varrho})\right)+\int_x^\infty\frac{\mathrm{d}t}{t(t^2-1)\log t}-\log2.$$

This is Riemann's main result, and here are two things (amongst others) that make it so remarkable (not counting the fact that Riemann didn't bother to rigorously prove half of the steps along the way).

First, the "main" term. I put _main_ in quotes, because just by looking at it, one couldn't tell which of these terms dominates. But remember that by the mid 19th century, the Prime Number Theorem has been unproved for half a century, and this was the first real justification (beyond empirical data, that is) in conjecturing that the density of the erratic primes would be given by a formula as simple as $$1/\log x$$. You may point out that we didn't actually count primes with $$J(x)$$, but indeed prime powers. However, we will take a closer look into this, and it will not be a big difference anyway. For the moment, just be reminded that we can recover $$\pi(x)$$ from $$J(x)$$ through Möbius inversion.

Second, the zeta zeros. When Gauss and Legendre conjectured their versions of the Prime Number Theorem, it was surprising to have any kind of simple _asymptotic_ for the number of primes. Riemann's result goes on step further. He did not approximate the number of primes, he computed them _exactly_. There's no uncertainty or error attached to this formula, if you diligently carry out every single calculation you will end up with the exact number of primes below $$x$$, not just a rough guess. Now, what does it mean to carry out all calculations? The logarithmic integral $$\mathrm{Li}(x)$$, though not quite elementary, is still quite easy to handle. The same goes for the integral and, well, $$-\log 2$$ is just a constant. All these terms can be evaluated to any desired precision by any modern computer. The series over the zeros however is a little different. We know that there's an infinite number of zeta zeros, which means that no machine can ever find the exact value of this term, no matter how much time (or money) you spend on it. Still, a truncated series can still be used to approximate the final value, and in this respect every zero that we add to the calculation makes Riemann's formula more accurate. Note how every single zero carries its individual secret about the primes in it, and they all come together to unravel the prime mystery, like notes in a beautiful symphony that form the music together.

I hope this glimpse of beauty makes up for all the toiling and sweating with the nasty integrals...
