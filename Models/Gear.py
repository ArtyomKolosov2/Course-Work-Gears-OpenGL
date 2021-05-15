class Gear:
    outputAngle = 0
    dx = 0
    dy = 0
    dz = 0

    def __init__(self, reflectance, innerRadius, outerRadius, thickness, toothSize, toothCount):
        self.reflectance = reflectance
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.thickness = thickness
        self.toothSize = toothSize
        self.toothCount = toothCount
        self.points = []