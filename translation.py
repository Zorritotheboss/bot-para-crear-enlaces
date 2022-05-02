class Translation(object):
    START_TEXT = """Hola {},
Soy un bot generador de enlaces
Puede cargar archivo | video a telegrama con enlace directo, usando este bot!
/help para mas detalles"""
    FORMAT_SELECTION = "Seleccione el formato deseado: <a href='{}'>tamaño del archivo puede ser aproximadamente</a> \nSi desea establecer una miniatura personalizada, envíe una foto antes o rápidamente después de tocar cualquiera de los botones a continuación.\nPuede usar /deletethumbnail para eliminar la miniatura generada automáticamente"
    SET_CUSTOM_USERNAME_PASSWORD = """Si desea descargar videos premium, proporcione el siguiente formato:
URL | nombre del archivo | usuario | contraseña"""
    DOWNLOAD_START = "📥Descargando..."
    UPLOAD_START = "📤Subiendo..."
    RCHD_TG_API_LIMIT = "Descargando en {} segundos.\nDetectando tamaño de archivo: {}\nLo siento no se pueden subir archivos de mas de 2gb telegram no los soporta."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Gracias por usarme \n\n<b>Agradecimientos a @ventaorosking creador del codigo espero que les guste</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Descargando en {} segundos.\nsubiendo en {} segundos.\n"
    SAVED_CUSTOM_THUMB_NAIL = "Miniatura de video / archivo personalizado guardado.Esta imagen se usará en el video / archivo."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Miniatura borrada correctamente."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Bot creador de enlaces directos soporta algunos tipos de enlace asta hora varios espero q sea de utilidad...el bot estaba en ingles yo lo traduci manualmente para q puedan usarlo sin facilmente cualquier error en la traducion ecrivanme al pv @ventaorosking :
    
   ☞My Name  : Creador de link ALL

   ☞Update  : 0.0.1 beta    

   ☞Language : Python3

   ☞Creador : <a @ventaorosking </a>"""
    HELP_USER = """Siga estos pasos
    
1. Envie link (ejemplo.dominio/Archivo.mp4 | nuevo nombre.mp4).
2. envie nueva miniatura para el video (Opcional).
3. seleciona el boton.
   
   Svideo: dale archivo como video con capturas de pantalla
   DFILE - Give el archivo (video) como archivo con capturas de pantalla
   Video - Dé el archivo como video sin capturas de pantalla
   Archivo: entregue el archivo sin capturas de pantalla

Si el bot no responde pregunteme @ventaorosking"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Responder /generatecustomthumbnail personalizada a un álbum de medios, para generar miniatura personalizada"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """El álbum de medios debe contener solo dos fotos.Vuelva a enviar el álbum de medios y luego vuelva a intentarlo, o envíe solo dos fotos en un álbum"
Puede usar /rename el comando después de recibir el archivo para cambiar el nombre de soporte de miniatura personalizada.
"""
    CANCEL_STR = "Proceso cancelado"
    ZIP_UPLOADED_STR = "Subiendo {} archivos en {} segundos"
    SLOW_URL_DECED = "Lo siento mi creador no me permite descargar archivos muy lentos por q no intenteas esto:==> https://shrtz.me/PtsVnf6 y consigueme un archivo rapido para poder subir sin afectar a los demas usuarios GRACIAS."
