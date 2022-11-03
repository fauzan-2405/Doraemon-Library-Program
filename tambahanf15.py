import os
  def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
      arr_data_all_string = [str(var) for var in arr_data]
      string_data += ",".join(arr_data_all_string)
      string_data += "\n"
    return string_data

  print(convert_datas_to_string())


  def saveFile(filename):
      print (open(filename)).write(datas_as_string)
      (open(filename)).close()

      return open(filename)

directory = input("Masukkan nama folder tempat penyimpanan: ")
parent_dir = "C:/"
path = os.path.join(parent_dir, directory)
print(path)
if os.path.isdir(path) == False :
  os.mkdirs(path)
else :
  saveFile()

