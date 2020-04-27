---
title: Visualising the Riemann Hypothesis
author: Markus Shepherd
type: post
date: 2016-04-10T18:59:25+00:00
url: /2016/04/visualising-the-riemann-hypothesis/
categories:
  - Zeta Function
tags:
  - Complex numbers
  - Dimensions
  - Graph
  - Sage
  - SageMath
  - Video
  - Visualisation
  - Zeta function

---
One stubborn source of frustration when working with complex numbers is the fact that visualisation becomes tedious, if not impossible. Complex numbers have 2 "real" dimensions in themselves, which give rise to the complex plane. That's all good and fair. But if you talk about a function with complex domain and codomain, you already deal with a 4-dimensional graph. Unfortunately, my mind can only handle 3 dimensions (on a good day). One can resort to taking the absolute value of the function instead, or map real and imaginary part individually, resulting in a 3-dimensional graph, but all of these solutions fail to satisfy in one respect or another.

However, there _is_ one more dimension we can exploit: time! Used in the right way, this can produce wonderful videos like this one:

{{< youtube NAMuls4q2f4 >}}

<!--more-->

What are we looking at? These are the values of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_82a19a183ea387e48e91dbd98d8c989b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_03c7c0ace395d80182db07ae2c30f034.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> goes up the critical line <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b4e049f764eff644c0d7cf3c92f84be9.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. We start at<sup id="rf1-819"><a href="#fn1-819" title="As far as I know, it&#039;s total coincidence we conventionally use t for both the imaginary part of a complex argument and a time variable, but it makes talking about&nbsp;this animation surprisingly natural." rel="footnote">1</a></sup> <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3e8f7b0adf6d7024b951f29a18225e4a.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> at the beginning of the video and go all the way up to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_81ac6b73c66f1b2eacd6b431b1e71362.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1c98a128696fa8e00d62b97da8f877dc.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so this is where the values start. From there, we make an anti-clockwise semicircle until we hit the real axis again. After that, the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-function "turns right" and settles into a clockwise spiral with most of the action happing in the right half-plane. This goes on and on forever. Notably, after about four seconds, the graph passes the origin for the first time. This is the first of infinitely many <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3c22ba7aade15ea2b2852cd51bb4d6d4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>-zeros on the critical line, at about <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e6abe0490e055a7d3eb594c7a54c89b5.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. From now, it winds around in seemingly unpredictable circles, sometimes small and hasty, sometimes wide and elegant, but it never forgets to visit the origin every so often.

I produced this video with a <a href="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/04/plot_critical_line.txt" target="_blank" rel="">relatively simple SageMath script</a> quite some time ago, but I didn't write this post up until now since I would really like to turn this into an interactive sheet where you can play with the values for yourself, step away from the critical line, see how the spiral will miss the origin, and so on. But it's unlikely I will get around to doing that any time soon, and I've realised the video got quite some audience on YouTube, so I thought it's high time I shared it here as well!

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-819">
    <p>
      As far as I know, it's total coincidence we conventionally use t for both the imaginary part of a complex argument and a time variable, but it makes talking about this animation surprisingly natural.&nbsp;<a href="#rf1-819" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
</ol>