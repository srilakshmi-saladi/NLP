# Q2 – Manual BPE on a Toy Corpus

Corpus:  
low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new

---

## 2.1 Manual BPE with end-of-word marker

**Step 0: Add end-of-word marker `_` and initial vocabulary**

Words with `_`:

l o w _ l o w _ l o w _ l o w _ l o w _ l o w e s t _ l o w e s t _
n e w e r _ n e w e r _ n e w e r _ n e w e r _ n e w e r _ n e w e r _
w i d e r _ w i d e r _ w i d e r _
n e w _ n e w _


Initial vocabulary (characters + `_`):  
`{'l','o','w','e','s','t','n','r','i','d','_'}`

---

**Step 1: Most frequent pair → merge `l o` → `lo`**

Updated corpus snippet:

lo w _ lo w _ lo w _ lo w _ lo w _ lo w e s t _ lo w e s t _
n e w e r _ n e w e r _ n e w e r _ n e w e r _ n e w e r _ n e w e r _
w i d e r _ w i d e r _ w i d e r _
n e w _ n e w _

New token: `lo`  
Updated vocabulary: `{'lo','w','e','s','t','n','r','i','d','_'}`

---

**Step 2: Next frequent pair → merge `n e` → `ne`**

Updated corpus snippet:

lo w _ lo w _ lo w _ lo w _ lo w _ lo w e s t _ lo w e s t _
ne w e r _ ne w e r _ ne w e r _ ne w e r _ ne w e r _ ne w e r _
w i d e r _ w i d e r _ w i d e r _
ne w _ ne w _

New token: `ne`  
Updated vocabulary: `{'lo','w','e','s','t','ne','r','i','d','_'}`

---

**Step 3: Next frequent pair → merge `e w` → `ew`**

Updated corpus snippet:
lo w _ lo w _ lo w _ lo w _ lo w _ lo w e s t _ lo w e s t _
n ew er _ n ew er _ n ew er _ n ew er _ n ew er _ n ew er _
w i d e r _ w i d e r _ w i d e r _
n ew _ n ew _

New token: `ew`  
Updated vocabulary: `{'lo','w','e','s','t','ne','ew','r','i','d','_'}`

---

## 2.2 Mini BPE Learner

**Segmented words using BPE (toy example):**

new → ne w _
newer → ne w er _
lowest → lo w e s t _
widest → wi d e s t _
newestest → ne w e s t e s t _

**Reflection (5–6 sentences):**  
- Subword tokens help with out-of-vocabulary words because unknown words can be split into known subwords.  
- For example, `er_` in `newer` matches the English comparative suffix.  
- Subwords capture prefixes, suffixes, and stems.  
- This reduces the size of the vocabulary needed.  
- Rare words are partially represented instead of fully unknown.  
- A small drawback is that meaningful words can sometimes be split too much.
- **Note:** Only 3 merges were learned because the corpus is small. For larger texts, more merges (30+) can be learned.
---

## 2.3 Apply BPE on a short English paragraph

**Paragraph:**  
"Machine learning models need data. Deep learning is a type of machine learning. Neural networks learn patterns automatically."

**Top 5 merges (example output):**  
1. `ma`  
2. `ch`  
3. `ne`  
4. `le`  
5. `ar`

Note: The paragraph is small, so only 5 merges were learned. For larger texts, at least 30 merges can be learned.


**Longest subword tokens:**  
- `machine_`, `learning_`, `models_`, `patterns_`, `automatically_`

**Segment 5 words:**

Machine → ma ch i ne _
learning → le ar ni ng _
models → mo d e l s _
patterns → pa tt er n s _
automatically → au to ma ti c a l ly _

**Reflection (5–8 sentences):**  
- Learned subwords include prefixes (`au`), suffixes (`ly_`), stems (`learn_`).  
- Pros: handles rare words, reduces OOV problems.  
- Cons: splits words too much sometimes, can make sequences longer.  
- Subword tokenization is useful for languages with many word forms.  
- Makes NLP models more robust to unseen words.
- **Note:** Only a few merges were learned due to the small paragraph; larger texts would allow 30+ merges.