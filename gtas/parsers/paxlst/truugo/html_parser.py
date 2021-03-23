import re
from bs4 import BeautifulSoup, Tag, NavigableString


class MySection:
    def __init__(self):
        self.code = ""
        self.name = ""
        self.repeat = ""
        self.content = ""
        self.desc = ""
        self.attributes = []

    def __str__(self):
        str_result = f'{self.code}({self.name}): {self.desc} : {self.repeat}'
        str_result += "\n--" + str.join('\n--', [s.__str__() for s in self.attributes])
        return str_result

class MyGroup():
    def __init__(self):
        self.code = ""
        self.name = None
        self.repeat = ""
        self.content = ""
        self.desc = ""
        self.sections = []

    def __str__(self):
        str_result = f'{self.code}: {self.desc} : {self.repeat}'
        str_result += "\n" + str.join('\n', [s.__str__() for s in self.sections])
        return str_result

class MyAttribute:
    def __init__(self):
        self.content = ""
        self.sub_content = ""
        self.code = ""
        self.name = ""
        self.desc = ""
        self.type = ""
        self.length = ""
        self.attributes = []

    def __str__(self):
        str_result = f'{self.code}({self.name}) : {self.desc}'
        if len(self.attributes) > 0:
            str_result += "\n----" + str.join('\n----', [s.__str__() for s in self.attributes])
        return str_result


class FormatParser():
    def __init__(self):
        self.my_sections = [] 

    def _decode_attribute(self, attribute_div):
        attribute = MyAttribute()
        attribute.content = attribute_div
        attribute_parts = attribute_div.find_all("div")
        attribute.code = attribute_parts[0].string
        attribute.name = self.fix_whitespace(attribute_parts[1].string)
        if isinstance(attribute_parts[2], Tag):
            repeat_parts = attribute_parts[2].find_all("span")
            attribute.repeat = repeat_parts[0].string
            if len(repeat_parts) > 1:
                # <div><span>Mandatory</span><span>an</span><span>0..3</span></div>
                attribute.type = repeat_parts[1].string
                attribute.length = repeat_parts[2].string
            else:    
                # <div><span>Mandatory</span></div>
                attribute.length = None
                attribute.type = None
        attribute.desc = self.fix_whitespace(attribute_parts[3].string.strip())
        # if it is a codeset there is an ahref sibling to the description
        possible_codeset_link = attribute_parts[3].find_next_sibling("a")
        if possible_codeset_link:
            attribute.codeset = possible_codeset_link['title']
        else:
            attribute.codeset = None
        return attribute

    def _decode_section_title(self, my_sec, section_heading):
        # UNH         MESSAGE HEADER       M 1
        title_parts = section_heading.find_all("span")
        my_sec.code = title_parts[0].string
        my_sec.name = self.fix_whitespace(title_parts[1].string)
        my_sec.repeat = self.fix_whitespace(title_parts[2].string)
        # Section description block
        section_desc = section_heading.find_next_sibling("div").find_all("div")[0] 
        desc = section_desc.find_all("span")[1].next_sibling.strip()
        if desc != None:
            my_sec.desc = self.fix_whitespace(desc)
        else:
            my_sec.desc = None

    def _decode_group_title(self, my_grp, group_heading):
        #<h3><a href="#"><span>GRP1</span><span> <span class="g_s">RFF</span> <span class="g_s">DTM</span></span><span>C 99</span></a></h3>
        title_parts = group_heading.find_all("span")
        my_grp.code = title_parts[0].string
        # Group description block
        section_desc = group_heading.find_next_sibling("div").find_all("div")[0]
        group_desc_parts = section_desc.find_all('span') 
        my_grp.repeat = group_desc_parts[1].string
        my_grp.repeat += ' ' + group_desc_parts[0].string
        desc = group_desc_parts[1].next_sibling.strip()
        if desc != None:
            my_grp.desc = self.fix_whitespace(desc)
        else:
            my_grp.desc = None

    def fix_whitespace(self, a_string):
        result = a_string.strip().replace('\n', ' ').replace('\r', '')
        while '  ' in result:
            result = result.replace('  ', ' ')
        return result

    def _next_non_string_sibling(self, tag):
        t = tag.next_sibling
        while isinstance(t, NavigableString):
            t = t.next_sibling
        return t

    def _decode_section(self, my_sec, section):
        # Section title is first child as h3
        #print(section.find_all("h3"))
        section_heading = section.find_all("h3")[0]
        self._decode_section_title(my_sec, section_heading)
        # Section attribute content is second div of the first sibling of the h3
        content = self._next_non_string_sibling(section_heading).find_all("div")[1]
        
        last_attribute = None
        for attribute_div in content.children:
            if isinstance(attribute_div, Tag):
                # a repeating set of divs, either top level attribute which has a class or parent div for sub attributes
                if attribute_div.has_attr('class'):
                    # A top level segment attribute
                    attribute = self._decode_attribute(attribute_div)
                    my_sec.attributes.append(attribute)
                    last_attribute = attribute
                else:
                    # nested attribute content
                    last_attribute.sub_content = attribute_div
                    # a list of normal attribues within a parent <div>
                    for sub_attribute_div in attribute_div.children:
                        if isinstance(sub_attribute_div, Tag):
                            # Nested segment attribute
                            attribute = self._decode_attribute(sub_attribute_div)
                            last_attribute.attributes.append(attribute)

    def _decode_group(self, my_grp, group):
        # Group title is first child as h3
        group_heading = group.find_all("h3")[0]
        self._decode_group_title(my_grp, group_heading)
        # the list of sections starts from the second div of the fist div sibling of the h3
        content = self._next_non_string_sibling(group_heading).find_all("div")[1]
        sections = content.children
        for section in sections:
            if isinstance(section, Tag):
                if 'class' in section.attrs:
                    if 'seg' in section['class']:
                        my_sec = MySection()
                        self._decode_section(my_sec, section)
                        my_grp.sections.append(my_sec)   
                    if 'grp' in section['class']:
                        my_sub_grp = MyGroup()
                        my_grp.sections.append(my_sub_grp)
                        self._decode_group(my_sub_grp, section)

    def parse(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        # Find all div children of the #view-message tag
        sections = soup.select("#view-message")[0].children

        for section in sections:
            if isinstance(section, Tag):
                if 'class' in section.attrs:
                    #print(section['class'])
                    if 'grp' in section['class']:
                        my_grp = MyGroup()
                        self.my_sections.append(my_grp)
                        self._decode_group(my_grp, section)
                    else: 
                        my_sec = MySection()
                        self.my_sections.append(my_sec)
                        self._decode_section(my_sec, section)

