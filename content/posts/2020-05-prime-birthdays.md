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

https://gitlab.com/snippets/1949899

Paul Erdős -- [our epsilon arrived](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s#Personality)

Possible example dates:

* Riemann's birthday (17 September 1826)
* Day of Riemann's death (20 July 1866)
* Publication date Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse (???)
* Euler's birthday (15 April 1707)
* Day of Euler's death (18 September 1783)[^os]

Formats to be examined:

* DDMM (2007)
* MMDD (0720)
* DDMMYY (200766)
* MMDDYY (072066)

Make online tool for users to examine their birthday! Primality tests:

* https://github.com/henrikfredriksson/prime-q
* https://github.com/indutny/primal
* https://github.com/indutny/miller-rabin
* https://primes.utm.edu/curios/includes/primetest.php
* https://www.mathsisfun.com/prime_numbers.html

[^os]: Died in Russia 7 September 1783 Old Style
