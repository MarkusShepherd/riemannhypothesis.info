---
title: More symmetry and Another Product
author: Markus Shepherd
type: post
date: 2013-12-01T21:29:17+00:00
url: /2013/12/more-symmetry-and-another-product/
categories:
  - "Riemann's Paper"
tags:
  - Polynomial
  - Product
  - Symmetry
  - Zeros
---

We've [seen](http://www.riemannhypothesis.info/2013/10/perfect-symmetry/) that $$\zeta(s)$$ satisfies the functional equation

$$!\zeta(1-s)=2^{1-s}\pi^{-s}\cos(\pi s/2)\Pi(s-1)\zeta(s).$$

(Well, it still needs to be proved, but let's just assume it's correct for now.) The goal of this post is an even more symmetrical form that will yield the function $$\xi(s)$$ which we can develop into an incredibly useful product expression.

On our wish list for $$\xi(s)$$ we find three items:



 	  1. It's  an _entire function_, i.e., a function that's holomorphic everywhere in $$\mathbb{C}$$ without any poles.
 	  2. It has zeros for all non-trivial zeros of the $$\zeta$$-function, and no others.
 	  3. It's perfectly symmetrical along the critical line, i.e., it satisfies $$\xi(1-s)=\xi(s)$$.

<!-- more -->
The first two requirements are fairly easy to satisfy. To make $$\zeta(s)$$ holomorphic, we just need to cancel out its single simple pole at $$s=1$$ by multiplying $$s-1$$. Keeping in mind the desired symmetry, we also multiply a factor $$s$$. To get rid of the trivial zeros $$s=-2,-4,-6,\ldots$$, plus the one we just introduced at $$s=0$$, we need to multiply by a function that has (simple) poles at exactly these points, and no zeros. From the functional equation, we know that the factorial function $$\Pi(s)$$ is a pretty good candidate, which has no zeros, but poles for $$s=-1,-2,-3,\ldots$$. So $$\Pi(s/2)$$ has poles at $$s=-2,-4,-6,\ldots$$, and $$\Pi(s/2-1)$$ has poles at $$s=0,-2,-4,\ldots$$, perfectly covering all the zeros we needed eliminated without introducing new ones. This leads us to

$$!\xi(s)=\zeta(s)s(s-1)\Pi(s/2-1)\hat{\xi}(s),$$

where $$\hat{\xi}(s)$$ is just a placeholder for other factors that may be necessary achieve requirement 3, the symmetry around the critical line. We are free to choose anything for $$\hat{\xi}(s)$$ as long as it does not interfere with the other two requirements, i.e., it cannot have zeros or poles. (Spoiler alert: Pretty much the only entire functions satisfying this are constant and exponential functions, and that's exactly what we will need.)

I won't try to create any further tension as we're almost there (and I suck at it anyway). Indeed, Riemann found the integral expression

$$!\pi^{-s/2}\Pi(s/2-1)\zeta(s)=-\frac{1}{s(1-s)}+\int_1^\infty\left(x^{s/2-1}+x^{-s-1/2}\right)\psi(x),\mathrm{d}x,$$

where

$$!\psi(x)=\sum_{n=1}^\infty e^{-\pi n^2 x}$$

is the exponential sum. I won't go into the details, but it is now obvious that the right-hand side is unchanged when you substitute $$s$$ by $$1-s$$. In other words, if we define ((The factor 1/2 has just been introduced to make certain calculations more convenient.))

$$!\xi(s)=\frac{1}{2}\pi^{-s/2}s(s-1)\Pi(s/2-1)\zeta(s)$$

we have found a function that satisfies all three requirements. Eureka!

So, why did we jump through all these hoops? I promised a nice product representation for $$\xi(s)$$, and we're now in the position to get cracking. More specifically, it's high time the zeros entered the scene!

Representing a function through a product over their zeros is a pretty common idea. Take, for instance, a polynomial function $$p(s)$$ of degree, say, $$d$$ with zeros $$\varrho_1,\ldots,\varrho_d$$. (Of course we are all aware of the fundamental theorem of algebra which ensures that every polynomial of degree $$d$$ has exactly $$d$$ zeros over the complex numbers, right?) Now, consider the expression

$$!\hat{p}(s)=p(0)\prod_{n=1}^d\left(1-\frac{s}{\varrho_n}\right).$$

For $$s=0$$, all factors are $$1$$, so $$\hat{p}(0)=p(0)$$. Further, if $$s=\varrho_i$$, i.e., one of the zeros, then the corresponding factor is $$0$$, and hence the whole product, as is the polynomial at this point, so $$\hat{p}(\varrho_i)=p(\varrho_i)$$. Now, we found an expression that corresponds to our polynomial in $$d+1$$ points (the $$d$$ zeros and the origin). Since the polynomial has $$d+1$$ degrees of freedom (the $$d+1$$ coefficients of the polynomial), it is completely determined by these points, and hence must correspond to our expression: $$\hat{p}(s)=p(s)$$ for all $$s$$. (In all I've just said I implicitly assumed the zeros to be simple, and $$p(0)\neq0$$, but these are just technical obstacles.)

Why shouldn't the same hold for infinitely many zeros? Holomorphic function are really just polynomials of infinite degree, so we would expect an expression like

$$!\xi(s)=\xi(0)\prod_\varrho\left(1-\frac{s}{\varrho}\right),$$

where the product runs over all the zeros of $$\xi(s)$$ which, by our construction, are exactly the non-trivial zeros of $$\zeta(s)$$. Of course, this argumentation is all very vague, and for the above expression to be correct, we at the very least need convergence of the product. As an additional obstacle, the product converges only conditionally, i.e., the convergence depends on the ordering of the zeros. It turns out the "right" ordering is to pair every zero $$\varrho$$ with the mirrored $$1-\varrho$$. Recalling what we learnt [earlier](http://www.riemannhypothesis.info/?p=45), it suffices then to prove that $$\sum_{\Im\varrho>0}1/|\varrho(1-\varrho)|$$ converges.

Riemann states in his paper (though he makes no attempt to prove it, so neither shall I feel under any obligation to do so) that the number of zeros of $$\zeta(s)$$ (or $$\xi(s)$$, if you prefer) in the critical strip with imaginary part between $$0$$ and $$T$$ is approximately

$$!\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}.$$

This implies, very roughly, that the $$n$$th zero has modulus about $$n/\log n$$, so the above sum behaves similar to $$\sum(\log n)^2/n^2$$ which indeed converges, and hence the product does.

There's a lot of hand-waving and unproved arguments in this article, some of which we may return to, some which we just leave as it is. But one conclusion will hopefully stick: We have the functions $$\zeta(s)$$ and $$\xi(s)$$ (which are essentially the same for all we are concerned about), and represented them as two products, one over the prime numbers, and one over the zeros in the critical strip. This intrinsically links these two together! We will go on to use the zeros to calculate primes, both approximately and exactly.
