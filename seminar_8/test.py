
with open ('test.txt', 'r') as f:
  old_data = f.read()

new_data = old_data.replace('что_меняем', 'на_что_меняем')

with open ('test.txt', 'w') as f:
  f.write(new_data)