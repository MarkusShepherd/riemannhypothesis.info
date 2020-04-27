---
title: If One at a Time is too Difficult, Try All at Once!
author: Markus Shepherd
type: post
date: 2014-12-27T12:00:16+00:00
url: /2014/12/if-one-at-a-time-is-too-difficult-try-all-at-once/
categories:
  - Feature
tags:
  - Analysis
  - Asymptotics
  - Combinatorics
  - Coursera
  - Derbyshire
  - Dirichlet
  - du Sautoy
  - Number theory
  - Riemann

---
In the past months, I spent as much time as I had on taking online courses at <a title="Coursera" href="https://www.coursera.org/" target="_blank">Coursera</a>. One particularly interesting course, both from a mathematical and computational point of view, is <a title="Analytic Combinatorics course" href="https://www.coursera.org/course/ac" target="_blank">Analytic Combinatorics</a> which applies combinatorics (i.e., the art of counting) to the analysis of algorithms by finding formulae, exact or asymptotic, for their running time.

It is notoriously difficult to find exact formulae for general combinatorial constructs. Typically, we want to know how many objects, e.g., trees, permutations, sequences, with certain properties there are of a given size. Famously, the number of binary trees (and about a million other constructions) is governed by the <a title="Catalan numbers" href="http://en.wikipedia.org/wiki/Catalan_number" target="_blank">Catalan numbers</a>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_ea9adc7859337ac76d2053e44eb85d79.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

<!--more-->

How do we get to this result?<sup id="rf1-673"><a href="#fn1-673" title=" The exact result depends on what exactly the question is, e.g., if you count internal nodes, external nodes, only full trees, etc. Either way, the Catalan numbers are a recurring theme. Here, we don&#039;t care about the details, but just the general idea. " rel="footnote">1</a></sup> We could start to construct small examples. How many trees are there of size 1? How many of size 2? 3, 4, 5? This will get tedious very soon, may not help you with finding a formula if the behaviour does not match any of the known sequences, or may even mislead if the beginning of the sequence is very different from the asymptotic behaviour.

You may be tempted to think of constructing a general formula like this: here we have <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> nodes, how many trees can I build from these? In some cases, this approach actually works, e.g., for permutations, but it soon reaches its limits. Working example by example, number by number, won't get us very far. But working on all examples _simultaneously_ will!

What I mean by this is that we find a general recipe to construct our object of interest, usually from smaller parts we already understand, i.e., atoms and smaller sub-structures. This is particularly natural for recursively defined structures like trees. Now, you have _all_ the objects at your disposal. The trick is to encode them all together in one function -- the _generating_ function.

In the case of combinatorial objects, we define a polynomial series of the form

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7387d396dae6861e2336a1c5bed16299.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> are the quantities we're interested in, i.e., <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> is the number of object of size <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7b8b965ad4bca0e41ab51de7b31363a1.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>. Once we understand the resulting function<sup id="rf2-673"><a href="#fn2-673" title="Of course, if we want to apply analytical tools, we need this series to converge, which isn&#039;t guaranteed at all. If it doesn&#039;t, we can usually make it converge by applying weights, e.g., inverses of factorials like in the definition of the exponential function." rel="footnote">2</a></sup> <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7852db5d43d5ab2b22775d9f2131b869.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, we can simply extract the coefficient of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_b41952e9dfed8e1ed562fddafeca7c70.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> to recover <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span>. This may sound pretty circular since we need the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_825b3fd5bafbc46b9a560ea9f16b21dd.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> to define the function in the first place, but the recursive constructions I mentioned before lead to functional equations that allow us to easily retrieve the function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_7852db5d43d5ab2b22775d9f2131b869.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> (i.e., write down a nice, closed form of the function). Once we have that, we can recover the coefficients by applying techniques like comparing it to other well-understood functions, calculating the Taylor coefficients, or finding asymptotic expressions for the coefficients.

You may now be enchanted by the magic powers of analytic combinatorics, but may ask: what does this again have to do with primes? In fact, _analytic_ number theory owes its name to the exact same reason as _analytic_ combinatorics: we take stubborn and hard to handle discrete objects (e.g., primes or trees), throw them all together into one nice function (e.g., the zeta function or a generating function), and -- voilà! -- finally, we have a handle on those objects by applying all these wonderful analytical<sup id="rf3-673"><a href="#fn3-673" title="At this point, I fully got confused between analytic and analytical. A quick internet search indicates that there is simply no difference. However, I didn&#039;t find a single mention of analytical number theory. Still, I somehow feel that analytical tools sound better than analytic tools. English is such a confusing language!" rel="footnote">3</a></sup> tools we developed over the centuries. It's as though we smooth out the erratic behaviour of these discrete<sup id="rf4-673"><a href="#fn4-673" title="Luckily, the distinction between discrete and discreet is an easy one!" rel="footnote">4</a></sup> structures by zooming out of the nitty-gritty details and taking a look at the big picture.

