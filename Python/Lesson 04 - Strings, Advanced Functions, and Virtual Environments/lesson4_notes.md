# Lesson 4 notes — Strings, advanced functions, venv

Working code: [`lesson4_notes.py`](lesson4_notes.py)

Session notes from 19 AUG 2026 (converted from `lesson4_notes.docx`; Copilot chat filler dropped).

---

## Indexing and slicing

Indexing picks one item by position. Slicing grabs a range. Python counts from **0**.

**Indexing**

- First item is index `0`.
- Positive: count forward (`0, 1, 2`).
- Negative: count backward (`-1` is last).
- Out of bounds → error.

**Slicing**

- `sequence[start:stop]` — up to but **not including** `stop`.
- `[:stop]` — from the start.
- `[start:]` — through the end.
- `[start:stop:step]` — skip by `step`. `[::-1]` reverses.

### Q: is `-3` equal to `0`?

No. They can **land on the same item** in a 3-element sequence, but they are different ways of counting.

`my_list = ['c', 'a', 't']`

| Character | `'c'` | `'a'` | `'t'` |
|-----------|-------|-------|-------|
| Forward | 0 | 1 | 2 |
| Backward | -3 | -2 | -1 |

```python
print(my_list[0])   # 'c'
print(my_list[-3])  # 'c'
```

---

## String methods (cheat sheet)

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `.upper()` | All uppercase | `"hi".upper()` | `"HI"` |
| `.lower()` | All lowercase | `"Hi".lower()` | `"hi"` |
| `.title()` | First letter of each word | `"hello world".title()` | `"Hello World"` |
| `.capitalize()` | First character only | `"hello".capitalize()` | `"Hello"` |
| `.strip()` | Trim whitespace both ends | `" hi ".strip()` | `"hi"` |
| `.replace(old, new)` | Replace substring | `"cat".replace("c", "b")` | `"bat"` |
| `.split(sep)` | Split into a list | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `.join(iterable)` | Join items into a string | `"-".join(["a", "b"])` | `"a-b"` |

---

## Exercise 1 — Username validator

**Rules:** 5–15 chars; letters, digits, or `_`; start with a letter; not end with `_`; at least one digit.

**Tests:** `"coder_42"` True · `"2cool"` False · `"hi"` False · `"python_dev_"` False · `"justletters"` False

**Verdict:** The `lesson4_notes.py` version is correct. Length first so `username[0]` cannot IndexError. `all(...isalnum or '_')` blocks junk chars. `any(...isdigit)` enforces a digit.

Regex can pack the same rules into one pattern; line-by-line checks are easier to debug. Canonical code is in the `.py` file, not regex.

---

## Exercise 2 — Secret message decoder

Scheme: reverse each word, lowercase, `#` instead of spaces, digits are junk. Capitalize the first letter of the sentence.

Example: `decode("eht7#terces#3edoc#si#nohtyp9")` → `"The secret code is python"`

### `"".join(char for char in message if not char.isdigit())`

Inside-out: loop each `char` → keep if not a digit → glue with `"".join` (no separator). `"eht7#"` becomes `"eht#"`.

### `words = clean_message.split("#")`

One list, many strings. `"eht#terces#edoc"` → `["eht", "terces", "edoc"]`. The `#` is gone.

### `reversed_words = [word[::-1] for word in words]`

List comprehension: for each word, slice with step `-1`. `["eht", "terces"]` → `["the", "secret"]`.

Then `" ".join(...)` and `.capitalize()`.

---

## PowerShell: `cd` and spaces

Paths with spaces (`CMU AI2C`, `Lesson 04...`) must be quoted:

```powershell
cd "C:\Programming\School\CMU AI2C\summer-course\Python\Lesson 04 - Strings, Advanced Functions, and Virtual Environments\"
```

Tab-complete after `cd C:\GDrive\Pro` so PowerShell inserts quotes.

---

## Imports — `area.rectangle_area`

`import area` then call `area.rectangle_area(20.5, 5)`.

Or `from area import rectangle_area` and call `rectangle_area(20.5, 5)` with no prefix.

Bare `rectangle_area(...)` after `import area` is a **NameError**.

---

## Exercise — `curve_grades` (default parameters)

`curve_grades(scores, bonus=5, max_score=100)` — add bonus, cap at `max_score`.

**First attempt broke:** list-comprehension used a multi-line `if/else` inside `[]` (SyntaxError); hardcoded `100` instead of `max_score`; `==` instead of assigning a capped value.

**Working version** (in `lesson4_notes.py`): loop, `adjusted = num + bonus`, append `max_score` if over.

One-liners (not required):

```python
return [min(num + bonus, max_score) for num in scores]
```

User input loop for how many grades, curve, and max is in the `.py` file.

---

## Exercise — `print_boarding_list` (`enumerate`)

Seats start at 1. Must use `enumerate`.

**Bug:** `return print(...)` inside the loop. `return` exits after the first passenger. `print()` also returns `None`.

**Fix:** print only — no `return` in the loop.

```python
def print_boarding_list(passengers):
    for i, passenger in enumerate(passengers, start=1):
        print(f'Seat {i}: {passenger}')
```

### Q: do functions always need `return`?

No.

| Kind | Need `return`? | Example |
|------|----------------|---------|
| Action | No — does a side effect (`print`, write file). Implicit return is `None`. | `print_boarding_list` |
| Calculation | Yes — hand a value back to the caller. | `curve_grades`, `decode` |

`print` = show a human. `return` = give another part of the program a value.
