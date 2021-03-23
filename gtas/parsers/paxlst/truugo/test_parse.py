import unittest
import html_parser as parse

class TestParse(unittest.TestCase):

    def test_simple_section_with_attribute_and_sub_attributes(self):
        html_text = """
        <div id="container">
            <div id="view-message">
                <div class="aggr seg">
                    <h3><a href="/edifact/d03a/qty/"><span>QTY</span><span>QUANTITY</span><span>C 9</span></a></h3>
                    <div>
                        <div><span>9</span><span>Conditional</span> A segment to indicate the number of persons onboard.
                        </div>
                        <div>
                            <div class="com elm">
                                <div>C186</div>
                                <div>QUANTITY DETAILS</div>
                                <div><span>Mandatory</span></div>
                                <div>Quantity information in a transaction, qualified when relevant. </div>
                            </div>
                            <div>
                                <div class="elm e">
                                    <div>6063</div>
                                    <div>Quantity type code qualifier</div>
                                    <div><span>Mandatory</span><span>an</span><span>0..3</span></div>
                                    <div>Code qualifying the type of quantity.</div><a href="/edifact/d03a/cl6063/"
                                        rel="nofollow" title="6063">Show all standard codes</a>
                                </div>
                                <div class="elm e">
                                    <div>6060</div>
                                    <div>Quantity</div>
                                    <div><span>Mandatory</span><span>an</span><span>0..35</span></div>
                                    <div>Alphanumeric representation of a quantity.</div>
                                </div>
                                <div class="elm e">
                                    <div>6411</div>
                                    <div>Measurement unit code</div>
                                    <div><span>Conditional</span><span>an</span><span>0..8</span></div>
                                    <div>Code specifying the unit of measurement.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        parser = parse.FormatParser()
        parser.parse(html_text)
        self.assertEqual(len(parser.my_sections), 1)
        section = parser.my_sections[0]
        self.assertEqual(section.code, 'QTY')
        self.assertEqual(section.name, 'QUANTITY')
        self.assertEqual(section.desc, 'A segment to indicate the number of persons onboard.')
        self.assertEqual(section.repeat, 'C 9')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, 'C186')
        self.assertEqual(attribute.name, 'QUANTITY DETAILS')
        self.assertEqual(attribute.desc, 'Quantity information in a transaction, qualified when relevant.')
        self.assertEqual(attribute.repeat, 'Mandatory')
        self.assertEquals(attribute.codeset, None)
        self.assertEqual(len(attribute.attributes), 3)
        sub_attribute = attribute.attributes[0]
        self.assertEqual(sub_attribute.code, '6063')
        self.assertEqual(sub_attribute.name, 'Quantity type code qualifier')
        self.assertEqual(sub_attribute.desc, 'Code qualifying the type of quantity.')
        self.assertEqual(sub_attribute.repeat, 'Mandatory')
        self.assertEqual(sub_attribute.type, 'an')
        self.assertEqual(sub_attribute.length, '0..3')
        self.assertEquals(sub_attribute.codeset, '6063')
        self.assertEqual(len(sub_attribute.attributes), 0)
        sub_attribute = attribute.attributes[1]
        self.assertEqual(sub_attribute.code, '6060')
        self.assertEqual(sub_attribute.name, 'Quantity')
        self.assertEqual(sub_attribute.desc, 'Alphanumeric representation of a quantity.')
        self.assertEqual(sub_attribute.repeat, 'Mandatory')
        self.assertEqual(sub_attribute.type, 'an')
        self.assertEqual(sub_attribute.length, '0..35')
        self.assertEquals(sub_attribute.codeset, None)
        self.assertEqual(len(sub_attribute.attributes), 0)
        sub_attribute = attribute.attributes[2]
        self.assertEqual(sub_attribute.code, '6411')
        self.assertEqual(sub_attribute.name, 'Measurement unit code')
        self.assertEqual(sub_attribute.desc, 'Code specifying the unit of measurement.')
        self.assertEqual(sub_attribute.repeat, 'Conditional')
        self.assertEqual(sub_attribute.type, 'an')
        self.assertEqual(sub_attribute.length, '0..8')
        self.assertEquals(sub_attribute.codeset, None)
        self.assertEqual(len(sub_attribute.attributes), 0)



    def test_group_two_sections(self):
        html_text = """
        <div id="container">
            <div id="view-message">
                <div class="aggr grp">
                    <h3><a href="#"><span>GRP1</span><span> <span class="g_s">RFF</span> <span
                                    class="g_s">DTM</span></span><span>C 99</span></a></h3>
                    <div>
                        <div><span>99</span><span>Conditional</span> A group of segments to identify the unique
                            reference number and date time details for the whole message.</div>
                        <div>
                            <div class="aggr seg">
                                <h3><a href="/edifact/d03a/rff/"><span>RFF</span><span>REFERENCE</span><span>M
                                            1</span></a></h3>
                                <div>
                                    <div><span>1</span><span>Mandatory</span> A segment to provide the unique reference
                                        number for the message, e.g. manifest number.</div>
                                    <div>
                                        <div class="com elm">
                                            <div>C506</div>
                                            <div>REFERENCE</div>
                                            <div><span>Mandatory</span></div>
                                            <div>Identification of a reference. </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="aggr seg">
                                <h3><a href="/edifact/d03a/dtm/"><span>DTM</span><span>DATE/TIME/PERIOD</span><span>C
                                            9</span></a></h3>
                                <div>
                                    <div><span>9</span><span>Conditional</span> A segment to indicate the date/time of
                                        the reference number for the message.</div>
                                    <div>
                                        <div class="com elm">
                                            <div>C507</div>
                                            <div>DATE/TIME/PERIOD</div>
                                            <div><span>Mandatory</span></div>
                                            <div>Date and/or time, or period relevant to the specified date/time/period
                                                type. </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        parser = parse.FormatParser()
        parser.parse(html_text)
        self.assertEqual(len(parser.my_sections), 1)
        grp = parser.my_sections[0]
        self.assertEqual(grp.code, 'GRP1')
        self.assertEqual(grp.name, None)
        self.assertEqual(grp.desc, 'A group of segments to identify the unique reference number and date time details for the whole message.')
        self.assertEqual(grp.repeat, 'Conditional 99')
        self.assertEqual(len(grp.sections), 2)
        section = grp.sections[0]
        self.assertEqual(section.code, 'RFF')
        self.assertEqual(section.name, 'REFERENCE')
        self.assertEqual(section.desc, 'A segment to provide the unique reference number for the message, e.g. manifest number.')
        self.assertEqual(section.repeat, 'M 1')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, 'C506')
        self.assertEqual(attribute.name, 'REFERENCE')
        self.assertEqual(attribute.desc, 'Identification of a reference.')
        self.assertEqual(attribute.repeat, 'Mandatory')
        self.assertEqual(len(attribute.attributes), 0)
        section = grp.sections[1]
        self.assertEqual(section.code, 'DTM')
        self.assertEqual(section.name, 'DATE/TIME/PERIOD')
        self.assertEqual(section.desc, 'A segment to indicate the date/time of the reference number for the message.')
        self.assertEqual(section.repeat, 'C 9')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, 'C507')
        self.assertEqual(attribute.name, 'DATE/TIME/PERIOD')
        self.assertEqual(attribute.desc, 'Date and/or time, or period relevant to the specified date/time/period type.')
        self.assertEqual(attribute.repeat, 'Mandatory')
        self.assertEqual(len(attribute.attributes), 0)


    def test_group_with_section_and_embedded_group(self):
        html_text = """
        <div id="container">
            <div id="view-message">
                <div class="aggr grp">
                    <h3><a href="#"><span>GRP2</span><span> <span class="g_s">NAD</span> <span class="g_s">DTM</span>
                                <span class="g_g">GRP3</span></span><span>C 99</span></a></h3>
                    <div>
                        <div><span>99</span><span>Conditional</span> A group of segments to identify contact and
                            communication contact information related to the person responsible for the cargo reporting
                            and/or to report crew members on a conveyance.</div>
                        <div>
                            <div class="aggr seg">
                                <h3><a href="/edifact/d03a/nad/"><span>NAD</span><span>NAME AND ADDRESS</span><span>M
                                            1</span></a></h3>
                                <div>
                                    <div><span>1</span><span>Mandatory</span> A segment to identify the person or party
                                        reporting the cargo and/or acting as a crew member on a conveyance.</div>
                                    <div>
                                        <div class="elm e">
                                            <div>3035</div>
                                            <div>PARTY FUNCTION CODE QUALIFIER</div>
                                            <div><span>Mandatory</span><span>an</span><span>0..3</span></div>
                                            <div>Code giving specific meaning to a party.</div><a
                                                href="/edifact/d03a/cl3035/" rel="nofollow" title="3035">Show all
                                                standard codes</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="aggr grp">
                                <h3><a href="#"><span>GRP3</span><span> <span class="g_s">CTA</span> <span
                                                class="g_s">COM</span></span><span>C 9</span></a></h3>
                                <div>
                                    <div><span>9</span><span>Conditional</span> A group of segments to identify a
                                        contact and its communication related party.</div>
                                    <div>
                                        <div class="aggr seg">
                                            <h3><a href="/edifact/d03a/cta/"><span>CTA</span><span>CONTACT
                                                        INFORMATION</span><span>M 1</span></a></h3>
                                            <div>
                                                <div><span>1</span><span>Mandatory</span> A segment to identify a person
                                                    or department within a party.</div>
                                                <div>
                                                    <div class="elm e">
                                                        <div>3139</div>
                                                        <div>CONTACT FUNCTION CODE</div>
                                                        <div><span>Conditional</span><span>an</span><span>0..3</span>
                                                        </div>
                                                        <div>Code specifying the function of a contact (e.g. department
                                                            or person).</div><a href="/edifact/d03a/cl3139/"
                                                            rel="nofollow" title="3139">Show all standard codes</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        parser = parse.FormatParser()
        parser.parse(html_text)
        self.assertEqual(len(parser.my_sections), 1)
        grp = parser.my_sections[0]
        self.assertEqual(grp.code, 'GRP2')
        self.assertEqual(grp.name, None)
        self.assertEqual(grp.desc, 'A group of segments to identify contact and communication contact information related to the person responsible for the cargo reporting and/or to report crew members on a conveyance.')
        self.assertEqual(grp.repeat, 'Conditional 99')
        self.assertEqual(len(grp.sections), 2)
        section = grp.sections[0]
        self.assertEqual(section.code, 'NAD')
        self.assertEqual(section.name, 'NAME AND ADDRESS')
        self.assertEqual(section.desc, 'A segment to identify the person or party reporting the cargo and/or acting as a crew member on a conveyance.')
        self.assertEqual(section.repeat, 'M 1')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, '3035')
        self.assertEqual(attribute.name, 'PARTY FUNCTION CODE QUALIFIER')
        self.assertEqual(attribute.desc, 'Code giving specific meaning to a party.')
        self.assertEqual(attribute.repeat, 'Mandatory')
        self.assertEqual(attribute.type, 'an')
        self.assertEqual(attribute.length, '0..3')
        self.assertEquals(attribute.codeset, '3035')
        self.assertEqual(len(attribute.attributes), 0)
        sub_grp = grp.sections[1]
        self.assertEqual(sub_grp.code, 'GRP3')
        self.assertEqual(sub_grp.name, None)
        self.assertEqual(sub_grp.desc, 'A group of segments to identify a contact and its communication related party.')
        self.assertEqual(sub_grp.repeat, 'Conditional 9')
        self.assertEqual(len(sub_grp.sections), 1)
        section = sub_grp.sections[0]
        self.assertEqual(section.code, 'CTA')
        self.assertEqual(section.name, 'CONTACT INFORMATION')
        self.assertEqual(section.desc, 'A segment to identify a person or department within a party.')
        self.assertEqual(section.repeat, 'M 1')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, '3139')
        self.assertEqual(attribute.name, 'CONTACT FUNCTION CODE')
        self.assertEqual(attribute.desc, 'Code specifying the function of a contact (e.g. department or person).')
        self.assertEqual(attribute.repeat, 'Conditional')
        self.assertEqual(attribute.type, 'an')
        self.assertEqual(attribute.length, '0..3')
        self.assertEquals(attribute.codeset, '3139')
        self.assertEqual(len(attribute.attributes), 0)


    def test_group_with_embedded_group_with_embedded_group(self):
        html_text = """
        <div id="container">
            <div id="view-message">
                <div class="aggr grp">
                    <h3><a href="#"><span>GRP7</span><span> <span class="g_s">CNI</span> <span class="g_s">CNT</span>
                                <span class="g_g">GRP8</span></span><span>C 9999</span></a></h3>
                    <div>
                        <div><span>9999</span><span>Conditional</span> A group of segments to provide details of the
                            consignment(s).</div>
                        <div>
                            <div class="aggr seg">
                                <h3><a href="/edifact/d03a/cni/"><span>CNI</span><span>CONSIGNMENT
                                            INFORMATION</span><span>M 1</span></a></h3>
                                <div>
                                    <div><span>1</span><span>Mandatory</span> A segment to sequentially number master
                                        bills reported in a multi-consignment message. For a single consignment message,
                                        this sequence number will always be 1.</div>
                                    <div>
                                        <div class="elm e">
                                            <div>1490</div>
                                            <div>CONSOLIDATION ITEM NUMBER</div>
                                            <div><span>Conditional</span><span>n</span><span>0..4</span></div>
                                            <div>To specify a consignment within a consolidation.</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="aggr grp">
                                <h3><a href="#"><span>GRP8</span><span> <span class="g_s">RFF</span> <span
                                                class="g_s">CNT</span> <span class="g_s">MOA</span> <span
                                                class="g_s">LOC</span> <span class="g_s">GEI</span> <span
                                                class="g_s">CUX</span> <span class="g_s">CPI</span> <span
                                                class="g_g">GRP9</span> <span class="g_g">GRP11</span> <span
                                                class="g_g">GRP13</span> <span class="g_g">GRP14</span></span><span>C
                                            9999</span></a></h3>
                                <div>
                                    <div><span>9999</span><span>Conditional</span> A group of segments specifying the
                                        details of each consignment.</div>
                                    <div>
                                    <div class="aggr seg">
                                            <h3><a href="/edifact/d03a/cpi/"><span>CPI</span><span>CHARGE PAYMENT
                                                        INSTRUCTIONS</span><span>C 9</span></a></h3>
                                            <div>
                                                <div><span>9</span><span>Conditional</span> A segment to specify the
                                                    cargo category type, e.g. weight valuation, prepaid/collect and
                                                    method of payment.</div>
                                                <div>
                                                   <div class="elm e">
                                                        <div>4237</div>
                                                        <div>PAYMENT ARRANGEMENT CODE</div>
                                                        <div><span>Conditional</span><span>an</span><span>0..3</span>
                                                        </div>
                                                        <div>Code specifying the arrangements for a payment.</div><a
                                                            href="/edifact/d03a/cl4237/" rel="nofollow"
                                                            title="4237">Show all standard codes</a>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="aggr grp">
                                            <h3><a href="#"><span>GRP9</span><span> <span class="g_s">TDT</span> <span
                                                            class="g_s">LOC</span> <span class="g_s">DTM</span> <span
                                                            class="g_s">MEA</span> <span
                                                            class="g_g">GRP10</span></span><span>C 9</span></a></h3>
                                            <div>
                                                <div><span>9</span><span>Conditional</span> A group of segments to
                                                    identify details of onward carriage for each consignment.</div>
                                                <div>
                                                    <div class="aggr seg">
                                                        <h3><a href="/edifact/d03a/tdt/"><span>TDT</span><span>TRANSPORT
                                                                    INFORMATION</span><span>M 1</span></a></h3>
                                                        <div>
                                                            <div><span>1</span><span>Mandatory</span> A segment to
                                                                specify the identity of the onward conveyance.</div>
                                                            <div>
                                                                <div class="elm e">
                                                                    <div>8051</div>
                                                                    <div>TRANSPORT STAGE CODE QUALIFIER</div>
                                                                    <div>
                                                                        <span>Mandatory</span><span>an</span><span>0..3</span>
                                                                    </div>
                                                                    <div>Code qualifying a specific stage of transport.
                                                                    </div><a href="/edifact/d03a/cl8051/" rel="nofollow"
                                                                        title="8051">Show all standard codes</a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            <div>
        </div>
        """
        parser = parse.FormatParser()
        parser.parse(html_text)
        self.assertEqual(len(parser.my_sections), 1)
        grp = parser.my_sections[0]
        self.assertEqual(grp.code, 'GRP7')
        self.assertEqual(grp.name, None)
        self.assertEqual(grp.desc, 'A group of segments to provide details of the consignment(s).')
        self.assertEqual(grp.repeat, 'Conditional 9999')
        self.assertEqual(len(grp.sections), 2)
        section = grp.sections[0]
        self.assertEqual(section.code, 'CNI')
        self.assertEqual(section.name, 'CONSIGNMENT INFORMATION')
        self.assertEqual(section.desc, 'A segment to sequentially number master bills reported in a multi-consignment message. For a single consignment message, this sequence number will always be 1.')
        self.assertEqual(section.repeat, 'M 1')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, '1490')
        self.assertEqual(attribute.name, 'CONSOLIDATION ITEM NUMBER')
        self.assertEqual(attribute.desc, 'To specify a consignment within a consolidation.')
        self.assertEqual(attribute.repeat, 'Conditional')
        self.assertEqual(attribute.type, 'n')
        self.assertEqual(attribute.length, '0..4')
        self.assertEqual(len(attribute.attributes), 0)
        sub_grp = grp.sections[1]
        self.assertEqual(sub_grp.code, 'GRP8')
        self.assertEqual(sub_grp.name, None)
        self.assertEqual(sub_grp.desc, 'A group of segments specifying the details of each consignment.')
        self.assertEqual(sub_grp.repeat, 'Conditional 9999')
        self.assertEqual(len(sub_grp.sections), 2)
        section = sub_grp.sections[0]
        self.assertEqual(section.code, 'CPI')
        self.assertEqual(section.name, 'CHARGE PAYMENT INSTRUCTIONS')
        self.assertEqual(section.desc, 'A segment to specify the cargo category type, e.g. weight valuation, prepaid/collect and method of payment.')
        self.assertEqual(section.repeat, 'C 9')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, '4237')
        self.assertEqual(attribute.name, 'PAYMENT ARRANGEMENT CODE')
        self.assertEqual(attribute.desc, 'Code specifying the arrangements for a payment.')
        self.assertEqual(attribute.repeat, 'Conditional')
        self.assertEqual(attribute.type, 'an')
        self.assertEqual(attribute.length, '0..3')
        self.assertEquals(attribute.codeset, '4237')
        self.assertEqual(len(attribute.attributes), 0)
        sub_grp2 = sub_grp.sections[1]
        self.assertEqual(sub_grp2.code, 'GRP9')
        self.assertEqual(sub_grp2.name, None)
        self.assertEqual(sub_grp2.desc, 'A group of segments to identify details of onward carriage for each consignment.')
        self.assertEqual(sub_grp2.repeat, 'Conditional 9')
        self.assertEqual(len(sub_grp2.sections), 1)
        section = sub_grp2.sections[0]
        self.assertEqual(section.code, 'TDT')
        self.assertEqual(section.name, 'TRANSPORT INFORMATION')
        self.assertEqual(section.desc, 'A segment to specify the identity of the onward conveyance.')
        self.assertEqual(section.repeat, 'M 1')
        self.assertEqual(len(section.attributes), 1)
        attribute = section.attributes[0]
        self.assertEqual(attribute.code, '8051')
        self.assertEqual(attribute.name, 'TRANSPORT STAGE CODE QUALIFIER')
        self.assertEqual(attribute.desc, 'Code qualifying a specific stage of transport.')
        self.assertEqual(attribute.repeat, 'Mandatory')
        self.assertEqual(attribute.type, 'an')
        self.assertEqual(attribute.length, '0..3')
        self.assertEquals(attribute.codeset, '8051')
        self.assertEqual(len(attribute.attributes), 0)

if __name__ == '__main__':
    unittest.main()