As Marcus du Sautoy<sup id="rf5-673"><a href="#fn5-673" title="In The Music of the Primes, chapter 3." rel="footnote">5</a></sup> puts it more poetically:

> The zeta function provided Riemann with a looking-glass in which the primes appeared transformed. As in _Alice in Wonderland_, Riemann's paper sucked mathematicians from their familiar world of numbers through a rabbit hole into a new and often counterintuitive mathematical land.

John Derbyshire<sup id="rf6-673"><a href="#fn6-673" title="In Prime Obsession, chapter 6." rel="footnote">6</a></sup> calls it "the great fusion": the discrete and the continuous worlds, that for centuries have been thought as being completely independent, "counting and measuring", "numbers _staccato_ and numbers _legato_", come together in an unexpected harmony. For me, this is what makes the beauty of mathematics: even the most harmless problems require the full power of our mind and imagination to come up with new and creative concepts. Only the brightest mathematicians will pioneer new techniques like Bernhard Riemann did.<sup id="rf7-673"><a href="#fn7-673" title="Derbyshire rightfully&nbsp;attributes&nbsp;&quot;the great fusion&quot; to&nbsp;Peter Gustav Lejeune Dirichlet who first used analytical methods to prove his famous theorem on arithmetic progressions, but it was Riemann who brought the subject to its full powers by leaving the known waters of the real numbers and set sail for the complex numbers." rel="footnote">7</a></sup> But by following their footsteps, we may hope to breathe some of the inspiration they exhale.

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-673">
    <p>
      The exact result depends on what exactly the question is, e.g., if you count internal nodes, external nodes, only full trees, etc. Either way, the Catalan numbers are a recurring theme. Here, we don't care about the details, but just the general idea. &nbsp;<a href="#rf1-673" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn2-673">
    <p>
      Of course, if we want to apply analytical tools, we need this series to converge, which isn't guaranteed at all. If it doesn't, we can usually make it converge by applying weights, e.g., inverses of factorials like in the definition of the exponential function.&nbsp;<a href="#rf2-673" class="backlink" title="Jump back to footnote 2 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn3-673">
    <p>
      At this point, I fully got confused between <em>analytic</em> and <em>analytical</em>. A quick internet search indicates that there is simply no difference. However, I didn't find a single mention of analytic<em>al</em> number theory. Still, I somehow feel that <em>analytical</em> tools sound better than <em>analytic</em> tools. English is such a confusing language!&nbsp;<a href="#rf3-673" class="backlink" title="Jump back to footnote 3 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn4-673">
    <p>
      Luckily, the distinction between <em>discrete</em> and <em>discreet</em> is an easy one!&nbsp;<a href="#rf4-673" class="backlink" title="Jump back to footnote 4 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn5-673">
    <p>
      In <a title="Buy the book on amazon.co.uk" href="http://www.amazon.co.uk/gp/product/1841155802/ref=as_li_tf_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=1841155802&linkCode=as2&tag=riemannhypo-21" target="_blank"><em>The Music of the Primes</em></a>, chapter 3.&nbsp;<a href="#rf5-673" class="backlink" title="Jump back to footnote 5 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn6-673">
    <p>
      In <a title="Buy the book on amazon.co.uk" href="http://www.amazon.co.uk/gp/product/0452285259/ref=as_li_tf_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=0452285259&linkCode=as2&tag=riemannhypo-21" target="_blank"><em>Prime Obsession</em></a>, chapter 6.&nbsp;<a href="#rf6-673" class="backlink" title="Jump back to footnote 6 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn7-673">
    <p>
      Derbyshire rightfully attributes "the great fusion" to Peter Gustav Lejeune Dirichlet who first used analytical methods to prove his famous <a title="Dirichlet's theorem on arithmetic progressions" href="http://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions" target="_blank">theorem on arithmetic progressions</a>, but it was Riemann who brought the subject to its full powers by leaving the known waters of the real numbers and set sail for the complex numbers.&nbsp;<a href="#rf7-673" class="backlink" title="Jump back to footnote 7 in the text.">&#8617;</a>
    </p>
  </li>
</ol>