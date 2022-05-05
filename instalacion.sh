echo "Bienvenido al asistente de instalacion de Psswrd, vamos a empezar por instalar las librerias de python."
pip install random
pip install choice
echo "Si te da error significa que ya las tienes instaladas o que tu version de python no es la adecuada, recuerda, Python3"
echo "ahora vamos a darle permisos de ejecucion al script, esto SOLO FUNCIONA EN SISTEMAS UNIX-LIKE"
chmod +x psswrd.py
echo "Ahora solo pon en tu consola "./psswrd.py" ya tienes el script listo"
echo "Gracias por instalar Psswrd, ahora vamos a borrar este instalador"
rm instalacion.sh
