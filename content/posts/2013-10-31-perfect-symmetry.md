---
title: Perfect Symmetry
author: Markus Shepherd
type: post
date: 2013-10-31T23:17:14+00:00
url: /2013/10/perfect-symmetry/
categories:
  - Functional Equation
---

So far, we have seen how the Euler product links the $$\zeta$$-function to the prime numbers. More precisely, it encodes the fundamental theorem of arithmetic. One may also say, it's the _analytic_ version of it, in a sense that should become clearer shortly.

What we have done so far works perfectly for the real numbers. The sum $$\sum n^{-s}$$ that defines $$\zeta(s)$$ converges for $$s>1$$, that's how Leonhard Euler found his product, and that's what Peter Gustav Lejeune Dirichlet used to prove the [prime number theorem in arithmetic progressions](http://en.wikipedia.org/wiki/Dirichlet's_theorem_on_arithmetic_progressions). The ingenious step In Riemann's 1859 paper was to allow for _complex_ values $$s$$. As mentioned before, the same argument as in the real case proves that the sum converges for $$\Re s>1$$. Since the convergence is absolute, $$\zeta(s)$$ is analytic in this domain. If you don't know what analytic is, just read it as _well-behaved_ or, even better, _cool_.

The shame is that -- as you certainly have already heard if you still read this blog -- all the action takes place in the _critical strip_, i.e. the area just to the left of our line of convergence with $$0\le\Re s\le1$$. Riemann showed that we can calculate values of $$\zeta(s)$$ for $$\Re s\le1$$ through the beautiful functional equation

$$!\zeta(1-s)=2^{1-s}\pi^{-s}\cos(\pi s/2)\Pi(s-1)\zeta(s).$$<!-- more -->

Setting aside what all of these symbols exactly mean, the important fact is that the functional equation relates $$\zeta(1-s)$$ on the left hand side to $$\zeta(s)$$ on the right. In other words: values of $$\zeta(1/2+s)$$ are intimately linked to $$\zeta(1/2-s)$$, their mirror image along the line with $$\Re s=1/2$$. This is the famous _critical line_ that lies at the heart of the Riemann Hypothesis.

OK, we know how to calculate $$\zeta(s)$$ for $$\Re s>1$$ and, courtesy of the functional equation, equally for $$\zeta(1-s)$$, i.e., $$\Re s<0$$. Rats, again the critical strip is left out. Riemann found an expression for $$\zeta(s)$$ that's valid everywhere, but it involves some nasty integrals, so let's take an easier route. What we will consider is the similar sum

$$!\sum_{n\ge1}(-1)^{n+1}n^{-s}=1-2^{-s}+3^{-s}-4^{-s}+5^{-s}-6^{-s}+\ldots$$

Those familiar with series will immediately see that this sum converges if $$n^{-s}$$ tends to zero (cue: Leibniz criterion), which it obviously does for $$\Re s>0$$. The resulting function is sometimes called $$\eta(s)$$. The interesting bit is that I can express $$\eta(s)$$ in terms of $$\zeta(s)$$. Note that

$$!\eta(s)=(1+2^{-s}+3^{-s}+4^{-s}+5^{-s}+6^{-s}+\ldots)-2\cdot(2^{-s}+4^{-s}+6^{-s}+8^{-s}+10^{-s}+12^{-s}+\ldots)$$

The first expression in parentheses is of course just $$\zeta(s)$$, from the second expression in parentheses we can factor out $$2^{-s}$$ which yields $$2^{-s}\zeta(s)$$. Summarising this, we obtain

$$!\eta(s)=\zeta(s)-2\cdot2^{-s}\zeta(s)=(1-2^{-s+1})\zeta(s).$$

In other words, if we want to know a value of $$\zeta(s)$$ for $$0<\Re s<1$$, we can just calculate the value of $$\eta(s)$$ through the series above, and then divide this by the elementary factor $$1-2^{-s+1}$$. Strike! We finally know how to calculate $$\zeta(s)$$ for $$\Re s>0$$ (through $$\eta(s)$$), and then even further for all values $$\Re s<1$$ with the aid of the functional equation.

Now let's take a look at all the different factors. First, $$2^{1-s}\pi^{-s}$$ is very harmless, these are exponential functions, no zeros, no poles, very well-behaved. Next, $$\cos(\pi s/2)$$ is the equally well-known cosine function, one of the fundamental trigonometric functions. It is analytic with simple zeros for $$\pi s/2=\pi(k+1/2)$$ with $$k\in\mathbb{Z}$$, that is, $$s=2k+1$$, in other words for $$s$$ odd, positive or negative.

The function $$\Pi(s-1)$$ is lesser known, though this is partially due to my notation. It's better known as $$\Gamma(s)$$, and is an analytic version of the factorial ((I cannot resist to tell an anecdote from my time in Cambridge: I was giving a talk on prime generating functions, most of which involved heavy use of factorials. Unfortunately, throughout the entire talk I followed my German instincts and referred to them as _faculties_. I really wish someone would have had the courage to correct my mistake during the talk instead of politely ignoring it...)) function. That is, it satisfies the functional equation $$\Pi(s)=s\Pi(s-1)$$. Together with $$\Pi(0)=1$$, this implies $$ \Pi(n)=n! $$ for all non-negative integers $$n$$. For obscure reasons, Adrien-Marie Legendre favoured the use of $$\Gamma(s)=\Pi(s-1)$$ which in turn satisfies the far less catchy $$ \Gamma(n)=(n-1)! $$. With Carl Friedrich Gauss ((Gauss is not really one of my sources in this case, but considering his importance to mathematics in general, and the topics in question in particular, you couldn't wish for a stronger testimonial.)), Bernhard Riemann, Harold Edwards, and John Derbyshire virtually all my primary sources use the $$\Pi(s)$$ notation for the factorial function, so I don't even need to resort to my healthy francophobia in order to resent the $$\Gamma(s)$$ notation. On the mathematical side, the factorial function is a holomorphic function, i.e., analytic except for simple poles at the negative integers $$s=-1,-2,-3,\ldots$$ without zeros. So the factor $$\Pi(s-1)$$ contributes no zeros, but poles at $$s=0,-1,-2,\ldots$$.

