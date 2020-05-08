---
title: Are Primes Independent?
author: Markus Shepherd
type: post
date: 2013-11-24T14:32:23+00:00
url: /2013/11/are-primes-independent/
categories:
  - Probability
tags:
  - Conjecture
  - Gauss
  - Hardy
  - Littlewood
  - Prime number theorem
  - Probability
  - Twin primes
---

The question may sound silly, but I hope it will become apparent that it's very reasonable to ask. What we will examine here is the _probabilistic interpretation_ of the prime distribution. So, essentially we ask: "What's the probability that a randomly chosen number is prime?" Those familiar with some basic probability theory know the notion of independency in this context, so the question I'm basically interested in here is if the probability to find a prime is independent of the preceding or following numbers. This post is a little out of the regular narrative, but it's something I have been thinking about recently, and I think it makes a cute article.

But one step back. First consider the following problem: We pick a number \\(X\\) not exceeding some (large) \\(n\\) at random. What are the odds this number is prime? Well, this is a classic example of a discrete probability, so the answer is _positive cases over all cases_, i.e.,

\\[ P(X\in\mathbb{P})=\frac{\pi(n)}{n}, \\]

where \\(\mathbb{P}\\) denotes the set of all primes, and \\(\pi(n)\\) is the prime counting function, i.e., the number of primes not exceeding \\(n\\). Now, the famous Prime Number Theorem states that we can approximate \\(\pi(n)\\) with the elementary function

\\[ \pi(n)\sim\frac{n}{\log n}. \\]

Don't worry too much about the exact meaning of the tilde, we will have plenty of opportunity to examine it further. For now just read it as "the left-hand side behaves similarly to the right-hand side". Now we can substitute this approximation in the calculation of the probability above, and obtain

\\[ P(X\in\mathbb{P})\sim\frac{n/\log n}{n}=\frac{1}{\log n}. \\]

<!-- more -->

In other words, a randomly chosen number between \\(1\\) and \\(n\\) is prime with probability roughly \\(1/\log n\\). What's more, we can even justify saying that a number "around a large \\(n\\)" is prime with probability \\(1/\log n\\). To illustrate, take \\(10^{100}\\), a \\(1\\) followed by 100 zeros. (And that is still a small number in the context of number theory.) Below it, there are of course plenty of numbers with 99 digits or less, but obviously 90% of the numbers up to \\(10^{100}\\) have 100 digits. This means that the vast majority of the weight in the above probability lies on these numbers, justifying the statement.

In fact, we can see that we're right in interpreting \\(1/\log n\\) as the probability that \\(n\\) is prime in a much more rigorous way. In the terms of probability theory, it means that \\(1/\log n\\) is something like the density function associated with our experiment. (Actually, it would need to be normalised, but let's not concern ourselves with that.) So, in order to get the number of all primes up to \\(n\\), we would need to sum up all these weights. Since we have a continuous function, we use the integral instead, and arrive at another estimate

\\[ \pi(n)\sim\int_0^n\frac{\mathrm{d}x}{\log x}. \\]

The function on the right-hand side is known as \\(\mathrm{Li}(n)\\), and was already examined by Gauss. The two approximations \\(n/\log n\\) and \\(\mathrm{Li}(n)\\) for \\(\pi(n)\\) are in a certain sense equivalent (just do a partial integration, if you're curious), but as it turns out, \\(\mathrm{Li}(n)\\) is empirically more accurate, predicting the distribution of primes with very small relative errors.

But I've gone astray a little. We wanted to know if primes are independent. Well, you may point out that obviously they're not: if \\(X\\) is a (large) prime, then it is odd, so \\(X+1\\) is even and hence composite. But \\(X+2\\) may be prime, and indeed there is an abundance of examples where both \\(X\\) and \\(X+2\\) are prime. These are called _twin primes_, and it is an open question if there are infinitely many of them. (Most mathematician would believe so, and we will make use of one more qualified conjecture in just a moment.)

After examining "single" primes, we may now ask how many many twin primes there are less than a given number. This number is usually denoted by \\(\pi_2(n)\\). What we are interested in for this article is the question: _What is the probability that \\(X+2\\) is prime if we already know that \\(X\\) is prime?_ Mathematically speaking, we want to calculate (or at least estimate) the conditional probability \\(P(X+2\in\mathbb{P}|X\in\mathbb{P})\\).

Two events \\(A\\) and \\(B\\) are said to be (stochastically) independent if \\(P(A|B)=P(A)\\), or in other words, if knowledge about event \\(B\\) yields no further information about event \\(A\\).[^independence]

Now, by just applying the definition of how to calculate a conditional probability above, we obtain

\\[ P(X+2\in\mathbb{P}|X\in\mathbb{P})=\frac{P(X,X+2\in\mathbb{P})}{P(X\in\mathbb{P})}. \\]

But the numerator is just the probability that we found a twin prime pair, and the denominator we already examined. This yields

\\[ P(X+2\in\mathbb{P}|X\in\mathbb{P})=\frac{\pi_2(n)/n}{\pi(n)/n}=\frac{\pi_2(n)}{\pi(n)}. \\]

We could affirm the above question about independence if \\(P(X+2\in\mathbb{P}|X\in\mathbb{P})\\) would equal \\(P(X+2\in\mathbb{P})\\), or behave as \\(1/\log n\\) as well. Given our last equation, this would be the case if could approximate \\(\pi_2(n)\\) by \\(n/(\log n)^2\\). Indeed, Hardy and Littlewood conjectured for the distribution of twin primes

\\[ \pi_2(n)\sim C\frac{n}{(\log n)^2}. \\]

This is well supported by calculations, but still far from being proved. But let's assume for a minute that this is accurate, then it yields the approximation

\\[ P(X+2\in\mathbb{P}|X\in\mathbb{P})\sim\frac{Cn/(\log n)^2}{n/\log n}=\frac{C}{\log n}. \\]

So the primes would indeed be independent if the constant \\(C\\) would have value \\(1\\). When I first research this, I got quite excited, as most often the value for \\(C\\) would be given as \\(1.32032\ldots\\). This would mean that the two events would not be independent, but indeed it would be _more_ likely to find a prime two spots after another one than at a random spot! In other words, primes would have a strong tendency to cluster together.

But alas, I misread the data. I have been sloppy in defining \\(\pi_2(n)\\) above, and so are most sources. What's usually counted is the total number of primes of the form \\(n\\) and \\(n+2\\), but we are only interested in the number of _pairs_. So indeed we need to cut the constant in half. More concretely, the conjectured constant is the _twin prime constant_

\\[ C=\prod_{p\ge 3}\frac{p(p-2)}{(p-1)^2}\approx0.66016 18158 46869 57392 78121 10014\dots \\]

This means the answer is _no_, primes are not independent. The probability of finding a prime two spots after another one is (conjectured to be)

\\[ P(X+2\in\mathbb{P}|X\in\mathbb{P})\sim0.66016P(X\in\mathbb{P}). \\]

Well, would have been too good to be true...

[^independence]: This is not quite the accurate definition, but it's the intuition behind it. Correctly, \\(A\\) and \\(B\\) are independent iff \\(P(A~\mathrm{and}~B) = P(A) \cdot P(B)\\).
