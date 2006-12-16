"""EDXL Distribution Element: XML element
Copyright (C) 2006  Sugree Phatanapherom <sugree@gmail.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""

from lxml import etree
from types import StringTypes,InstanceType
from datetime import datetime
import dateutil.parser

EDXLDE_NS = 'urn:oasis:names:tc:emergency:EDXL:DE:1.0'
CAP_NS = 'urn:oasis:names:tc:emergency:cap:1.1'

REQUIRED = 'required'
OPTIONAL = 'optional'
SINGLE = 'single'
MULTIPLE = 'multiple'

class ElementBase(etree.ElementBase):
    def _make(self,tag,*args,**kw):
        return etree.SubElement(self,tag,*args,**kw)

    def _get(self,tag,attribute,ordinality):
        ret = None
        if ordinality == 'single':
            ret = self.findtext(tag)
        else:
            ret = self.findall(tag)
        return ret

    def _set(self,tag,attribute,ordinality,value):
        if ordinality == 'single':
            el = self.find(tag)
            if not el:
                el = etree.SubElement(self,tag)
            el.text = value
        else:
            for el in self.findall(tag):
                self.remove(el)
            for v in value:
                el = etree.SubElement(self,tag)
                el.text = v

class _EDXLDE(ElementBase):
    def getDistributionID(self):
        return self._get('distributionID',REQUIRED,SINGLE)
    def setDistributionID(self,value):
        return self._set('distributionID',REQUIRED,SINGLE,value)
    distributionID = property(getDistributionID,setDistributionID)

    def getSenderID(self):
        return self._get('senderID',REQUIRED,SINGLE)
    def setSenderID(self,value):
        return self._set('senderID',REQUIRED,SINGLE,value)
    senderID = property(getSenderID,setSenderID)

    def getDateTimeSent(self):
        return dateutil.parser.parse(self._get('dateTimeSent',REQUIRED,SINGLE))
    def setDateTimeSent(self,value):
        return self._set('dateTimeSent',REQUIRED,SINGLE,value.isoformat())
    dateTimeSent = property(getDateTimeSent,setDateTimeSent)

    def getDistributionStatus(self):
        return self._get('distributionStatus',REQUIRED,SINGLE)
    def setDistributionStatus(self,value):
        return self._set('distributionStatus',REQUIRED,SINGLE,value)
    distributionStatus = property(getDistributionStatus,setDistributionStatus)

    def getDistributionType(self):
        return self._get('distributionType',REQUIRED,SINGLE)
    def setDistributionType(self,value):
        return self._set('distributionType',REQUIRED,SINGLE,value)
    distributionType = property(getDistributionType,setDistributionType)

    def getCombinedConfidentiality(self):
        return self._get('combinedConfidentiality',OPTIONAL,MULTIPLE)
    def setCombinedConfidentiality(self,value):
        return self._set('combinedConfidentiality',OPTIONAL,MULTIPLE,value)
    combinedConfidentiality = property(getCombinedConfidentiality,setCombinedConfidentiality)

    def getLanguage(self):
        return self._get('language',OPTIONAL,MULTIPLE)
    def setLanguage(self,value):
        return self._set('language',OPTIONAL,MULTIPLE,value)
    language = property(getLanguage,setLanguage)

    def makeSenderRole(self,*args,**kw):
        el = self._make(make_tag('senderRole'))
        el.init(*args,**kw)
        return el
    def getSenderRole(self):
        return self._get('senderRole',OPTIONAL,MULTIPLE)
    def setSenderRole(self,value):
        return self._set('senderRole',OPTIONAL,MULTIPLE,value)
    senderRole = property(getSenderRole,setSenderRole)

    def makeRecipientRole(self,*args,**kw):
        el = self._make(make_tag('recipientRole'))
        el.init(*args,**kw)
        return el
    def getRecipientRole(self):
        return self._get('recipientRole',OPTIONAL,MULTIPLE)
    def setRecipientRole(self,value):
        return self._set('recipientRole',OPTIONAL,MULTIPLE,value)
    recipientRole = property(getRecipientRole,setRecipientRole)

    def makeKeyword(self,*args,**kw):
        el = self._make(make_tag('keyword'))
        el.init(*args,**kw)
        return el
    def getKeyword(self):
        return self._get('keyword',OPTIONAL,MULTIPLE)
    def setKeyword(self,value):
        return self._set('keyword',OPTIONAL,MULTIPLE,value)
    keyword = property(getKeyword,setKeyword)

    def getDistributionReference(self):
        return self._get('distributionReference',OPTIONAL,MULTIPLE)
    def setDistributionReference(self,value):
        return self._set('distributionReference',OPTIONAL,MULTIPLE,value)
    distributionReference = property(getDistributionReference,setDistributionReference)

    def makeExplicitAddress(self,*args,**kw):
        el = self._make(make_tag('explicitAddress'))
        el.init(*args,**kw)
        return el
    def getExplicitAddress(self):
        return self._get('explicitAddress',OPTIONAL,MULTIPLE)
    def setExplicitAddress(self,value):
        return self._set('explicitAddress',OPTIONAL,MULTIPLE,value)
    explicitAddress = property(getExplicitAddress,setExplicitAddress)

    def makeTargetArea(self):
        el = self._make(make_tag('targetArea'))
        return el
    def getTargetArea(self):
        return self._get('targetArea',OPTIONAL,MULTIPLE)
    def setTargetArea(self,value):
        return self._set('targetArea',OPTIONAL,MULTIPLE,value)
    targetArea = property(getTargetArea,setTargetArea)

    def makeContentObject(self,*args,**kw):
        el = self._make(make_tag('contentObject'))
        return el
    def getContentObject(self):
        return self._get('contentObject',OPTIONAL,MULTIPLE)
    def setContentObject(self,value):
        return self._set('contentObject',OPTIONAL,MULTIPLE,value)
    contentObject = property(getContentObject,setContentObject)

class _ListAndAssociatedValue(ElementBase):
    def init(self,name=None,value=[]):
        if name:
            self.valueListUrn = name
        if value:
            self.value = value

    def getValueListUrn(self):
        return self._get('valueListUrn',OPTIONAL,SINGLE)
    def setValueListUrn(self,value):
        return self._set('valueListUrn',OPTIONAL,SINGLE,value)
    valueListUrn = property(getValueListUrn,setValueListUrn)

    def getValues(self):
        return self._get('value',OPTIONAL,MULTIPLE)
    def setValues(self,value):
        return self._set('value',OPTIONAL,MULTIPLE,value)
    value = property(getValues,setValues)

class _ExplicitAddress(ElementBase):
    def init(self,name=None,value=[]):
        if name:
            self.explicitAddressScheme = name
        if value:
            self.explicitAddressValue = value

    def getExplicitAddressScheme(self):
        return self._get('explicitAddressScheme',OPTIONAL,SINGLE)
    def setExplicitAddressScheme(self,value):
        return self._set('explicitAddressScheme',OPTIONAL,SINGLE,value)
    explicitAddressScheme = property(getExplicitAddressScheme,setExplicitAddressScheme)

    def getExplicitAddressValue(self):
        return self._get('explicitAddressValue',OPTIONAL,MULTIPLE)
    def setExplicitAddressValue(self,value):
        return self._set('explicitAddressValue',OPTIONAL,MULTIPLE,value)
    explicitAddressValue = property(getExplicitAddressValue,setExplicitAddressValue)

class _TargetArea(ElementBase):
    def makeCircle(self,*args,**kw):
        el = self._make(make_tag('circle'))
        el.init(*args,**kw)
        return el
    def getCircles(self):
        return self._get('circle',OPTIONAL,MULTIPLE)
    def setCircles(self,value):
        return self._set('circle',OPTIONAL,MULTIPLE,value)
    circle = property(getCircles,setCircles)

    def makePolygon(self,*args,**kw):
        el = self._make(make_tag('polygon'))
        el.init(*args,**kw)
        return el
    def getPolygons(self):
        return self._get('polygon',OPTIONAL,MULTIPLE)
    def setPolygons(self,value):
        return self._set('polygon',OPTIONAL,MULTIPLE,value)
    polygon = property(getPolygons,setPolygons)

    def getSubdivisions(self):
        return self._get('subdivision',OPTIONAL,MULTIPLE)
    def setSubdivisions(self,value):
        return self._set('subdivision',OPTIONAL,MULTIPLE,value)
    subdivision = property(getSubdivisions,setSubdivisions)

    def getLocCodeUNs(self):
        return self._get('locCodeUN',OPTIONAL,MULTIPLE)
    def setLocCodeUNs(self,value):
        return self._set('locCodeUN',OPTIONAL,MULTIPLE,value)
    locCodeUN = property(getLocCodeUNs,setLocCodeUNs)

class _Circle(ElementBase):
    def init(self,latitude,longitude,radius=0):
        self._latitude = self._longitude = self._radius = 0

        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius

    def _update_text(self):
        self.text = '%f,%f,%f' % (self._latitude,self._longitude,self._radius)

    def getLatitude(self):
        return self._latitude
    def setLatitude(self,value):
        self._latitude = value
        self._update_text()
        return self._latitude
    latitude = property(getLatitude,setLatitude)

    def getLongitude(self):
        return self._longitude
    def setLongitude(self,value):
        self._longitude = value
        self._update_text()
        return self._longitude
    longitude = property(getLongitude,setLongitude)

    def getRadius(self):
        return self._radius
    def setRadius(self,value):
        self._radius = value
        self._update_text()
        return self._radius
    radius = property(getRadius,setRadius)

class _Polygon(ElementBase):
    def init(self,points):
        self.points = points

    def _update_text(self):
        self.text = ' '.join(map(lambda latlong: '%f,%f' % latlong,self.points))

    def getPoints(self):
        return self._points
    def setPoints(self,value):
        self._points = value
        self._update_text()
        return self._points
    points = property(getPoints,setPoints)

class _ContentObject(ElementBase):
    def getContentDescription(self):
        return self._get('contentDescription',OPTIONAL,SINGLE)
    def setContentDescription(self,value):
        return self._set('contentDescription',OPTIONAL,SINGLE,value)
    contentDescription = property(getContentDescription,setContentDescription)

    def getConfidentiality(self):
        return self._get('confidentiality',OPTIONAL,SINGLE)
    def setConfidentiality(self,value):
        return self._set('confidentiality',OPTIONAL,SINGLE,value)
    confidentiality = property(getConfidentiality,setConfidentiality)

    def makeContentKeyword(self,*args,**kw):
        el = self._make(make_tag('contentKeyword'))
        el.init(*args,**kw)
        return el
    def getContentKeyword(self):
        return self._get('contentKeyword',OPTIONAL,MULTIPLE)
    def setContentKeyword(self,value):
        return self._set('contentKeyword',OPTIONAL,MULTIPLE,value)
    contentKeyword = property(getContentKeyword,setContentKeyword)

    def makeEmbeddedXMLContent(self,*args,**kw):
        el = self._make(make_tag('embeddedXMLContent'))
        el.init(*args,**kw)
        return el
    def getEmbeddedXMLContent(self):
        return self._get('embeddedXMLContent',OPTIONAL,MULTIPLE)
    def setEmbeddedXMLContent(self,value):
        return self._set('embeddedXMLContent',OPTIONAL,MULTIPLE,value)
    embeddedXMLContent = property(getEmbeddedXMLContent,setEmbeddedXMLContent)

    def makeNonXMLContent(self,*args,**kw):
        el = self._make(make_tag('nonXMLContent'))
        el.init(*args,**kw)
        return el
    def getNonXMLContent(self):
        return self._get('nonXMLContent',OPTIONAL,MULTIPLE)
    def setNonXMLContent(self,value):
        return self._set('nonXMLContent',OPTIONAL,MULTIPLE,value)
    nonXMLContent = property(getNonXMLContent,setNonXMLContent)

class _EmbeddedXMLContent(ElementBase):
    def init(self,el,nsmap=None):
        if nsmap is not None:
            elns = Element(el.tag,attrib=el.attrib,nsmap=nsmap)
            for i in el.iterchildren():
                elns.append(i)
            el = elns
            
        self.append(el)

class _NonXMLContent(ElementBase):
    def init(self,mimeType=None,size=None,digest=None,uri=None,contentData=None):
        if mimeType:
            self.mimeType = mimeType
        if size:
            self.size = size
        if digest:
            self.digest = digest
        if contentData:
            self.contentData = contentData

    def getMimeType(self):
        return self._get('mimeType',OPTIONAL,SINGLE)
    def setMimeType(self,value):
        return self._set('mimeType',OPTIONAL,SINGLE,value)
    mimeType = property(getMimeType,setMimeType)

    def getSize(self):
        return self._get('size',OPTIONAL,SINGLE)
    def setSize(self,value):
        return self._set('size',OPTIONAL,SINGLE,value)
    size = property(getSize,setSize)

    def getDigest(self):
        return self._get('digest',OPTIONAL,SINGLE)
    def setDigest(self,value):
        return self._set('digest',OPTIONAL,SINGLE,value)
    digest = property(getDigest,setDigest)

    def getUri(self):
        return self._get('uri',OPTIONAL,SINGLE)
    def setUri(self,value):
        return self._set('uri',OPTIONAL,SINGLE,value)
    uri = property(getUri,setUri)

    def getContentData(self):
        return self._get('contentData',OPTIONAL,SINGLE)
    def setContentData(self,value):
        return self._set('contentData',OPTIONAL,SINGLE,value)
    contentData = property(getContentData,setContentData)

element_map = [
    ('EDXLDistribution',_EDXLDE),
    ('senderRole',_ListAndAssociatedValue),
    ('recipientRole',_ListAndAssociatedValue),
    ('keyword',_ListAndAssociatedValue),
    ('explicitAddress',_ExplicitAddress),
    ('targetArea',_TargetArea),
    ('circle',_Circle),
    ('polygon',_Polygon),
    ('contentObject',_ContentObject),
    ('contentKeyword',_ListAndAssociatedValue),
    ('embeddedXMLContent',_EmbeddedXMLContent),
    ('nonXMLContent',_NonXMLContent),
]

MODULE_PARSER = None
_Element = None

def _initialize():
    global MODULE_PARSER,_Element
#    fallback = etree.ElementDefaultClassLookup(element=etree.Element)
#    lookup = etree.ElementNamespaceClassLookup(fallback)
    lookup = etree.ElementNamespaceClassLookup()

#    MODULE_PARSER = etree.XMLParser()
    MODULE_PARSER = etree.XMLParser(remove_blank_text=True)
    MODULE_PARSER.setElementClassLookup(lookup)
    _Element = MODULE_PARSER.makeelement
#    objectify.setDefaultParser(MODULE_PARSER)

    namespace = etree.Namespace(EDXLDE_NS)
    for name,klass in element_map:
        namespace[name] = klass

_initialize()

def make_tag(tag):
    return '{%s}%s' % (EDXLDE_NS,tag)

def Element(tag,*args,**kw):
    if not kw.has_key('nsmap'):
        kw['nsmap'] = {None: EDXLDE_NS}
    if kw.has_key('parent'):
        parent = kw.get('parent',None)
        del kw['parent']
        if parent is not None:
            return etree.SubElement(parent,tag,*args,**kw)
    return _Element(tag,*args,**kw)

def make_edxlde(nsmap={None: EDXLDE_NS}):
    return Element(make_tag('EDXLDistribution'),nsmap=nsmap)

def _test_write():
    import commands
    import base64
    from cStringIO import StringIO

    cap = '''
<alert xmlns = "urn:oasis:names:tc:emergency:cap:1.1">
   <identifier>Vendor generated</identifier>
   <sender>AZ DOT</sender>
   <sent>2005-11-15T16:58:00-05:00</sent>
   <status>Exercise</status>
   <msgType>Update</msgType>
   <scope>Public</scope>
   <info>
      <category>Transport</category>
      <event>Traffic Routes</event>
      <urgency>Immediate</urgency>
      <severity>Moderate</severity>
      <certainty>Likely</certainty>
      <description>Traffic adjustments ensure clear routes to St. Josephs Hospital and Phoenix Childrens Hospital on Thomas Rd. </description>
      <area>
         <areaDesc>Best Routes</areaDesc>
         <polygon>38.91655012246089,-77.02016267943407 38.91655012246089,-77.0117098391165 38.907662564641285,-77.0117098391165 38.907662564641285,-77.02016267943407  38.91655012246089,-77.02016267943407 </polygon>
      </area>
   </info>
</alert>
'''

    root = make_edxlde()
    root.distributionID = commands.getoutput('uuidgen')
    root.senderID = 'sugree@gmail.com'
    root.dateTimeSent = datetime.now()
    root.distributionStatus = 'Green'
    root.distributionType = 'Excercise'
    keyword = root.makeKeyword('http://www.niem.gov/EventTypeList',
                               ['Explosion'])
    root.senderRole = ['Agent']
    root.recipientRole = ['Reporter']
    ea = root.makeExplicitAddress('ABC',['DEF','GHI'])
    targetArea = root.makeTargetArea()
    circle = targetArea.makeCircle(1,1,0)
    polygon = targetArea.makePolygon([(33.4745,-112.1174),
                                      (33.4745,-112.0238),
                                      (33.4238,-112.0238),
                                      (33.4238,-112.1174),
                                      (33.4745,-112.1174)])
    targetArea.subdivision = ['ABC','DEF']
    targetArea.locCodeUN = ['GHI','JKL']

    contentObject = root.makeContentObject()
    contentObject.contentDescription = 'CAP message from DOT advising best alternate Routes'
    contentKeyword = contentObject.makeContentKeyword(
        'urn:sandia:gov:sensor:detection.event.id',
        ['10.2.2.1:2005-08-07T18:00:00Z'])
    contentObject.confidentiality = 'Unclassified'
    nonXMLContent = contentObject.makeNonXMLContent(
        'text/xml',
        uri='http://sentry/photoCapture/10.2.2.1:2005-08-07T18:00:00Z',
        contentData=base64.encodestring(cap))
    capet = etree.parse(StringIO(cap),MODULE_PARSER).getroot()
    embeddedXMLContent = contentObject.makeEmbeddedXMLContent(
        capet,
        nsmap={'cap': CAP_NS})

    return etree.tostring(root,pretty_print=True)

def _test_read(s):
    from cStringIO import StringIO

    root = etree.parse(StringIO(s),MODULE_PARSER)
    print etree.tostring(root,pretty_print=True)

if __name__ == '__main__':
    s = _test_write()
    _test_read(s)
