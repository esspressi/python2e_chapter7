def main(): 
  num_videos = int(input('how many videos are in the project? '))
  video_file = open('video_times.txt', 'w')
  print('enter the running times for each video.')
  
  for count in range(1, num_videos + 1):
    run_time = float(input('video #' + str(count) + ': '))
    video_file.write(str(run_time) + '\n')

  video_file.close()
  print('the times have been saved to video_times.txt.')

main()
