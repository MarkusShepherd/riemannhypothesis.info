---
title: How NOT to Earn a Million Dollars
author: Markus Shepherd
type: post
date: 2014-11-02T12:06:30+00:00
url: /2014/11/how-not-to-earn-a-million-dollars/
categories:
  - Feature
tags:
  - Bombieri
  - CMI
  - Gauss
  - Littlewood
  - Logarithm
  - Mertens
  - Millennium
  - Million
  - Numberphile
  - Riemann
  - YouTube
  - Zagier

---
I recently spent some time on the formidable website <a title="Numberphile" href="http://www.numberphile.com/" target="_blank">Numberphile</a> which explains mathematical ideas, some important, some recreational, in short and accessible videos. Definitely worth checking out. One of the videos that is most relevant to us explains the Riemann Hypothesis:

{{< youtube d6c6uIyieoo >}}

<!--more-->

(Here is the link to the <a title="Riemann Hypothesis" href="http://www.numberphile.com/videos/riemann_hypothesis.html" target="_blank">video directly on the Numberphile webpage</a>.) As [mentioned before][1], it's not easy to explain the details and the beauty of the Riemann Hypothesis in few words, but I think the video definitely succeeds in compressing the essentials into 17 minutes.

One thing that caught my attention is the discussion of the CMI's Millennium Prize. Of course, you couldn't possibly fail to mention the $1,000,000 bounty on the problem in a popular account on it, but I was surprised to hear that you could earn the money not only by _proving_ the RH, but also by _disproving_ it. I was convinced that I read somewhere that a counterexample would not earn you the prize, so I took a look at the <a title="Rules for the Millennium Prizes" href="http://www.claymath.org/millennium-problems/rules-millennium-prizes" target="_blank">rules for the Millennium Prize</a> -- and indeed, a counterexample would be considered a solution the same way as a proof. (So where the heck did I read the opposite? I couldn't find it anymore...)

Mathematicians' believes if the RH is true or false is an interesting discussion in itself. But since we are on the topic of the money it's also an interesting thought if it's worth putting resources in calculating zeta zeros in the hope to find a counterexample, i.e., a zero off the critical line -- after all, it would earn you a million bucks.

But there are two reasons why this would be ill invested money. First, much computing power has gone into calculating zeta zeros, worth well in excess of the prize money.

In fact, there goes the anecdote that the RH is responsible for the "most expensive bottles of wine ever drunk": the two eminent mathematicians Don Zagier and Enrico Bombieri made a bet (worth two bottles of good Bordeaux wine) that there would be no counterexamples to the RH amongst the first 300,000,000 zeros. As it so happened, a research team around Herman te Riele and Richard Brent some time later confirmed the RH for the first 200,000,000 zeros. When they learnt about the bet, they went the extra mile and calculated another 100,000,000 zeros just to settle the bet -- of course in favour of Bombieri who is a firm believer in the RH. But the point to this story is that at that time (we talk about the late 70s) the calculating power to find these extra 100,000,000 zeros was worth $700,000 alone -- all this to settle a bet for two bottles of wine!

So if you think it's a good investment to calculate zeta zeros in the hope to find a counterexample just to win the Millennium Prize -- it's a safer choice to buy a lottery ticket.

The second reason is that it seems extremely unlikely to find a (hypothetical) counterexample within the reach of today's computing capabilities. There are two famous conjectures closely related to the Riemann Hypothesis which seem perfectly sound to any number you could possibly calculate, but have been proven wrong by theoretical or indirect means. The first is Gauss's conjecture that the logarithmic integral <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8b418ad702ddb01df8c66e6c74032fe4.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> always overestimates the number of primes up to <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_9dd4e461268c8034f5c8564e155c67a6.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>. This has been vaporised by John Edensor Littlewood in 1914<sup id="rf1-644"><a href="#fn1-644" title="Based on Riemann&#039;s work, by the way, which is kind of ironic since Riemann himself mentions the conjecture towards the end of&nbsp;his paper and sees his results as evidence for its truth." rel="footnote">1</a></sup>. In fact, Littlewood's student Stanley Skewes later found an explicit upper bound for the first violation of Gauss's conjecture -- this mind-boggling number is now known as <a title="Skewes' Number" href="http://en.wikipedia.org/wiki/Skewes%27_number" target="_blank">Skewes' Number</a>.<sup id="rf2-644"><a href="#fn2-644" title="Of course, this number has later been dwarfed by Graham&#039;s Number, which I couldn&#039;t fail to mention..." rel="footnote">2</a></sup>

The second is the <a title="Mertens Conjecture" href="http://en.wikipedia.org/wiki/Mertens_conjecture" target="_blank">Mertens Conjecture</a> which I mentioned in the [previous article:][1]

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_26e25965171dcffa1ad1d578fc08de62.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

This one has been disproved by  Andrew Odlyzko and Herman te Riele by calculating zeta zeros to high precision, but would still hold true if you just calculated ever higher of <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_505b30474bf75fb6f9f0d876bf9fdcf1.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Prime numbers are governed by weird things like iterated logarithms which make even the longest and most intensive calculations look like pre-school counting exercised.

As it's said in the video: if you want a really, _really_ arduous way of earning a million dollars, do number theory...

**Edit**: Just found this video where Numberphile regular <a title="James Grime's homepage" href="http://singingbanana.com/" target="_blank">James Grime</a> claims (towards the end) that a counterexample to the Riemann Hypothesis will not earn you the million dollars. It's certainly not where I first heard this, but clearly those statements do exist!

{{< youtube rGo2hsoJSbo >}}

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-644">
    <p>
      Based on Riemann's work, by the way, which is kind of ironic since Riemann himself mentions the conjecture towards the end of his paper and sees his results as evidence for its truth.&nbsp;<a href="#rf1-644" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn2-644">
    <p>
      Of course, this number has later been dwarfed by <a title="Graham's Number" href="http://en.wikipedia.org/wiki/Graham%27s_number" target="_blank">Graham's Number</a>, which I couldn't fail to mention...&nbsp;<a href="#rf2-644" class="backlink" title="Jump back to footnote 2 in the text.">&#8617;</a>
    </p>
  </li>
</ol>

 [1]: http://www.riemannhypothesis.info/2014/10/tossing-the-prime-coin/ "Tossing the Prime Coin"