from skimage import feature


class HOG:

    def __init__(self, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3), transform=False):
        """
        :param orientations: defines how many gradient orientations will be in each histogram
        :param pixels_per_cell: defines the number of pixels that will fall into each cell
        :param cells_per_block: normalize each of the histograms according to the number of cells that fall into each block
        :param transform: apply power law compression which can lead to better accuracy of the descriptor.
        """
        self.orienations = orientations
        self.pixels_per_cell = pixels_per_cell
        self.cells_per_block = cells_per_block
        self.transform = transform

    def describe(self, image):
        hist = feature.hog(image,
                           orientations=self.orienations,
                           pixels_per_cell=self.pixels_per_cell,
                           cells_per_block=self.cells_per_block,
                           transform_sqrt=self.transform)
        return hist
