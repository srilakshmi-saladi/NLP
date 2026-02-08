# Q3 Bayes Rule :

 cMAP = argmax P(c) . P(d | c)
           c∈C


1)Tasks:
Explain in your own words what each term means: P(c), P(d∣c) and P(c∣d). 
Why can the denominator P(d) be ignored when comparing classes?



What each term means :


     cMAP = argmax  P(c | d)
              c∈C

     cMAP = argmax P(c) . P(d | c)
              c∈C  ---------------
                       P(d)

     cMAP = argmax P(c) . P(d | c)
              c∈C


P(c) — Prior probability of the class
This is how common a class is overall, before looking at the document.

Example: If 60% of emails are spam, then spam has a higher prior.

P(d∣c) — Likelihood of the document given the class
This measures how likely it is to see the words in the document if it belongs to a certain class.

Example: Words like “win” and “free” are more likely if the class is spam.

P(c∣d) — Posterior probability of the class given the document
This is what we actually want: the probability that the document belongs to a class after seeing its words.


2)Why the denominator P(d) can be ignored

P(d) is the probability of the document regardless of class.

When comparing different classes for the same document, P(d) is the same for all classes.

So, it does not affect which class has the highest probability.

This is why in Naive Bayes we simply use:
 
       cMAP = argmax P(c) . P(d | c)
              c∈C


Summary :

P(c) = how common the class is

P(d∣c) = how well the document fits the class

P(c∣d) = probability the document belongs to the class after seeing it

P(d) can be ignored because it is the same for all classes
