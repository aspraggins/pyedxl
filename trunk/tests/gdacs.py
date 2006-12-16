#!/usr/bin/env python

from datetime import datetime
import copy

import lxml.etree as etree
from edxl import edxl

RSS = "http://backend.userland.com/rss2"
ICBM = "http://postneo.com/icbm/"
DC = "http://purl.org/dc/elements/1.1/"
ASGARD = "http://asgard.jrc.it"
GDAS = "http://www.gdacs.org"
DFO = "http://www.gdacs.org"
GEO = "http://www.w3.org/2003/01/geo/"
GLIDE = "http://glidenumber.net"

class Translator:

    handlers = ['edxl','gdas','asgard','dfo','geo','rss']

    def __init__(self,senderID,parser=None):
        self.senderID = senderID
        self.parser = parser

    def clean_ns(self,xml):
        if not self.parser:
            return xml
        tree = etree.parse(StringIO(xml),self.parser)
        return etree.tostring(tree.getroot(),pretty_print=True)

    def feed(self,root):
        root = tree.getroot()
        items = tree.findall('{%s}channel/{%s}item' % (RSS,RSS))
        self.xml = []
        for item in items:
            self.xml.append(self.item_to_edxl(item))

    def item_to_edxl(self,item):
        o = edxl.make_edxlde()
        for handler in self.handlers:
            method = getattr(self,'handler_%s' % handler)
            method(o,item)
        return self.clean_ns(etree.tostring(o))

    def handler_rss(self,o,item):
        contentObject = o.makeContentObject()
        nsmap = {'rss2':RSS}
#        rss_item = etree.Element(etree.QName(RSS,'item'),nsmap=nsmap)
#        for child in item.getchildren():
#            if child.prefix is None:
#                el = etree.SubElement(rss_item,etree.QName(RSS,child.tag),attrib=child.attrib)
#                el.text = child.text
#            else:
#                rss_item.append(child)
        rss_item = copy.copy(item)
        contentObject.makeEmbeddedXMLContent(rss_item)
#        contentObject.makeEmbeddedXMLContent(item)
#        rss_item = etree.Element(etree.QName(RSS,'item'))
#        for child in item.getchildren():
#            rss_item.append(copy.copy(child))
#        o.contentObject = [edxl.ContentObject(xmlContent=edxl.EmbeddedXMLContent(rss_item))]

    def handler_edxl(self,o,item):
        o.dateTimeSent = datetime.now()
        o.senderID = self.senderID
        o.language = ['EN']
        o.distributionType = 'Report'
        o.distributionStatus = 'Actual'
        o.combinedConfidentiality = ['UNCLASSIFIED AND NOT SENSITIVE']

    def handler_gdas(self,o,item):
#        o.distributionType = item.findtext('{%s}eventType' % GDAS)
#        o.distributionStatus = item.findtext('{%s}alertLevel' % GDAS)
        pass

    def handler_asgard(self,o,item):
        if not o.distributionID:
            distributionID = item.findtext('{%s}ID' % ASGARD)
            if distributionID:
                o.distributionID = 'asgard:'+distributionID

    def handler_dfo(self,o,item):
        if not o.distributionID:
            distributionID = 'dfo:'+item.findtext('{%s}ID' % DFO)
            if distributionID:
                o.distributionID = 'dfo:'+distributionID

    def handler_geo(self,o,item):
        lat = item.findtext('{%s}lat' % GEO)
        long = item.findtext('{%s}long' % GEO)
        if not lat:
            lat = item.findtext('{%s}point/{%s}lat' % (GEO,GEO))
            long = item.findtext('{%s}point/{%s}long' % (GEO,GEO))
        radius = 0
        area = o.makeTargetArea()
        circle = area.makeCircle(float(lat),float(long),radius)

if __name__ == '__main__':
    import sys
    import urllib2
    from cStringIO import StringIO

    sender = 'rss@gdacs.org'
    gdacs_file = 'http://www.gdacs.org/XML/RSS.xml'

    if len(sys.argv) > 1:
        sender = sys.argv[1]
    if len(sys.argv) > 2:
       gdacs_file = sys.argv[2]

    parser = etree.XMLParser(remove_blank_text=True,ns_clean=True)

    xml = urllib2.urlopen(gdacs_file).read()
    xml = xml.replace('<rss ','<rss xmlns="%s" ' % RSS)
    tree = etree.parse(StringIO(xml),parser)
    root = tree.getroot()
#    print root.nsmap
    t = Translator(sender,parser)
    t.feed(root)
    print t.xml[0]
