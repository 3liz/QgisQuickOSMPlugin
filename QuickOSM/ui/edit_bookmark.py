"""Dialog that edit a bookmark"""

from qgis.gui import QgsFileWidget
from qgis.PyQt.QtWidgets import QDialog

from QuickOSM.core.utilities.query_saved import QueryManagement
from QuickOSM.definitions.format import Format
from QuickOSM.definitions.gui import Panels
from QuickOSM.definitions.osm import LayerType
from QuickOSM.qgis_plugin_tools.tools.i18n import tr
from QuickOSM.qgis_plugin_tools.tools.resources import load_ui

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'

FORM_CLASS = load_ui('edit_bookmark.ui')


class EditBookmark(QDialog, FORM_CLASS):
    """Dialog that edit a bookmark"""

    def __init__(self, parent=None, data_bookmark: dict = None):
        """Constructor."""
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.previous_name = data_bookmark['file_name']
        self.current_query = 0
        self.nb_queries = len(data_bookmark['query'])

        for k in range(self.nb_queries):
            self.list_queries.addItem(tr('Query ') + str(k + 1))

        self.button_add.clicked.connect(self.add_query)
        self.list_queries.currentRowChanged.connect(self.change_query)

        self.combo_output_format.addItem(
            Format.GeoPackage.value.label, Format.GeoPackage)
        self.combo_output_format.addItem(
            Format.GeoJSON.value.label, Format.GeoJSON)
        self.combo_output_format.addItem(
            Format.Shapefile.value.label, Format.Shapefile)
        self.combo_output_format.addItem(
            Format.Kml.value.label, Format.Kml)

        self.output_directory.lineEdit().setPlaceholderText(
            tr('Save to temporary file'))
        self.output_directory.setStorageMode(
            QgsFileWidget.GetDirectory)

        self.data = data_bookmark
        if self.data:
            self.bookmark_name.setText(self.data['file_name'])
            self.description.setPlainText('\\n'.join(self.data['description']))

            self.data_filling_form()

        self.button_validate.clicked.connect(self.validate)
        self.button_cancel.clicked.connect(self.close)

    def data_filling_form(self, num_query: int = 0):
        """Writing the form with data from bookmark"""

        self.layer_name.setText(self.data['query_name'][num_query])
        self.query.setPlainText(self.data['query'][num_query])

        self.area.setText(self.data['area'][num_query])
        self.bbox.setText(self.data['bbox'][num_query])

        if LayerType.Points in self.data['output_geom_type'][num_query]:
            self.checkbox_points.setChecked(True)
        if LayerType.Lines in self.data['output_geom_type'][num_query]:
            self.checkbox_lines.setChecked(True)
        if LayerType.Multilinestrings in self.data['output_geom_type'][num_query]:
            self.checkbox_multilinestrings.setChecked(True)
        if LayerType.Multipolygons in self.data['output_geom_type'][num_query]:
            self.checkbox_multipolygons.setChecked(True)

        if self.data['white_list_column'][num_query]['points']:
            self.white_points.setText(self.data['white_list_column'][num_query]['points'])
        if self.data['white_list_column'][num_query]['lines']:
            self.white_lines.setText(self.data['white_list_column'][num_query]['lines'])
        if self.data['white_list_column'][num_query]['multilinestrings']:
            self.white_multilinestrings.setText(self.data['white_list_column'][num_query]['multilinestrings'])
        if self.data['white_list_column'][num_query]['multipolygons']:
            self.white_multipolygons.setText(self.data['white_list_column'][num_query]['multipolygons'])

        index = self.combo_output_format.findData(self.data['output_format'][num_query])
        self.combo_output_format.setCurrentIndex(index)

        self.output_directory.setFilePath(self.data['output_directory'][num_query])

    def change_query(self, new: bool = False):
        """Display the selected query in the view."""
        self.gather_parameters(self.current_query)
        if new:
            self.current_query = self.list_queries.count() - 1
        else:
            self.current_query = self.list_queries.currentRow()
        self.data_filling_form(self.current_query)

    def add_query(self):
        """Add a query in the bookmark"""
        q_manage = QueryManagement()
        self.data = q_manage.add_empty_query_in_bookmark(self.data)

        self.list_queries.addItem(tr('Query ') + str(self.nb_queries + 1))
        self.nb_queries += 1

        self.change_query(True)

    def gather_general_parameters(self):
        """Save the general parameters."""
        self.data['file_name'] = self.bookmark_name.text()
        description = self.description.toPlainText().split('\\n')
        self.data['description'] = description

    def gather_parameters(self, num_query: int = 0):
        """Save the parameters."""
        self.data['query_name'][num_query] = self.layer_name.text()
        self.data['query'][num_query] = self.query.toPlainText()
        self.data['area'][num_query] = self.area.text()
        self.data['bbox'][num_query] = self.bbox.text()

        output_geom = []
        if self.checkbox_points.isChecked():
            output_geom.append(LayerType.Points)
        if self.checkbox_lines.isChecked():
            output_geom.append(LayerType.Lines)
        if self.checkbox_multilinestrings.isChecked():
            output_geom.append(LayerType.Multilinestrings)
        if self.checkbox_multipolygons.isChecked():
            output_geom.append(LayerType.Multipolygons)
        self.data['output_geom_type'][num_query] = output_geom

        if self.white_points.text():
            white_list = {'points': self.white_points.text()}
        else:
            white_list = {'points': None}
        if self.white_lines.text():
            white_list['lines'] = self.white_lines.text()
        else:
            white_list['lines'] = None
        if self.white_multilinestrings.text():
            white_list['multilinestrings'] = self.white_multilinestrings.text()
        else:
            white_list['multilinestrings'] = None
        if self.white_multipolygons.text():
            white_list['multipolygons'] = self.white_multipolygons.text()
        else:
            white_list['multipolygons'] = None
        self.data['white_list_column'][num_query] = white_list

        self.data['output_format'][num_query] = self.combo_output_format.currentData()
        self.data['output_directory'][num_query] = self.output_directory.filePath()

    def validate(self):
        """Update the bookmark"""
        self.gather_parameters(self.current_query)
        self.gather_general_parameters()

        q_manage = QueryManagement()
        if self.previous_name != self.data['file_name']:
            q_manage.rename_bookmark(self.previous_name, self.data['file_name'], self.data)
        else:
            q_manage.update_bookmark(self.data)

        self.parent().external_panels[Panels.QuickQuery].update_bookmark_view()
        self.close()
