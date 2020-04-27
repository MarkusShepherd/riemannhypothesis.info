---
title: Applying the Explicit Formula
author: Markus Shepherd
type: post
date: 2014-11-23T10:47:17+00:00
url: /2014/11/applying-the-explicit-formula/
categories:
  - "Riemann's Paper"
tags:
  - Approximation
  - Prime counting function
  - Prime number theorem
  - Primes
  - Riemann
  - Zeros
  - Zeta function
  - Zeta zeros

---
It's quite some time since we [arrived][1] at Riemann's main result, the explicit formula

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9beae9ff028f160d1066428f8b643757.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is the prime power counting function introduced [even earlier][2]. It's high time we applied this!

First, let's take a look at <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> when calculating it exactly:

[<img class="aligncenter wp-image-655 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-1024x763.png" alt="J(x)" width="474" height="353" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-1024x763.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-768x572.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-1200x894.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][3]<!--more-->

You see how this jumps by one unit at prime values (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c81e728d9d4c2f636f067f89cc14862c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e4da3b7fbbce2345d7772b0674a318d5.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8f14e45fceea167a5a36dedd4bea2543.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6512bd43d9caa6e02c990b0a82652dca.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c51ce410c124a10e0db5e4b97fc2af39.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_70efdf2ec9b086079795c442636b55fb.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1f0e3dad99908345f7439f8ffabdffc4.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>), by half a unit at squares of primes (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a87ff679a2f3e71d9181a67b7542122c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_45c48cce2e2d7fbdea1afc51c7c6ad26.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>), by a third at cubes (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c9f0f895fb98ab9159f51fd0297e236d.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>), and by a quarter at fourth powers (<span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c74d97b01eae257e44aa9d5bade97baf.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>), but is constant otherwise.

Now, the point about Riemann's formula is that if you worked out diligently every single term on the right hand side exactly (and there's an infinity of smooth functions there) -- you'd end up with the same step function I just plotted!

This thought always makes my brain hurt a little, so let's take it step by step. Of course, it's impossible to work _every_ term since this would require to know the value of every single zeta zero. Instead, we will look at increasingly better approximations as we add more and more zeros into the equation. Let start from what it looks like when we only use the terms without the zeta zeros, i.e., <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8b418ad702ddb01df8c66e6c74032fe4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_32ed51537f2052f5bfd269d33071b496.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and the integral:

[<img class="aligncenter wp-image-657 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0-1024x763.png" alt="J(x) plus approximation" width="474" height="353" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0-1024x763.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0-768x572.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0-1200x894.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][4]

This already looks like a pretty good approximation, but we already do much better by just adding the first three<sup id="rf1-580"><a href="#fn1-580" title="In what follow I always refer to the zeros ordered in increasing height up the critical line plus their respective mirror images with negative imaginary part." rel="footnote">1</a></sup> zeros:

[<img class="aligncenter wp-image-659 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3-1024x763.png" alt="J(x) plus approximation with 3 zeros" width="474" height="353" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3-1024x763.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3-768x572.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3-1200x894.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][5]

Note how elegantly the previously monotonous function dances in waves around the prime steps. But this is only the start -- with ten zeros the waves are getting more dense:

[<img class="aligncenter wp-image-660 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10-1024x763.png" alt="J(x) plus approximation with 10 zeros" width="474" height="353" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10-1024x763.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10-768x572.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10-1200x894.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][6]

By the time we added one hundred zeros it's getting pretty hard to distinguish the two functions:

[<img class="aligncenter wp-image-661 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100-1024x763.png" alt="J(x) plus approximation with 100 zeros" width="474" height="353" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100-1024x763.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100-768x572.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100-1200x894.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][7]

I think you can't get much closer to seeing the music of the primes!

If you're worried that we just got lucky with the small values, here's a plot of the values up to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3644a684f98ea8fe223c713b77189a77.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> with twenty zeros used in the approximation:

[<img class="aligncenter wp-image-662 size-large" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20-1024x764.png" alt="J(x) plus approximation with 20 zeros" width="474" height="354" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20-1024x764.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20-300x224.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20-768x573.png 768w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20-1200x896.png 1200w" sizes="(max-width: 474px) 100vw, 474px" />][8]

Note what a close match the approximation is for small values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, but even further up the approximation will never let <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> go too far astray.

I could carry on with more plots with higher values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> or more zeros added, but this would only really look like two identical smooth lines, so the way this works is actually much clearer in smaller values.

I'll conclude with two thoughts: First, the equation and the pictures are in terms of this somewhat exotic <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, but we were really interested in <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, the number or primes less than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>. This is really not a big deal, since we can just apply Möbius inversion to the definition of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and get back the values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_237fd63d0c0557f24d3153c707ca816d.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Just plug in our approximations for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0e1bdd682c4fb6a43493d0eb21d9bf0d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and we will get out an approximation for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

Second, the approximations are smooth functions, but our actual objects of study are discrete step functions. In particular, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can only ever take on integer values, which actually helps a lot when doing computations. We don't need to add more and more zeros to get the precise value of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e5cb16c20d9f01bbbfe8f299e28d1f4b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Instead, as soon as our approximation is zooming in on an integer, this must be the correct value, and we can move on.

That said, calculating the approximation to any degree of accuracy for high values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> requires precise knowledge of a lot of zeta zeros and even more computing power. In the end, it is much faster just to tabulate the prime numbers and count them directly.

But of course, we are not doing this for a particular practical reason, but to understand prime numbers -- and Riemann's formula gave the researchers of his time finally the tools to prove the Prime Number Theorem.

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-580">
    <p>
      In what follow I always refer to the zeros ordered in increasing height up the critical line <em>plus</em> their respective mirror images with negative imaginary part.&nbsp;<a href="#rf1-580" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://www.riemannhypothesis.info/2014/04/integral-madness/ "Integral Madness"
 [2]: http://www.riemannhypothesis.info/2014/01/counting-primes-functionally/ "Counting Primes Functionally"
 [3]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20.png
 [4]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-0.png
 [5]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-3.png
 [6]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-10.png
 [7]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-20-100.png
 [8]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2014/11/pi2-200-20.png