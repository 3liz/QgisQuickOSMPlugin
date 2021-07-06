"""Manage the saved query in history or bookmark."""
import json
import logging
import re

from os import listdir, remove, rename
from os.path import join
from typing import List, Union

from qgis.core import QgsRectangle

from QuickOSM.core.utilities.json_encoder import EnumEncoder, as_enum
from QuickOSM.core.utilities.tools import query_bookmark, query_historic
from QuickOSM.definitions.format import Format

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'


LOGGER = logging.getLogger('QuickOSM')


class QueryManagement:
    """Manage the saved query in history or bookmark."""

    def __init__(
            self,
            query: Union[str, List[str]] = '',
            name: str = '',
            description: Union[str, List[str]] = '',
            area: Union[str, List[str]] = None,
            bbox: QgsRectangle = None,
            output_geometry_types: list = None,
            white_list_column: dict = None,
            output_directory: str = None,
            output_format: Format = None
    ):
        """Constructor"""
        if isinstance(query, str):
            self.query = [query]
        else:
            self.query = query
        self.name = name
        if isinstance(description, str):
            self.description = [description]
        else:
            self.description = description
        self.area = area
        self.bbox = bbox
        self.output_geom_type = output_geometry_types
        self.white_list = white_list_column
        self.output_directory = output_directory
        self.output_format = output_format

    def write_query_historic(self):
        """Write new query in the history folder"""
        history_folder = query_historic()
        files = listdir(history_folder)
        nb_files = len(files)

        if nb_files == 10:
            remove(join(history_folder, 'query_saved_0.json'))
            files = listdir(history_folder)
            for k, file in enumerate(files):
                former_file = join(history_folder, file)
                new_file = join(history_folder, 'query_saved_{}.json'.format(k))
                rename(former_file, new_file)
            new_file = join(history_folder, 'query_saved_{}.json'.format(nb_files - 1))
        else:
            new_file = join(history_folder, 'query_saved_{}.json'.format(nb_files))

        self.write_json(new_file)

    def add_bookmark(self, name: str):
        """Add a new query in the bookmark folder"""
        bookmark_folder = query_bookmark()
        files = listdir(bookmark_folder)
        nb_files = len(files)

        final_name = name + '.json' if name != "OsmQuery" else 'bookmark_{}.json'.format(nb_files)

        new_file = join(bookmark_folder, final_name)
        self.write_json(new_file)

    def write_json(self, file: str):
        """Write the saved file in json"""
        data = {
            'query': [self.query],
            'description': self.description,
            'file_name': self.name,
            'query_name': [self.name],
            'area': self.area,
            'bbox': self.bbox,
            'output_geom_type': self.output_geom_type,
            'white_list_column': self.white_list,
            'output_directory': self.output_directory,
            'output_format': self.output_format
        }

        with open(file, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, cls=EnumEncoder)

    @staticmethod
    def remove_bookmark(name: str):
        """Remove a bookmark query"""
        bookmark_folder = query_bookmark()

        file = join(bookmark_folder, name + '.json')
        remove(file)
        if name.startswith('bookmark_'):
            list_bookmark = filter(lambda query_file: query_file.startswith('bookmark_'), name)
            num = re.findall('bookmark_(0-9)', name)[0]
            for k, file in enumerate(list_bookmark):
                if k >= num:
                    former_file = join(bookmark_folder, file + '.json')
                    new_file = join(bookmark_folder, 'bookmark_{}.json'.format(k))
                    rename(former_file, new_file)

    @staticmethod
    def add_query_in_bookmark(query: str, name: str):
        """Add a query in a bookmark file"""
        bookmark_folder = query_bookmark()

        file = join(bookmark_folder, name + '.json')

        with open(file, encoding='utf8') as json_file:
            data = json.load(json_file, object_hook=as_enum)
        data['query'].append(query)
        with open(file, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, cls=EnumEncoder)

    def rename_bookmark(self, former_name: str, new_name: str):
        """Rename a bookmark query"""
        bookmark_folder = query_bookmark()

        former_file = join(bookmark_folder, former_name + '.json')
        new_file = join(bookmark_folder, new_name + '.json')

        with open(former_file, encoding='utf8') as json_file:
            data = json.load(json_file, object_hook=as_enum)
            data['name'] = new_name
        with open(new_file, 'w', encoding='utf8') as new_json_file:
            json.dump(data, new_json_file, cls=EnumEncoder)

        self.remove_bookmark(former_name)
