---
title: Numbers of the World
author: Markus Shepherd
type: post
date: 2016-10-20T16:41:00+00:00
url: /2016/10/numbers-of-the-world/
categories:
  - Recreational Maths
tags:
  - binary
  - chain
  - connected component
  - cycle
  - Cypher
  - Danish
  - English
  - Esperanto
  - fixed point
  - French
  - German
  - GitHub
  - Graph
  - Indonesian
  - languages
  - Latvian
  - letters
  - literumi
  - Lithuanian
  - Matt Parker
  - Neo4j
  - nombroj
  - Norwegian
  - numbers
  - path
  - Polish
  - Portuguese
  - Python
  - recreational maths
  - Roman numerals
  - Russian
  - Spanish
  - spelling
  - words
  - world
  - YouTube

---
Recently <a href="http://standupmaths.com/" target="_blank">Matt Parker</a> uploaded a video to his <a href="https://www.youtube.com/user/standupmaths" target="_blank">YouTube channel</a> where he discussed numbers and the words used to represent them in different languages, more precisely the length of these words:

{{< youtube LYKn0yUTIU4 >}}

The basic idea is the following:

  1. _one_ has 3 letters,
  2. _two_ has 3 letters,
  3. _three_ has 5 letters,
  4. _four_ has 4 letters,
  5. _five_ has 4 letters,
  6. _six_ has 3 letters,
  7. _seven_ has 5 letters,
  8. _eight_ has 5 letters,
  9. _nine_ has 4 letters,
 10. _ten_ has 3 letters,

and so on... This can be seen as a function

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_d0e299fc5a206788e0c103a5a572ae66.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

<!--more-->

