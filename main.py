print("Bienvenidos!");
Nombre=input("Ingrese su nombre por Favor:");
Age=int(input("Ingrese su año de nacimiento:"));
resta=int(2022 - Age);
if (resta >= 18):
    sem1=int(input("Ingrese las ventas del primer semestre:"));
    sem2=int(input("ingrese las ventas del segundo semestre:"));
    VentaAnual=float(sem1+sem2);
    if(sem1 > sem2):
        resultado="1er semestre";
    else:
        resultado="2do semestre";

    if (VentaAnual <= 100000):
        premio="un dia libre";
        medalla="Medalla de bronce";
    elif(VentaAnual>=100001 and VentaAnual< 500000):
        premio="un dia libre con un bono de Q250";
        medalla="medalla de plata"
    elif(VentaAnual>=500001 and VentaAnual< 1000000):
        premio="un dia libre con un bono de Q500";
        medalla="Medalla de oro"
    elif(VentaAnual>=1000001):
        premio=" dos dias libres y un bono de Q1000";
        medalla="Medalla de diamante";

    print("Vendedor:",Nombre);
    print("Ventas Anuales:",VentaAnual);
    print("Mejor semestre:",resultado);
    print("Medalla Acreditada:",medalla);
    print("Premio",premio);
else:
   print("Eres menor de edad, lo sentimos");