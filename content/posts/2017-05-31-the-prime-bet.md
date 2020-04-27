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

> We'll choose two positive integers at random. If they have any divisor in common (other than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>) I'll pay you a dollar, else you'll pay me a dollar. Are you in?

Apart from the question what kind of establishments you frequent, you should be wondering: is this a good bet for you?

When two integers have no divisors in common except the trivial divisor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> we say they are _coprime_ or _relatively prime_. <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1679091c5a880faf6fb5e6087eb1b2dc.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_45c48cce2e2d7fbdea1afc51c7c6ad26.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> have the common divisor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, so they are _not_ coprime, whilst <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c9f0f895fb98ab9159f51fd0297e236d.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_45c48cce2e2d7fbdea1afc51c7c6ad26.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> only have the trivial common divisor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, so they are coprime.

This makes you start thinking: "As numbers grow bigger, aren't there a lot of divisors out there? After all, half the numbers are even, so if we hit two even numbers, they'll have the factor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c81e728d9d4c2f636f067f89cc14862c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> in common and I'll win. And then there's <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e4da3b7fbbce2345d7772b0674a318d5.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8f14e45fceea167a5a36dedd4bea2543.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, ... Seems like a good deal!"<!--more-->

Is it, though? Let's do some experiments! This simply Python script should give a decent approximation:

<pre>from math import gcd
from random import randint
from sys import maxsize

repetitions = 10**8
count = sum(1 if gcd(randint(1, maxsize),
                     randint(1, maxsize)) == 1
            else 0
            for _ in range(repetitions))

print('{count:d} out of {repetitions:d} pairs were coprime ({pct:.3f}%)'
      .format(count=count,
              repetitions=repetitions,
              pct=100 * count / repetitions))</pre>

This will pick two (largish) integers at random<sup id="rf1-919"><a href="#fn1-919" title="I was (deliberately) vague when saying choose two random numbers. There is no way of choosing two arbitrarily large integers uniformly at random, so what you need to do is pick an upper bound N&nbsp;and choose numbers below N uniformly at random. In the calculations of the probabilities you&#039;d take the limit N &rarr;&nbsp;&infin;. But we&#039;ll be hand-waving to begin with, so no reason to be exact here." rel="footnote">1</a></sup>, check if they are coprime – which is the same as saying that they're greatest common divisor (_gcd_) is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> – and repeat the procedure 100 million times. At the end, it will print something like this:

<pre>60797595 out of 100000000 pairs were coprime (60.798%)</pre>

If you run this, the exact numbers will obviously be different, but the bottom line is that in over 60% of the cases you'll end up with two coprime numbers. Don't take the bet! (This is generally a good rule of thumb when a stranger makes you any kind of offer.)

So, where does that number – <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a4f0522bbd6f051747034d5ae90d9c42.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>ish – come from? There is a nice and easy representation of the exact number, and if you've never heard of this problem, you might be surprised that the answer involves <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4f08e3dba63dc6d40b22952c7a9dac6d.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> – the ubiquitous constant of circle fame. What's it got to do in number theory? Quite frankly, I'm not sure, but we can prove it, so bear with me.

First, let's look at the above probability more closely. For two numbers to have a non-trivial common divisor means in particular that there is a prime that divides both of these numbers. If they are coprime, then there's no prime dividing both of them. What are the odds of that? Well, half the numbers will be divisible by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c81e728d9d4c2f636f067f89cc14862c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> – the even numbers. The probability that both numbers are even is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cac0355c41b2f5f4ee480bb12a5b7040.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so the probability that they are not divisible by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c81e728d9d4c2f636f067f89cc14862c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> is the complement <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a6aa3e224a9bb6e6764cb19581d00b50.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Likewise, a third of all numbers are divisible by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, so the probability of having <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> as a common factor is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e021c106d0b6468b927391a8c37bc696.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, with a complement of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4377ea1c62a46686871789ae3779a6b2.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

