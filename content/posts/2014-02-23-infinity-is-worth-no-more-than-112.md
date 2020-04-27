---
title: Infinity Is Worth No More Than -1/12
author: Markus Shepherd
type: post
date: 2014-02-23T10:38:53+00:00
url: /2014/02/infinity-is-worth-no-more-than-112/
categories:
  - Feature
tags:
  - Infinity
  - Series

---
On 16 January 1913, a confused manuscript reached the famous mathematician G. H. Hardy in Cambridge. Other researchers have received similar letters before, and rejected it due to the seemingly incoherent formulae mixed with trivial mathematical results. Professional mathematicians are used to receiving manuscripts by amateurs who believe to have solved famous problems, but this particularly odd scribble caught the eye:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a0a0f2b9c3fce588e1c0145c8bff9c15.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Did this amateur mathematician really think that the sum of all natural numbers, a value that will exceed any given boundary at some point, will wind up being a negative fraction? M. J. M. Hill of the University College, London, simply responded that the author must have fallen victim to the pitfalls of divergent series and referred him to a standard textbook on the topic.

So, was this really just the work of a lunatic? Well, recently, the <a href="http://www.nytimes.com/2014/02/04/science/in-the-end-it-all-adds-up-to.html" target="_blank" rel="noopener noreferrer">New York Times</a> covered the topic, linking a <a href="http://www.numberphile.com/videos/analytical_continuation1.html" target="_blank" rel="noopener noreferrer">video</a> in which two physicists explain the importance of this result in modern string theory. While many physicists may not be too far from lunatics, these two make a pretty strong argument in this case:<!--more-->

We will start with a different sum <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9f15cdedd8d76e4abb50732f5727065b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which just adds ones and subtracts them again:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_77a9123ff4e158bc302582970d5bdf81.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

What's the value of this infinite sum? If you stop at an odd position, you will get <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, but if you move on to next even position, it will be back to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cfcd208495d565ef66e7dff9f98764da.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. This will continue for ever and ever, so the value of the sum will alternate between <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_cfcd208495d565ef66e7dff9f98764da.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. It seems like these two values fight to dominate the sum, but the answer is surprisingly Solomonian: <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_93b05c90d14a117ba52da1d743a43ab1.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Here's why: We subtract the sum from <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and see what happens:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3a5625cc7fb7000ed0a37e0283478e4c.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

But this is just the original sum again! Hence, we just found the simple relationship

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_37f0b6bc791254d8761e908ff56cef04.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which we can solve easily to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6c568c556a007612e6e8c867027ef1af.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.<sup id="rf1-200"><a href="#fn1-200" title="For the record, this sum is also know as Grandi&#039;s series." rel="footnote">1</a></sup> If you think this was weird, just wait for it.

Next, we'll look at a sum that also involves all natural numbers, but we use them alternating as in <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9f15cdedd8d76e4abb50732f5727065b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. This sum is

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e4d8361ade4593bb30eeab9a305f3ae8.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

What we will do now is add the sum to itself, obtaining <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_06f5a1b00879f30f5d4462f1987e8f21.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. But when we add the two, we will shift the second sum by one position. See what happens:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e37c9df98b22b073988782b128e82708.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

At this point you probably scream out: But that's just <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9f15cdedd8d76e4abb50732f5727065b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> again! Just like magic, we ended up with a value that we already know:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e028bb0765bd9ca1d5c5337bb59e2024.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

which directly yields <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6eeae67f08a3ea90bccaceb28fb6e6e9.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Cool! Now, we're only one step away from unraveling the mystery sum. What we do now is subtract our new friend <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a3de00c1597600a387128a7add5b354f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> from our original sum which we shall call for short <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b04273967bba467b66b3cb9741a67c6e.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_16537f79df9ce1b43a723468c9eccf0f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

So we end up with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_0495f86b6ec3e1850929611c7f794097.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> We notice that all summands are a multiple of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a87ff679a2f3e71d9181a67b7542122c.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, so we can take that out of the sum, and obtain:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_dc044e7767ba28ca49d9e450bd90f52e.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Another moment to exclaim: We got back to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5dbc98dcc983a70728bd082d1a47546e.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>! Also, remember that we know <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a3de00c1597600a387128a7add5b354f.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> to have the value <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_eca3bf81573307ec3002cf846390d363.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Putting all things together, this yields

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_30c54b6b82f3003b8ce1e5d202f74930.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Exercising our rusty algebra a little, we finally arrive at

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c94f511e46a3b4c86934d93337a35443.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

