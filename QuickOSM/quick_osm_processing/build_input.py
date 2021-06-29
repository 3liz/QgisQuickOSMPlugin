"""Set up the parameters for the processing algorithms."""

from processing.algs.qgis.QgisAlgorithm import QgisAlgorithm
from qgis.core import (
    Qgis,
    QgsProcessingParameterDefinition,
    QgsProcessingParameterExtent,
    QgsProcessingParameterNumber,
    QgsProcessingParameterString,
)

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

from QuickOSM.core.utilities.tools import get_setting
from QuickOSM.definitions.overpass import OVERPASS_SERVERS
from QuickOSM.qgis_plugin_tools.tools.i18n import tr


class BuildBased(QgisAlgorithm):
    """Set up the parameters for a raw query input."""

    TIMEOUT = 'TIMEOUT'
    SERVER = 'SERVER'

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.feedback = None
        self.timeout = None
        self.server = None

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        self.timeout = self.parameterAsInt(parameters, self.TIMEOUT, context)
        self.server = self.parameterAsString(parameters, self.SERVER, context)

    def add_top_parameters(self):
        """Set up the parameters."""
        pass

    def add_bottom_parameters(self):
        """Set up the advanced parameters."""
        param = QgsProcessingParameterNumber(
            self.TIMEOUT, tr('Timeout'), defaultValue=25, minValue=5)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        help_string = tr('The timeout to use for the Overpass API.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)

        server = get_setting('defaultOAPI', OVERPASS_SERVERS[0]) + 'interpreter'
        param = QgsProcessingParameterString(
            self.SERVER,
            tr('Overpass server'),
            optional=False,
            defaultValue=server)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)
        help_string = tr('The Overpass API server to use to build the encoded URL.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)


class BuildRaw(BuildBased):
    """Set up the parameters for a raw query input."""

    QUERY = 'QUERY'
    EXTENT = 'EXTENT'
    AREA = 'AREA'
    OUTPUT_URL = 'OUTPUT_URL'
    OUTPUT_OQL_QUERY = 'OUTPUT_OQL_QUERY'

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.query = None
        self.extent = None
        self.crs = None
        self.area = None

    def fetch_based_parameters(self, parameters, context):
        """Get the parameters."""
        self.query = self.parameterAsString(parameters, self.QUERY, context)
        self.extent = self.parameterAsExtent(parameters, self.EXTENT, context)
        self.crs = self.parameterAsExtentCrs(parameters, self.EXTENT, context)
        self.area = self.parameterAsString(parameters, self.AREA, context)

    def add_top_parameters(self):
        """Set up the parameters."""
        param = QgsProcessingParameterString(
            self.QUERY, tr('Query'), optional=False, multiLine=True
        )
        help_string = tr(
            'A XML or OQL query to be send to the Overpass API. It can contains some {{}} tokens.'
        )
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)

    def add_bottom_parameters(self):
        """Set up the advanced parameters."""
        super().add_bottom_parameters()

        param = QgsProcessingParameterExtent(
            self.EXTENT, tr('Extent, if "{{bbox}}" in the query'),
            optional=True
        )
        param.setFlags(
            param.flags() | QgsProcessingParameterDefinition.FlagAdvanced
        )
        help_string = tr(
            'If the query has a {{bbox}} token, this extent will be used for replacement.'
        )
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)

        param = QgsProcessingParameterString(
            self.AREA,
            tr('Area (if {{geocodeArea}} in the query)'),
            optional=True
        )
        param.setFlags(
            param.flags() | QgsProcessingParameterDefinition.FlagAdvanced
        )
        help_string = tr('If the query has a {{geocodeArea}} token, this place will be used.')
        if Qgis.QGIS_VERSION_INT >= 31500:
            param.setHelp(help_string)
        else:
            param.tooltip_3liz = help_string
        self.addParameter(param)
