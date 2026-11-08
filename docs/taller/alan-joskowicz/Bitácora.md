# 19-10-2026 Prueba de la aplicación - 2 horas
Se clona el repositorio original (https://github.com/krahd/BatLLM.git) para probar su funcionamiento.
Se sigue el README del proyecto para su instalación y se verifica que sea exitosa.
Se prueban algunos prompts para obtener una respuesta sin mucho éxito.
Se detecta un problema con la configuración de la resolución de la aplicación en Windows. Solución temporal:
- .\.venv_BatLLM\Scripts\Activate.ps1
- $env:KIVY_METRICS_DENSITY = "0.9"

# 20-10-2026 Primera reunión - 1 hora
Se tiene una primera reunión con el equipo para presentar el proyecto y el objetivo del taller.
Se propone que para la siguiente reunión le demos un vistazo al repositorio y probemos usar la aplicación

# 21-10-2026 Lectura del repositorio - 2 horas
Se hace un seguimiento del flujo del código desde el repositorio original.
Se determina que seguir el flujo end-to-end es inviable. Para futuras sesiones se seguirá el flujo de secciones acotadas del proyecto.

# 23-10-2026 Configuración del modelo - 4 horas
El modelo seleccionado queda siempre mal configurado a partir del primer cambio.
Se detecta que el problema es un mal parseo de la respuesta de la librería modelito al cambiar el modelo.
Se propone una solución y se abre un PR para incorporarla al proyecto original: https://github.com/krahd/BatLLM/pull/60#issue-6005426222
Se detecta un test que falla al cambiar a cualquier modelo distinto al original: https://github.com/krahd/BatLLM/issues/59#issue-6005417793

# 3-11-2026 Segunda reunión - 1 hora
Se tiene una segunda reunión con el equipo en la que nos presentamos más personalmente.
Se propone un flujo de trabajo en GitHub más concreto: fork de un fork del proyecto original.
Se propone que cada uno (o en subgrupos) dediquemos tiempo a entender a una sección del flujo del código.
Se propone que busquemos puntos de mejora: tanto solucionar erroes como expandir el proyecto.

# 8-11-2026 Primer bitácota - 4 hora
Se crea un fork desde https://github.com/Taller-BatLLM/BatLLM.git y se clona localmente.
Se redacta la bitácota hasta esta entrada.
Se crea parser_analysis.py con el objetivo de ejecutar un test sobre si conviene implementar un parser que fuerce al modelo a responder con un formato JSON dado. Tdoavía en proceso.