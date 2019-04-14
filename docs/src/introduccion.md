Introducción
============

En este capítulo se presenta Whitewater, así como los objetivos y las
motivaciones del proyecto.
También se incluye una sección sobre temas relaciones con el proyecto pero
que quedan fuera del ámbito del mismo.
Finalmente se encuentra una breve revisión de la estructure de la memoria.

Descripción
-----------
El campo de Data Science ha visto un incremento exponencial de mercado en los
últimos años, con predicciones vaticinando que hasta un millón de científicos
de datos serán necesarios para 2018 [@onemillion].
Los científicos de datos se encuentran en una situación excepcional, para el
Harvard Business Review es *"the sexiest job of the 21st century"* [@sexy].
Y sin embargo, a pesar de todo esto faltan profesionales que puedan cubrir
estos puestos, la disciplina es inherentemente multidisciplinaria [@venn],
incluyendo conocimiento de estadísticas, matemáticas, programación y
del dominio.
Esto hace que el camino para convertirse en un experto sea largo y complejo,
lo cual desemboca en las llamadas *"cazas de unicornios"* [@unicorn] y [@hunt].

Herramientas como scikit-learn[^sci], Weka o Tableau permiten un acceso
simplificado y de alto nivel a las herramientas necesarias para hacer Data
Science, suavizando la curva de aprendizaje y aumentando la oferta de
profesionales capaces de desarrollar análisis de datos.

Estas herramientas por otro lado requieren programación, se centran en tareas
de limpieza y pre-procesamiento de datos, o proveen una interfaz muy limitada.

Whitewater pretende proporcionar una interfaz visual para scikit-learn, dando
la habilidad de crear complejos procesos de análisis sin escribir una sola
línea de código, dando al usuario una expresividad comparable a la programación
tradicional a la vez que se le ayuda mediante estímulos visuales.

Para poder conseguir esto el proyecto explora las siguientes disciplinas,

* Dataflow Programming. Este paradigma representa programas como grafos
    aciclicos dirigidos, iniciado en los 60 en el MIT y los laboratios Bell
    [@bell].
    Modela los programas como un flujo de datos que pasa por una serie de
    intrucciones en vez de una serie de instrucciones que operan en unos datos
    externos, i.e. los datos fluyen por las instrucciones, no al revés (de ahí
    el nombre de dataflow).
    Esto produce programas paralelos por naturaleza, más cercanos al
    paradigma funcional que al imperativo y a la arquitectura Von
    Neumann [sección 15, @backus1978can].

* Programación Visual. La elección por naturaleza para representar un lenguaje
    de dataflow es una interfaz visual, pudiendo representar el grafo de forma
    clara y precisa [@shu1988visual].
    Mejorar más avanzadas que se pueden implementar gracias a la presentación
    visual incluyen comprobación de tipos en tiempo de escritura, indicador
    de ejecución (señalando que funciones se están ejecutando en el momento),
    etc.

* Experiencia del Usuario. El proyecto se nutre de la experiencia de los
    participantes en los experimentos con el prototipo.
    La interfaz debe indicar el camino para realizar la acción deseada por el
    usuario, dando facilidades para reducir la dificultad de uso.

* Ingeniería del Software. Comunicación con múltiples librerías y frameworks,
    definición de interfaces y organización del código mediante tecnicas de
    programación orientada a objetos y modulos.

* Aprendizaje Automático. Aunque no se implementan los algoritmos en sí, es
    necesario extenso conocimiento de la implementación, ya que hay que
    propocionar un punto de acceso a los hyperparametros y otros tipos de
    configuración que permite sklearn [@scikitlearn].

* Transformación de Datos. Algunas precondiciones sobre los datos han de ser
    asumidas o el usuario ha de ser provisto con las herramientas necesarias
    para realiar las transformaciones necesarias.

* Compiladores. El grafo visual que el usuario dibujo tiene que ser compilado
    a codigo fuente en Python (Transcompilación).

La hipótesis del proyecto es que la representación visual del programa y los
conceptos asociados puede ayudar con el aprendizaje y uso de técnicas de
aprendizaje automático, así como acelerar el trabajo de exploración temprana
típico del análisis de datos.

Esta hipótesis converge con el espíritu de sklearn [@scikitlearn, pp29] en el
hecho de que intenta simplificar el uso y acceso a herramientas de aprendizaje
automático.

