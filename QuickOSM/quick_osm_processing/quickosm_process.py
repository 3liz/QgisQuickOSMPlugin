"""Run the process of the plugin as an algorithm."""

import processing

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (
    Qgis,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFile,
)

from QuickOSM.core.api.connexion_oapi import ConnexionOAPI
from QuickOSM.core.parser.osm_parser import OsmParser
from QuickOSM.qgis_plugin_tools.tools.i18n import tr

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

from QuickOSM.quick_osm_processing.build_input import BuildRaw


def init_output(alg: QgisAlgorithm):
    """Set up the output parameter."""
    param = QgsProcessingParameterFile(
        alg.FILE, tr('Output file'),
        extension='gpkg', optional=True)
    param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
    help_string = tr('Path where the file will be download.')
    if Qgis.QGIS_VERSION_INT >= 31500:
        param.setHelp(help_string)
    else:
        param.tooltip_3liz = help_string
    alg.addParameter(param)


class DownloadOSMDataRawQuery(BuildRaw):
    """Run the process of the plugin as an algorithm with a raw query input."""

    FILE = 'FILE'

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.file = None

    @staticmethod
    def name() -> str:
        """Return the name of the algorithm."""
        return 'downloadosmdatarawquery'

    @staticmethod
    def displayName() -> str:
        """Return the display name of the algorithm."""
        return tr('Download OSM data from a raw query')

    def shortHelpString(self) -> str:
        """Return an helper for the algorithm."""
        return 'Fetch the OSM data that match the request.'

    def flags(self):
        """Return the flags."""
        return super().flags()

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        self.file = self.parameterAsFile(parameters, self.FILE, context)

    def initAlgorithm(self, config=None):
        """Set up of the algorithm."""
        self.add_top_parameters()
        self.add_bottom_parameters()
        init_output(self)

    def processAlgorithm(self, parameters, context, feedback):
        """Run the algorithm."""
        self.feedback = feedback

        raw_query = processing.run(
            "quickosm:buildrawquery",
            {
                'AREA': self.area,
                'EXTENT': self.extent,
                'QUERY': self.query,
                'SERVER': self.server
            }
        )

        url = raw_query['OUTPUT_URL']
        connexion_overpass_api = ConnexionOAPI(url)
        osm_file = connexion_overpass_api.run()

        osm_parser = OsmParser(
            osm_file=osm_file
        )

        osm_parser.processing_parse()
