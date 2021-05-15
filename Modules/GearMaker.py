import math


class GearMaker:

    @staticmethod
    def makeGear(gl, reflectance, innerRadius, outerRadius, thickness, toothSize, toothCount):
        result_list = gl.glGenLists(1)
        gl.glNewList(result_list, gl.GL_COMPILE)
        gl.glMaterialfv(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE,
                        reflectance)

        r0 = innerRadius
        r1 = outerRadius - toothSize / 2.0
        r2 = outerRadius + toothSize / 2.0
        delta = (2.0 * math.pi / toothCount) / 4.0
        z = thickness / 2.0

        gl.glShadeModel(gl.GL_FLAT)

        for i in range(2):
            if i == 0:
                sign = +1.0
            else:
                sign = -1.0

            gl.glNormal3d(0.0, 0.0, sign)

            gl.glBegin(gl.GL_QUAD_STRIP)

            for j in range(toothCount + 1):
                angle = 2.0 * math.pi * j / toothCount
                gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
                gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
                gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), sign * z)
                gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

            gl.glEnd()

            gl.glBegin(gl.GL_QUADS)

            for j in range(toothCount):
                angle = 2.0 * math.pi * j / toothCount
                gl.glVertex3d(r1 * math.cos(angle), r1 * math.sin(angle), sign * z)
                gl.glVertex3d(r2 * math.cos(angle + delta), r2 * math.sin(angle + delta), sign * z)
                gl.glVertex3d(r2 * math.cos(angle + 2 * delta), r2 * math.sin(angle + 2 * delta), sign * z)
                gl.glVertex3d(r1 * math.cos(angle + 3 * delta), r1 * math.sin(angle + 3 * delta), sign * z)

            gl.glEnd()

        gl.glBegin(gl.GL_QUAD_STRIP)

        for i in range(toothCount):
            for j in range(2):
                angle = 2.0 * math.pi * (i + (j / 2.0)) / toothCount
                s1 = r1
                s2 = r2

                if j == 1:
                    s1, s2 = s2, s1

                gl.glNormal3d(math.cos(angle), math.sin(angle), 0.0)
                gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), +z)
                gl.glVertex3d(s1 * math.cos(angle), s1 * math.sin(angle), -z)

                gl.glNormal3d(s2 * math.sin(angle + delta) - s1 * math.sin(angle),
                              s1 * math.cos(angle) - s2 * math.cos(angle + delta), 0.0)
                gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), +z)
                gl.glVertex3d(s2 * math.cos(angle + delta), s2 * math.sin(angle + delta), -z)

        gl.glVertex3d(r1, 0.0, +z)
        gl.glVertex3d(r1, 0.0, -z)
        gl.glEnd()

        gl.glShadeModel(gl.GL_SMOOTH)

        gl.glBegin(gl.GL_QUAD_STRIP)

        for i in range(toothCount + 1):
            angle = i * 2.0 * math.pi / toothCount
            gl.glNormal3d(-math.cos(angle), -math.sin(angle), 0.0)
            gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), +z)
            gl.glVertex3d(r0 * math.cos(angle), r0 * math.sin(angle), -z)

        gl.glEnd()

        gl.glEndList()

        return result_list
