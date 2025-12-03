# Christmas Lights Kata

## 🎄 Descripción del ejercicio

Esta kata consiste en una cuadrícula de luces (por defecto **1000 × 1000**) que pueden estar **encendidas** o **apagadas**.  A partir de un fichero de instrucciones (ver `instructions.md`) se deben aplicar operaciones de:

- `turn on x1,y1 through x2,y2`
- `turn off x1,y1 through x2,y2`
- `toggle x1,y1 through x2,y2`

Al final del proceso hay que responder **¿cuántas luces quedan encendidas?**.

## 📦 Código base

En `src/lights.py` encontrarás una única clase **`ChristmasLights`** que combina:

1. La representación de la cuadrícula.
2. La lógica de manipulación (encender, apagar, alternar).
3. Un parser muy simple de las líneas de instrucciones.
4. Un método de renderizado para depuración.

## 🛠️ Qué debes hacer

1. **Ejecuta la kata** para comprobar que funciona tal cual está:

   ```bash
   python3 -m christmas_lights_kata.src.controller christmas_lights_kata/instructions.md
   ```

   Debería imprimirse el número de luces encendidas.
   - **SRP** – Separa la lógica de la cuadrícula, el parser y la presentación en clases diferentes.
   - **OCP** – Introduce una abstracción `BaseLight` y permite añadir nuevos tipos de luz sin modificar la cuadrícula.
   - **LSP** – Asegúrate de que cualquier sub‑clase de `BaseLight` pueda usarse en la cuadrícula.
   - **ISP** – Crea interfaces pequeñas (`Switchable`, `InstructionParser`, `Renderable`).
   - **DIP** – Haz que el controlador dependa de abstracciones y no de implementaciones concretas.
2. **Añade pruebas** (por ejemplo con `pytest`) que verifiquen que:
   - Cada operación afecta a la región correcta.
   - El número de luces encendidas después de aplicar todas las instrucciones coincide con la solución esperada.
3. **Documenta** cualquier cambio importante en este `README` (por ejemplo, nuevos archivos o clases creadas).

## ✅ Criterios de éxito

- El proyecto compila y la kata se ejecuta sin errores.
- El número de luces encendidas es correcto.

## 📚 Recursos útiles

- [Principios SOLID – Nabeel's](https://docs.google.com/presentation/d/1uX26evBBGtGahxOkK_N5CLJB3tL9te2iu6kyxGdpUxo/edit?slide=id.gcb9a3abeb_0_23#slide=id.gcb9a3abeb_0_23)
- [Kata‑Log – Christmas Lights Kata](https://kata-log.rocks/christmas-lights-kata)

---
*Diviértete refactorizando y aprendiendo SOLID mientras enciendes luces navideñas.*