It may be madness, but there's a system behind it!

Now, the trained mathematicians or other sceptical minds may have impatiently waited to destroy my little show by pointing out the obvious mistake in this chain of arguments. Strictly, that is _analytically_, speaking, none of these sums converge, so me treating them as numbers and manipulating the equations as though they were numbers indeed is pretty much cheating. But rearranging (infinite) sums _formally_ and neglecting the question of convergence is a surprisingly powerful and useful tool. One particular master of this craft was Leonard Euler who by these means solved the famous [Basel problem][1]

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_34536b8da2925019b336fe160a9633c5.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This proves that sometimes the restraints of convergence are too tight and formal manipulations can lead to interesting and useful results. Indeed, Euler himself is credited<sup id="rf2-200"><a href="#fn2-200" title="This is somewhat controversial, but given his other work entirely possible." rel="footnote">2</a></sup> with finding the result that all natural numbers sum up to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c6a9c36e1c5111b8c5eefafed3201c59.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

This is all fair enough, but how is some formal manipulation relevant to the prime numbers and the rest of this blog? As always, it comes down to the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function. Remember the definition:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7072f09fba155eb4fb40d643f7770d9c.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This converges for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_aac7aa6fd4216f20d11bec700bdf5749.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and hence gives meaningful results only in this domain. But this is largely due to the singularity of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> at <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_73bbe012edfb61eca43444d61fefe937.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> where the defining series boils down to the harmonic series. Let's forget convergence for a second, and just plug <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c6cba76d96b32f5a93b9e97798357864.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> into the definition of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. What we get is

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b6c537cf60160e81316cd97a973e559.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I hope by now your excitement to rediscover our mystery sum has not eased up but intensified: <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4a4f73e802f63c114e7e9823ab252b04.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Euler couldn't get past the singularity in the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function as he only considered real values for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_03c7c0ace395d80182db07ae2c30f034.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, but Riemann could! Extending the domain to complex numbers, he was able to circumvent the singularity and attach a meaningful value to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5027096c94f3ac16da6a67c4e8a346cc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. So now, it's time to go back to the [functional equation][2]

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4f70a2965db95d12849cf5c9ee35d261.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Setting <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_23b583065f5b7336c728011ccd7375b2.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, we obtain our ominous <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_5027096c94f3ac16da6a67c4e8a346cc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> on the left hand side. What do we get on the right? Well, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6d868d3c1429fd0762cc1cd3f3d67c04.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> are just constants, <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c539112d12ff1accc18d41941b89ce70.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6bb61e3b7bce0931da574d19d1d82c88.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_870c56e8002d233c440e1e679cf02836.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_34c6116f6332110f0f2e845cd7d31290.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> or simply <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_c4ca4238a0b923820dcc509a6f75849b.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. We're left with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ba30ff66532ff5c093a06e1a5f7555b7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> which happens to be the series over the reciprocals of all square numbers. Wait, didn't we see this just now? Yes, that's the famous Basel problem! What Euler calculated was nothing but the value of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ba30ff66532ff5c093a06e1a5f7555b7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Combining all this, we arrive at

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7367cb19cbd3b7df867096dd576ea85f.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

I'll give you a moment to breathe in the full beauty of mathematics.

Done?

We started out with a seemingly non-sense question about the sum of all natural numbers, came up with a downright insane answer, and ended up combining various deep results to give a real meaning to all this madness. Mathematics at its best.

By the way, the "lunatic" who sent the letter to Hardy was no one less than Srinivasa Ramanujan who is now widely regarded as one of mathematics' greatest genii. Whoever remembers M. J. M. Hill?

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-200">
    <p>
      For the record, this sum is also know as <a href="http://en.wikipedia.org/wiki/Grandi%27s_series" target="_blank" rel="noopener noreferrer">Grandi's series</a>.&nbsp;<a href="#rf1-200" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn2-200">
    <p>
      This is somewhat <a href="http://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF#History" target="_blank" rel="noopener noreferrer">controversial</a>, but given his other work entirely possible.&nbsp;<a href="#rf2-200" class="backlink" title="Jump back to footnote 2 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://localhost:8885/riemannhypothesis.info/2017/05/the-prime-bet/
 [2]: http://www.riemannhypothesis.info/?p=93 "Perfect Symmetry"