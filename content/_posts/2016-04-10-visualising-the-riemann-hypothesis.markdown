---
author: Markus
date: 2016-04-10 18:59:25+00:00
draft: false
title: Visualising the Riemann Hypothesis
type: post
url: /riemannhypothesis.info/2016/04/visualising-the-riemann-hypothesis/
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

https://www.youtube.com/watch?v=NAMuls4q2f4

<!-- more -->

What are we looking at? These are the values of $$\zeta(s)$$ as $$s$$ goes up the critical line $$s=\frac12+ti$$. We start at ((As far as I know, it's total coincidence we conventionally use t for both the imaginary part of a complex argument and a time variable, but it makes talking about this animation surprisingly natural.)) $$t=0$$ at the beginning of the video and go all the way up to $$t=200$$. $$\zeta(1/2)\approx-1.4603545\!\ldots$$, so this is where the values start. From there, we make an anti-clockwise semicircle until we hit the real axis again. After that, the $$\zeta$$-function "turns right" and settles into a clockwise spiral with most of the action happing in the right half-plane. This goes on and on forever. Notably, after about four seconds, the graph passes the origin for the first time. This is the first of infinitely many $$\zeta$$-zeros on the critical line, at about $$t\approx14.134725\!\ldots$$. From now, it winds around in seemingly unpredictable circles, sometimes small and hasty, sometimes wide and elegant, but it never forgets to visit the origin every so often.

I produced this video with a [relatively simple SageMath script](http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/04/plot_critical_line.txt) quite some time ago, but I didn't write this post up until now since I would really like to turn this into an interactive sheet where you can play with the values for yourself, step away from the critical line, see how the spiral will miss the origin, and so on. But it's unlikely I will get around to doing that any time soon, and I've realised the video got quite some audience on YouTube, so I thought it's high time I shared it here as well!