Which brings us back to $$\zeta(s)$$. So far, we only understand the half-plane $$\Re s>1$$ where $$\zeta(s)$$ is analytic and has no zeros because of the Euler product. Further, it has a (simple) pole at $$s=1$$ as the defining series of $$\zeta(s)$$ then becomes the harmonic series. As it turns out, this poles is simple as well.

Through all this, we can describe $$\zeta(s)$$ pretty well for $$\Re s<0$$. Let's recap the contribution of the different factors in the domain $$\Re s>1$$. The exponential functions $$2^{1-s}\pi^{-s}$$ don't really do much. The cosine $$\cos(\pi s/2)$$ has zeros for $$s=1,3,5,\ldots$$, while the factorial function $$\Pi(s-1)$$ is equally boring without zeros or poles. Similarly, $$\zeta(s)$$ has no zeros, but the notorious pole at $$s=1$$. To summarise, the right hand side of the functional equation is zero for $$s=3,5,7,\ldots$$, the pole of $$\zeta(s)$$ at $$s=1$$ being neutralised by the zero of $$\cos(\pi s/2)$$, and has no poles. Since we're talking about an equation, the same must hold for $$\zeta(1-s)$$, i.e., $$\zeta(s)$$ in the domain $$\Re s<0$$ is analytic with zeros at $$s=-2,-4,-6,\ldots$$ These are the _trivial_ zeros of the $$\zeta$$-functions which are of little interest and don't contribute to the prime numbers.

The other zeros lie in the critical strip $$0\le\Re s\le1$$. These are the non-trivial zeros which are the subject of the Riemann Hypothesis: _All non-trivial zeros have real part $$1/2$$._ We will later see how these zeros are intimately linked to the distribution of the primes. As mentioned before, the functional equation establishes a symmetry of $$\zeta(s)$$ along the critical line $$\Re s=1/2$$. This means that any zero $$s$$ implies another zero $$1-s$$. We will later see that $$\zeta$$ is also symmetrical along the real axis, i.e., $$\zeta(\overline{s})=\overline{\zeta(s)}$$. This means, with every zero $$s$$ in the critical strip, we actually get four zeros: $$s$$, $$1-s$$, $$\overline{s}$$, and $$1-\overline{s}$$.

Before we look further into the zeros, we should try to understand where the functional equation comes from, and how we can use it to obtain yet another function, called $$\xi(s)$$, which exhibits an even more beautifully symmetrical behaviour. This will finally lead to yet another product representation of $$\zeta(s)$$ that will be key in the link between the $$\zeta$$-zeros and the distribution of the primes.

But I get ahead of myself. Let's summarise this long article: The series $$\sum n^{-s}$$ defines $$\zeta(s)$$ as an analytic function in the half-plane $$\Re s>1$$, but can be extended to a holomorphic function on the whole complex plane with a single simple pole at $$s=1$$ via the functional equation

$$!\zeta(1-s)=2^{1-s}\pi^{-s}\cos(\pi s/2)\Pi(s-1)\zeta(s).$$

It has zeros for the negative even numbers $$s=-2,-4,-6,\ldots$$ which are so uninteresting that mathematicians refer to them as the trivial zeros. The interesting, _non-trivial zeros_ lie in the critical strip $$0\le\Re s\le1$$ which are of paramount importance in the distribution of the primes.
