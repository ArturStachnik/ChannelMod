import csv
import random
from itertools import zip_longest
from random import randint
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle



def main():

    x_list = []
    x1_list = []
    y_list = []
    espesor_list = []
    anchura_list = []
    espesorNEG_list = []
    area_list = []


    #Valores de entrada de la malla

    with open('valores_malla.csv', 'r', newline='', encoding="ISO-8859-1") as csvfile:
      reader = csv.reader(csvfile)
      next(reader, None)

      for row in reader:

        x1 = int((row[0]))
        x2 = int((row[1]))
        y1 = int((row[2]))
        amax = int((row[3]))


    #Pozo1

    with open('pozo1.csv', 'r', newline='', encoding="ISO-8859-1") as csvfile:
      reader = csv.reader(csvfile)
      next(reader, None)

      for row in reader:

        y_list.append(row[0])
        espesor_list.append(row[1])



    y_list = [float(i) for i in y_list]
    espesor_list = [float(i) for i in espesor_list]


    #Sacar los cuerpos arenosos del Pozo 1, para el if de la lista de los cuerpos

    cuerpos_pozo1 = len(y_list)

    #Pozo 2

    with open('pozo2.csv', 'r', newline='', encoding="ISO-8859-1") as csvfile:
      reader = csv.reader(csvfile)
      next(reader, None)

      for row in reader:

        y_list.append(row[0])
        espesor_list.append(row[1])



    y_list = [float(i) for i in y_list]
    espesor_list = [float(i) for i in espesor_list]


    #Distancia entre los pozos

    dist_pozos = x2


    ##############################################


    for i in range(len(y_list)):
      espesor = espesor_list[i]

      anchura = ((1.7845*(espesor**2)) + (11.309*espesor) + 1.1341)
      anchura_list.append(anchura)

      x = randint(0,100)
      a = (-x*anchura)/100

      if i<cuerpos_pozo1:
        x_list.append(a)
      else:
        x_list.append(a+dist_pozos)






    ##############################################


    #######################################################################################################################################

    c = int(input('Introduce el numero de canales: '))



    for i in range(c):

      #Generar número aleatorio
        a = randint(0,100)

       #Calcular coordenada X

        x = random.randint(x1,x2)


      #Calcular Espesor
        espesor = (0.0774*a + 2.9016)* 0.8
        espesor_list.append(espesor)


      #Calcular Anchura
        anchura = ((1.7845*(espesor**2)) + (11.309*espesor) + 1.1341)
        anchura_list.append(anchura)

      #Control de sondeo lateral
        while  x + anchura >=dist_pozos:
          x = random.randint(0,x2)
        x_list.append (x)

      #Calcular coordenada Y
        y = random.randint(-y1,0)
        y_list.append(y)

      #Calcular area del canal
        area = espesor * anchura
        area_list.append(area)

      #Calcular el área total de arena
        atot = sum(area_list)



    if atot > amax:
        print()
        print('-------------------------------------------------------------------------------------------------------')
        print('El Area calculada supera la permitida: ', atot, '>', amax)
        print()
        print('Introduce un Numero MENOR de Canales')
        print()
        print('Reiniciando el Programa...')
        print('--------------------------------------------------------------------------------------------------------')
        print()
        print()
        main()
    elif ((atot/amax)*100) < 75:
        print()
        print('-------------------------------------------------------------------------------------------------------')
        print('El Area calculada es demasiado baja: ', atot, '<<', amax)
        print()
        print('Introduce un Numero MAYOR de Canales')
        print()
        print('Reiniciando el Programa...')
        print('--------------------------------------------------------------------------------------------------------')
        print()
        print()
        main()

    else:
        # Convertir X + Longitud

        for i in range(0, len(x_list)):
            x1_list.append(x_list[i] + anchura_list[i])

        # Generar el valor espesor negativo para representarlo en autocad

        for i in range(0, len(espesor_list)):
            espesorNEG_list.append(-espesor_list[i])

            # Exportar a CSV

            d = [x_list, x1_list, espesorNEG_list, y_list]

            export_data = zip_longest(*d, fillvalue='')

            with open('Hoja1.csv', 'w', encoding="ISO-8859-1", newline='') as f:
                wr = csv.writer(f)
                wr.writerow(('X', 'X1', 'Espesor Comp (-)', 'Y'))
                wr.writerows(export_data)

        ################################################################################################
        ####################################################################################################################

        # Calcular porcentaje de arena relleno por los canales aleatorios

        porcentaje_relleno = 100 - ((atot / amax) * 100)

        # Calcular la media de los canales

        media_anchura = (sum(anchura_list) / atot)*100
        media_espesor_comp = (sum(espesor_list) / atot)*100

        print()
        print()
        print(
            '------------------------------------------------------------------------------------------------------------')
        print('Area calculada: ', atot, '<', amax, 'Area maxima')
        print()
        print('Tienes un ', porcentaje_relleno, '% de espacio sin rellenar')
        print()
        print('El espesor compactado medio de los', c, 'canales generados es de: ', media_espesor_comp, 'm')
        print()
        print('La anchura media de los', c, 'canales generados es de: ', media_anchura, 'm')
        print()
        print('Abre el archivo Hoja1.csv para consultar los datos')
        print(
            '------------------------------------------------------------------------------------------------------------')
        print()
        print()
        print('---> Code written by Artur Stachnik & Martin Garcia (2021) <---')

        #######################################################################################

        # Grafico

        fig, ax = plt.subplots(1)

        plt.xlim(-200, (dist_pozos + 200))
        plt.ylim(0, -y1 - 20)
        ax.invert_yaxis()

        matplotlib.pyplot.title('Canales Modelizados')

        # Lineas de los Pozos

        linea1X = [0, 0]
        linea1Y = [0]
        linea2X = []
        linea2Y = [0]

        linea1Y.append(-y1)
        linea2X.append(x2)
        linea2X.append(x2)
        linea2Y.append(-y1)

        # Longitud de la lista

        longitud = len(espesor_list)

        # Representación

        plt.plot(linea1X, linea1Y, color='r', label='Pozo 1')
        plt.plot(linea2X, linea2Y, color='r', label='Pozo 2')

        for i in range(longitud):
            ax.add_patch(Rectangle((x_list[i], y_list[i]), anchura_list[i], espesorNEG_list[i]))

        plt.legend()
        plt.show()

main()
