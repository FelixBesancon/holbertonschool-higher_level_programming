#!/usr/bin/python3
"""
This module provides serialize_to_xml function
for serializing in XML and deserialize_from_xml
function to deserializing dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): XML file to read.

    Returns:
        dict: Dictionary reconstructed from XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    obj = dict()

    for child in root:
        obj[child.tag] = child.text
    return obj
