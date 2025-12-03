# The Kata—Christmas Lights Kata 🚀

Source: [https://kata-log.rocks/christmas-lights-kata](https://kata-log.rocks/christmas-lights-kata)

## 🎄 Exercise Description

This kata consists of a grid of lights (by default **1000×1000**) that can be either **on** or **off**. 
Using an instructions file (see `instructions.md`), you must apply the following operations:

- `turn on x1,y1 through x2,y2`
- `turn off x1,y1 through x2,y2`
- `toggle x1,y1 through x2,y2`

At the end, you must answer: **How many lights are on?**

## 📦 Starter Code

In `src/lights.py` you will find a single class **`ChristmasLights`** that combines:

1. The grid representation.
2. The manipulation logic (turn on, turn off, toggle).
3. A very simple parser for instruction lines.
4. A render method for debugging.

## 🛠️ What you need to do

1. **Run the kata** to check that it works as-is:

   ```bash
   python3 -m christmas_lights_kata.src.controller christmas_lights_kata/instructions.md
   ```

   It should print the number of lights that are on.
2. **Add tests** (for example with `pytest`) to verify that:
   - Each operation affects the correct region.
   - The number of lights on after applying all instructions matches the expected solution.

## ✅ Success Criteria

- The project runs and the kata executes without errors.
- The number of lights on is correct.

## 📚 Useful Resources

- [SOLID Principles – Nabeel's](https://docs.google.com/presentation/d/1uX26evBBGtGahxOkK_N5CLJB3tL9te2iu6kyxGdpUxo/edit?slide=id.gcb9a3abeb_0_23#slide=id.gcb9a3abeb_0_23)
- [Kata‑Log – Christmas Lights Kata](https://kata-log.rocks/christmas-lights-kata)

---
*Have fun refactoring and learning SOLID while lighting up Christmas lights.*
