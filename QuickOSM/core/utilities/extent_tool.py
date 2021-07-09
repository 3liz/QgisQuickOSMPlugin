"""A tool that enable to select an extent in the canvas."""
import logging

from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsPointXY,
    QgsProject,
    QgsRectangle,
    QgsWkbTypes,
)
from qgis.gui import QgsMapTool, QgsRubberBand
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtGui import QColor

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

LOGGER = logging.getLogger('QuickOSM')


class SelectExtentTool(QgsMapTool):
    """Select an extent in canvas."""

    ExtentSelected = pyqtSignal(QgsRectangle)

    def __init__(self, canvas):
        """Constructor"""
        QgsMapTool.__init__(self, canvas)

        self.canvas = canvas
        self.rubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
        color = QColor(30, 230, 30, 65)
        self.rubberBand.setColor(color)
        self.rubberBand.setWidth(1)
        self.start_point = self.end_point = None
        self.is_drawing = False

        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)

    def canvasPressEvent(self, event):
        """Set up the begin of the drawing"""
        self.start_point = self.toMapCoordinates(event.pos())
        self.end_point = self.start_point
        self.is_drawing = True
        self.showExtent(self.start_point, self.end_point)

    def canvasReleaseEvent(self, event):
        """Set up the end of the drawing"""
        _ = event
        self.is_drawing = False
        self.rubberBand.hide()
        self.transformCoordinates()

        extent = QgsRectangle(self.start_point, self.end_point)

        self.ExtentSelected.emit(extent)

    def canvasMoveEvent(self, event):
        """Update the drawing"""
        if not self.is_drawing:
            return

        self.end_point = self.toMapCoordinates(event.pos())
        self.showExtent(self.start_point, self.end_point)

    def showExtent(self, start_point, end_point):
        """Draw and display a extent on the canvas"""
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
        if start_point.x() == end_point.x() or start_point.y() == end_point.y():
            return

        point1 = QgsPointXY(start_point.x(), start_point.y())
        point2 = QgsPointXY(start_point.x(), end_point.y())
        point3 = QgsPointXY(end_point.x(), end_point.y())
        point4 = QgsPointXY(end_point.x(), start_point.y())

        self.rubberBand.addPoint(point1, False)
        self.rubberBand.addPoint(point2, False)
        self.rubberBand.addPoint(point3, False)
        self.rubberBand.addPoint(point4, True)  # true to update canvas
        self.rubberBand.show()

    def transformCoordinates(self):
        """Transform the coordinates in 4326."""
        if self.start_point is None or self.end_point is None:
            return None
        if self.start_point.x() == self.end_point.x() or self.start_point.y() == self.end_point.y():
            return None

        # Defining the crs from src and destiny
        epsg = self.canvas.mapSettings().destinationCrs().authid()
        crs_src = QgsCoordinateReferenceSystem(epsg)
        crs_dest = QgsCoordinateReferenceSystem('EPSG:4326')

        # Creating a transformer
        transformer = QgsCoordinateTransform(crs_src, crs_dest, QgsProject.instance())

        # Transforming the points
        self.start_point = transformer.transform(self.start_point)
        self.end_point = transformer.transform(self.end_point)


class ShowExtent(QgsMapTool):
    """Show an extent in the canvas"""

    ShowEnded = pyqtSignal()

    def __init__(self, canvas):
        """Constructor"""
        QgsMapTool.__init__(self, canvas)

        self.canvas = canvas
        self.rubberBand = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
        color = QColor(30, 230, 30, 65)
        self.rubberBand.setColor(color)
        self.rubberBand.setWidth(1)

        self.start_point = self.end_point = None

    def canvasPressEvent(self, event):
        """Change the outcome of the click event to end  the ongoing process."""
        _ = event
        self.rubberBand.hide()
        self.ShowEnded.emit()

    def show_extent(self, extent: QgsRectangle):
        """Display the extent on the canvas"""
        self.start_point = QgsPointXY(extent.xMinimum(), extent.yMinimum())
        self.end_point = QgsPointXY(extent.xMaximum(), extent.yMaximum())
        self.transform_coordinates()

        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)

        point1 = QgsPointXY(self.start_point.x(), self.start_point.y())
        point2 = QgsPointXY(self.start_point.x(), self.end_point.y())
        point3 = QgsPointXY(self.end_point.x(), self.end_point.y())
        point4 = QgsPointXY(self.end_point.x(), self.start_point.y())

        self.rubberBand.addPoint(point1, False)
        self.rubberBand.addPoint(point2, False)
        self.rubberBand.addPoint(point3, False)
        self.rubberBand.addPoint(point4, True)
        self.rubberBand.show()

        rect = QgsRectangle(self.start_point, self.end_point)
        self.canvas.setExtent(rect)

    def transform_coordinates(self):
        """Transform the coordinates in 4326."""
        if self.start_point is None or self.end_point is None:
            return None
        if self.start_point.x() == self.end_point.x() or self.start_point.y() == self.end_point.y():
            return None

        # Defining the crs from src and destiny
        epsg = self.canvas.mapSettings().destinationCrs().authid()
        crs_dest = QgsCoordinateReferenceSystem(epsg)
        crs_src = QgsCoordinateReferenceSystem('EPSG:4326')

        # Creating a transformer
        transformer = QgsCoordinateTransform(crs_src, crs_dest, QgsProject.instance())

        # Transforming the points
        self.start_point = transformer.transform(self.start_point)
        self.end_point = transformer.transform(self.end_point)
