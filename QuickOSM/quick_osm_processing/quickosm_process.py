"""Run the process of the plugin as an algorithm."""

import processing

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (
    Qgis,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingContext,
    QgsProcessingOutputVectorLayer,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFile,
    QgsProcessingUtils,
)

from QuickOSM.core.api.connexion_oapi import ConnexionOAPI
from QuickOSM.core.parser.osm_parser import OsmParser
from QuickOSM.qgis_plugin_tools.tools.i18n import tr

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

from QuickOSM.quick_osm_processing.build_input import BuildRaw


class DownloadOSMData(QgisAlgorithm):
    """Set up the parameters needed for the download algorithms."""

    FILE = 'FILE'
    OUTPUT_POINTS = 'OUTPUT_POINTS'
    OUTPUT_LINES = 'OUTPUT_LINES'
    OUTPUT_MULTILINESTRINGS = 'OUTPUT_MULTILINESTRINGS'
    OUTPUT_MULTIPOLYGONS = 'OUTPUT_MULTIPOLYGONS'

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.file = None

    def shortHelpString(self) -> str:
        """Return an helper for the algorithm."""
        return tr('Fetch the OSM data that match the request.')

    def flags(self):
        """Return the flags."""
        return super().flags() | QgsProcessingAlgorithm.FlagHideFromModeler

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        self.file = self.parameterAsFile(parameters, self.FILE, context)

    def add_output_file_parameter(self):
        """Set up the output file parameter."""
        param = QgsProcessingParameterFile(
            self.FILE, tr('Output file'),
            extension='gpkg', optional=True)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        help_string = tr('Path where the file will be download.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)

    def add_outputs(self):
        """Set up the outputs of the algorithm."""
        output = QgsProcessingOutputVectorLayer(
            self.OUTPUT_POINTS, self.tr('Output points'), QgsProcessing.TypeVectorPoint)
        help_string = tr('The point layer from the OGR OSM driver.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            pass
            # output.setHelp(help_string)
        else:
            output.tooltip_3liz = help_string
        self.addOutput(output)

        output = QgsProcessingOutputVectorLayer(
            self.OUTPUT_LINES, self.tr('Output lines'), QgsProcessing.TypeVectorLine)
        help_string = tr('The line layer from the OGR OSM driver.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            pass
            # output.setHelp(help_string)
        else:
            output.tooltip_3liz = help_string
        self.addOutput(output)

        output = QgsProcessingOutputVectorLayer(
            self.OUTPUT_MULTILINESTRINGS, self.tr('Output multilinestrings'),
            QgsProcessing.TypeVectorLine
        )
        help_string = tr('The multilinestrings layer from the OGR OSM driver.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            pass
            # output.setHelp(help_string)
        else:
            output.tooltip_3liz = help_string
        self.addOutput(output)

        output = QgsProcessingOutputVectorLayer(
            self.OUTPUT_MULTIPOLYGONS, self.tr('Output multipolygons'),
            QgsProcessing.TypeVectorPolygon
        )
        help_string = tr('The multipolygon layer from the OGR OSM driver.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            pass
            # output.setHelp(help_string)
        else:
            output.tooltip_3liz = help_string
        self.addOutput(output)

    def initAlgorithm(self, config=None):
        """Set up of the algorithm."""
        self.add_top_parameters()
        self.add_bottom_parameters()
        self.add_output_file_parameter()
        self.add_outputs()


class DownloadOSMDataRawQuery(BuildRaw, DownloadOSMData):
    """Run the process of the plugin as an algorithm with a raw query input."""

    @staticmethod
    def name() -> str:
        """Return the name of the algorithm."""
        return 'downloadosmdatarawquery'

    @staticmethod
    def displayName() -> str:
        """Return the display name of the algorithm."""
        return tr('Download OSM data from a raw query')

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        BuildRaw.fetch_based_parameters(self, parameters, context)
        DownloadOSMData.fetch_based_parameters(self, parameters, context)

    def processAlgorithm(self, parameters, context, feedback):
        """Run the algorithm."""
        self.feedback = feedback
        self.fetch_based_parameters(parameters, context)

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

        layers = osm_parser.processing_parse()
        """
        for layer in layers:
            layers[layer]['layer_decorated'] = processing.run(
                "quickosm:decoratelayer",
                {
                    'LAYER': layers[layer]['vector_layer']
                }
            )
        """
        context.temporaryLayerStore().addMapLayer(layers['points']['vector_layer'])
        point = QgsProcessingUtils.mapLayerFromString(layers['points']['vector_layer'].id(), context, True)
        context.addLayerToLoadOnCompletion(
            layers['points']['vector_layer'].id(),
            QgsProcessingContext.LayerDetails(
                'OSMQuery_points',
                context.project(),
                self.OUTPUT_POINTS
            )
        )

        outputs = {
            self.OUTPUT_POINTS: point.id(),
            self.OUTPUT_LINES: layers['lines']['vector_layer'].id(),
            self.OUTPUT_MULTILINESTRINGS: layers['multilinestrings']['vector_layer'].id(),
            self.OUTPUT_MULTIPOLYGONS: layers['multipolygons']['vector_layer'].id(),
        }
        return outputs
