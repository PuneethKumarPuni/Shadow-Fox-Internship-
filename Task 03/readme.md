# Task 3 - List Operations + Bonus: Justice League Leader Prediction

## Completed as part of Python Development Internship by Shadow Fox


---

## Objectives:

- Practice list operations like adding, removing, inserting, replacing, and sorting.
- Simulate real-world scenarios using Python list manipulation.
- Predict the new team leader using sorting logic.

---

## Tasks Completed:

### 1. Initial Setup:
- Created a list of Justice League members:
  ```python
  ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
  ```
- Counted total members using `len()`:  
   Total: `6`

---

### 2. Team Expansion:
- Added **Batgirl** and **Nightwing** using `.append()`:
  ```python
  justice_league.append("Batgirl")
  justice_league.append("Nightwing")
  ```

---

### 3. Leadership Change:
- Moved **Wonder Woman** to the front using `.remove()` and `.insert()`:
  ```python
  justice_league.remove("Wonder Woman")
  justice_league.insert(0, "Wonder Woman")
  ```

---

### 4. Conflict Management:
- **Green Lantern** placed between **Aquaman** and **Flash** to separate them.

---

### 5. Team Reformation:
- Replaced the entire list with new heroes:
  ```python
  ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
  ```

---

### 6. Sorting and Leader Prediction:
- Sorted the list alphabetically using `.sort()`:
  ```python
  ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
  ```
- Predicted new leader (first in sorted list):  
   **Cyborg**

---

## Python Concepts Used:
- List creation and indexing
- `.append()`, `.remove()`, `.insert()`
- `.sort()` for alphabetical sorting
- `len()` to count members
- Real-world simulation using Python logic

---

## Final Output:
```python
Sorted Justice League: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
Predicted New Leader: Cyborg
```

---

## Author:
Intern Puneeth Kumar P.