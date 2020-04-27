---
title: A Toy Keyless Encryption Protocol
author: Markus Shepherd
type: post
date: 2015-10-02T11:00:37+00:00
url: /2015/10/a-toy-keyless-encryption-protocol/
categories:
  - Cryptography
tags:
  - Alice
  - Bob
  - Elliptic Curves
  - Eve
  - Groups
  - Information Theory
  - Lattice
  - Number theory
  - OTP
  - Primes
  - XOR

---
Cryptography is a natural application of number theory and so I'd like to write down a few thoughts about it in this blog. (The fact that there are _real world_ applications to number theory deserves some appreciation in itself, but it would throw us too much off track here.) One particularly nice feature of cryptography is the ability to explain its inner workings with real world analogies about security.

For instance, one way two parties (who we, by convention, call Alice and Bob) could hide their secrete communication is if Alice writes a letter, puts it in a box, and locks it with a padlock for which both she and Bob have a key, but no one else. Then Alice can send this box safely through any public means as anyone who intercepts it will not be able to open the box, rendering it useless to them. This is the principle behind symmetric cryptography. The obvious problem is that Alice and Bob will only be able to communicate if they managed to obtain identical keys beforehand.

Alternatively, Bob could distribute padlocks for which only he possesses the key to anyone who's interested. Now Alice can obtain such a padlock, use it to close the box with her letter and send it off to Bob. She won't be able to open the box, but neither will anybody else -- except Bob. It sounds tedious to ship padlocks for every single communication, but the advantage is that there's no need whatsoever for Bob to restrict distribution to trusted parties, making it possible for anyone to send him messages securely. This is the basis of public key cryptography (a field which is extremely number theory heavy -- a course about it will feature extensively theorems on primes, groups, elliptic curves, lattices, and many more really abstract concepts).

But there is yet another way parties could communicate securely. Let's imagine Alice uses a lock for which only she has a key. She ships this of to Bob who cannot unlock it himself -- instead, he'll add another padlock himself and sends everything back to Alice. She couldn't open it herself anymore, but she can remove her padlock and still send it off to Bob once more knowing no one except Bob will be able to open her secret. Finally, Bob opens his lock and can read Alice's message. No need to meet up and share keys, no shipping padlocks.<!--more-->

