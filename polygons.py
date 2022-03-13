#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:18:06 2021

@author: bryantorsuprime
"""
from PIL import Image, ImageDraw
import math


class ConvexPolygon:
    """ Clase encargada de representar un Poligono, estar vació, ser un punto,
    una linea, o polygonos más normales. Siempre teniendo en cuenta que es convexo.
    Si se crea una instancia del polygono primero se calcula el convexhull de el,
    si se utilizan las operaciones entre poligones se presupone que son convexos"""

    def __init__(self, P):
        """Constructora de la clase, puede estar vació, ser un punto, linea, polygon
        mas normal. Consta de los atributos: puntos -> sentido antihorario.
        puntosal -> sentido horario. Ambos con el primer y último elemento igual.
        color -> indica el color del pólygono. Perimetro, area y centroide."""
        if len(P) >= 3:
            self.puntos = self.compute_hull(P)
            self.puntosal = self.cal_puntosal(self.puntos)
            self.perimetro = self.cal_perimetro(self.puntos)
            (a, b) = self.cal_area_centroide(self.puntos)
            self.area = a
            self.centroide = b

        elif len(P) == 2:
            self.puntos = self.puntosal = P
            self.perimetro = self.cal_perimetro(P)
            self.area = None
            self.centroide = None
        elif len(P) == 1:
            self.puntos = self.puntosal = P
            self.perimetro = None
            self.area = None
            self.centroide = None
        elif P == []:
            self.puntos = self.puntosal = []
            self.perimetro = None
            self.area = None
            self.centroide = None
        self.color = (255, 0, 0)

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    def get_puntos(self):
        return self.puntos

    def get_puntosal(self):
        return self.puntosal

    def get_perimetro(self):
        return self.perimetro

    def get_area(self):
        return self.area

    def get_centroide(self):
        return self.centroide

    def get_regular(self):
        return self.regular

    def get_color(self):
        return self.color

    def get_edges(self):
        return len(self.puntos) - 1

    def print_polygon(self):

        """Crea una imagen con el polygon de la instancia."""

        self.drawpolygon("imagen.png", [self.puntos], [self.color])

    def calc_vertices(self, P):

        """Dado los puntos de un poligon, calcula su número de vertices.
        El primer y ultimo punto del polygono tienen que ser el mismo"""

        return len(P) - 1

    def get_boundingbox(self, P):

        """Dado los puntos de un polygono(primer y último punto igual), calcula
        su caja contenedora"""

        ymin = 99999
        xmin = 99999
        ymax = -99999
        xmax = -99999
        for i in P:
            if i[0] < xmin:
                xmin = i[0]
            if i[0] > xmax:
                xmax = i[0]
            if i[1] > ymax:
                ymax = i[1]
            if i[1] < ymin:
                ymin = i[1]
        return [(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)]

    def polygon_in(self, P):

        """retorna si el poligono pasado esta dentro de la instacnia de polygono
        creada"""

        for i in P:
            if not self.inside(i, self.puntos):
                return False
        return True

    def intersect_with(self, P):
        """Retorna la intersección del poligono de la instacia y el poligona pasado"""

        return self.intersection(self.puntosal, P)

    def Union_with(self, P):
        """Retorna la intersección del poligona de la instancia y el poligono pasado"""
        sol = self.puntos
        for i in P:
            if i not in sol:
                sol.append(i)
        return self.cal_puntosal(self.compute_hull(sol))

    def union(self, P1, P2):

        """Dado dos poligonos conexos, retorna su union (ConvexHull)
        """
        a = P1
        a.pop()
        sol = a
        for i in range(len(P2)-1):
            if P2[i] not in sol:
                sol.append(P2[i])
        return self.cal_puntosal(self.compute_hull(sol))

    def may_intersect(self, P1, P2, P3, P4):
        """ Función que retorna si dos lineas instersectan o no.
        Los dos primeros parametros son un segmento, y los dos restantes, es el
        segmento restante"""
        def ccw(A, B, C):
            return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])
        return ccw(P1, P3, P4) != ccw(P2, P3, P4) and ccw(P1, P2, P3) != ccw(P1, P2, P4)

    def line_intersection(self, P1, P2, P3, P4):
        """Retorna el punto de intersección de dos segmentos se van a intersectar.
        :param P1: punto del primer segmento.
        :paran P2: punto del primer segmento.
        :param P3: punto del segundo segmento.
        :para P4: punto del segundo segmento.
        """

        xdiff = (P1[0] - P2[0], P3[0] - P4[0])
        ydiff = (P1[1] - P2[1], P3[1] - P4[1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return (-1, -1)
        d = (det(P1, P2), det(P3, P4))
        x = det(d, xdiff)/div
        y = det(d, ydiff)/div
        return (x, y)

    def inter_seg_poly(self, P1, P2, Pol):
        for i in range(1, len(Pol)):
            if self.may_intersect(P1, P2, Pol[i-1], Pol[i]):
                return self.line_intersection(P1, P2, Pol[i-1], Pol[i])

    def intersection(self, P1, P2):
        """Función que retorna la interseción de dos poligonos conexos.
        Guarda los puntos que estan dentro del otro poligona, calcula las intersecciones
        cuando hay un segmento con una parte fuera y la otra dentro del otro poligono.
        Con todos los puntos que forman parte de la intersección retorna su poligono
        conexo."""
        sol = []
        for i in range(1, len(P2)):
            if self.inside(P2[i-1], P1):
                if self.inside(P2[i], P1):
                    if P2[i] not in sol:
                        sol.append(P2[i])
                else:
                    if self.inter_seg_poly(P2[i-1], P2[i], P1) is not None:
                        if self.inter_seg_poly(P2[i-1], P2[i], P1) not in sol:
                            sol.append(self.inter_seg_poly(P2[i-1], P2[i], P1))
            else:
                if self.inside(P2[i], P1):
                    if self.inter_seg_poly(P2[i-1], P2[i], P1) is not None:
                        if self.inter_seg_poly(P2[i-1], P2[i], P1) not in sol:
                            sol.append(self.inter_seg_poly(P2[i-1], P2[i], P1))
                        if P2[i] not in sol:
                            sol.append(P2[i])
        for i in P1:
            if self.inside(i, P2) and i not in sol:
                sol.append(i)
        sol = list(set(sol))
        return self.compute_hull(sol)

    def is_regular(self, P):
        """ Retorna si el poligono enviado como parametro es reguar True/False"""
        aux = math.dist(P[0], P[1])
        for i in range(2, len(P)-1):
            if aux != math.dist(P[i], P[i+1]):
                return False
        return True

    def proces_draw(self, P, pmin, pmax):
        """Redimenciona los puntos de un polygona apartir de los puntos más extremos
        (pmin/pmax), ajusta los puntos para representarse en 400*400pixeles.
        Retorna la nueva posición de los puntos para representarlo como pixeles."""
        sol = []
        for i in P:
            sol.append((i[0]-pmin[0], i[1]-pmin[1]))
        eixx = pmax[0] - pmin[0]
        eixy = pmax[1] - pmin[1]
        res = []
        for (x, y) in sol:
            res.append((x*398/eixx, 398.0 - (y*398/eixy)))
        return res

    def is_left(self, O, P1, P2):
        return (P1[0] - O[0]) * (P2[1] - O[1]) - (P2[0] - O[0]) * (P1[1] - O[1])

    def inside(self, P, Pol):
        """Indica si un punto esta dentro de un poligono, ambos pasados por
        parametro respectivamente"""
        return self.point_insegment(P, Pol) or self.point_inside(P, Pol)

    def polygon_inside(self, P1, P2):
        """Retorna si el poligono P1 se encuentra adentro del poligono P2,
        Para realizar esta función se utilizar otras funciones más senzillas.
        :param P1: polygono de adentro?
        :para P2: poligono de afuera?
        """
        for i in P1:
            if not self.inside(i, P2):
                return False
        return True
    # con puntosal

    def point_insegment(self, P, Pol):
        """Retorna si un punto esta dentro de un segmento de un poligona. Ambas
        variables pasadas por parametro.
        :param P: punto a analizar.
        :param Pol: Poligono que contiene los segmentos."""

        for i in range(len(Pol) - 1):
            if math.dist(Pol[i], Pol[i+1]) == math.dist(Pol[i], P) + math.dist(P, Pol[i + 1]):
                return True
        return False
    # Algortimo que se utiliza con puntosal

    def point_inside(self, P, Pol):
        """Retorna si un punto se encuentra adentro de un poligo, no cuenta todos
        los segmentos. Cuando devuelve False no podemos asegurar que encuentre
        en una de las caras del polygono. Para eso hay otras funciones (point_insegment())
        :param P: punto.
        :param Pol: poligono."""
        wn = 0

        for i in range(len(Pol)-1):     # edge from V[i] to V[i+1]
            if Pol[i][1] <= P[1]:        # start y <= P[1]
                if Pol[i+1][1] > P[1]:     # an upward crossing
                    if self.is_left(Pol[i], Pol[i+1], P) > 0:  # P left of edge
                        wn += 1           # have a valid up intersect
            else:                      # start y > P[1] (no test needed)
                if Pol[i+1][1] <= P[1]:    # a downward crossing
                    if self.is_left(Pol[i], Pol[i+1], P) < 0:  # P right of edge
                        wn -= 1           # have a valid down intersect
        if wn != 0:
            return True
        else:
            return False

    def drawpolygon(self, name, listP, listC):
        """
        Proceso para dibujar una secuencia de poligonos, todos con sus
        respectivos colores. listP -> lista de polygonos. listC, lista con los
        colores de los poligonos en la misma orden.
        :name : nombre de la imagen que se guardara.
        :param listP: lista con los polygonos a dibujar.
        :para listC: lista con los colores de los poligonos.
        """

        P = []
        for i in listP:
            P.append(self.get_boundingbox(i))
        ymin = xmin = 9999999
        ymax = xmax = -9999999
        for i in P:
            if i[0][0] < xmin:
                xmin = i[0][0]
            if i[2][0] > xmax:
                xmax = i[2][0]
            if i[2][1] > ymax:
                ymax = i[2][1]
            if i[0][1] < ymin:
                ymin = i[0][1]

        dista = math.dist((0, ymin), (0, ymax))
        disth = math.dist((xmin, 0), (xmax, 0))

        pmin = (xmin, ymin)
        pmax = (xmax, ymax)

        img = Image.new('RGB', (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        for i in range(len(listP)):
            draw.polygon(self.proces_draw(listP[i], pmin, pmax), fill=(255, 255, 255), outline=listC[i])
        img.save(name)
        img.show()

    def _get_orientation(self, origin, p1, p2):
        '''
        Returns the orientation of the Point p1 with regards to Point p2 using origin.
        Negative if p1 is clockwise of p2.
        :param p1:
        :param p2:
        :return: integer
        '''
        (originx, originy) = origin
        (p1x, p1y) = p1
        (p2x, p2y) = p2
        difference = (((p2x - originx) * (p1y - originy)) - ((p1x - originx) * (p2y - originy)))

        return difference

    def compute_hull(self, P):
        """Retorna el ConvexHull con los puntos pasados por parametro.
        :param P: Lista de puntos representados con tuplas."""
        points = P
        sol = []

        # get leftmost point
        (startx, starty) = points[0]
        min_x = startx
        for (px, py) in points[1:]:
            if px < min_x:
                min_x = px
                (startx, starty) = (px, py)

        point = (startx, starty)
        sol.append(point)

        far_point = None

        while far_point != (startx, starty):

            # get the first point (initial max) to use to compare with others
            p1 = None
            for p in points:
                if p == point:
                    continue
                else:
                    p1 = p
                    break

            far_point = p1

            for p2 in points:
                # ensure we aren't comparing to self or pivot point
                if p2 == point or p2 == p1:
                    continue
                else:
                    direction = self._get_orientation(point, far_point, p2)
                    if direction > 0:
                        far_point = p2

            sol.append(far_point)
            point = far_point
        return sol

    def cal_puntosal(self, P):
        """Pasa un poligono de sentido antihorario a asentido horario.
        :param P : poligono con primer y último punto igual."""
        sol = []
        sol.append(P[0])
        for i in range((len(P)-2), -1, -1):
            sol.append(P[i])
        return sol

    def cal_perimetro(self, P):
        """ Calcula el perimetro del poligono pasado por parametro.
        :param P : poligono con primer y último punto igual."""
        sol = 0.0
        if len(P) > 1:
            for i in range(1, len(P)):
                sol += math.dist(P[i-1], P[i])
            return sol
        else:
            return 0.000

    def cal_area_centroide(self, P):
        """Calcula la area del poligona pasado por parametro.
        :param P: Poligono con primer y último punto igual.
        """
        sola = 0.0
        solc = 0.0
        auxx = 0
        auxy = 0
        for i in range(len(P)-3):
            v1, v2, v3 = 0, i+1, i+2
            aux_area = abs(0.5*(P[v1][0]*(P[v2][1]-P[v3][1]) + P[v2][0]*(P[v3][1]-P[v1][1]) + P[v3][0]*(P[v1][1]-P[v2][1])))
            auxx += ((P[v1][0]+P[v2][0]+P[v3][0])/3)*aux_area
            auxy += ((P[v1][1]+P[v2][1]+P[v3][1])/3)*aux_area
            sola += aux_area
        solc = ((auxx/sola), (auxy/sola))
        return (sola, solc)
