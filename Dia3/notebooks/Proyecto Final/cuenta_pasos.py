import sys
import math
import time 

from android import Android
droid = Android()
 
mensaje1='Hola, me llamo Contador, y te ayudaré a contar los pasos que das en 8 segundos'
droid.ttsSpeak(mensaje1)

time.sleep(10)

droid.dialogCreateAlert(
    '¿Listo para iniciar?',
    
)
 
droid.dialogSetPositiveButtonText('Si')
droid.dialogSetNegativeButtonText('No')
 
droid.dialogShow()
 
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
	mensaje4='Uno'
	droid.ttsSpeak(mensaje4)
	time.sleep(2)
	mensaje5='Dos'
	droid.ttsSpeak(mensaje5)
	time.sleep(2)
	mensaje6='Tres'
	droid.ttsSpeak(mensaje6)

	tiempo=0
	final=10000
	dt=100
	
	droid.startSensingTimed(2, dt)
    	start = droid.sensorsReadAccelerometer().result
    	while tiempo <= final:
        	
        	datos = droid.sensorsReadAccelerometer().result
        	
        	time.sleep(dt/1000.0)
        	tiempo += dt
        
    	droid.stopSensing()
    	mov = math.fabs((datos[0] + datos[1] + datos[2]) - (start[0] + start[1] + start[2]) / 8000)
	
	
	mensaje8= 'Los pasos que diste son aproximadamente' + str(mov)
	droid.ttsSpeak(mensaje8)