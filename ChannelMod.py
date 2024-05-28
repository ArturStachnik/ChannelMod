import csv
import random
from itertools import zip_longest
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def read_csv(file_name, encoding="ISO-8859-1"):
    data = []
    try:
        with open(file_name, 'r', newline='', encoding=encoding) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                data.append([float(value) for value in row])
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"Error: {e}")
    return data

def calculate_anchura(espesor):
    return (1.7845 * (espesor ** 2)) + (11.309 * espesor) + 1.1341

def generate_channels(c, x1, x2, y1, dist_pozos, espesor_list, anchura_list, x_list, y_list):
    area_list = []
    for _ in range(c):
        a = random.uniform(0, 100)
        x = random.uniform(x1, x2)
        espesor = (0.0774 * a + 2.9016) * 0.8
        anchura = calculate_anchura(espesor)
        
        while x + anchura >= dist_pozos:
            x = random.uniform(0, x2)
        
        y = random.uniform(-y1, 0)
        area = espesor * anchura
        
        espesor_list.append(espesor)
        anchura_list.append(anchura)
        x_list.append(x)
        y_list.append(y)
        area_list.append(area)
    
    return sum(area_list)

def write_csv(file_name, x_list, x1_list, espesorNEG_list, y_list):
    data = zip_longest(x_list, x1_list, espesorNEG_list, y_list, fillvalue='')
    try:
        with open(file_name, 'w', encoding="ISO-8859-1", newline='') as f:
            wr = csv.writer(f)
            wr.writerow(('X', 'X1', 'Espesor Comp (-)', 'Y'))
            wr.writerows(data)
    except Exception as e:
        print(f"Error: {e}")

def plot_model(dist_pozos, y1, espesor_list, anchura_list, x_list, y_list, optimal_channels):
    fig, ax = plt.subplots(1)
    plt.xlim(-200, dist_pozos + 200)
    plt.ylim(0, -y1 - 20)
    ax.invert_yaxis()
    plt.title(f'Optimal Channel Number: {optimal_channels}')
    
    linea1X = [0, 0]
    linea1Y = [0, -y1]
    linea2X = [dist_pozos, dist_pozos]
    linea2Y = [0, -y1]

    plt.plot(linea1X, linea1Y, color='r', label='Bore 1')
    plt.plot(linea2X, linea2Y, color='r', label='Bore 2')
    
    for i in range(len(espesor_list)):
        ax.add_patch(Rectangle((x_list[i], y_list[i]), anchura_list[i], -espesor_list[i]))
    
    plt.legend(loc='lower right')
    plt.show()

def find_optimal_channels(x1, x2, y1, amax, pozo1_data, pozo2_data):
    # Read pozo1 values
    y_list = [row[0] for row in pozo1_data]
    espesor_list = [row[1] for row in pozo1_data]
    
    # Read pozo2 values
    y_list += [row[0] for row in pozo2_data]
    espesor_list += [row[1] for row in pozo2_data]
    
    # Calculate anchura
    anchura_list = [calculate_anchura(espesor) for espesor in espesor_list]
    
    # Calculate x_list
    dist_pozos = x2
    x_list = []
    for i, espesor in enumerate(espesor_list):
        anchura = anchura_list[i]
        x = random.uniform(0, 100)
        a = (-x * anchura) / 100
        if i < len(pozo1_data):
            x_list.append(a)
        else:
            x_list.append(a + dist_pozos)
    
    min_channels = 1
    max_channels = 1000  
    target_coverage = 0.95
    optimal_channels = -1
    
    while min_channels <= max_channels:
        mid_channels = (min_channels + max_channels) // 2
        area = generate_channels(mid_channels, x1, x2, y1, dist_pozos, espesor_list, anchura_list, x_list, y_list)
        coverage = area / amax
        if coverage >= target_coverage:
            optimal_channels = mid_channels
            max_channels = mid_channels - 1
        else:
            min_channels = mid_channels + 1
    
    return optimal_channels

def main(num_executions):
    for _ in range(num_executions):

      malla_values = read_csv('valores_malla.csv')
      if not malla_values:
          return
      x1, x2, y1, amax = [int(value) for value in malla_values[0]]

      pozo1_data = read_csv('pozo1.csv')
      if not pozo1_data:
          return

      pozo2_data = read_csv('pozo2.csv')
      if not pozo2_data:
          return
      
      optimal_channels = find_optimal_channels(x1, x2, y1, amax, pozo1_data, pozo2_data)
      print(f'\nIteration Number: {_+1}\n')
      

      y_list = [row[0] for row in pozo1_data] + [row[0] for row in pozo2_data]
      espesor_list = [row[1] for row in pozo1_data] + [row[1] for row in pozo2_data]
      anchura_list = [calculate_anchura(espesor) for espesor in espesor_list]
      dist_pozos = x2
      x_list = []
      for i, espesor in enumerate(espesor_list):
          anchura = anchura_list[i]
          x = random.uniform(0, 100)
          a = (-x * anchura) / 100
          if i < len(pozo1_data):
              x_list.append(a)
          else:
              x_list.append(a + dist_pozos)
      

      generate_channels(optimal_channels, x1, x2, y1, dist_pozos, espesor_list, anchura_list, x_list, y_list)
      plot_model(dist_pozos, y1, espesor_list, anchura_list, x_list, y_list, optimal_channels)

if __name__ == "__main__":
    num_executions = 1  # Change the iteration number
    main(num_executions)
    print('\n---> Original Code written by Artur Stachnik & Martin Garcia (2021) Last update 05/2024 <---')
