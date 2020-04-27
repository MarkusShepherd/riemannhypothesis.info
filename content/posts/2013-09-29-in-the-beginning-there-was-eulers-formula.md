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
I will start this blog the way Bernhard Riemann started his paper: with Euler's product formula that John Derbyshire called the _golden key_:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9defc5d4c411322ab10101d3f73a78b6.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This holds for any complex number <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_03c7c0ace395d80182db07ae2c30f034.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_2ce86d693ef1d4209b1cd04d4c07b3ad.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. If you look up a proof in any modern textbook, you will find a number technical rearrangements that end up in an examination of the absolute convergence on both sides. But actually, the formula is nothing but a fancy way of writing out the <a href="http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes" target="_blank">Sieve of Eratosthenes</a>. Let's start by writing out the sum on the left hand side:<!--more-->

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ffea9264b48cc3e44e2c5bd9551ca3df.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Now, let's sift out all even terms by multiplying the equation by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c78bc32635b8e432f9ffb296eeeb2873.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f875ce0f393632e94dc0a7900a43d51c.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

and subtracting the second from the first equation:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8842dd54a4fd0dbca1134fb73942e491.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

OK, all even terms are gone, now let's eliminate all remaining multiples of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eccbc87e4b5ce2fe28308fd9f2a7baf3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. We multiply by <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c77c803ee9ebf5af05c91381bb499ad0.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_247f409bac8d75e7cb4b369be71b0ea6.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

and subtract again:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5bd80a35bba5177a2723643251e203ef.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I think by now the pattern is clear. We continue by multiplying all the primes <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_96ebcd7de1bc79a7dd3876898ce1b808.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9e0a45f1fcdffa94fe515eaf3c05e722.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_fc13530a9afd3b82191e4462e8b53549.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, ..., and continue subtracting from what we've got before, and arrive at

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7143839e614f7c46b3bed17dc9843e26.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Dividing by the factors on the left hand side, we arrive at our final result:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cdb5e835783d56bf386458ee413edc31.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Magic!