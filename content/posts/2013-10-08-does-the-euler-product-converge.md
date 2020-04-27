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

It's a well known fact that the harmonic series (which we shortly touched in the [previous post][1]) <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_729287cedef2d45a59d98c6934e858ab.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> diverges. I think the best (though not easiest) proof of this to compare it with the corresponding integral:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_288c955e6c5fccc0dc8567792ee762c2.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

(Let's pause for a moment to celebrate the first of the numerous appearances of our good friend the logarithm.)<!--more--> Though this does require some basic calculus, it's nice because 

_a)_ it not only tells us that the harmonic series grows to infinity, but also _how fast_ it does so (incredibly slowly, for the record), and _b)_ the same argument works to prove that the series _converges_ if you sum over <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f26afdb571649553d71185cafe316f89.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6efd7056b68be5fc93ced37d8ae5a2db.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> instead. In other words, the harmonic series is _just about_ divergent (explaining the slow rate of divergence).

So we have the series <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_19a97ba2e107df01d3324f0e09e8860f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which we know to be convergent for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6efd7056b68be5fc93ced37d8ae5a2db.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and thus call <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as a function. The exact same argument works for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aac7aa6fd4216f20d11bec700bdf5749.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> since for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_88cfb14eeb197012acc2ae01c147377d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> we have

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_45867a9b95cfa3f129b116b5aef224c9.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Don't worry if you didn't get that, it's just an aside. We've already seen two arguments why the series defining <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> would equal the Euler product. Since the series is known to be convergent, the product better be convergent as well, right? Well, to be perfectly honestly, I would have had to establish my equalities first for some finite case, and then take limits, prove convergence, and so on. I don't care much about technicalities, but let's still convince ourselves that the Euler product does converge.

So, how do you prove the convergence of a product? The best strategy in mathematics is always to reduce the problem in front of you to a different problem that you already understand well. In this case, the well-understood problem is the convergence of series. Now a tool that can turn a product into a sum would be incredibly helpful. This tool is, of course, the logarithm. Let's say we want to know if a certain product <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_01aafb8fe74953e6c61ecdaab2b029df.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> converges. This means the expression evaluates to a finite number, in which case we can take logarithms, and -- behold! -- we have a series:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e7cf8995bb12df8003ccd86abe8a6837.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Note also, much like series <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f0afac1c323085173c097617d4f9056a.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can only converge if <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> tends to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cfcd208495d565ef66e7dff9f98764da.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, products <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_01aafb8fe74953e6c61ecdaab2b029df.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> can only converge if <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> tends to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. This is why we usually express a product as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_697f6c666f3a3c2a64a65a3332860a52.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

Knowing this, in order to prove that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_97000f7ee0408847984e6a295388897d.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> converges, we need to prove that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3d8ff78455c9fd3b751b751654fa1634.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> converges. I tried to spell this out myself, but failed miserably as I worked my way through the technicalities. Instead, we just notice that if <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_717e3e03da1eb11d9e7797c2c3bddc07.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> converges, so does <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e51fbe84ac8fa0d0f7d40230634fc690.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, and hence by the above remark <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4aa249da7baa084e328b459891d86a1b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. In our case, we need to examine <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_24390fbf199069df8da5cfc6c0c84159.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> (where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6cbb60d59d04d1d7c9e64fd2a001c8c6.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is a common notation for the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>-th prime).

Piece of cake after all that we know. We just note that the series that runs over all natural numbers instead of just the primes certainly is larger than the original sum, and hence

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5d5f1a598ee71ca5bdcc59dd9de542dc.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which is just the harmonic series again that we know to be convergent for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aac7aa6fd4216f20d11bec700bdf5749.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Wasn't so bad, huh?

For those that are still with me, let's take a look at the assertion that we just brushed over above. We want to prove that the convergence of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_717e3e03da1eb11d9e7797c2c3bddc07.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> implies the convergence of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e51fbe84ac8fa0d0f7d40230634fc690.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. For this, we need the incredibly useful expansion

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_60526d1800b743c371276f7325ae1348.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which is valid for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_708f34bef2a294f42baad1b211de17a3.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Taking the modulus yields

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_716badf88e38ddfa36db0564b30c390e.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where the geometric series made another guest appearance. Now, for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5ea67645aca777496b7051ac995c1b93.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> this yields

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3ba754227ddf8d893d041745ed590785.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

We assumed that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_717e3e03da1eb11d9e7797c2c3bddc07.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> converges, hence <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c68908becce230637b52e22ca92cbb36.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> certainly satisfies <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0c218b0658b31bad44bd80990efd02c6.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> for sufficiently large <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, and thus

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_78584255464f3d5ba1587c7d9fac543b.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

So the convergence of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_717e3e03da1eb11d9e7797c2c3bddc07.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> immediately implies the (absolute) convergence of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e51fbe84ac8fa0d0f7d40230634fc690.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

OK, enough of the technicalities, I promise we won't bother too much with these convergence examinations in the future.

 [1]: http://www.riemannhypothesis.info/2013/10/euler-product-revisited/ "Euler Product Revisited"