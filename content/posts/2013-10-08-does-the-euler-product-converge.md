---
title: Does the Euler Product Converge?
author: Markus Shepherd
type: post
date: 2013-10-08T18:36:28+00:00
url: /2013/10/does-the-euler-product-converge/
categories:
  - Euler product
tags:
  - Euler
  - Product
  - Series
---

Usually, I don't care too much about convergence as a general overview of the argument is what I aim at here, and otherwise I'll just trust that things "behave well". But some words concerning convergence won't harm.

It's a well known fact that the harmonic series (which we shortly touched in the [previous post](http://www.riemannhypothesis.info/2013/10/euler-product-revisited/)) \\(\sum1/n\\) diverges. I think the best (though not easiest) proof of this to compare it with the corresponding integral:

\\[ \sum_{n=1}^x\frac{1}{n}>\int_1^x\frac{1}{t}\mathrm{d}t=\log x\longrightarrow\infty. \\]

(Let's pause for a moment to celebrate the first of the numerous appearances of our good friend the logarithm.)<!-- more --> Though this does require some basic calculus, it's nice because _a)_ it not only tells us that the harmonic series grows to infinity, but also _how fast_ it does so (incredibly slowly, for the record), and _b)_ the same argument works to prove that the series _converges_ if you sum over \\(1/n^s\\) with \\(s>1\\) instead. In other words, the harmonic series is _just about_ divergent (explaining the slow rate of divergence).

So we have the series \\(\sum n^{-s}\\) which we know to be convergent for \\(s>1\\), and thus call \\(\zeta(s)\\) as a function. The exact same argument works for \\(\Re s>1\\) since for \\(s=\sigma+it\\) we have

\\[ |n^{-s}|=|n^{-\sigma-it}|=|n^{-\sigma}|\cdot|n^{-it}|=|n^{-\sigma}|. \\]

Don't worry if you didn't get that, it's just an aside. We've already seen two arguments why the series defining \\(\zeta(s)\\) would equal the Euler product. Since the series is known to be convergent, the product better be convergent as well, right? Well, to be perfectly honestly, I would have had to establish my equalities first for some finite case, and then take limits, prove convergence, and so on. I don't care much about technicalities, but let's still convince ourselves that the Euler product does converge.

So, how do you prove the convergence of a product? The best strategy in mathematics is always to reduce the problem in front of you to a different problem that you already understand well. In this case, the well-understood problem is the convergence of series. Now a tool that can turn a product into a sum would be incredibly helpful. This tool is, of course, the logarithm. Let's say we want to know if a certain product \\(\prod a_n\\) converges. This means the expression evaluates to a finite number, in which case we can take logarithms, and -- behold! -- we have a series:

\\[ \log\prod a_n=\sum\log a_n. \\]

Note also, much like series \\(\sum a_n\\) can only converge if \\(a_n\\) tends to \\(0\\), products \\(\prod a_n\\) can only converge if \\(a_n\\) tends to \\(1\\). This is why we usually express a product as \\(\prod (1+a_n)\\).

Knowing this, in order to prove that \\(\prod (1-p^{-s})^{-1}\\) converges, we need to prove that \\(-\sum\log(1-p^{-s})\\) converges. I tried to spell this out myself, but failed miserably as I worked my way through the technicalities. Instead, we just notice that if \\(\sum|a_n|\\) converges, so does \\(\sum\log(1+a_n)\\), and hence by the above remark \\(\prod(1+a_n)\\). In our case, we need to examine \\(a_n=-p_n^{-s}\\) (where \\(p_n\\) is a common notation for the \\(n\\)-th prime).

Piece of cake after all that we know. We just note that the series that runs over all natural numbers instead of just the primes certainly is larger than the original sum, and hence

\\[ \sum_{n\ge1}|-p_n^{-s}|\le\sum_{n\ge1}\frac{1}{n^s} \\]

which is just the harmonic series again that we know to be convergent for \\(\Re s>1\\). Wasn't so bad, huh?

For those that are still with me, let's take a look at the assertion that we just brushed over above. We want to prove that the convergence of \\(\sum|a_n|\\) implies the convergence of \\(\sum\log(1+a_n)\\). For this, we need the incredibly useful expansion

\\[ \log(1+x)=\sum_{n\ge1}\frac{(-1)^{n+1}}{n}x^n \\]

which is valid for \\(|x|<1\\). Taking the modulus yields

\\[ |\log(1+x)|\le\sum_{n\ge1}\frac{|x|^n}{n}\le\sum_{n\ge1}|x|^n=\frac{|x|}{1-|x|} \\]

where the geometric series made another guest appearance. Now, for \\(|x|\le\frac{1}{2}\\) this yields

\\[ |\log(1+x)|\le\frac{|x|}{1-|x|}\le2|x|. \\]

We assumed that \\(\sum|a_n|\\) converges, hence \\(|a_n|\\) certainly satisfies \\(|a_n|\le\frac{1}{2}\\) for sufficiently large \\(n\\), and thus

\\[ \sum_{n\ge1}|\log(1+a_n)|\lt\sum_{n\ge1}|a_n|. \\]

So the convergence of \\(\sum|a_n|\\) immediately implies the (absolute) convergence of \\(\sum\log(1+a_n)\\).

OK, enough of the technicalities, I promise we won't bother too much with these convergence examinations in the future.
