## Kata Letter – Christmas Lights Kata

**Objetivo**: Después de ejecutar una serie de operaciones sobre una cuadrícula de luces (por defecto 1000 × 1000), determinar cuántas luces quedan encendidas.

### Operaciones disponibles

- `turn on x1,y1 through x2,y2` – enciende todas las luces dentro del rectángulo definido por las coordenadas.
- `turn off x1,y1 through x2,y2` – apaga todas las luces dentro del rectángulo.
- `toggle x1,y1 through x2,y2` – invierte el estado de cada luz dentro del rectángulo (encendida → apagada, apagada → encendida).

### Instrucciones del Kata

```
turn on 887,9 through 959,629
turn on 454,398 through 844,448
turn off 539,243 through 559,965
turn off 370,819 through 676,868
turn off 145,40 through 370,997
turn off 301,3 through 808,453
turn on 351,678 through 951,908
toggle 720,196 through 897,994
toggle 831,394 through 904,860
```

**Pregunta**: Después de aplicar todas las instrucciones, ¿cuántas luces están encendidas?

### Ejemplo de Entrada/Salida (para pruebas)

- Entrada: la lista de instrucciones anterior.
- Salida esperada: `?` (el número exacto que obtendrás al ejecutar el código).

---
*Esta letra proviene de la página oficial del kata en Kata‑Log.*
