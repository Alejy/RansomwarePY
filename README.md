# RansomwarePY
Ransomware escrito en python (Academico)<br/>
Este ransomware está escrito únicamente para utilizarlo en entornos académicos.

##¿Qué contiene este programa?<br/>
<ol>
  <li>Un archivo data_ransomware.txt donde podremos modificar 3 parámetros:<br/>
    <OL>	
      <li>El directorio donde se va a ejecutar el ransomware.
      <li>La key con la que se van a cifrar los archivos
      <li>El texto de un banner que se generara en el escritorio indicando que se han cifrado los archivos.
    </OL>
  <li>El archivo .py que contiene el código ejecutable:
    <OL>	
      <li>Instala las librerías
      <li>Recopila los parámetros de data_ransomware.txt
      <li>Recopila el path de cada uno de los archivos.
      <li>Cambia la extensión de los archivos a .txt
      <li>Cifra el contenido de los archivos junto con la key.
      <li>Crea un banner .txt en el escritorio.
    </OL>
  <li>Un directorio Data donde se pueden encontrar los archivos cifrados
  <li>Un directorio DataBackup con los archivos sin cifrar para realizar las pruebas.
</OL>
