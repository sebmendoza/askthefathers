import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re


class ThMLParser:
    def __init__(self):
        self.metadata = {}
        self.sections = []

    def split_into_sentences(self, text):
        """Split text into sentences using regex patterns"""
        # Pattern matches sentence endings while preserving abbreviations like "St.", "Mr.", etc.
        pattern = r'(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])'
        sentences = re.split(pattern, text)
        # Further split on other punctuation if needed
        all_sentences = []
        for sentence in sentences:
            # Split on question marks and exclamation points that aren't already at the end
            subsents = re.split(r'(?<!\.)(?<=\?|\!)\s+(?=[A-Z])', sentence)
            all_sentences.extend(subsents)
        return [s.strip() for s in all_sentences if s.strip()]

    def parse_document(self, thml_content):
        """Parse ThML document and extract structured content"""
        # Clean up any XML declarations
        thml_content = re.sub(r'<\?xml.*?\?>', '', thml_content)

        # Parse the XML
        try:
            root = ET.fromstring(thml_content)
        except ET.ParseError as e:
            # Fall back to BeautifulSoup if XML is malformed
            soup = BeautifulSoup(thml_content, 'xml')
            root = soup.find('ThML')

        # Extract metadata from ThML.head
        head = root.find('ThML.head')
        if head is not None:
            self.parse_metadata(head)

        # Extract content from ThML.body
        body = root.find('ThML.body')
        if body is not None:
            self.parse_body(body)

        return {
            'metadata': self.metadata,
            'sections': self.sections
        }

    def parse_metadata(self, head):
        """Extract metadata from ThML.head section"""
        # Extract Dublin Core metadata
        dc = head.find('DC')
        if dc is not None:
            for element in dc:
                tag = element.tag.replace('DC.', '').lower()
                self.metadata[tag] = element.text

        # Extract other important metadata
        for element in ['description', 'firstPublished', 'pubHistory']:
            elem = head.find(f'.//{element}')
            if elem is not None:
                self.metadata[element] = elem.text

    def parse_body(self, body, current_path=''):
        """Recursively parse body content, preserving structure and creating sentence-level chunks"""
        for element in body:
            # Handle different types of divisions
            if element.tag.startswith('div'):
                # Create a section entry for the division title
                if 'title' in element.attrib:
                    self.sections.append({
                        'type': 'title',
                        'content': element.get('title'),
                        'metadata': {
                            'type': element.get('type', ''),
                            'path': f"{current_path}/{element.get('n', '')}".strip('/'),
                            'level': element.tag[3] if len(element.tag) > 3 else '1'
                        }
                    })

                # Parse content within this division
                self.parse_body(
                    element, f"{current_path}/{element.get('n', '')}".strip('/'))
            else:
                # Process the content and break into sentences
                content = self.process_element(element)
                if content.strip():
                    sentences = self.split_into_sentences(content)
                    for sentence in sentences:
                        if sentence.strip():
                            self.sections.append({
                                'type': 'sentence',
                                'content': sentence.strip(),
                                'metadata': {
                                    'path': current_path,
                                    'element_type': element.tag
                                }
                            })

    def process_element(self, element):
        """Process individual elements, preserving semantic information"""
        text = ''

        # Handle element-specific processing
        if element.tag in ['scripRef', 'scripture', 'scripCom']:
            # Handle scripture references with their attributes
            attrs = ' '.join([f'{k}="{v}"' for k, v in element.attrib.items()])
            text += f"[{element.tag}: {attrs}] {element.text or ''} "
        elif element.tag == 'note':
            # Handle footnotes and annotations
            text += f"[Note: {element.text or ''}] "
        elif element.tag == 'foreign':
            # Handle foreign language text
            lang = element.get('lang', '')
            text += f"[{lang}: {element.text or ''}] "
        elif element.text:
            text += element.text + ' '

        # Process child elements recursively
        for child in element:
            text += self.process_element(child)
            if child.tail:
                text += child.tail + ' '

        return text.strip()

    def get_chunks(self):
        """Return all chunks (titles and sentences) with their metadata"""
        return self.sections


def process_thml_for_rag(thml_content):
    """Process ThML content and return chunks with metadata"""
    parser = ThMLParser()
    parsed_content = parser.parse_document(thml_content)
    chunks = parser.get_chunks()

    return {
        'metadata': parsed_content['metadata'],    # Document-level metadata
        'chunks': chunks                          # Sentence-level chunks and titles
    }


# Example usage
if __name__ == "__main__":
    with open('../xmls/ignatius.xml', 'r') as file:
        thml_content = file.read()

    processed = process_thml_for_rag(thml_content)

    # Print document metadata
    print("\nDocument Metadata:")
    for key, value in processed['metadata'].items():
        if value:  # Only print non-empty metadata
            print(f"{key}: {value[:100]}...")  # Print first 100 chars of value

    # Print some sample chunks
    print("\nSample Chunks:")
    for i, chunk in enumerate(processed['chunks'][5:]):  # Print first 5 chunks
        print(f"\nChunk {i+1}:")
        print(f"Type: {chunk['type']}")
        print(f"Content: {chunk['content']}...")  # First 100 chars
        print(f"Metadata: {chunk['metadata']}")
