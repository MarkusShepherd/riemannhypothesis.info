---
author: Markus
date: 2015-10-02 11:00:37+00:00
draft: false
title: A Toy Keyless Encryption Protocol
type: post
url: /riemannhypothesis.info/2015/10/a-toy-keyless-encryption-protocol/
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

But there is yet another way parties could communicate securely. Let's imagine Alice uses a lock for which only she has a key. She ships this of to Bob who cannot unlock it himself -- instead, he'll add another padlock himself and sends everything back to Alice. She couldn't open it herself anymore, but she can remove her padlock and still send it off to Bob once more knowing no one except Bob will be able to open her secret. Finally, Bob opens his lock and can read Alice's message. No need to meet up and share keys, no shipping padlocks.<!-- more -->

The problem when trying to translate this to some mathematical model is that "adding Bob's padlock" in most encryption schemes actually means taking Alice's locked box, _putting it in another box_, and then adding the padlock. When Alice receives this package, all of a sudden she's unable to remove her padlock anymore. In proper mathematical terms: encryption is not commutative. (Sorry, it's going to get a little mathematical. Feel free to skip a few paragraphs until you feel again comfortable with the formula-to-text ratio.) What we are trying to achieve looks like this:

$$!D(k_B,D(k_A,E(k_B,E(k_A,m))))=m,$$

where $$E$$ and $$D$$ stand for encryption and decryption, and $$k_A$$ and $$k_B$$ for Alice's and Bob's key, respectively. This simply does not check out in general, since all we can rely on is

$$!D(k,E(k,m))=m.$$

What we need is a scheme where

$$!D_B \circ D_A \circ E_B \circ E_A = D_B \circ E_B \circ D_A \circ E_A = \mathrm{id},$$

with $$\circ$$ meaning the composition or chaining of functions, and $$\mathrm{id}$$ standing for the identity, i.e., the lazy operation that just leaves every argument as it is, exactly what we want for an encrypted then decrypted message. (End of the mathsy symbols section. Please switch brains back on _now_!)

It turns out there is one encryption scheme with this property, and what's more, it's in fact the best possible encryption: the **one time pad** (OTP). ((The name comes from the fact that it can indeed only be used once and will be completely insecure if the same key is used twice.)) It's a deep (though not hard to prove) result in information theory that the OTP provides perfect secrecy, i.e., an attacker who intercepts the encrypted message has no chance of learning any information about the original message whatsoever. This is an incredible strong statement: it does not depend on the smartness, luck, or resources of the attacker, it's a mathematical fact: not a single bit of the message will be revealed. Unfortunately, it requires a secrete (shared) key that is as long as the plaintext, and if the two parties have a way to communicate this key securely -- why not use this channel to send the message in the first place?

Here we go back to the scheme I described earlier --  Alice and Bob add their padlocks individually, no need to exchange keys beforehand. Concretely, this means Alice and Bob each choose their own keys which have to be as long as the original message, but there's no need to ever communicate these with anyone.

So, how does the OTP work? It's about as simple as it could be:

$$!E(k,m) = k \oplus m \quad \text{and} \quad D(k,c) = k \oplus c.$$

Here, the "funny plus" $$\oplus$$ means XOR if you're a computer scientist or (bitwise) addition modulo 2 if you're a mathematician. If you're neither, just think of it as a special kind of addition and don't worry about the details. The important fact is that it has all the properties of regular addition, plus the following: $$a\oplus a=0$$, i.e., an element XORed with itself vanishes. This is all it takes to show that the OTP has the required consistency property:

$$!D(k,E(k,m)) = k \oplus (k \oplus m) = (k \oplus k) \oplus m = 0 \oplus m = m,$$

just as we needed. The secrecy follows from the fact that if the $$k$$ looks like "random noise", so will the resulting cipher text. In other words, if I intercept a cipher $$c$$, _any_ message $$m$$ (of the same length) is equally likely to be the original message. This is what it means that the eavesdropper learns nothing about the plaintext.

How would our little keyless protocol work? First, Alice and Bob both choose keys $$k_A$$ and $$k_B$$ uniformly at random. (As I stated above, the whole security of the OTP hinges on this being truly random, which is non-trivial, or maybe impossible, ((If P=NP. I'm glad you asked.)) with software, but this way beyond our scope here.) Then the dance begins:



	  1. Alice sends Bob $$c_1=k_A\oplus m$$.
	  2. Bob sends Alice $$c_2=k_B\oplus c_1$$.
	  3. Alice sends Bob $$c_3=k_A\oplus c_2$$.
	  4. Bob retrieves the message as $$m=k_B\oplus c_3$$.

You don't believe me that this checks out? Well, let's see... Plugging things in from bottom up yields:

$$!k_B\oplus(k_A\oplus(k_B\oplus(k_A\oplus m)))=(k_A\oplus k_A)\oplus(k_B\oplus k_B)\oplus m=m.$$

All we need is the fact that XOR, like any good addition, is commutative and associative, i.e., order does not matter, and neither do parentheses.

_Of course, this protocol is absolutely and entirely useless._

Why? Well, I claimed throughout that it was Bob who added his lock. But how do we know that it was in fact Bob? What do we know about this "Bob guy" anyways? It could in fact be anyone at all! There's no proof of his identity. So, when we receive the double-locked package back with our little secrete safely inside, and remove our lock as dutifully as gullibly, we may have unlocked it in fact for Eve, Alice's evil cousin, who intercepted our message en route, and sent it back with her own lock instead of Bob's. It's a good example of why secrecy against eavesdropping is never enough --  we must equally protect against any tempering. ((Also, we just tripled traffic on our network by sending packages back and forth. Just saying.))

But it comes worse. Note that the problem above holds for my real world padlock analogy just the same: when we unlock our part, we have no clue who added the second padlock. In fact, if there was no previous contact, how could we have any information at all about that other party? At least, we are guaranteed that no one else could read our message, even if we don't know who that other dude is we're communicating with.

Alas, our use of the OTP does not provide even that guarantee. Anyone who intercepted our exchange can recover Bob's key easily and hence eventually the plaintext. Just look what happens when I XOR the first to cipher texts:

$$!c_1 \oplus c_2 = c_1 \oplus (k_B\oplus c_1) = (c_1 \oplus c_1) \oplus k_B = k_B.$$

Out falls $$k_B$$, so nothing stops us from using this to unlock $$c_3$$ and hence steal the secrete message $$m$$. This is just more evidence for the first rule of cryptography:


<blockquote>Don't invent your own crypto -- particularly if you're a clueless number theorist writing some weird blog... ;-)</blockquote>



