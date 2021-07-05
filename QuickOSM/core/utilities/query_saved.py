"""Manage the saved query in history or bookmark."""
import json
import logging
import re
from os import listdir, remove, rename, mkdir
from os.path import join

from QuickOSM.core.utilities.tools import query_historic, query_bookmark

__copyright__ = 'Copyright 2021, 3Liz'
__license__ = 'GPL version 3'
__email__ = 'info@3liz.org'


LOGGER = logging.getLogger('QuickOSM')


class QueryManagement:
    """Manage the saved query in history or bookmark."""

    @staticmethod
    def write_query_historic(query: str, name: str):
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

        data = {
            'query': query,
            'name': name
        }

        with open(new_file, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file)

    @staticmethod
    def add_bookmark(query: str, name: str, description: str):
        """Add a new query in the bookmark folder"""
        bookmark_folder = query_bookmark()
        files = listdir(bookmark_folder)
        nb_files = len(files)

        final_name = name + '.json' if name != "OsmQuery" else 'bookmark_{}.json'.format(nb_files)

        new_file = join(bookmark_folder, final_name)

        data = {
            'query': [query],
            'description': [description],
            'name': name
        }

        with open(new_file, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file)

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
            data = json.load(json_file)
        data['query'].append(query)
        with open(file, 'w', encoding='utf8') as json_file:
            json.dump(data, json_file)

    def rename_bookmark(self, former_name: str, new_name: str):
        """Rename a bookmark query"""
        bookmark_folder = query_bookmark()

        former_file = join(bookmark_folder, former_name + '.json')
        new_file = join(bookmark_folder, new_name + '.json')

        with open(former_file, encoding='utf8') as json_file:
            data = json.load(json_file)
            data['name'] = new_name
        with open(new_file, 'w', encoding='utf8') as new_json_file:
            json.dump(data, new_json_file)

        self.remove_bookmark(former_name)
