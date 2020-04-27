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

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c0698c7e8fa6d277f992eb151de90d31.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

of the Euler product, and we know how to express <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f3a761cd56a9193ecefdec155ab9eecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as a product over its roots

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a0d6be66f24b5ce6a1534fbc2ac05f14.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e56bc4174ead7583a8bb4618380f26b8.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

High time we put everything together -- the reward will be the long expected _explicit formula_ for counting primes!<!--more-->

First, let's bring the two formulae for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f3a761cd56a9193ecefdec155ab9eecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> together and rearrange them such that we obtain a formula for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_07cdb66406fd774121c9a997d3f3e4fb.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Before we proceed, let's get rid of this unnecessarily complicated factor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f88822d7fa96cc9586aaeae14270e634.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Using the formula above, this is

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_74a96239c643055fea40971405a66e3d.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

The value of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c8861f030f7a00fffa91b74f5959003d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can be obtained in a similar fashion to [that of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5027096c94f3ac16da6a67c4e8a346cc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>][1] by interpreting it as the sum

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_97f66ffca73229019ba6e66b2a52880b.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which winds up to be, somewhat surprisingly, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b5a9867e53fa53c95c2bea1cdedc0a4e.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, giving us <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_d10b391cdbb6488bf9271f780e2ffccf.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

In our formula for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, we have <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_69326d66e8d5968ec1c10653946b9ecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so it appears wise to take logarithms of both sides. Remembering  that the logarithm translates products into sums we obtain

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ba8245d1476f4aa3faa85cf7cacbf8b2.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

If you're scared by this expression, remember that we need to plug it into our integral to get back to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Prime research is only for the valiant. But before we can do this, we first need to transform the integral slightly (through partial integration) to

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_462e8c0a35b17b06575164818126d9d3.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Now we can substitute the term <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_69326d66e8d5968ec1c10653946b9ecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> by the above sum. Luckily, both differentiation and integration are transparent to addition, hence we can handle five (slightly) less intimidating integrals instead of one monster integral.

The derivation of these terms fill the better part of the second half in Riemann's paper, so I'm not gonna give a full account of the intricate arguments required to arrive at the final terms, but will instead be satisfied with a few remarks on each of them.

Let's start with the easiest one as an appetiser. The term <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9ef854fc860d6c7346703e249bc9bebe.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> will simplify to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_fc63920c4dcc2d0d2ccd9d68187adea0.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> when divided by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_03c7c0ace395d80182db07ae2c30f034.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, and then vanish completely when differentiated with respect to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_03c7c0ace395d80182db07ae2c30f034.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>. Nice! Unfortunately, the other terms won't behave nearly half as nicely as this one.

Another one, however, is still reasonably well behaved. The term <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4e1765be017972a2fedaf62e8503b613.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> when plugged into the integral, gives us

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0c0188d6e550b04f0ed5df4e8a247174.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

If you follow all steps through, this all just boils down to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_32ed51537f2052f5bfd269d33071b496.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> -- not too bad either.

OK, now let's roll up our sleeves, and get on with the real troublemakers. The next term we consider is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3a59d85adbd091c16974200ef22665ff.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which yields the integral

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_691e2bbb937ff15fc722f2cda963a3cb.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This integral is by no means easily simplified, so I'll just present you with the final version which is<sup id="rf1-521"><a href="#fn1-521" title="You may -- rightfully -- remark that during integration, the integrand 1/log t is undefined for t = 1 since log 1 = 0, and we cannot divide by zero. But rest assured that this is just another technicality that&#039;s easily circumvented. In fact, it&#039;s never quite sure which version an author works with: the integral that starts at 0 or the one that starts at 2. However, these two just differ by an additive constant, which is completely negligible when it comes to the asymptotic behaviour." rel="footnote">1</a></sup>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a03aaad4f643b8cb3b94325bf9453e44.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

The function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8b418ad702ddb01df8c66e6c74032fe4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is also called the _logarithmic integral_, and will turn out to be the main term in our formula for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and a great approximation for the number of primes less than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> in general. I've [mentioned it before][2], and interpreted there <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_2da99e6fadc82988795086af351e7311.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as the density of the primes "near" <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e358efa489f58062f10dd7316b65649e.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. This means we need to sum, or rather integrate, along all values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e358efa489f58062f10dd7316b65649e.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> to obtain the total number of primes. Those working with (continuous) probabilities will be familiar with the concept.

All these words just to avoid admitting that I won't work out more details about the derivation of the main term at this point. Luckily, we still have more work to do anyway. Next, let's look at the sum over the roots <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a580e52c299e1520e712033d28b55829.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. The tricky bit here is that we would like to take the sum out of differentiation and integration, but this is not so straightforward since the sum only converges conditionally and hence care needs to be taken when interchanging limits. So, we are grateful to all the smart minds who did the hard work for us, and go on exchanging the order to obtain

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_68d5f05f08aaf84c1bfc0a8afb78a3dd.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I hope you see the resemblance to the expression above that led to the main term, so we will  expect a similar result. The main difference is that, as noted, the convergence of the sum is only conditional, and hence the order in which the zeros are summed does matter. So, which is the right order?

