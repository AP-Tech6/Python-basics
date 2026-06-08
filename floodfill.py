class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        oldcolor = image[sr][sc]

        # if already same color
        if oldcolor == color:
            return image

        def floodfill(i, j):

            # boundary condition
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return

            # if color not matching
            if image[i][j] != oldcolor:
                return

            # change color
            image[i][j] = color

            # down
            floodfill(i+1, j)

            # up
            floodfill(i-1, j)

            # right
            floodfill(i, j+1)

            # left
            floodfill(i, j-1)

        floodfill(sr, sc)

        return image


        #color all paths exceptdiagonal and also same color no need to color