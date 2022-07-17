import os

intput_dir = './files/'
output_dir = './outputs/'

os.makedirs(output_dir, exist_ok=True)
files = os.listdir(intput_dir)

for file in files:
  input = intput_dir + file
  output = output_dir + file[:-4] + '.pdf'
  print('Converting ' + input + ' to ' + output)
  os.system('./caj2pdf convert %s -o %s' % (input, output))
