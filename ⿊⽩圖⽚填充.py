image = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]

start = [1, 1]

def Fill(image, row, col):
    
    if row<0 or row >= len(image) or col<0 or col >= len(image[0]) or image[row][col] != 0:
        return image
    
    image[row][col] = 2
    Fill(image, row-1, col)
    Fill(image, row+1, col)
    Fill(image, row, col-1)
    Fill(image, row, col+1)

Fill(image, start[0], start[1])

for i in image:
    print(i)