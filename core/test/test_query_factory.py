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


from qgis.testing import unittest

from QuickOSM.definitions.osm import QueryType, OsmType
from QuickOSM.core.exceptions import QueryFactoryException
from QuickOSM.core.query_factory import QueryFactory


# noinspection PyTypeChecker
class TestQueryFactory(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_impossible_queries(self):
        """Test queries which are not possible and must raise an exception."""
        # Query type
        query = QueryFactory('fake_query_type', area='foo')
        msg = 'Wrong query type.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        # Missing query type
        query = QueryFactory(key='foo', value='bar', area='paris')
        msg = 'Wrong query type.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        # OSM object
        query = QueryFactory(QueryType.BBox)
        self.assertEqual(3, len(query._osm_objects))
        query = QueryFactory(QueryType.BBox, osm_objects=[OsmType.Node])
        self.assertEqual(1, len(query._osm_objects))
        query = QueryFactory(QueryType.BBox, osm_objects=['foo'])
        msg = 'Wrong OSM object.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        # Query type with distance
        query = QueryFactory(QueryType.AroundArea)
        msg = 'No distance provided with "around".'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        query = QueryFactory(QueryType.AroundArea, around_distance='foo')
        msg = 'Wrong distance parameter.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        # One value but no key
        query = QueryFactory(query_type=QueryType.BBox, value='b')
        msg = 'Not possible to query a value without a key.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

        # Query with named area
        query = QueryFactory(QueryType.InArea)
        msg = 'Named area required or WKT.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()
        query = QueryFactory(QueryType.InArea, around_distance=500)
        msg = 'Distance parameter is incompatible with this query.'
        with self.assertRaisesRegex(QueryFactoryException, msg):
            query._check_parameters()

    def test_replace_template(self):
        """Test replace template."""
        query = ' area="paris"'
        expected = ' {{geocodeArea:paris}}'
        self.assertEqual(QueryFactory.replace_template(query), expected)

        query = ' area_coords="paris,france"'
        expected = ' {{geocodeCoords:paris,france}}'
        self.assertEqual(QueryFactory.replace_template(query), expected)

        query = ' bbox="custom"'
        expected = ' {{bbox}}'
        self.assertEqual(QueryFactory.replace_template(query), expected)

    def test_possible_queries(self):
        """Test queries which are possible and must return a XML query."""

        def test_query(query, xml, xml_with_template):
            """Internal helper for testing queries."""
            self.assertTrue(query._check_parameters())
            self.assertEqual(xml, query.generate_xml())
            self.assertEqual(xml_with_template, query._make_for_test())

        # Key value and named place
        query = QueryFactory(
            query_type=QueryType.InArea, key='foo', value='bar', area='paris')
        expected_xml = (
            '<osm-script output="xml" timeout="25">'
            '<id-query area="paris" into="area_0"/>'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0" />'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0" />'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0" />'
            '</query>'
            '</union>'
            '<union>'
            '<item />'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body" />'
            '</osm-script>')
        expected_xml_with_template = (
            '<osm-script output="xml" timeout="25">'
            '<id-query {{geocodeArea:paris}} into="area_0"/>'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0"/>'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0"/>'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo" v="bar"/>'
            '<area-query from="area_0"/>'
            '</query>'
            '</union>'
            '<union>'
            '<item/>'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body"/>'
            '</osm-script>'
        )
        test_query(query, expected_xml, expected_xml_with_template)

        # Key in bbox
        query = QueryFactory(query_type=QueryType.BBox, key='foo', timeout=35)
        expected_xml = (
            '<osm-script output="xml" timeout="35">'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo" />'
            '<bbox-query bbox="custom" />'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo" />'
            '<bbox-query bbox="custom" />'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo" />'
            '<bbox-query bbox="custom" />'
            '</query>'
            '</union>'
            '<union>'
            '<item />'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body" />'
            '</osm-script>'
        )
        expected_xml_with_template = (
            '<osm-script output="xml" timeout="35">'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo"/>'
            '<bbox-query {{bbox}}/>'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo"/>'
            '<bbox-query {{bbox}}/>'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo"/>'
            '<bbox-query {{bbox}}/>'
            '</query>'
            '</union>'
            '<union>'
            '<item/>'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body"/>'
            '</osm-script>'
        )
        test_query(query, expected_xml, expected_xml_with_template)

        # Double place name, with node only
        query = QueryFactory(
            query_type=QueryType.InArea,
            key='foo',
            area='paris;dubai',
            osm_objects=[OsmType.Node],
        )
        expected_xml = (
            '<osm-script output="xml" timeout="25">'
            '<id-query area="paris" into="area_0"/>'
            '<id-query area="dubai" into="area_1"/>'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo" />'
            '<area-query from="area_0" />'
            '</query>'
            '<query type="node">'
            '<has-kv k="foo" />'
            '<area-query from="area_1" />'
            '</query>'
            '</union>'
            '<union>'
            '<item />'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body" />'
            '</osm-script>'
        )
        expected_xml_with_template = (
            '<osm-script output="xml" timeout="25">'
            '<id-query {{geocodeArea:paris}} into="area_0"/>'
            '<id-query {{geocodeArea:dubai}} into="area_1"/>'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo"/>'
            '<area-query from="area_0"/>'
            '</query>'
            '<query type="node">'
            '<has-kv k="foo"/>'
            '<area-query from="area_1"/>'
            '</query>'
            '</union>'
            '<union>'
            '<item/>'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="body"/>'
            '</osm-script>'
        )
        test_query(query, expected_xml, expected_xml_with_template)

        # Around query with meta and one key
        query = QueryFactory(
            query_type=QueryType.AroundArea,
            key='foo',
            around_distance=1000,
            print_mode='meta',
            area='a')
        expected_xml = (
            '<osm-script output="xml" timeout="25">'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo" />'
            '<around area_coords="a" radius="1000" />'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo" />'
            '<around area_coords="a" radius="1000" />'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo" />'
            '<around area_coords="a" radius="1000" />'
            '</query>'
            '</union>'
            '<union>'
            '<item />'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="meta" />'
            '</osm-script>'
        )
        expected_xml_with_template = (
            '<osm-script output="xml" timeout="25">'
            '<union>'
            '<query type="node">'
            '<has-kv k="foo"/>'
            '<around {{geocodeCoords:a}} radius="1000"/>'
            '</query>'
            '<query type="way">'
            '<has-kv k="foo"/>'
            '<around {{geocodeCoords:a}} radius="1000"/>'
            '</query>'
            '<query type="relation">'
            '<has-kv k="foo"/>'
            '<around {{geocodeCoords:a}} radius="1000"/>'
            '</query>'
            '</union>'
            '<union>'
            '<item/>'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="meta"/>'
            '</osm-script>'
        )
        test_query(query, expected_xml, expected_xml_with_template)

        # No key, no value, one object
        query = QueryFactory(
            query_type=QueryType.AroundArea,
            around_distance=1000,
            print_mode='meta',
            osm_objects=[OsmType.Node],
            area='a')
        expected_xml = (
            '<osm-script output="xml" timeout="25"><union>'
            '<query type="node">'
            '<around area_coords="a" radius="1000" />'
            '</query>'
            '</union>'
            '<union>'
            '<item /><recurse type="down"/>'
            '</union><print mode="meta" /></osm-script>')
        expected_xml_with_template = (
            '<osm-script output="xml" timeout="25">'
            '<union>'
            '<query type="node">'
            '<around {{geocodeCoords:a}} radius="1000"/>'
            '</query>'
            '</union>'
            '<union>'
            '<item/>'
            '<recurse type="down"/>'
            '</union>'
            '<print mode="meta"/>'
            '</osm-script>'
        )
        test_query(query, expected_xml, expected_xml_with_template)

    def test_make(self):
        """Test make query wuth valid indentation and lines."""
        query = QueryFactory(
            query_type=QueryType.BBox, key='foo', value='bar')
        expected = (
            '<osm-script output="xml" timeout="25">\n    '
            '<union>\n        <query type="node">\n            '
            '<has-kv k="foo" v="bar"/>\n            '
            '<bbox-query {{bbox}}/>\n        </query>\n        '
            '<query type="way">\n            '
            '<has-kv k="foo" v="bar"/>\n            '
            '<bbox-query {{bbox}}/>\n        </query>\n        '
            '<query type="relation">\n            '
            '<has-kv k="foo" v="bar"/>\n            '
            '<bbox-query {{bbox}}/>\n        </query>\n    '
            '</union>\n    <union>\n        <item/>\n        '
            '<recurse type="down"/>\n    </union>\n    '
            '<print mode="body"/>\n</osm-script>\n')
        self.assertEqual(query.make(), expected)


if __name__ == '__main__':
    suite = unittest.makeSuite(TestQueryFactory)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
