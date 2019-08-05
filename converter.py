# Dependencies
import imageio
import os

# Video clip
clip = os.path.abspath('rise.mp4')

# gifMaker function
def gifMaker(inputPath, targetFormat):
  outputPath = os.path.splitext(inputPath)[0] + targetFormat

  print('Converting ' + inputPath + '\n to ' + outputPath)

  reader = imageio.get_reader(inputPath)
  fps = reader.get_meta_data()['fps']

  writer = imageio.get_writer(outputPath, fps=fps)

  for frames in reader:
    writer.append_data(frames)
    print('Frame ' + frames)

  print('Complete')
  writer.close()

gifMaker(clip, '.gif')