Remember that zeros come in "pairs of pairs" since <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f2414807eae258d1f7bb6050bffac7ea.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> has two symmetries. First, it is symmetrical along the real axis, that is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0b5fb58da66c61e3e9db00a228c4d0ac.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_df0b80064ee2a2bcba9c3a02e4686bfd.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is the complex conjugate which is nothing but the mirror image along the real axis. Since every single zeros that's been found is of the form <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_95c9703ced2e84b52e8ce4d951804e65.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e358efa489f58062f10dd7316b65649e.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> is a real number, this means that every zeros has a "twin" <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_39851e918e063d8e90062b42521fa7cb.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

But there is another symmetry, the symmetry along the critical line <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1a359f27d311b365c45208afb3ce154a.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. The function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f3a761cd56a9193ecefdec155ab9eecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> has been defined such that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_34828e6aa242d1dd30fb0c98a00badfb.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. This means that for every zero <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b61719e4483d24b6b51917d6c1d2bb14.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> we have another zero <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_bbb863913bec8046c7e4bd86225e8157.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. For a zero <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_95c9703ced2e84b52e8ce4d951804e65.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> on the critical line, this is actually the same "twin" <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_de497471d216df782b8bc3343279162f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, but if there's any zero off the magical line, this will yield a total of three distinct other zeros associated with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b61719e4483d24b6b51917d6c1d2bb14.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, which are <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3ccb1202af3f1867002e0b020a15c7da.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_bbb863913bec8046c7e4bd86225e8157.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f2e1c551a4e84dcf6355255ca87e5ac3.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

Back to our original topic, we wanted to find the right order of summation. When it comes to summing real values, usually the right thing to do is to sum in increasing order. Unfortunately, the zeros are complex and hence have no natural order. However, we know they are condensed to the critical strip, and we will just sum them up according to their imaginary part. But that's not enough -- we will also need to pair each zero <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b61719e4483d24b6b51917d6c1d2bb14.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> with one of it's "twins". It turns out the right one is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_bbb863913bec8046c7e4bd86225e8157.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, the mirror image with respect to the point <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_854941d6b39ed8b308d9ac6db0607b3d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

All this combined with some more careful analysis, we arrive at the penultimate term in our expression for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_978fcc8d1e41b035359709aa3046453f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This leaves the term <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c7f3bf01b9bb5b1a3c72c344d46a5a2.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and the corresponding integral

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e01ce0b7b8d37b23fc86a96c6eec2b3a.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

There's a series for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5f1d6a73ba9f495ec25bc5ca4f0d22e9.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> that translates this integral into a series of integrals, each one similar to the ones we have seen before. Summing these up again, we arrive at the final term

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e72d323f0e118fa373dcccf7f9a39785.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This may look scarier than it is, particularly since this integral grows small very quickly and will thus be asymptotically negligible.

It's high time we wrapped up things and take a look at the result of all this madness:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b8304d4aee66fa23c30f8e696a06bcca.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This is Riemann's main result, and here are two things (amongst others) that make it so remarkable (not counting the fact that Riemann didn't bother to rigorously prove half of the steps along the way).

First, the "main" term. I put _main_ in quotes, because just by looking at it, one couldn't tell which of these terms dominates. But remember that by the mid 19th century, the Prime Number Theorem has been unproved for half a century, and this was the first real justification (beyond empirical data, that is) in conjecturing that the density of the erratic primes would be given by a formula as simple as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_de2e64936a04ba95648e5ce0a950598c.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. You may point out that we didn't actually count primes with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, but indeed prime powers. However, we will take a closer look into this, and it will not be a big difference anyway. For the moment, just be reminded that we can recover <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> from <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> through Möbius inversion.

Second, the zeta zeros. When Gauss and Legendre conjectured their versions of the Prime Number Theorem, it was surprising to have any kind of simple _asymptotic_ for the number of primes. Riemann's result goes on step further. He did not approximate the number of primes, he computed them _exactly_. There's no uncertainty or error attached to this formula, if you diligently carry out every single calculation you will end up with the exact number of primes below <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, not just a rough guess. Now, what does it mean to carry out all calculations? The logarithmic integral <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8b418ad702ddb01df8c66e6c74032fe4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, though not quite elementary, is still quite easy to handle. The same goes for the integral and, well, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6444238b888ccc03ef250dd9feaf90c0.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is just a constant. All these terms can be evaluated to any desired precision by any modern computer. The series over the zeros however is a little different. We know that there's an infinite number of zeta zeros, which means that no machine can ever find the exact value of this term, no matter how much time (or money) you spend on it. Still, a truncated series can still be used to approximate the final value, and in this respect every zero that we add to the calculation makes Riemann's formula more accurate. Note how every single zero carries its individual secret about the primes in it, and they all come together to unravel the prime mystery, like notes in a beautiful symphony that form the music together.

I hope this glimpse of beauty makes up for all the toiling and sweating with the nasty integrals...

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-521">
    <p>
      You may -- rightfully -- remark that during integration, the integrand 1/log t is undefined for t = 1 since log 1 = 0, and we cannot divide by zero. But rest assured that this is just another technicality that's easily circumvented. In fact, it's never quite sure which version an author works with: the integral that starts at 0 or the one that starts at 2. However, these two just differ by an additive constant, which is completely negligible when it comes to the asymptotic behaviour.&nbsp;<a href="#rf1-521" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://www.riemannhypothesis.info/2014/02/infinity-is-worth-no-more-than-112/ "Infinity Is Worth No More Than -1/12"
 [2]: http://localhost:8885/riemannhypothesis.info/2013/11/are-primes-independent/ "Are Primes Independent?"