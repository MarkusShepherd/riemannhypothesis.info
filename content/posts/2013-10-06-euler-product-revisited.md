---
title: Euler Product Revisited
author: Markus Shepherd
type: post
date: 2013-10-06T22:24:34+00:00
url: /2013/10/euler-product-revisited/
categories:
  - Euler product
tags:
  - Euler
  - Product
  - Series

---
From the [previous][1] post we know that the harmless looking series <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_19a97ba2e107df01d3324f0e09e8860f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can be extended to the product <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_97000f7ee0408847984e6a295388897d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. At first sight, this does not seem terribly helpful, and it actually makes the rather easy series more complicated. So what's the big deal?

It's what has actually been suppressed in the above notation: The sequences we run through. The series runs over all natural numbers (or positive integers, if you prefer), the product runs through all prime numbers. Now, that's cool, isn't it? We found a series over the natural numbers that, as we will see later, defines a well-behaved function which is accessible to all the nice methods modern mathematics can offer, and related it to the prime numbers.

In other words: Riemann's <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function encodes the mysteries of the primes.<!--more-->

If you are still not convinced, just remember the following: Primes have been studied for two millennia<sup id="rf1-33"><a href="#fn1-33" title="citation needed" rel="footnote">1</a></sup> and rather little was (and still is) known. They are defined in the simplest terms, and the smartest minds have dealt with them, yet still they seemed to remain an invulnerable fortress. Now and again, one of these smart minds has got a glimpse through a window, but no more. It's presumptuous to claim that Riemann has conquered the fortress, but at least he has found a way how to assault it. Proving the Riemann Hypothesis would mean executing the final blow and taking residence in the prime fortress.

But back to the Euler product. The proof using the sieve of Eratosthenes dates back to Euler himself and couldn't be clearer and more insightful. Still, I'd like to take a look at a more technical proof, partly because it is a great practice in dealing with sums, partly because the Euler product is so immensely important that it's worth dwelling a little on it.

The careful reader will observe that plugging <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_73bbe012edfb61eca43444d61fefe937.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> into <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> yields <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fdc675cab14fa8d6fd72dd80a767475.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which is known as the <a href="http://en.wikipedia.org/wiki/Harmonic_series_(mathematics)" target="_blank">harmonic series</a>, one of the most fundamental series in mathematics, and usually the first example of a divergent series. The second proof makes use of the second of the three most important series in mathematics (the other one being the <a href="http://en.wikipedia.org/wiki/Exponential_function" target="_blank">exponential series</a>, with an honorary mention of the <a href="http://en.wikipedia.org/wiki/Dirichlet_series" target="_blank">Dirichlet series</a> as the Riemann <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function is a special case of it). So, we need to remember the formula for the <a href="http://en.wikipedia.org/wiki/Geometric_series" target="_blank">geometric series</a>:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ed771029ff906c3008f1d7ada240fbd4.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a1c2ce42ff27983965d1d690d742615a.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Now, as long as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aac7aa6fd4216f20d11bec700bdf5749.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, we have <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_21c1bdf46062167276721803f8e4de04.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> for any prime <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, so can expand the Euler product (yes, we kind of move backwards) to

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_52efe955d440e4a4a4eeba1fc06c99e4.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Again, instead of an infinite product, we now have an infinite product of infinite series --  doesn't look easier at all. But let's just write out a few of these terms:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_15108704cf04f0e690d30ace96d166bb.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Expanding the product just means picking one summand from each factor at a time, and then sum up all the possible combinations. If I always pick the first summand, I certainly get

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_29904ebc2f10b87529337984e3867bf8.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

OK, not too spectacular. Now, we pick the second summand of the first factor, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> everywhere else. This yields

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_995e3affd6bc5a92c411c00d2b9e41f9.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I think it is clear enough that I can obtain in similar ways a summand <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0a3016839173a5802586efe4e2dd3d25.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> for every prime <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_83878c91171338902e0fe0fb97a8c47a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> by picking the second summand of the respective factor, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> otherwise. What else would I get? Can I get, say, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_68f999cbea59b0bb3b01152928b4e50f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Sure I can! I just pick the third summand of the first factor and the second summand of the second factor, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> otherwise. We get

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4e49109e87d1794e859a9d23f741b96f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I hope by now it is clear that we will get this way a summand <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e129757d575b978841cace34bfd51503.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> for every natural number <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> when expending the product. On the other hand, the <a href="http://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic" target="_blank">fundamental theorem of arithmetic</a> asserts that each natural number has a unique factorisation into prime powers, which means in our case that we will have each summand <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e129757d575b978841cace34bfd51503.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> once _and once only_. Hence we can conclude

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_d4d884097ef1649bf62e2bc7de0c230b.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which we knew all along, but have now proved in a different way. Before, I claimed that the Euler product would encode the prime mystery, now I can claim that it encodes the fundamental theorem of arithmetic -- which is cool, since this theorem really is the reason why we got into primes in the first place.

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-33">
    <p>
      citation needed&nbsp;<a href="#rf1-33" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://www.riemannhypothesis.info/2013/09/in-the-beginning-there-was-eulers-formula/ "In the Beginning, There Was... Euler's Formula!"