(Note that it says "number of letters" and not "length of word" – English and most other languages put spaces, commas, hyphens, and other decorations in between words for numbers, which we'll ignore in everything that follows.)

As the title of the video points out, we have <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_27e524d8f9d6e95a006827a48ee53b5b.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. This is called a fixed point, i.e., a point that just refuses to move when you apply the function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> to it. "Four" is the only word/number with this property in English. What's more, you can repeatedly apply the word-length-function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> on the result of itself, which yields a sort chain:

<p style="text-align: center;">
  <strong>one</strong> → <strong>three</strong> → <strong>five</strong> → <strong>four</strong> → <strong>four</strong> → <strong>four</strong> → ...
</p>

OK, we're kinda stuck at this point. In fact, every number will eventually get stuck in this very loop when <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is applied to it over and over.  These chains make pretty pictures:

[<img class="aligncenter size-large wp-image-868" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/en-1024x640.png" alt="Englis number-word-graph" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/en-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/en-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/en-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][1]

This graph uses every number up to 10000, but leaves out leaves (pun intended), i.e., those numbers that have no other number pointing to them. In other words: for every number you see in the graph above, there is a number (below 10001) in the English language with that length. In the original video, Matt presents a chain of length 6 (a three letter word), we can now extend that one to 7 (five letters) elements:

<p style="text-align: center;">
  <strong>one hundred and twenty-four</strong> → <strong>twenty-three</strong> → <strong>eleven</strong> → <strong>six</strong> → <strong>three</strong> → <strong>five</strong> → <strong>four</strong>,
</p>

which brings us back to the infinite loop of the fixed point. This is probably a good point to discuss the inherit ambiguity in the function's definition: natural languages are a mess. You might well have chosen to represent 124 above as "one hundred twenty-four" instead, which yields a disappointing chain of length 6. The best you can do is choose one convention and stick to it. I didn't have much of a choice – I used existing software libraries to generate the spellings for me, so their convention is mine.

This pretty much all there is to say about English. Numerologically, it's a pretty dull language. The graph is not particularly inspiring, no really long chains, it has only one fixed point, no other cycle, and every initial condition leads to the same number. What about other languages?

## German

[<img class="aligncenter size-large wp-image-871" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/de-1024x640.png" alt="German" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/de-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/de-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/de-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][2]

OK, call this nepotism, because the only reason I included German is that this is my native language. The same single fixed point as English, and no chain longer than 6. German deserves the title of _dullest of all languages_. Sigh...

## Danish

[<img class="aligncenter size-large wp-image-872" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/da-1024x640.png" alt="Danish" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/da-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/da-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/da-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][3]

No particularly long chains, but no less than 3 fixed points. Pretty self-centred! Unlike German and English, you can categorise numbers depending on what infinite loop they will be stuck in eventually, any of the three fixed points 2, 3, or 4 (popular choices for fixed points, by the way). In graph theory, we call this the _connected components_ of a graph. Here's some homework for you: calculate the proportion of numbers in each connected component!

## Indonesian

[<img class="aligncenter size-large wp-image-874" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/id-1024x640.png" alt="Indonesian" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/id-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/id-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/id-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][4]

Indonesian is our first example of a language with a non-trivial cycle: 4 (_empat_) maps to 5 (_lima_) which maps back to 4.  It also forms some pretty long chains, the longest having 8 elements:

<p style="text-align: center;">
  <strong>delapan puluh delapan</strong> (88) → <strong>sembilan belas</strong> (19) → <strong>tiga belas</strong> (13) → <strong>sembilan</strong> (9) → <strong>delapan</strong> (8) → <strong>tujuh</strong> (7) → <strong>lima</strong> (5) → <strong>empat</strong> (4)
</p>

Again, there's a bit of convention necessary how to count the chains: I opted for counting the longest chain without having duplicate members. This does favour languages with long cycles: every chain is at least as long as that cycle, plus however long it takes to reach that cycle. Well, so be it.

## Esperanto

[<img class="aligncenter size-large wp-image-875" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/eo-1024x640.png" alt="Esperanto" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/eo-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/eo-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/eo-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][5]

Another language that made the list mostly because of personal taste. This constructed language is as regular as it could be – generating all the number words in Esperanto takes only a <a href="https://github.com/MarkusShepherd/literumi/blob/master/literumi/esperanto.py" target="_blank">dozen or so lines of code</a>.  It has the same three fixed points we've seen in Danish – 2, 3, and 4 – but the graph overall is really compact: the longest chain has a mere 4 members. If you think this is only possible in an artificial language, wait for our next candidate:

## Norwegian

[<img class="aligncenter size-large wp-image-876" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/no-1024x640.png" alt="Norwegian" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/no-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/no-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/no-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][6]

A little "bushier" than Esperanto, but the same short routes – no other natural language has shorter chains. (And again, it's the same egoistic numbers 2, 3, and 4.)

## Lithuanian

[<img class="aligncenter size-large wp-image-877" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lt-1024x640.png" alt="Lithuanian" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lt-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lt-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lt-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][7]

So far we've either seen fixed points, or one longer cycle. Lithuanian has both: the fixed point 7 (_septyni_) and the cycle 4 (_keturi_) → 6 (_šeši_) → 4.

## French

[<img class="aligncenter size-large wp-image-878" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/fr-1024x640.png" alt="French" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/fr-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/fr-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/fr-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][8]

French boasts the longest cycle in our little survey with 4 members:

<p style="text-align: center;">
  <strong>quatre</strong> (4) → <strong>six</strong> (6) → <strong>trois</strong> (3) → <strong>cinq</strong> (5)
</p>

Every number will settle in this loop, and still French has no chains longer than 7, so every number pretty quickly hits one of the four members of the omnipotent French cycle.

## Russian

[<img class="aligncenter size-large wp-image-879" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/ru-1024x640.png" alt="Russian" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/ru-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/ru-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/ru-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][9]

As well as being the only non-Latin script in contest, it also seems to have a pretty lonely number 3 (_три_). It's not all alone though: 2 (_два_) and 100 (_сто_) point to it. Still, this is the smallest connected component we've seen so far. Russian also has one other fixed point (11 – _одиннадцать_) and a 3-cycle:

<p style="text-align: center;">
  <strong>четыре</strong> (4)→ <strong>шесть</strong> (6)→ <strong>пять</strong> (5)
</p>

A lot of structure for one language!

## Polish

[<img class="aligncenter size-large wp-image-880" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pl-1024x640.png" alt="Polish" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pl-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pl-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pl-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][10]

The thing you notice immediately in Polish is just how spread out it is – in fact it takes some numbers 7 steps before they reach the language's all-consuming 3-cycle, which gives a record chain of 10 elements:

<p style="text-align: center;">
  <strong>dwieście sześćdziesiąt dziewięć</strong> (269) → <strong>dwadzieścia dziewięć</strong> (29) → <strong>dziewiętnaście</strong> (19) → <strong>czternaście</strong> (14) → <strong>jedenaście</strong> (11) → <strong>dziesięć</strong> (10) → <strong>osiem</strong> (8) → <strong>pięć</strong> (5) → <strong>cztery</strong> (4) → <strong>sześć</strong> (6)
</p>

Just for the fun of it, I give you three more languages, not because they have properties we haven't seen, but just because they're pretty.

## Spanish

[<img class="aligncenter size-large wp-image-882" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/es-1024x640.png" alt="Spanish" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/es-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/es-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/es-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][11]

## Portuguese

[<img class="aligncenter size-large wp-image-883" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pt_BR-1024x640.png" alt="Portuguese" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pt_BR-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pt_BR-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pt_BR-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][12]

## Latvian

[<img class="aligncenter size-large wp-image-884" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lv-1024x640.png" alt="Latvian" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lv-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lv-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lv-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][13]

But why stop at natural languages?

## Binary

[<img class="aligncenter size-large wp-image-885" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/binary-1024x640.png" alt="Binary" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/binary-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/binary-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/binary-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][14]

Matt mentions in his video binary, i.e., spelling out 10101 as _one zero one zero one_. The most interesting fact about this number system is the large value of its fixed point 18 – or _one zero zero one zero_ to those who like to talk to their computers.

## Roman numerals

[<img class="aligncenter size-large wp-image-886" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/roman-1024x640.png" alt="Roman numerals" width="474" height="296" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/roman-1024x640.png 1024w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/roman-300x188.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/roman-768x480.png 768w" sizes="(max-width: 474px) 100vw, 474px" />][15]

Not strictly speaking a spelling system, yet a way of representing numbers with letters. Not surprisingly, this graph is pretty sleek – and it deserves an honourable mention since it's the one time the number one (1) actually makes it into one of our graphs.

## Matt's <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> conjecture

In the video, Matt conjectures that in every language there is some threshold <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> for which every value greater than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> is mapped to a value smaller than <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> under that language's function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>. Since most (maybe all?) languages reflect our base 10 positional number system, the information each part of the word contains when placed in front of a previous number word grows exponentially, which means that <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> is essentially logarithmic, so large numbers will be rapidly "passed down" to the small numbers where all the action takes place.

[<img class="aligncenter size-full wp-image-890" src="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/plot007.png" alt="Esperanto" width="800" height="600" srcset="http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/plot007.png 800w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/plot007-300x225.png 300w, http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/plot007-768x576.png 768w" sizes="(max-width: 800px) 100vw, 800px" />][16]

This plot shows the values for <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8fa14cdd754f91cc6554c9e71929cce7.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> in Esperanto which I chose mostly for performance reasons. It is clear just how slow the function grows.

## Technical notes

If you made it this far in the article, you might appreciate a few words on how I produced all the graphics in this article. There are a few steps to it.

### Spell out numbers

Despite the many exceptions, latest from numbers above 100 things get very regular and are pretty much just concatenations of what happened before, so this task screams for computer programs. Many exist, but most are dirty one-time scripts. One pretty decent Python library is _<a href="https://github.com/savoirfairelinux/num2words" target="_blank">num2words</a>_ which is where most of the number words in this article come from. Unfortunately, the code is little messy as well, and I just wasn't able to extend it to add Esperanto support, so I started my own project _<a href="https://github.com/MarkusShepherd/literumi" target="_blank">literumi</a>_ ("spell" in Esperanto) which right now is mostly a thin wrapper around _num2words_, but that might change over time.

Since I had to rely on these software tools for the spelling of the numbers in most of the above languages I cannot guarantee their correctness – if you spot any mistakes, please do let me know!

### List of numbers

There are plenty of sites on the Internet that list the first couple of numbers, maybe up to 100, in a bunch of languages. (<a href="http://www.zompist.com/numbers.shtml" target="_blank">This site</a> really should get an honourable mention for listing 5000 languages, albeit only numbers 1 to 10.) But that's all dictionary style and meant to be educational, not to be processed easily with a machine. This article might be the only application for it, but it bothered me that there are no readily available files where nothing but the first couple of thousand number words are listed. So – of course – I started a project for it: <a href="https://github.com/MarkusShepherd/nombroj" target="_blank"><em>nombroj</em></a> ("numbers" in Esperanto).

This pretty much only contains lists I could generate with _literumi_, but I also tried the approach of sending the English number words to Google Translate and thus receiving a list in any of their dozens of languages. But the approach has two flaws: (a) Google Translate is extremely expensive – if you use their API they charge you about USD1 for translating 1000 numbers. (b) It's terrible – the spellings are inconsistent if not incorrect and are often interspersed with the expression in digits. And you charge for this, Google?

### Graphs

All the graphs (in the mathematical sense, other people would maybe call them networks) you see above are produced with Neo4j, an excellent graph database. I wrote a small script (another <a href="https://github.com/MarkusShepherd/number-graph" target="_blank">project on GitHub</a>, of course) to load the data into Neo4j, and then used their default visualisation in the browser to get the graphics – I simply made a screenshot. This is the query I used for English:

<pre>MATCH (n1:Number)
WHERE (n1)&lt;-[:LINK {lang: "en"}]-(:Number)
OPTIONAL MATCH (n1)&lt;-[e1:LINK {lang: "en"}]-(n2:Number)
WHERE (n2)&lt;-[:LINK {lang: "en"}]-(:Number)
RETURN n1, e1, n2</pre>

There might be smarter ways of doing this, but I'm very much a Neo4j novice and it certainly does the trick for me.

The last plot of the function <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a8988ce0f88f5292aa28b6e49f114d45.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> was created with _matplotlib_, through something like this:

<pre>import matplotlib.pyplot as plt
from literumi import spell
mx = 10**7 + 1
x = range(mx)
y = [len(spell(i, lang='eo')) for i in range(mx)]
plt.plot(x, y, linestyle='', marker='.')
plt.show()</pre>

 [1]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/en.png
 [2]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/de.png
 [3]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/da.png
 [4]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/id.png
 [5]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/eo.png
 [6]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/no.png
 [7]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lt.png
 [8]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/fr.png
 [9]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/ru.png
 [10]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pl.png
 [11]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/es.png
 [12]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/pt_BR.png
 [13]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/lv.png
 [14]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/binary.png
 [15]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/roman.png
 [16]: http://localhost:8885/riemannhypothesis.info/wp-content/uploads/2016/10/plot007.png