We can consider the probabilities of being divisible by any two given prime numbers as independent, so we can just multiply all these terms together for the probability <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_44c29edb103a2872f519ad0c9a0fdaaa.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> that two integers are coprime:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a16985cb3db5e5a49848c3a9a2b9f55f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where the product runs over all primes <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. This should look awfully familiar to you. If it's been to long and I need to jog your brain, remember the Euler product that is at the very core of our investigations:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9aeaefc866851b1c0b495901082e9b97.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

In other words, our probability is nothing but

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_fef003ce85c7117beb4a06ee323fe171.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

The value of this particular sum <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7a72196029f7dfbca19c375be7dda32e.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> became rather famous in its own right as the **Basel problem**, first posed in 1644 and finally solved in 1734 by none less than the great Leonhard Euler. By now, dozens of proofs have been published, most of which calculate some form of integral, but none is clearer and more beautiful than the master's original one, so let's dive into that.

We'll obtain two series representations of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cdba58911c590ced3e2435dfa39f6873.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and compare them with one another. First, let's take a look at the **Taylor series** of the sine function. In general, this series is defined for a smooth (read: well-behaved) function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_50bbd36e1fd2333108437a2ca378be62.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_bfe402f37d36554eb9c60ee689008a77.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e78dd0c70c48a61ca7caed1a92e4f92.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is the factorial function and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c9b34b7a649b447750927c19ff1e336b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>-th derivative of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> evaluated at <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e11729b0b65ecade3fc272548a3883fc.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. The derivates of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6eb3daa863c21e84e72a568c40963922.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> are about as easy as they get:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7228d202559622c813103b9f09e00ce0.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

from where it all begins over and over in a neat <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a87ff679a2f3e71d9181a67b7542122c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>-cycle. In particular we have <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6243891d228d359288906bea34685ec2.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3f10f229b72d5bb7c65946584e9f5032.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5d621a4043161e09ae4a4ccbfe74d114.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, which yields the following classic series representation for the sine-function:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_62621851c608c1c76701a725fc5d6948.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

We'll take one <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> out of the sum and use the slightly different form

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b19ed15af7ccabe34d6001c977c2799e.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Half way there. Now we'll develop a product representation for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cdba58911c590ced3e2435dfa39f6873.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, more precisely an expression over its zeros. We used a very similar expression when we developed the [product representation for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f3a761cd56a9193ecefdec155ab9eecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>][1]. The general form is

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9d433b07a7cfb7c0c47c244a31d4ffef.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where the product runs over all the zeros <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b61719e4483d24b6b51917d6c1d2bb14.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Euler was very much ahead of his time in using such a product and just manipulated formal expressions, much like in the [famous sum <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_739e8ea2041bf5ccc200f3f6f9e4f523.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>][2]. It wasn't until the late 19th century, when Karl Weierstraß formally proved products like this in an attempt to verify some of the claims in Riemann's famous paper.

Now, remembering that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cdba58911c590ced3e2435dfa39f6873.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> has zeros for all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9d7cc79577d0cbeaa96d7c2ea30d87a4.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6686e0d0fda5627c015ebc472384baed.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e566b7260b89903011d84ab68fa998d5.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3960e95b44eb268b76deab0320901745.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, we can write

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aadd1456365a4b42166bcf9e9112d12d.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This is a product of sums in <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, so if we manage to multiply out everything we'll have another series representation of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9b886211f606e2ff14be4c879c616336.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. In general, multiplying out such an expression means for every <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> choosing either the left (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>) or the right (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_887e6484ca197c62f4bcb326167fa3d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>) summand and then summing everything up over all possible combinations (like _left, left, left, ..._ or _left, right, left, ..._). This is actually much easier than it sounds since we don't need to deal with all the infinite coefficients which in turn will be infinite sums. Instead, all we care about are the terms that contain <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_32f5240d0dbf2ccbe75ef7f8ef2015e0.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. Because all factors of the product above are of the form <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_dc6f3bb91a1f12029575f4d89cb4c510.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> this means we choose for one <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> the right summand and the left ones (which are all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>) for everything else. Hence the above product will expand into a series like so:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_15abc260223f8c3ba2e890d3fe4c2c95.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