<span style="line-height: 1.5;">The problem when trying to translate this to some mathematical model is that "adding Bob's padlock" in most encryption schemes actually means taking Alice's locked box, </span><em style="line-height: 1.5;">putting it in another box</em><span style="line-height: 1.5;">, and then adding the padlock. When Alice receives this package, all of a sudden she's unable to remove her padlock anymore. In proper mathematical terms: encryption is not commutative. (Sorry, it's going to get a little mathematical. Feel free to skip a few paragraphs until you feel again comfortable with the formula-to-text ratio.) What we are trying to achieve looks like this:</span>

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_d6a6f895d00f96ef275e4596c0b55e28.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

where <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_3a3ea00cfc35332cedf6e5e9a32e94da.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_f623e75af30e62bbd73d6df5b50bb7b5.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> stand for encryption and decryption, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_19d7691f6d9fc1dd503107094b60ab00.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a65e5fea37e3c3b57087a180ec6f345c.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> for Alice's and Bob's key, respectively. This simply does not check out in general, since all we can rely on is

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e38892c38005a3ef91c1913b4fb66334.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

What we need is a scheme where

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4290f4105d9bc870439c6c117c96e5a4.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

with <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1b3c1a40f9cb094d47e8c6f9b0df773f.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> meaning the composition or chaining of functions, and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_324fdfbc5c58346688fdca1d375230d2.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> standing for the identity, i.e., the lazy operation that just leaves every argument as it is, exactly what we want for an encrypted then decrypted message. (End of the mathsy symbols section. Please switch brains back on _now_!)

It turns out there is one encryption scheme with this property, and what's more, it's in fact the best possible encryption: the **one time pad** (OTP).<sup id="rf1-741"><a href="#fn1-741" title="The name comes from the fact that it can indeed only be used once and will be completely insecure if the same key is used twice." rel="footnote">1</a></sup> It's a deep (though not hard to prove) result in information theory that the OTP provides perfect secrecy, i.e., an attacker who intercepts the encrypted message has no chance of learning any information about the original message whatsoever. This is an incredible strong statement: it does not depend on the smartness, luck, or resources of the attacker, it's a mathematical fact: not a single bit of the message will be revealed. Unfortunately, it requires a secrete (shared) key that is as long as the plaintext, and if the two parties have a way to communicate this key securely -- why not use this channel to send the message in the first place?

Here we go back to the scheme I described earlier --  Alice and Bob add their padlocks individually, no need to exchange keys beforehand. Concretely, this means Alice and Bob each choose their own keys which have to be as long as the original message, but there's no need to ever communicate these with anyone.

So, how does the OTP work? It's about as simple as it could be:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_1f147692cfcea8fee01c3d72624ad793.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Here, the "funny plus" <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_61a41642d26f221806dcbccfcebc2ef8.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> means XOR if you're a computer scientist or (bitwise) addition modulo 2 if you're a mathematician. If you're neither, just think of it as a special kind of addition and don't worry about the details. The important fact is that it has all the properties of regular addition, plus the following: <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_47cc3e8ff8121e00797a7b426c2d90f9.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, i.e., an element XORed with itself vanishes. This is all it takes to show that the OTP has the required consistency property:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_bc018634f3184baa6e49be734bd2e732.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

just as we needed. The secrecy follows from the fact that if the <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_8ce4b16b22b58894aa86c421e8759df3.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> looks like "random noise", so will the resulting cipher text. In other words, if I intercept a cipher <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_4a8a08f09d37b73795649038408b5f33.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>, _any_ message <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6f8f57715090da2632453988d9a1501b.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span> (of the same length) is equally likely to be the original message. This is what it means that the eavesdropper learns nothing about the plaintext.

How would our little keyless protocol work? First, Alice and Bob both choose keys <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_19d7691f6d9fc1dd503107094b60ab00.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> and <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a65e5fea37e3c3b57087a180ec6f345c.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span> uniformly at random. (As I stated above, the whole security of the OTP hinges on this being truly random, which is non-trivial, or maybe impossible,<sup id="rf2-741"><a href="#fn2-741" title="If P=NP. I&#039;m glad you asked." rel="footnote">2</a></sup> with software, but this way beyond our scope here.) Then the dance begins:

  1. Alice sends Bob <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e4c07cb458d92abe65012186d69107df.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.
  2. Bob sends Alice <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_88cc25671ff8faa25aac191a53992d99.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.
  3. Alice sends Bob <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_834b1bc9a39033569983d51441362670.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.
  4. Bob retrieves the message as <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_dcb8860113edac30e82aa98465d0cbb1.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>.

You don't believe me that this checks out? Well, let's see... Plugging things in from bottom up yields:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_e534f55e073f09f3dcc979e13edd5230.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

All we need is the fact that XOR, like any good addition, is commutative and associative, i.e., order does not matter, and neither do parentheses.

_Of course, this protocol is absolutely and entirely useless._

Why? Well, I claimed throughout that it was Bob who added his lock. But how do we know that it was in fact Bob? What do we know about this "Bob guy" anyways? It could in fact be anyone at all! There's no proof of his identity. So, when we receive the double-locked package back with our little secrete safely inside, and remove our lock as dutifully as gullibly, we may have unlocked it in fact for Eve, Alice's evil cousin, who intercepted our message en route, and sent it back with her own lock instead of Bob's. It's a good example of why secrecy against eavesdropping is never enough --  we must equally protect against any tempering.<sup id="rf3-741"><a href="#fn3-741" title="Also, we just tripled traffic on our network by sending packages back and forth. Just saying." rel="footnote">3</a></sup>

But it comes worse. Note that the problem above holds for my real world padlock analogy just the same: when we unlock our part, we have no clue who added the second padlock. In fact, if there was no previous contact, how could we have any information at all about that other party? At least, we are guaranteed that no one else could read our message, even if we don't know who that other dude is we're communicating with.

Alas, our use of the OTP does not provide even that guarantee. Anyone who intercepted our exchange can recover Bob's key easily and hence eventually the plaintext. Just look what happens when I XOR the first to cipher texts:

<p style='text-align:center;'>
  <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_53ecc2df70f1640095c68707e9a0217d.gif' style='vertical-align: middle; border: none;' class='tex' alt="" /></span>
</p>

Out falls <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_a65e5fea37e3c3b57087a180ec6f345c.gif' style='vertical-align: middle; border: none; ' class='tex' alt="" /></span>, so nothing stops us from using this to unlock <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_20b620923ab918a6f2b7a0eb419f8fc4.gif' style='vertical-align: middle; border: none; padding-bottom:1px;' class='tex' alt="" /></span> and hence steal the secrete message <span class='MathJax_Preview'><img src='http://localhost:8885/riemannhypothesis.info/wp-content/plugins/latex/cache/tex_6f8f57715090da2632453988d9a1501b.gif' style='vertical-align: middle; border: none; padding-bottom:2px;' class='tex' alt="" /></span>. This is just more evidence for the first rule of cryptography:

> Don't invent your own crypto -- particularly if you're a clueless number theorist writing some weird blog... 😉

&nbsp;

<hr class="footnotes" />

<ol class="footnotes">
  <li id="fn1-741">
    <p>
      The name comes from the fact that it can indeed only be used once and will be completely insecure if the same key is used twice.&nbsp;<a href="#rf1-741" class="backlink" title="Jump back to footnote 1 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn2-741">
    <p>
      If P=NP. I'm glad you asked.&nbsp;<a href="#rf2-741" class="backlink" title="Jump back to footnote 2 in the text.">&#8617;</a>
    </p>
  </li>
  
  <li id="fn3-741">
    <p>
      Also, we just tripled traffic on our network by sending packages back and forth. Just saying.&nbsp;<a href="#rf3-741" class="backlink" title="Jump back to footnote 3 in the text.">&#8617;</a>
    </p>
  </li>
</ol>