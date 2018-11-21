import xml.dom.minidom
class Create_Xml:
    def __init__(self):
        self.doc = xml.dom.minidom.Document()

    def create_node(self, xml_node, xml_node_name=None):
        if xml_node_name:
            tmp_node = self.doc.createElement(xml_node)
            tmp_node.appendChild(self.doc.createTextNode(xml_node_name))
        else:
            tmp_node = self.doc.createElement(xml_node)
        return tmp_node

    def father_link_child(self, child_node, father_node=None):
        if father_node:
            father_node.appendChild(child_node)
        else:
            self.doc.appendChild(child_node)

    def create_node_to_link(self, child_xml_node, child_xml_node_name=None, father_node=None):
        child_node = self.create_node(child_xml_node, child_xml_node_name)
        self.father_link_child(child_node, father_node)
        return child_node

    def create_xml_file(self, xml_path):
        fp = open(xml_path, 'w')
        self.doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='uft-8')


if __name__ == '__main__':
    CX=Create_Xml()
    root_node = CX.create_node('root_node')
    CX.father_link_child(root_node)
    child_node = CX.create_node('child_node', 'hello Xml')
    CX.father_link_child(child_node, root_node)
    CX.create_xml_file('text.xml')
    CX1 = Create_Xml()
    root_node = CX1.create_node_to_link('root_node_2')
    CX1.create_node_to_link('child_node_2', 'Hello to Swift', root_node)
    CX1.create_xml_file('test2.xml')