# Q1 – Regex Solutions

This file contains regex patterns for each sub-question, with simple explanations and examples.

---

## 1. U.S. ZIP codes :
**Regex:** \b\d{5}(?:[- ]\d{4})?\b

**Explanation:**  
- `\b` → word boundary (ensures we match whole tokens only).  
- `\d{5}` → exactly 5 digits.  
- `(?:[- ]\d{4})?` → optional part: a hyphen or space followed by 4 digits.  
- `?` → makes the +4 part optional.  

**Matches:**  
- `12345`  
- `12345-6789`  
- `12345 6789`

---

## 2. Words not starting with a capital letter :
**Regex:** \b(?![A-Z])[A-Za-z]+(?:['-][A-Za-z]+)*\b

**Explanation:**  
- `(?![A-Z])` → negative lookahead: first letter is **not** uppercase.  
- `[A-Za-z]+` → one or more letters.  
- `(?:['-][A-Za-z]+)*` → allows apostrophes or hyphens inside the word (e.g., *don’t*, *state-of-the-art*).  
- `\b` → word boundaries.  

**Matches:**  
- `don’t`  
- `state-of-the-art`  
- `hello`

---

## 3. Numbers (sign, commas, decimals, scientific notation) :
**Regex:** [+-]?\d{1,3}(?:,\d{3})*(?:.\d+)?(?:[eE][+-]?\d+)?

**Explanation:**  
- `[+-]?` → optional plus or minus sign.  
- `\d{1,3}(?:,\d{3})*` → digits with optional thousands separators (e.g., 1,234).  
- `(?:\.\d+)?` → optional decimal part.  
- `(?:[eE][+-]?\d+)?` → optional scientific notation (e.g., `e-4`).  

**Matches:**  
- `123`  
- `+1,234.56`  
- `-3.45e-10`

---

## 4. Variants of “email” :
**Regex (case-insensitive):** (?i)\be[ -‐]?mail\b

**Explanation:**  
- `(?i)` → case-insensitive.  
- `e` followed by optional space, hyphen `-`, or en-dash `‐`.  
- `mail` → the word “mail”.  
- `\b` → word boundary.  

**Matches:**  
- `email`  
- `e-mail`  
- `E Mail`

---

## 5. “gooo…” interjection with punctuation :
**Regex:** \bgo+\b[!.,?]?

**Explanation:**  
- `g` followed by `o+` → one or more “o”s.  
- `\b` → word boundary.  
- `[!.,?]?` → optional punctuation (`!`, `.`, `,`, `?`) after the word.  

**Matches:**  
- `go`  
- `gooo!`  
- `goo?`

---

## 6. Lines ending with a question mark (with closing quotes/brackets) :
**Regex:** ?\s*["'”’)]]\s$

**Explanation:**  
- `\?` → a question mark.  
- `\s*` → optional spaces.  
- `["'”’)\]]*` → optional closing quotes/brackets.  
- `\s*$` → optional spaces until end of line.  

**Matches:**  
- `Are you coming?`  
- `Are you sure?")`  
- `What time is it?”`