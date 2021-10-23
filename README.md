
# CoverMyFuckingPasswd

Pequeño script para convertir tus contraseñas fáciles en hashes y copiarlas de manera "segura" en público :P 

No sé cuánto les servirá, pero estaba aburrido y quise hacer esto. 

## Instalar dependencias

```bash
pip install pyperclip
```

### Error al usar el módulo en Linux

#### Distribuciones basadas en Debian

```bash
apt-get install xsel
```
o
```bash
apt-get install xclip
```

#### Distribuciones basadas en Arch

```bash
pacman -S xclip
```
o
```bash
pacman -S xsel
```

## ¿Cómo usarlo?

```bash
python cmfp.py 
```
También tiene las opciones:
```bash
python cmfp.py --hash sha512 # Algoritmo a convertir
```
```bash
python cmfp.py --timeout 3   # Tiempo restante antes de eliminar el password del portapapeles
``` 
**Nota:** el *hash* por defecto es md5 y el *tiempo* es de 5

## Llevarlo contigo

Para poder usarlo donde quieras, deberás convertirlo en ejecutable, puedes usar pyinstaller o similar.