Esta estrategia parece haber funcionado para sklearn, convirtiéndose en uno de
los proyectos de aprendizaje automático de código libre más importantes, con
más de 16000 estrellas en
[Github](https://github.com/scikit-learn/scikit-learn), siendo usado por
compañías como Spotify, Facebook o Evernote [@whosklearn].


Motivación
----------
Tras cursar Aprendizaje Automático el año pasado tuve una beca en una empresa
de trading algorítmico como parte del equipo de quants[^quant].

Allí mi principal responsabilidad era reescribir parte de las herramientas
de MATLAB a Python, durante ese proceso observé como algunos de los integrantes
del equipo experimentaban dificultades con el cambio de lenguaje.

Todos los integrantes venían de disciplinas más "puras" (Física, Matemática,
Estadística, Ingeniería Aeroespacial, etc..).

Los expertos de estos campos están acostumbrados a trabajar con lenguajes
de dominio específico como MATLAB, R, Simulink o Julia, y el cambio a un
lenguaje deu so general trae dificultades como la programación orientada a
objectos, complejas estructuras de datos, optimización o tipos más "fuertes".

La situación es aún mas difícil para aquellos que comienzan el aprendizaje,
ya que no solo tienen que lidiar con la barrera de la programación, sino que
además tienen que superar la dificultad de los algoritmos en sí.


Objetivos
---------
Estudio Viabilidad:
:   El proyecto tiene que explorar el espacio de posibles soluciones visuales
    de aprendizaje automático, evaluando distintas estrategias en el front y
    backend de la aplicación.

Diseño y Usabilidad:
:   El sistema ha de ser diseñado acorde a los requerimientos, tanto en
    términos de hacer sencillo el progreso a traves de milestones, como
    produciendo software usable en cada release.
    En todos los casos se debe balancear la complejidad contra la expresividad
    del sistema, proviniendo al usuario deu na herramiento potente sin producir
    una interface compleja.

Evaluación:
:   El sistema será evaluado por participantes que pertenecen a la audiencia
    potencial del software, un formulario debe ser preparando detallando las
    actividades que tendrán que realizar, así como serán tratados sus datos.

Herramienta de aprendizaje:
:   El software debe ayudar con la barrera de programación, facilitando el
    aprendizaje de Machine Learning, ayudando al estudiante a centrarse en las
    conexiones, intuiciones y bases matemáticas de los algoritmos y no en los
    detalles de implementación y peculiaridades del lenguaje.

Acelerar análisis exploratorio:
:   Proveyendo una interfaz visual fácil de usar con la capacidad de arrastrar
    y soltar el usuario puede provar una plétora de algoritmos, ajustando los
    hyperparámetros acorde a la evaluación sin escribir una sola línea de
    código.

Implementación:
:   Hay ciertos **requerimientos no-funcionales** que deben ser cumplidos como
    el proyect ocorriendo en las principales plataformas de escritorio,
    ser distribuido en un ejecutable fácil de instalar para facilitar la
    evaluación, tener un framerate que permita el uso prolongado,
    y hacer uso de multiple hilos de jecución para que la interfaz se mantenga
    usable mientras el grafo se ejecuta.


Que no es el proyecto
---------------------
El proyecto no lidia con los siguientes temas:

* Procesado de datos genéricos. Aunque hay algunas funciones de manipulación de
    datos que son necesarios y/o están incluidas en sklearn, la manipulación
    de datos está fuera del ambito del proyecto, Whitewater trabaja con datos
    ya limpios.
    Esto se hace porque estas funciones son difífiles de presentar de manera
    visual, requiriendo interfaces especiales para ser utiles.
* Visualización de Datos. Ya que esto suele requerir código específico para
    cada caso, y depende de las características concretas de los datos a
    visualizar.
* Programación Visual de uso general. Ya que centrando el sistema en el
    aprendizaje automático permite hacer asunciones sobre los posibles
    programas que se pueden crear, permitiendo características como
    simplificación de tipos (capítulo type) o eliminar la necesidad de
    especificar el orden de ejecución (capítulo literature review).

Estructura de la memoria
------------------------
La estructura de la memoria sigue la cronología del proyecto.
Iniciando con la revisión de la literatura académica y la definición de
workflow (proceso).
En el siguiente capítulo las milestones del proyecto son explicadas, incluyendo
un diagrama de Gantt.
Siguiendo se encuentra el capitulo de análisis de riesgos, con una table de
riesgos así como una review de la metodología de desarrollo.

Hacia la mitad de la memoria en el capítulo de interfaz se expone las razones
que llevan al actual aspecto de la interfaz.
El capítulo de implementación explica el proceso iterativo del proyecto,
centrándose en problemas complejos e interesante que el proyecto ha tenido que
superar.
En la sección de type checking múltiples conceptos teóricos son introducidos,
sobretodo teoría de lenguajes funcionales, compiladores, teoría de tipos
y la representación inmediata.

La última sección antes del post-mortem explica el proceso de evaluación y los
resultados.
En el post-mortem se exponen las conclusiones del proyecto, así como posible
áreas de trabajo futuro.

[^sci]: Scikit-learn es una librería de Python que trae una multitud de
    algoritmos de aprendizaje automático a una API que permite el uso y
    comparación del os mismos en un alto nivel de abstracción.
[^quant]: Analista Cuantitativo, en inglés Quantitative Analyst, abreviado
    Quant.
