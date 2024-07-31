# york
Paquete de pruebas para el modelamiento y control del robot YORK.   
   
El paquete contiene un modelo URDF del robot YORK y un lanzador que permite su visualización en rviz2.   
<image src="/images/york_rviz.png" alt="Visualización del modelo en rviz2">   
## Actividades propuestas
Como una autoevaluación de tus conocimientos en la construcción de paquetes en ROS2, intenta realizar las siguientes mejoras que complementarán el modelo actual.
### 1. Mejora el modelo
1.1. Los límites de colisión de cada link, actualmente utilizan archivos mesh con extensión STL, que resultan muy "pesados" para los cálculos de colisión. En el archivo URDF, cambia la geometría de colisión de las ruedas por cilindros de radio 0.0485 metros y longitud 0.04 metros, para hacer más simples los cálculos de colisión en el simulador.   
1.2. Agrega algún elemento visual de tu elección sobre el robot. Puede ser una forma simple que represente algún sensor o, mejor aún, un modelo STL del sensor (puedes encontrar muchos en la web). Considera que las dimensiones de archivo STL deben estar en metros.   
1.3. Cambia el sentido de giro de las ruedas del lado izquierdo. Actualmente, los angulos positivos en las articulaciones del lado izquierdo (flw_joint y blw_joint) mueven la rueda hacia atrás. Haz que se muevan en sentido contrario, cambiando la orientación del eje z en estas articulaciones.   

### 2. Agrega un controlador
2.1. Tomando como ejemplo el controlador construido en el paquete "my_robot" (https://github.com/cmoralesd/my_robot/tree/finished), haz un controlador para el robot YORK, que permita moder las ruedas a partir de comandos de velocidad en el tópico */cmd_vel*. Considera que ahora el tópico */joint_states* debe publicar las coordenadas de los joint de YORK, y que el cálculo de las velocidades angulares de las articulaciones debe hacerse mediante las siguientes expresiones:   
   
```
    r1, r2 = 0.0384, 0.01 # radio mayor y menor de las ruedas mecanum
    a, b = 0.125, 0.105 # distancias entre ruedas
    blw_joint_velocity = (-wr*(a*r2+b*(r1+r2))+r2*vy+vx*(r1+r2))/((r1)**2+2*r1*r2+2*r2**2)
    brw_joint_velocity = (wr*(a*r2+b*(r1+r2))-r2*vy+vx*(r1+r2))/((r1)**2+2*r1*r2+2*r2**2)
    frw_joint_velocity = (wr*(a*r2+b*(r1+r2))+r2*vy+vx*(r1+r2))/((r1)**2+2*r1*r2+2*r2**2)
    flw_joint_velocity = (-wr*(a*r2+b*(r1+r2))-r2*vy+vx*(r1+r2))/((r1)**2+2*r1*r2+2*r2**2)
```
2.2. Una vez que tengas el controlador. Agrega el nodo "joy_velocity_publisher" para mover tu robot mediante un joystick.   
   
¡Éxito en la construcción de tu modelo mejorado del robot YORK!   

