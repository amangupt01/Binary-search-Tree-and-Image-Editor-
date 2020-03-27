# name: File path of the pgm image file
# Output is a 2D list of integers
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
				line += '\n'
			fout.write(line)

########## Function Calls ##########
#x = readpgm('test.pgm')			# test.pgm is the image present in the same working directory
#writepgm(x, 'test_o.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
###################################


fileToCompute = 'test.pgm'

def get_average_image(imageFileName):
	x = readpgm(imageFileName)
	height = len(x)
	width = len(x[0])
	# print(height)
	# print(width)
	# print(len(row))
	out_x = [[0 for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			if(i==0 or j==0 or i==(height-1) or j==(width-1)):
				out_x[i][j] = x[i][j]
			else:
				out_x[i][j] = (x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i][j-1]+x[i][j]+x[i][j+1]+x[i+1][j-1]+ x[i+1][j]+x[i+1][j+1])/9
				out_x[i][j] = int( out_x[i][j])

	# print(len(out_x))
	# print(len(out_x[0]))
	writepgm(out_x, 'average_'+imageFileName)


get_average_image(fileToCompute)



def get_edge_image(imageFileName):
	import math
	image = readpgm(imageFileName)
	# print('started making edge image')

	height = len(image)
	width = len(image[0])
    #now we have to wrap this image with 0s at all boundary
	for rowIndex in range(height):
		image[rowIndex].insert(0, 0)
		image[rowIndex].append(0)

	zeroRow = [0 for i in range(width+2)]
	image.insert(0,zeroRow)
	image.append(zeroRow)

	hdif = [[0 for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			# original i is i+1 and j is j+1
			hdif[i][j] = (image[i-1+1][j-1+1]-image[i-1+1][j+1+1]) + 2*(image[i+1][j-1+1]-image[i+1][j+1+1]) + (image[i+1+1][j-1+1]-image[i+1+1][j+1+1])

	vdif = [[0 for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			vdif[i][j] = (image[i-1+1][j-1+1]-image[i+1+1][j-1+1]) + 2*(image[i-1+1][j+1]-image[i+1+1][j+1]) + (image[i-1+1][j+1+1]-image[i+1+1][j+1+1])

	grad = [[0 for i in range(width)] for j in range(height)]

	maxGrad = 0
	for i in range(height):
		for j in range(width):
			grad[i][j] = int(math.sqrt((hdif[i][j]*hdif[i][j])+(vdif[i][j]*vdif[i][j])))
			maxGrad = max(maxGrad,grad[i][j])			
	
	# Scaling
	for i in range(height):
		for j in range(width):
			grad[i][j] = round(grad[i][j]*255/maxGrad)

	writepgm(grad, 'edge_'+imageFileName)


get_edge_image(fileToCompute)




def get_min_path_image(imageFileName):
	import math
	image = readpgm(imageFileName)
	# print('started making edge image')
	height = len(image)
	width = len(image[0])
	for rowIndex in range(height):
		image[rowIndex].insert(0, 0)
		image[rowIndex].append(0)
	zeroRow = [0 for i in range(width+2)]
	image.insert(0,zeroRow)
	image.append(zeroRow)
	hdif = [[0 for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			hdif[i][j] = (image[i-1+1][j-1+1]-image[i-1+1][j+1+1]) + 2*(image[i+1][j-1+1]-image[i+1][j+1+1]) + (image[i+1+1][j-1+1]-image[i+1+1][j+1+1])

	vdif = [[0 for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			vdif[i][j] = (image[i-1+1][j-1+1]-image[i+1+1][j-1+1]) + 2*(image[i-1+1][j+1]-image[i+1+1][j+1]) + (image[i-1+1][j+1+1]-image[i+1+1][j+1+1])

	grad = [[0 for i in range(width)] for j in range(height)]
	maxGrad = 0
	for i in range(height):
		for j in range(width):
			grad[i][j] = int(math.sqrt((hdif[i][j]*hdif[i][j])+(vdif[i][j]*vdif[i][j])))
			maxGrad = max(maxGrad,grad[i][j])			
	
	# Scaling
	for i in range(height):
		for j in range(width):
			grad[i][j] = round(grad[i][j]*255/maxGrad)

	########################Grad till above############################

	cumulativeImage = [[[0,[]] for i in range(width)] for j in range(height)]

	# make 1st row
	for i in range(width):
		cumulativeImage[0][i][0] = grad[0][i]

	for i in range(1,height):
		for j in range(width):
	
			if(j==0):
				above_mid = cumulativeImage[i-1][j][0]
				above_right = cumulativeImage[i-1][j+1][0] 
				min_1 = min(above_mid,above_right)
				cumulativeImage[i][j][0] = grad[i][j]+ min_1
				if above_mid == min_1 :
					cumulativeImage[i][j][1].append(0)
				if above_right == min_1 :
					cumulativeImage[i][j][1].append(1)

			elif(j==(width-1)):
				above_mid = cumulativeImage[i-1][j][0]
				above_left = cumulativeImage[i-1][j-1][0]
				min_2 = min(above_mid,above_left)
				cumulativeImage[i][j][0] = grad[i][j]+ min_2
				if above_mid == min_2 :
					cumulativeImage[i][j][1].append(0)
				if above_left == min_2 :
					cumulativeImage[i][j][1].append(-1)
			else:
				above_mid = cumulativeImage[i-1][j][0]
				above_left = cumulativeImage[i-1][j-1][0]
				above_right = cumulativeImage[i-1][j+1][0]
				min_3 = min(above_mid,above_left,above_right)
				cumulativeImage[i][j][0] = grad[i][j]+ min_3
				if above_mid == min_3 :
					cumulativeImage[i][j][1].append(0)
				if above_left == min_3 :
					cumulativeImage[i][j][1].append(-1)
				if above_right == min_3 :
					cumulativeImage[i][j][1].append(1)
	cells_with_min_energy_in_last_row = []

	minCumulativeEnergy = 255*(height)+1
	for j in range(width):
		if cumulativeImage[height-1][j][0]<minCumulativeEnergy :
			minCumulativeEnergy = cumulativeImage[height-1][j][0]
			cells_with_min_energy_in_last_row = [[height-1,j]]
		elif cumulativeImage[height-1][j][0]==minCumulativeEnergy :
			cells_with_min_energy_in_last_row.append([height-1,j])

	print(cells_with_min_energy_in_last_row)
	print('the minimum culmulative energy from top to bottom is',minCumulativeEnergy)
	my_out_image = readpgm(imageFileName)
	set_of_cell = set()
	#to avoid calling the same cell called multiple times
	def highlight_the_min_path(cell):
		set_of_cell.add(tuple(cell))
		if cell[0] == 0 :
			my_out_image[0][cell[1]] = 255
		else :
			my_out_image[cell[0]][cell[1]] = 255
			for i in cumulativeImage[cell[0]][cell[1]][1]:
				if tuple([cell[0]-1,cell[1]+i])  not in set_of_cell :
					highlight_the_min_path([cell[0]-1,cell[1]+i])
	for i in range(len(cells_with_min_energy_in_last_row)):
		highlight_the_min_path(cells_with_min_energy_in_last_row[i])
	writepgm(my_out_image, 'min_path_'+imageFileName)
get_min_path_image(fileToCompute)


















