---
title: The Prime Bet
author: Markus Shepherd
type: post
date: 2017-05-31T05:41:25+00:00
url: /2017/05/the-prime-bet/
categories:
  - Euler product
  - Primes
  - Probability
tags:
  - Apéry
  - Basel problem
  - Bet
  - constant
  - Coprime
  - Divisor
  - Euler
  - gcd
  - pi
  - Prime factor
  - Probability
  - Pub
  - Python
  - Random
  - Riemann
  - Wiles
  - Zeta function
  - Zhang
---

Let's say you sit in a pub, minding your own business, when all of a sudden a stranger walks up to you and offers you a bet:

> We'll choose two positive integers at random. If they have any divisor in common (other than \\(1\\)) I'll pay you a dollar, else you'll pay me a dollar. Are you in?

Apart from the question what kind of establishments you frequent, you should be wondering: is this a good bet for you?

When two integers have no divisors in common except the trivial divisor \\(1\\) we say they are _coprime_ or _relatively prime_. \\(6\\) and \\(9\\) have the common divisor \\(3\\), so they are _not_ coprime, whilst \\(8\\) and \\(9\\) only have the trivial common divisor \\(1\\), so they are coprime.

This makes you start thinking: "As numbers grow bigger, aren't there a lot of divisors out there? After all, half the numbers are even, so if we hit two even numbers, they'll have the factor \\(2\\) in common and I'll win. And then there's \\(3\\), \\(5\\), \\(7\\), ... Seems like a good deal!"

<!-- more -->

Is it, though? Let's do some experiments! This simply Python script should give a decent approximation:

```python
from math import gcd
from random import randint
from sys import maxsize

repetitions = 10 ** 8
count = sum(
    1 if gcd(randint(1, maxsize), randint(1, maxsize)) == 1 else 0
    for _ in range(repetitions)
)
pct = 100 * count / repetitions

print(f"{count} out of {repetitions} pairs were coprime ({pct:.3f}%)")
```

This will pick two (largish) integers at random ((I was (deliberately) vague when saying _choose two random numbers_. There is no way of choosing two _arbitrarily large_ integers uniformly at random, so what you need to do is pick an upper bound _N_ and choose numbers below _N_ uniformly at random. In the calculations of the probabilities you'd take the limit _N_ → ∞. But we'll be hand-waving to begin with, so no reason to be exact here.)), check if they are coprime – which is the same as saying that they're greatest common divisor (_gcd_) is \\(1\\) – and repeat the procedure 100 million times. At the end, it will print something like this:

```
60797595 out of 100000000 pairs were coprime (60.798%)
```

If you run this, the exact numbers will obviously be different, but the bottom line is that in over 60% of the cases you'll end up with two coprime numbers. Don't take the bet! (This is generally a good rule of thumb when a stranger makes you any kind of offer.)

So, where does that number – \\(0.608\\)ish – come from? There is a nice and easy representation of the exact number, and if you've never heard of this problem, you might be surprised that the answer involves \\(\pi\\) – the ubiquitous constant of circle fame. What's it got to do in number theory? Quite frankly, I'm not sure, but we can prove it, so bear with me.

First, let's look at the above probability more closely. For two numbers to have a non-trivial common divisor means in particular that there is a prime that divides both of these numbers. If they are coprime, then there's no prime dividing both of them. What are the odds of that? Well, half the numbers will be divisible by \\(2\\) – the even numbers. The probability that both numbers are even is \\(\frac1{2^2}\\), so the probability that they are not divisible by \\(2\\) is the complement \\(1-\frac1{2^2}\\). Likewise, a third of all numbers are divisible by \\(3\\), so the probability of having \\(3\\) as a common factor is \\(\frac1{3^2}\\), with a complement of \\(1-\frac1{3^2}\\).

We can consider the probabilities of being divisible by any two given prime numbers as independent, so we can just multiply all these terms together for the probability \\(P\\) that two integers are coprime:

