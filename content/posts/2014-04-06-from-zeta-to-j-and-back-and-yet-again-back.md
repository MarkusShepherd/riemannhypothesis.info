---
title: From Zeta to J and Back (And Yet Again Back)
author: Markus Shepherd
type: post
date: 2014-04-06T14:13:42+00:00
url: /2014/04/from-zeta-to-j-and-back-and-yet-again-back/
categories:
  - Euler product
tags:
  - Euler
  - Functions
  - Fundamental Theorem
  - Golden Key
  - Logarithm
  - Newton

---
We know a lot about the [<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_195246810f9bfc228bca491859062b14.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-functions][1], we've learnt all about the different [prime counting functions][2], most notably <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so it's high time we found a connection between the two. Probably not too surprisingly, the crucial link is our good friend, the Euler product

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7fcf2e9062ba30e86b4a69675e878a31.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

What we want to develop now is a version of this product that will suit us to find a formula that magically can count primes. (Remember that the Euler product is an [analytical version of the fundamental theorem of arithmetic][3], so this is a natural starting point for our search.)<!--more-->

The only trouble is that we have a product, but analysis is all about _series_. Luckily, we have another good and reliable friend that can transform a product into a sum: the logarithm. So, by taking <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cb139ffd45872a9a5f17ece5cdb1d314.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> on both sides, we obtain something easier to handle:

<span style="line-height: 1.5;">

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1fb89d31a10b1bb4b6f0d9c245ab7b46.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p></span>

The cool bit is that there is a classical result that gives us a series expression for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e1cb2aabb062151486e430abfb0fa7d9.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. This dates back to Isaac Newton and goes as follows:

<span style="line-height: 1.5;">

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1669cb37e6a0dac1686c5abcaffb0b5f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p></span>

which immediately allows us to substitute the inner term:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4ff3470051c07c4629ecc71d7e8edcb7.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

With some technical acrobatics we can convince ourselves that the series are sufficiently well behaved, such that we can swap the order of summation and write instead

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_58aaf89adc36d2cea2b2050501869872.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

<span style="line-height: 1.5;">Granted, this doesn't look any easier or even friendly than our nice, familiar Euler product, but remember the slightly esoteric function we defined to count prime powers:</span>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f0242a45f83dae782e881889db4df48a.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

As you see, the only real differences are that the innermost sum is truncated at <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ce54e85c9f18c2de4a984e3e93874f00.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and the additional factor <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9742b47df817f00346e45486467ca4ca.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> in the sum. We will handle both issues by introducing analysis' killer feature: integrals. If you just exercise a little basic calculus, it's easy to see that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9742b47df817f00346e45486467ca4ca.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can be expressed as

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_fc4c336c7954df86c4f0258da8c0d57b.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

(Just notice that the antiderivative of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7ba92d89dcfa98376ab31c45fd9b8d26.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_073eb41278e8310fd27fd688a470b11e.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which is zero at infinity since we assume here <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aac7aa6fd4216f20d11bec700bdf5749.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.) Now, let's plug this into our expression above:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8991d9ad96f5946ea51eb65402b59972.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Yes, I know this looks even messier than before, but bare with me, it's worth it and will become clearer shortly. What we want to do next is drag the integral sign out of the sums. This is no problem in principal since integration is "transparent" under addition, but we have to keep two things in mind: First, since we talk about infinite sums, caution is in order to ensure convergence, and second, the range of integration depends on the variables we're summing over, so we need to think how this range may change. As usual, we don't pay too much attention to the question of convergence, but are just happy for others to take care of the technicalities. The second point, however, needs some thinking. The easiest way to find the right boundaries for integration and summation is to consider the different ranges and formulate common constraints. In this case we sum over all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_faf1b3a30453e631b14c4b627225001e.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> (this will remain unchanged), all primes <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, and integrate over all <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4d09a6acd4467ab31239df57c9aa8a6f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. So, if we want to take the integral out of the sums and make the range independent of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, we extend it to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3eb81ef9afcaa39a5b5025ea6632a83e.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, but need to add the restriction <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ce54e85c9f18c2de4a984e3e93874f00.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> then to the summation over the primes <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. That's it! We obtain:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_10508ffe9150f5e57b0d625d0da84a75.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I've already put the parentheses in the right place, so we only need to compare this to our definition above, and notice with a sign of relieve that things start to look prettier:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_227aee4d69ba5eb75c6a5570d8e37a43.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

John Derbyshire dubbed this formula the _Calculus Version of the Golden Key_, his nickname to the Euler product. He also gave a little more (graphical) intuition behind the deduction of the formula in chapter 19.V-VI of his book.

<span style="line-height: 1.5;"> You may still not be convinced that any of this is useful. After all, we didn't get anything other than an expression for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_69326d66e8d5968ec1c10653946b9ecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> that not only contains a formula we can hardly control, but on top of it all is even hidden away in an integral. But just as we recovered <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_dd212270229767191a8e42b95f2e9c33.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> from the definition of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> through a clever trick known as Möbius-inversion, we can now recover <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> from the formula we found through an even more powerful tool called Fourier-inversion. Again, this would not only deserve its own article, but rather its own blog. Instead, I will just present you the result that we obtain by applying a little Fourier-magic to the <em>Golden Key</em>:</span>

<span style="line-height: 1.5;"><span style="line-height: 1.5;">

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_84c8a374d5fa7ed873def5b515b6fd4f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p></span></span>

where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0cc175b9c0f1b6a831c399e269772661.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> is any real number with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e70b602f75e57a1f275932c9121ac225.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Now, recall that we can express <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as a product over its zeros (which means we have a series expression for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_69326d66e8d5968ec1c10653946b9ecc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>), and hence we will be able to express <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as a sum over the legendary <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-zeros. Further, we can calculate <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> from <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> (in fact, these behave the same asymptotically), and so we can exactly (mind, these are strict equalities, not only approximations) count the primes by virtue of calculating the zeros.

These stubborn, erratic creatures that we call primes are thereby completely determined by the zeros of Riemann's <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function. This is what makes the Riemann Hypothesis so powerful and surprising: Primes are volatile and unpredictable, but they obey the law of the zeros, and if Riemann was right, these zeros fall all on one single straight line, out of all possible places in the critical strip. Bernhard Riemann brought order to the chaos that governed the prime research for two millennia!

 [1]: http://www.riemannhypothesis.info/2013/12/more-symmetry-and-another-product/ "More symmetry and Another Product"
 [2]: http://www.riemannhypothesis.info/2014/01/counting-primes-functionally/ "Counting Primes Functionally"
 [3]: http://www.riemannhypothesis.info/2013/10/perfect-symmetry/ "Perfect Symmetry"