import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("load")
Load=parser.parse_args()

def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(len(arr_cpy)):
    if (i == 3 or i == 5):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

def split(sentence):
    key = []
    tmp=''
    for i in sentence:
        if i == ";" or i == "," :
            key.append(tmp)
            tmp = ""
        else:
            tmp += i
    key.append(tmp)
    return key

def convert_line_to_data(line):
    raw_array_of_data = split(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def load(file):
    f = open(file,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    matrix = []
    raw_header = lines.pop(0)
    header = [convert_line_to_data(raw_header)]
    for line in lines:
        array_of_data = convert_line_to_data(line)
        if file == "consumable.csv" or file == "gadget.csv":
            real_values = convert_array_data_to_real_values(array_of_data)
            matrix.append(real_values)
        else:
            real_values = array_of_data
            matrix.append(real_values)
    matrix = header + matrix
    return(matrix)