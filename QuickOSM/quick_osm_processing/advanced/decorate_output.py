"""Decorate the layer as a QuickOSM output."""

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (
    Qgis,
    QgsCategorizedSymbolRenderer,
    QgsLayerMetadata,
    QgsProcessingAlgorithm,
    QgsProcessingOutputVectorLayer,
    QgsProcessingParameterVectorLayer,
    QgsRendererCategory,
    QgsSymbol,
    QgsWkbTypes,
)
from qgis.PyQt.QtGui import QColor

from QuickOSM.core import actions
from QuickOSM.qgis_plugin_tools.tools.i18n import tr

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'


class DecorateLayerAlgorithm(QgisAlgorithm):
    """Decorate the layer as a QuickOSM output."""

    LAYER = 'LAYER'
    OUTPUT_LAYER = 'OUTPUT_LAYER'

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.feedback = None
        self.layer = None

    @staticmethod
    def name() -> str:
        """Return the name of the algorithm."""
        return 'decoratelayer'

    @staticmethod
    def displayName() -> str:
        """Return the display name of the algorithm."""
        return tr('Decorate a layer from OSM')

    @staticmethod
    def group() -> str:
        """Return the group of the algorithm."""
        return tr('Advanced')

    @staticmethod
    def groupId() -> str:
        """Return the id of the group."""
        return 'advanced'

    def shortHelpString(self) -> str:
        """Return an helper for the algorithm."""
        return tr('Decorate the layer as an QuickOSM output.')

    def flags(self):
        """Return the flags."""
        return super().flags() | QgsProcessingAlgorithm.FlagHideFromToolbox

    def add_parameters(self):
        """Set up the parameters."""
        param = QgsProcessingParameterVectorLayer(
            self.LAYER, tr('Layer')
        )
        help_string = tr('Path where the file will be download.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)

    def add_outputs(self):
        """Set up the outputs of the algorithm."""
        output = QgsProcessingOutputVectorLayer(
            self.OUTPUT_LAYER, self.tr('Output layer')
        )
        help_string = tr('The layer with metadata, actions and maybe style.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            pass
            # output.setHelp(help_string)
        else:
            output.tooltip_3liz = help_string
        self.addOutput(output)

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        self.layer = self.parameterAsVectorLayer(parameters, self.LAYER, context)

    def initAlgorithm(self, config=None):
        """Set up of the algorithm."""
        self.add_parameters()
        self.add_outputs()

    def processAlgorithm(self, parameters, context, feedback):
        """Run the algorithm."""
        self.feedback = feedback
        self.fetch_based_parameters(parameters, context)

        fields = self.layer.fields().names()
        layer_type = self.layer.wkbType()
        if "colour" in fields:
            self.feedback.pushInfo('Creating the style from OSM data "colour".')
            index = fields.index('colour')
            colors = self.layer.uniqueValues(index)
            categories = []
            for value in colors:
                if layer_type in ['lines', 'multilinestrings']:
                    symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.LineGeometry)
                elif layer_type == "points":
                    symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.PointGeometry)
                elif layer_type == "multipolygons":
                    symbol = QgsSymbol.defaultSymbol(QgsWkbTypes.PolygonGeometry)
                else:
                    break
                symbol.setColor(QColor(value))
                category = QgsRendererCategory(str(value), symbol, str(value))
                categories.append(category)

            renderer = QgsCategorizedSymbolRenderer("colour", categories)
            self.layer.setRenderer(renderer)

        self.feedback.pushInfo('Set up the QuickOSM actions on the layer.')
        actions.add_actions(self.layer, fields)

        self.feedback.pushInfo('Write the metadata of the layer.')
        metadata = QgsLayerMetadata()
        metadata.setRights([tr("© OpenStreetMap contributors")])
        metadata.setLicenses(['https://openstreetmap.org/copyright'])
        self.layer.setMetadata(metadata)

        outputs = {
            self.OUTPUT_LAYER: self.layer,
        }
        return outputs