The rest will be higher order terms of degree <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a87ff679a2f3e71d9181a67b7542122c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> or more which we don't care about. What we've obtained are two series representations for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9b886211f606e2ff14be4c879c616336.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, both of the form <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_102344bf822b468365084013c336178b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. It's pretty easy to show that if you have two such series for the same function, all of their coefficients must be identical. This means in particular that the coefficients in front of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_32f5240d0dbf2ccbe75ef7f8ef2015e0.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> must match. From the Taylor series we got <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ff1ed889ed5a31470d82bd9610067c1c.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, while the product yielded <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_84ccb79138d357f8af01f1ffdaaa97fb.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so we just obtained the equality

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_52203e09ef484181914eba03a0266fc9.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

We can take the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4f08e3dba63dc6d40b22952c7a9dac6d.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>s out of the series since they don't depend on <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and rearrange a little to finally arrive at Euler's solution to the Basel problem:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ac1c74737db09bdef5c13cb7914b592b.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Using this in our calculations above we obtain the exact result for the probability <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_44c29edb103a2872f519ad0c9a0fdaaa.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> that two randomly chosen positive integers are coprime:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_642df54e961449b2268d513d3cba7fa8.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

As I said before, I'm still puzzled every time I work on this how the trigonometric constant <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4f08e3dba63dc6d40b22952c7a9dac6d.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> manages to creep up all over maths in seemingly unrelated fields.

Euler's solution I presented here lacks some form of rigour since he couldn't prove that the product representation actually converges, but his manipulations as formal identities not only solved the famous Basel problem correctly, it can actually do lot more. When multiplying out the product above I ignored any terms higher than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_32f5240d0dbf2ccbe75ef7f8ef2015e0.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. However, if you do carry out these calculations you'll get expressions in <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_2ad2bf15772d125e9b6943ff49ee6bc5.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so you'll obtain similar results for all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6e6aa62f802383a57bf3ef0759a3fd50.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. The exact calculations are well beyond our scope here, but it's worth noticing that Euler solved the values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6e6aa62f802383a57bf3ef0759a3fd50.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> for all even integers, and in particular we know therefore that all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6e6aa62f802383a57bf3ef0759a3fd50.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> are irrational and even transcendental numbers since they are expressions in <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8d8d532ed0bfbb379874e1f22041b6ae.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. You might ask: what about odd arguments <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aa2bd0ee2c98e5792861c22545a8db0b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>?

Somewhat surprisingly the answer is: very little. It wasn't until 1978 that Roger Apéry proved that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_86d9b72b6d4d9748733612814fb72868.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, a number that's now referred to as _Apéry's constant_, is irrational. No other value of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aa2bd0ee2c98e5792861c22545a8db0b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is known to be irrational<sup id="rf2-919"><a href="#fn2-919" title="Some progress has been made, but no single value has been cracked so far." rel="footnote">2</a></sup> (or rational for that matter), let alone any nice closed form like we had with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_2a4790de836da858b34777c7d4198ec6.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

I'll leave you with the somewhat comforting note that Apéry was of the almost biblical age (for a mathematician) of over 60 years when he made his breakthrough. Mathematics is often called "a young men's discipline" – you either make a significant contribution before you reach tenure or you never will. Roger Apéry is one counter-example, Andrew Wiles and Yitang Zhang are others. It's never too late to start working on that one big theorem!

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-919">
    <p>
      I was (deliberately) vague when saying <em>choose two random numbers</em>. There is no way of choosing two <em>arbitrarily large</em> integers uniformly at random, so what you need to do is pick an upper bound <em>N</em> and choose numbers below <em>N</em> uniformly at random. In the calculations of the probabilities you'd take the limit <em>N</em> → ∞. But we'll be hand-waving to begin with, so no reason to be exact here.&nbsp;<a href="#rf1-919" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn2-919">
    <p>
      Some progress has been made, but no single value has been cracked so far.&nbsp;<a href="#rf2-919" class="backlink" title="Jump back to footnote 2 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://localhost:8885/riemannhypothesis.info/2013/12/more-symmetry-and-another-product/
 [2]: http://localhost:8885/riemannhypothesis.info/2014/02/infinity-is-worth-no-more-than-112/