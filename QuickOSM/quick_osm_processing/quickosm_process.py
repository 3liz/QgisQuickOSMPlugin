"""Run the process of the plugin as an algorithm."""
from os.path import dirname, basename

import processing

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (
    Qgis,
    QgsProcessing,
    QgsProcessingAlgorithm,
    QgsProcessingContext,
    QgsProcessingMultiStepFeedback,
    QgsProcessingOutputVectorLayer,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterFileDestination,
    QgsProcessingUtils,
)

from QuickOSM.core.api.connexion_oapi import ConnexionOAPI
from QuickOSM.core.parser.osm_parser import OsmParser
from QuickOSM.definitions.format import Format
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
        self.file = self.parameterAsFileOutput(parameters, self.FILE, context)

    def add_output_file_parameter(self):
        """Set up the output file parameter."""
        param = QgsProcessingParameterFileDestination(
            self.FILE, tr('Output file'),
            optional=True)
        param.setFileFilter('*.gpkg')
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
        self.feedback = QgsProcessingMultiStepFeedback(5, feedback)
        self.fetch_based_parameters(parameters, context)

        self.feedback.setCurrentStep(0)

        if self.feedback.isCanceled():
            self.feedback.pushDebug('Aie canceled')
            outputs = {
                self.OUTPUT_POINTS: None,
                self.OUTPUT_LINES: None,
                self.OUTPUT_MULTILINESTRINGS: None,
                self.OUTPUT_MULTIPOLYGONS: None
            }
            return outputs

        self.feedback.setCurrentStep(1)
        self.feedback.pushInfo('Building the query.')

        raw_query = processing.run(
            "quickosm:buildrawquery",
            {
                'AREA': self.area,
                'EXTENT': self.extent,
                'QUERY': self.query,
                'SERVER': self.server
            },
            feedback=self.feedback
        )

        self.feedback.setCurrentStep(2)
        self.feedback.pushInfo('Downloading data and OSM file.')

        url = raw_query['OUTPUT_URL']
        connexion_overpass_api = ConnexionOAPI(url)
        osm_file = connexion_overpass_api.run()

        self.feedback.setCurrentStep(3)
        self.feedback.pushInfo('Processing downloaded file.')

        out_dir = dirname(self.file) if self.file else None
        out_file = basename(self.file)[:-5] if self.file else None

        osm_parser = OsmParser(
            osm_file=osm_file,
            output_format=Format.GeoPackage,
            output_dir=out_dir,
            prefix_file=out_file,
            feedback=self.feedback
        )

        layers = osm_parser.processing_parse()

        self.feedback.setCurrentStep(4)
        self.feedback.pushInfo('Decorating the requested layers.')

        layer_output = []
        OUTPUT = {
            'points': self.OUTPUT_POINTS,
            'lines': self.OUTPUT_LINES,
            'multilinestrings': self.OUTPUT_MULTILINESTRINGS,
            'multipolygons': self.OUTPUT_MULTIPOLYGONS
        }

        for layer in layers:
            layers[layer]['layer_decorated'] = processing.run(
                "quickosm:decoratelayer",
                {
                    'LAYER': layers[layer]['vector_layer']
                },
                feedback=self.feedback
            )

            context.temporaryLayerStore().addMapLayer(layers[layer]['vector_layer'])
            layer_output.append(
                QgsProcessingUtils.mapLayerFromString(
                    layers[layer]['vector_layer'].id(), context, True
                )
            )
            context.addLayerToLoadOnCompletion(
                layers[layer]['vector_layer'].id(),
                QgsProcessingContext.LayerDetails(
                    'OSMQuery_' + layer,
                    context.project(),
                    OUTPUT[layer]
                )
            )

        outputs = {
            self.OUTPUT_POINTS: layer_output[0].id(),
            self.OUTPUT_LINES: layer_output[1].id(),
            self.OUTPUT_MULTILINESTRINGS: layer_output[2].id(),
            self.OUTPUT_MULTIPOLYGONS: layer_output[3].id(),
        }
        return outputs
