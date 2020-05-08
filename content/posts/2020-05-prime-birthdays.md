---
title: Prime Birthdays
draft: true
author: Markus Shepherd
type: post
date: 2020-05-02T08:44:25+03:00
url: /2020/05/prime-birthdays/
categories:
  - Primes
  - Probability
tags:
  - Python
---

Last year, our first epsilon[^erdos] arrived. In between all the excitement about the new life, the mathematician in me couldn't help but be proud of her date of birth: *a prime* – in the right format…

## Overview

* Format: `%d%m` (Euler's birthday: 1504 👎) \
  14.8% of dates are primes in this format! (21600 out of 146097)
* Format: `%m%d` (Euler's birthday: 0415 👎) \
  15.9% of dates are primes in this format! (23297 out of 146097)
* Format: `%d%m%y` (Euler's birthday: 150407 👍) \
  8.5% of dates are primes in this format! (12444 out of 146097)
* Format: `%m%d%y` (Euler's birthday: 041507 👍) \
  9.3% of dates are primes in this format! (13516 out of 146097)
* Format: `%d%m%Y` (Euler's birthday: 15041707 👎) \
  6.1% of dates are primes in this format! (8953 out of 146097)
* Format: `%m%d%Y` (Euler's birthday: 04151707 👎) \
  6.4% of dates are primes in this format! (9337 out of 146097)
* Format: `%y%m%d` (Euler's birthday: 070415 👎) \
  8.1% of dates are primes in this format! (11857 out of 146097)
* Format: `%Y%m%d` (Euler's birthday: 17070415 👎) \
  6.0% of dates are primes in this format! (8816 out of 146097)

## Notes

* Graph probilities per year / month
* Is there a date that is prime in all formats?

## Further tasks

Make online tool for users to examine their birthday! Primality tests:

* https://github.com/henrikfredriksson/prime-q
* https://github.com/indutny/primal
* https://github.com/indutny/miller-rabin
* https://primes.utm.edu/curios/includes/primetest.php
* https://www.mathsisfun.com/prime_numbers.html

[^erdos]: The Hungarian mathematician Paul Erdős, famous for his nomadic lifestyle, myriad of conjectures, and very own expressions, used to refer to babies as [epsilons](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s#Personality), a play on the Greek letter mathematicians often use to denote a very small (but positive) number.
