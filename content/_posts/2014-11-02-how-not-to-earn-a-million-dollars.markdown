---
author: Markus
date: 2014-11-02 12:06:30+00:00
draft: false
title: How NOT to Earn a Million Dollars
type: post
url: /riemannhypothesis.info/2014/11/how-not-to-earn-a-million-dollars/
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

I recently spent some time on the formidable website [Numberphile](http://www.numberphile.com/) which explains mathematical ideas, some important, some recreational, in short and accessible videos. Definitely worth checking out. One of the videos that is most relevant to us explains the Riemann Hypothesis:

http://youtu.be/d6c6uIyieoo

<!-- more -->

(Here is the link to the [video directly on the Numberphile webpage](http://www.numberphile.com/videos/riemann_hypothesis.html).) As [mentioned before](http://www.riemannhypothesis.info/2014/10/tossing-the-prime-coin/), it's not easy to explain the details and the beauty of the Riemann Hypothesis in few words, but I think the video definitely succeeds in compressing the essentials into 17 minutes.

One thing that caught my attention is the discussion of the CMI's Millennium Prize. Of course, you couldn't possibly fail to mention the $1,000,000 bounty on the problem in a popular account on it, but I was surprised to hear that you could earn the money not only by _proving_ the RH, but also by _disproving_ it. I was convinced that I read somewhere that a counterexample would not earn you the prize, so I took a look at the [rules for the Millennium Prize](http://www.claymath.org/millennium-problems/rules-millennium-prizes) -- and indeed, a counterexample would be considered a solution the same way as a proof. (So where the heck did I read the opposite? I couldn't find it anymore...)

Mathematicians' believes if the RH is true or false is an interesting discussion in itself. But since we are on the topic of the money it's also an interesting thought if it's worth putting resources in calculating zeta zeros in the hope to find a counterexample, i.e., a zero off the critical line -- after all, it would earn you a million bucks.

But there are two reasons why this would be ill invested money. First, much computing power has gone into calculating zeta zeros, worth well in excess of the prize money.

In fact, there goes the anecdote that the RH is responsible for the "most expensive bottles of wine ever drunk": the two eminent mathematicians Don Zagier and Enrico Bombieri made a bet (worth two bottles of good Bordeaux wine) that there would be no counterexamples to the RH amongst the first 300,000,000 zeros. As it so happened, a research team around Herman te Riele and Richard Brent some time later confirmed the RH for the first 200,000,000 zeros. When they learnt about the bet, they went the extra mile and calculated another 100,000,000 zeros just to settle the bet -- of course in favour of Bombieri who is a firm believer in the RH. But the point to this story is that at that time (we talk about the late 70s) the calculating power to find these extra 100,000,000 zeros was worth $700,000 alone -- all this to settle a bet for two bottles of wine!

So if you think it's a good investment to calculate zeta zeros in the hope to find a counterexample just to win the Millennium Prize -- it's a safer choice to buy a lottery ticket.

The second reason is that it seems extremely unlikely to find a (hypothetical) counterexample within the reach of today's computing capabilities. There are two famous conjectures closely related to the Riemann Hypothesis which seem perfectly sound to any number you could possibly calculate, but have been proven wrong by theoretical or indirect means. The first is Gauss's conjecture that the logarithmic integral $$\mathrm{Li}(x)$$ always overestimates the number of primes up to $$x$$. This has been vaporised by John Edensor Littlewood in 1914 ((Based on Riemann's work, by the way, which is kind of ironic since Riemann himself mentions the conjecture towards the end of his paper and sees his results as evidence for its truth.)). In fact, Littlewood's student Stanley Skewes later found an explicit upper bound for the first violation of Gauss's conjecture -- this mind-boggling number is now known as [Skewes' Number](http://en.wikipedia.org/wiki/Skewes%27_number). ((Of course, this number has later been dwarfed by [Graham's Number](http://en.wikipedia.org/wiki/Graham%27s_number), which I couldn't fail to mention...))

The second is the [Mertens Conjecture](http://en.wikipedia.org/wiki/Mertens_conjecture) which I mentioned in the [previous article:](http://www.riemannhypothesis.info/2014/10/tossing-the-prime-coin/)

$$!\left|\sum\mu(k)\right|=|M(n)|<\sqrt{n}.$$

This one has been disproved by  Andrew Odlyzko and Herman te Riele by calculating zeta zeros to high precision, but would still hold true if you just calculated ever higher of $$M(n)$$. Prime numbers are governed by weird things like iterated logarithms which make even the longest and most intensive calculations look like pre-school counting exercised.

As it's said in the video: if you want a really, _really_ arduous way of earning a million dollars, do number theory...

**Edit**: Just found this video where Numberphile regular [James Grime](http://singingbanana.com/) claims (towards the end) that a counterexample to the Riemann Hypothesis will not earn you the million dollars. It's certainly not where I first heard this, but clearly those statements do exist!

http://youtu.be/rGo2hsoJSbo
