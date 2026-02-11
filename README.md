# ÍNDICE
<ul>
<li><a href='#introduccion'>Introducción</a></li>
<li><a href='#manual'>Manual</a></li>
<li><a href='#metodologia'>Metodología</a></li>
<li><a href='#diseno'>Diseño</a></li>



## <div id= 'introduccion'>Introducción</div>

Juan Mateo Álvarez Álvarez  - <a href='https://github.com/Juan071825'>@Juan071825</a> <br/>
Adrián González González    - <a href= 'https://github.com/Adriceka'>@Adriceka</a>

Este proyecto consiste en escribuir un programa que dado un número de DNI obtenga la letra del NIF. 
## <div id='manual'>Manual</div>
#### Instalación

Para ejecutar este proyecto, asegúrate primero de tener **Python** instalado en tu sistema.  
A continuación, descarga el proyecto desde GitHub y accede a la carpeta del repositorio:

git clone https://github.com/Juan071825/PROYECTO-MASTERMIND-1-DAM.git

Acedemos a la carpeta vincuada con cd

#### Entorno virtual
Este proyecto utiliza uv, una herramienta que automatiza la creación del entorno virtual y la instalación de dependencias.
Para su instalación ponemos en la terminal "pip install uv".

Luego ponemos en la terminal "uv sync" para crear un entorno virtual aislado e instalar todas las librerias del proyecto.

## <div id='metodologia'>Metodología</div>

Para llevar a cabo el Kata del DNI decidimos comenzar definiendo claramente la lógica del problema: el cálculo de la letra correspondiente a un número de DNI según el algoritmo oficial.

La metodología empleada tiene un enfoque inspirado en 
<a href='https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas'>TDD</a> 
y consta de tres pasos:

<ol>
<li>
Definimos los requisitos que debía cumplir el módulo principal, como:
<ul>
<li>Validar que el número introducido tenga el formato correcto.</li>
<li>Calcular la letra del DNI utilizando el algoritmo oficial (módulo 23).</li>
<li>Comprobar si un DNI completo (número + letra) es válido.</li>
</ul>
</li>
<br/>

<li>
Se desarrolló la funcionalidad principal del cálculo de la letra del DNI, mientras paralelamente se implementaban casos de prueba para verificar:
<ul>
<li>Casos válidos.</li>
<li>Casos con formato incorrecto.</li>
<li>Casos con letra errónea.</li>
</ul>
</li>
<br/>

<li>
Finalmente, se ejecutaron los casos test para comprobar que cada módulo cumplía los requisitos definidos previamente.
</li>
<br/>
</ol>

---

## <div id='diseno'>Diseño y Principios SOLID</div>

En el desarrollo del Kata del DNI se aplicaron principios SOLID para estructurar el código de manera clara y mantenible:

<ul>

<li>
<strong>SRP (Single Responsibility Principle)</strong>:  
Se separó la lógica en responsabilidades concretas, por ejemplo:
<ul>
<li>Un componente encargado únicamente del cálculo de la letra.</li>
<li>Otro encargado de la validación del formato.</li>
<li>Otro responsable de verificar la validez completa del DNI.</li>
</ul>
De esta forma, cada módulo tiene un único motivo para cambiar.
</li>
<br/>

<li>
<strong>OCP (Open/Closed Principle)</strong>:  
La implementación permite extender funcionalidades (por ejemplo, añadir validación de NIE en el futuro) sin modificar la lógica principal ya implementada.
</li>
<br/>

<li>
<strong>LSP (Liskov Substitution Principle)</strong>:  
En caso de implementar una jerarquía de clases (por ejemplo, una clase base `DocumentoIdentidad` y una clase derivada `DNI`),
