# Bot para ver si la embajada de Italia publicó un aviso acerca de la apertura de turnos para la recontrucción de la ciudadania

# Configuración

> Hay que configurar dos cosas. Nuestro email y passwd

En este caso está hecho para gmail, por lo que necesita una configuración especial. Hay que ir a las settings de nuestra cuenta y añadir una contraseña para "aplicaciones no seguras" y eso nos permite logear e interactuar con el correo. De otra forma, no se puede.

Luego, hay que llenar el array con la lista de receptores, ya que cuando encuentre coincidencia va a enviar un correo a todos los que aparezcan ahi.


## Uso
---
Arrancar el entorno virtual estando en el directorio
```
venv/Scripts/activate
```
Instalar dependencias
```python
pip install -r requirements.txt
```
Correr el archivo de forma independiente
```python
python main.py
```
