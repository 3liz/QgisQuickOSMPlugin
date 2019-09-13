"""
/***************************************************************************
 QuickOSM
 A QGIS plugin
 OSM Overpass API frontend
                             -------------------
        begin                : 2014-06-11
        copyright            : (C) 2014 by 3Liz
        email                : info at 3liz dot com
        contributor          : Etienne Trimaille
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import logging
import urllib.request

from os.path import dirname, join, exists

from qgis.PyQt.QtCore import QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QMenu, QAction
from qgis.core import (
    QgsApplication,
    QgsCoordinateTransform,
    QgsCoordinateReferenceSystem,
    QgsProject,
    QgsSettings,
)

from QuickOSM.core.custom_logging import setup_logger
from QuickOSM.quick_osm_processing.provider import Provider
from QuickOSM.core.utilities.tools import (
    tr,
    resources_path,
)

LOGGER = logging.getLogger('QuickOSM')


class QuickOSMPlugin(object):

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        setup_logger('QuickOSM')

        # initialize locale
        try:
            locale = QgsSettings().value('locale/userLocale', 'en')[0:2]
        except AttributeError:
            # Fallback to english #132
            LOGGER.warning(
                'Fallback to English as default language for the plugin')
            locale = 'en'
        locale_path = join(
            dirname(__file__),
            'i18n',
            'QuickOSM_{0}.qm'.format(locale))

        if exists(locale_path):
            LOGGER.info('Translation to {}'.format(locale))
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.provider = None

        # Add the toolbar
        self.toolbar = self.iface.addToolBar('QuickOSM')
        self.toolbar.setObjectName('QuickOSM')

        self.quickosm_menu = None
        self.vector_menu = None
        self.main_window_action = None
        self.josm_action = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = Provider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

        # Setup menu
        self.quickosm_menu = QMenu('QuickOSM')
        self.quickosm_menu.setIcon(
            QIcon(resources_path('icons', 'QuickOSM.svg')))
        self.vector_menu = self.iface.vectorMenu()
        self.vector_menu.addMenu(self.quickosm_menu)

        # Main window
        self.main_window_action = QAction(
            QIcon(resources_path('icons', 'QuickOSM.svg')),
            'QuickOSM…',
            self.iface.mainWindow())
        # noinspection PyUnresolvedReferences
        self.main_window_action.triggered.connect(self.open_dialog)
        self.toolbar.addAction(self.main_window_action)

        # Action JOSM
        self.josm_action = QAction(
            QIcon(resources_path('icons', 'josm_icon.svg')),
            tr('JOSM Remote'),
            self.iface.mainWindow())
        self.josm_action.triggered.connect(self.josm_remote)
        self.toolbar.addAction(self.josm_action)

        # Insert in the good order
        self.quickosm_menu.addAction(self.main_window_action)
        self.quickosm_menu.addAction(self.josm_action)

    def unload(self):
        self.iface.removePluginVectorMenu('&QuickOSM', self.main_window_action)
        self.iface.removeToolBarIcon(self.main_window_action)
        QgsApplication.processingRegistry().removeProvider(self.provider)

    def josm_remote(self):
        map_settings = self.iface.mapCanvas().mapSettings()
        extent = map_settings.extent()
        crs_map = map_settings.destinationCrs()
        if crs_map.authid() != 'EPSG:4326':
            crs_4326 = QgsCoordinateReferenceSystem(4326)
            transform = QgsCoordinateTransform(
                crs_map, crs_4326, QgsProject.instance())
            extent = transform.transform(extent)

        url = 'http://localhost:8111/load_and_zoom?'
        query_string = 'left=%f&right=%f&top=%f&bottom=%f' % (
            extent.xMinimum(), extent.xMaximum(), extent.yMaximum(),
            extent.yMinimum())
        url += query_string
        try:
            request = urllib.request.Request(url)
            result_request = urllib.request.urlopen(request)
            result = result_request.read()
            result = result.decode('utf8')
            if result.strip().upper() != 'OK':
                self.iface.messageBar().pushCritical(
                    tr('JOSM Remote'), result)
            else:
                self.iface.messageBar().pushSuccess(
                    tr('JOSM Remote'), tr('Import done, check JOSM'))
        except IOError:
            self.iface.messageBar().pushCritical(
                tr('JOSM Remote'), tr('Is the remote enabled?'))

    @staticmethod
    def open_dialog():
        """Create and open the main dialog."""
        from QuickOSM.ui.main_window_dialog import MainDialog
        dialog = MainDialog()
        dialog.menu_widget.setCurrentRow(0)
        dialog.exec_()