\\[ P = \prod_p \left( 1 - \frac{1}{p^2} \right), \\]

where the product runs over all primes \\(p\\). This should look awfully familiar to you. If it's been to long and I need to jog your brain, remember the Euler product that is at the very core of our investigations:

\\[ \zeta(s) = \sum_{n\ge1} \frac{1}{n^s} = \prod_p \frac{1}{1 - \frac{1}{p^s}}. \\]

In other words, our probability is nothing but

\\[ P = \frac{1}{\zeta(2)} = \frac{1}{\sum_n \frac{1}{n^2}}. \\]

The value of this particular sum \\(\sum n^{-2}\\) became rather famous in its own right as the **Basel problem**, first posed in 1644 and finally solved in 1734 by none less than the great Leonhard Euler. By now, dozens of proofs have been published, most of which calculate some form of integral, but none is clearer and more beautiful than the master's original one, so let's dive into that.

We'll obtain two series representations of \\(\sin x\\) and compare them with one another. First, let's take a look at the **Taylor series** of the sine function. In general, this series is defined for a smooth (read: well-behaved) function \\(f(x)\\) as

\\[ f(x) = \sum_{n\ge0} \frac{f^{(n)}(0)}{n!} x^n, \\]

where \\( n! \\) is the factorial function and \\(f^{(n)}(0)\\) is the \\(n\\)-th derivative of \\(f\\) evaluated at \\(x=0\\). The derivates of \\(f(x)=\sin x\\) are about as easy as they get:

\\[ f(x) = f^{(0)}(x) = \sin x, \\]
\\[ f^{(1)}(x) = \cos x, \\]
\\[ f^{(2)}(x) = -\sin x, \\]
\\[ f^{(3)}(x) = -\cos x, \\]
\\[ f^{(4)}(x) = \sin x, \\]

from where it all begins over and over in a neat \\(4\\)-cycle. In particular we have \\(f^{(4n+1)}(0)=\cos0=1\\), \\(f^{(4n+3)}(0)=-\cos0=-1\\), and \\(f^{(2n)}(0)=\pm\sin0=0\\), which yields the following classic series representation for the sine-function:

\\[ \sin x = \sum_{n\ge0} \frac{(-1)^n}{(2n+1)!} x^{2n+1}. \\]

We'll take one \\(x\\) out of the sum and use the slightly different form

\\[ \frac{\sin x}{x} = \sum_{n\ge0} \frac{(-1)^n}{(2n+1)!} x^{2n} = 1 - \frac{1}{6} x^2 + \frac{1}{120} x^4 \mp \ldots \\]

Half way there. Now we'll develop a product representation for \\(\sin x\\), more precisely an expression over its zeros. We used a very similar expression when we developed the [product representation for \\(\xi(s)\\)]({{<ref "posts/2013-12-01-more-symmetry-and-another-product">}}). The general form is

\\[ f(x) = f(0) \prod_\varrho \left(1-\frac{x}{\varrho}\right), \\]

where the product runs over all the zeros \\(\varrho\\) of \\(f\\). Euler was very much ahead of his time in using such a product and just manipulated formal expressions, much like in the [famous sum \\(1+2+3+\ldots=-\frac{1}{12}\\)]({{<ref "posts/2014-02-23-infinity-is-worth-no-more-than-112">}}). It wasn't until the late 19th century, when Karl Weierstraß formally proved products like this in an attempt to verify some of the claims in Riemann's famous paper.

Now, remembering that \\(\sin x\\) has zeros for all \\(k\pi\\) with \\(k\in\mathbb{Z}\\), and \\(\frac{\sin x}{x}\to1\\) as \\(x\to0\\), we can write

\\[ \frac{\sin x}{x} = 1 \cdot \prod_{k\ge1} \left(1-\frac{x}{k\pi}\right) \left(1+\frac{x}{k\pi}\right) = \prod_{k\ge1} \left(1-\frac{x^2}{k^2\pi^2}\right). \\]

