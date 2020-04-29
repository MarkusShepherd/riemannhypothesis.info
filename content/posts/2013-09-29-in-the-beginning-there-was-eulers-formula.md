---
title: "In the Beginning, There Was... Euler's Formula!"
author: Markus Shepherd
type: post
date: 2013-09-29T17:39:48+00:00
url: /2013/09/in-the-beginning-there-was-eulers-formula/
categories:
  - Euler product
tags:
  - Euler
  - Primes
  - Product
  - Riemann
  - Series
---

I will start this blog the way Bernhard Riemann started his paper: with Euler's product formula that John Derbyshire called the *golden key*:

\\[ \zeta(s)=\sum_{n\ge1}n^{-s}=\prod_{p}(1-p^{-s})^{-1} \\]

This holds for any complex number \\(s\\) with \\(\\Re s > 1\\). If you look up a proof in any modern textbook, you will find a number technical rearrangements that end up in an examination of the absolute convergence on both sides. But actually, the formula is nothing but a fancy way of writing out the [Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Let's start by writing out the sum on the left hand side:

<!-- more -->

\\[ \zeta(s)=1^{-s}+2^{-s}+3^{-s}+4^{-s}+5^{-s}+6^{-s}+7^{-s}+8^{-s}+9^{-s}+10^{-s}+\ldots \\]

Now, let's sift out all even terms by multiplying the equation by \\(2^{-s}\\)

\\[ 2^{-s}\zeta(s)=2^{-s}+4^{-s}+6^{-s}+8^{-s}+10^{-s}+12^{-s}+14^{-s}+16^{-s}+18^{-s}+\ldots \\]

and subtracting the second from the first equation:

\\[ (1-2^{-s})\zeta(s)=1^{-s}+3^{-s}+5^{-s}+7^{-s}+9^{-s}+11^{-s}+13^{-s}+15^{-s}+\ldots \\]

OK, all even terms are gone, now let's eliminate all remaining multiples of \\(3\\). We multiply by \\(3^{-s}\\)

\\[ 3^{-s}(1-2^{-s})\zeta(s)=3^{-s}+9^{-s}+15^{-s}+21^{-s}+27^{-s}+33^{-s}+39^{-s}+45^{-s}+\ldots \\]

and subtract again:

\\[ (1-3^{-s})(1-2^{-s})\zeta(s)=1^{-s}+5^{-s}+7^{-s}+9^{-s}+11^{-s}+13^{-s}+\ldots \\]

I think by now the pattern is clear. We continue by multiplying all the primes \\(5^{-s}\\), \\(7^{-s}\\), \\(11^{-s}\\), ..., and continue subtracting from what we've got before, and arrive at

\\[ \cdots(1-17^{-s})(1-13^{-s})(1-11^{-s})(1-7^{-s})(1-5^{-s})(1-3^{-s})(1-2^{-s})\zeta(s)=1 \\]

Dividing by the factors on the left hand side, we arrive at our final result:

\\[ \zeta(s)=(1-2^{-s})^{-1}(1-3^{-s})^{-1}(1-5^{-s})^{-1}(1-7^{-s})^{-1}\cdots=\prod_{p}(1-p^{-s})^{-1} \\]

Magic!
