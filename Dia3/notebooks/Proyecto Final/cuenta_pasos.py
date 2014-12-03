#importamos las librerias que utiliza la aplicación
import sys
import math
import time
#el siguiente coduigo es escencial para que el dialogCreateAlert funcione
from android import Android
droid = Android()
#Primera llamada de la aplicacion con el interprete de android
mensaje1='Hola, me llamo Contador, y te dire cuanto te mueves en 30 segundos'
droid.ttsSpeak(mensaje1)
# tiempo de espera en segundos para ejecucion del siguiente codigo
time.sleep(5)
#Mensaje de dialogo
droid.dialogCreateAlert('Cuenta pasos', '¿Listo para iniciar?')
droid.dialogSetPositiveButtonText('Si')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()
#dependiendo de la respuesta escogida en el dialogo será el resultado, si es no la opcion escogida se despide el interprete y
#se finaliza la aplicacion, si es si inicia la aplicacion para contar los pasos aproximados en 8 segundos
response = droid.dialogGetResponse().result
droid.dialogDismiss()
if not 'which' in response or response['which'] != 'positive':
mensaje2='Bueno, nos vemos'
droid.ttsSpeak(mensaje2)
sys.exit()
else:
mensaje3='A la cuenta de tres comienza a caminar'
droid.ttsSpeak(mensaje3)
time.sleep(3)
droid.makeToast('Uno')
time.sleep(2)
droid.makeToast('Dos')
time.sleep(2)
droid.makeToast('Tres')
# se inicializa el sensor del acelerometro con 100 milisegundos se toma de lecturas
droid.startSensingTimed(2, 100)
# se almacenan los valores iniciales del acelerometro
start = droid.sensorsReadAccelerometer().result
#se da un tiempo de 30 segundos para tomar los siguientes valores
time.sleep(30)
#se toman los valores finales del acelerometro considerando que ya camino la persona o si no lo hizo
datos = droid.sensorsReadAccelerometer().result
#se termina el sensor del acelerometro
droid.stopSensing()
#se asigna a la variable mov, la diferencia entre los valores finales e iniciales seran los pasos que dio la persona
#la palabra reservada int sirve para tomar el valor entero de una fraccion
#esto: start[1] or 0, siginifica que si el valor almacenado en la posicion es nonetype se reconozca coo valor 0, con esto evitamos error de
#tipos de datos que no concuerden.
mov = (int(datos[0] or 0) + int(datos[1] or 0) + int(datos[2] or 0)) - (int(start[0] or 0) + int(start[1] or 0) + int(start[2] or 0))
#La suma se divide entre el total del tiempo
mov = mov / 30000
# se muestra con el interprete los pasos que dio la persona y acaba la aplicacion
droid.dialogCreateAlert('Cuenta pasos', 'Te moviste ' + str(mov))
droid.dialogSetPositiveButtonText('Aceptar')
droid.dialogShow()
mensaje8= 'Te moviste es ' + str(mov)
droid.ttsSpeak(mensaje8)