This is a product of sums in \\(x\\), so if we manage to multiply out everything we'll have another series representation of \\(\sin x/x\\). In general, multiplying out such an expression means for every \\(k\\) choosing either the left (\\(1\\)) or the right (\\(-\frac{x^2}{k^2\pi^2}\\)) summand and then summing everything up over all possible combinations (like _left, left, left, ..._ or _left, right, left, ..._). This is actually much easier than it sounds since we don't need to deal with all the infinite coefficients which in turn will be infinite sums. Instead, all we care about are the terms that contain \\(x^2\\). Because all factors of the product above are of the form \\(1-c_k x^2\\) this means we choose for one \\(k\\) the right summand and the left ones (which are all \\(1\\)) for everything else. Hence the above product will expand into a series like so:

\\[ \frac{\sin x}{x} = 1 - \left( \sum_{k\ge1} \frac{1}{k^2\pi^2} \right) x^2 \pm \ldots \\]

The rest will be higher order terms of degree \\(4\\) or more which we don't care about. What we've obtained are two series representations for \\(\sin x/x\\), both of the form \\(\sum c_k x^k\\). It's pretty easy to show that if you have two such series for the same function, all of their coefficients must be identical. This means in particular that the coefficients in front of \\(x^2\\) must match. From the Taylor series we got \\(-1/6\\), while the product yielded \\(\sum1/k^2\pi^2\\), so we just obtained the equality

\\[ - \frac{1}{6} = - \sum_{k\ge1} \frac{1}{k^2\pi^2}. \\]

We can take the \\(\pi\\)s out of the series since they don't depend on \\(k\\) and rearrange a little to finally arrive at Euler's solution to the Basel problem:

\\[ \zeta(2) = \sum_{n\ge1} \frac{1}{n^2} = \frac{\pi^2}{6}. \\]

Using this in our calculations above we obtain the exact result for the probability \\(P\\) that two randomly chosen positive integers are coprime:

\\[ P = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \approx 0.60792710185403\ldots \\]

As I said before, I'm still puzzled every time I work on this how the trigonometric constant \\(\pi\\) manages to creep up all over maths in seemingly unrelated fields.

Euler's solution I presented here lacks some form of rigour since he couldn't prove that the product representation actually converges, but his manipulations as formal identities not only solved the famous Basel problem correctly, it can actually do lot more. When multiplying out the product above I ignored any terms higher than \\(x^2\\). However, if you do carry out these calculations you'll get expressions in \\(\sum 1/k^{2n}\pi^{2n}\\), so you'll obtain similar results for all \\(\zeta(2n)\\). The exact calculations are well beyond our scope here, but it's worth noticing that Euler solved the values of \\(\zeta(2n)\\) for all even integers, and in particular we know therefore that all \\(\zeta(2n)\\) are irrational and even transcendental numbers since they are expressions in \\(\pi^{2n}\\). You might ask: what about odd arguments \\(\zeta(2n+1)\\)?

Somewhat surprisingly the answer is: very little. It wasn't until 1978 that Roger Apéry proved that \\(\zeta(3)=\sum n^{-3}\\), a number that's now referred to as _Apéry's constant_, is irrational. No other value of \\(\zeta(2n+1)\\) is known to be irrational ((Some progress has been made, but no single value has been cracked so far.)) (or rational for that matter), let alone any nice closed form like we had with \\(\zeta(2)=\pi^2/6\\).

I'll leave you with the somewhat comforting note that Apéry was of the almost biblical age (for a mathematician) of over 60 years when he made his breakthrough. Mathematics is often called "a young men's discipline" – you either make a significant contribution before you reach tenure or you never will. Roger Apéry is one counter-example, Andrew Wiles and Yitang Zhang are others. It's never too late to start working on that one big theorem!
