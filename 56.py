#56. 共参照解析
import xml.etree.ElementTree as ET

root = ET.parse("nlp.txt.xml")

rep_dict = {}
for coreference in root.iterfind('./document/coreference/coreference'):

    rep_text = coreference.findtext('./mention[@representative="true"]/text')

    for mention in coreference.iterfind('./mention'):
        if mention.get('representative', 'false') == 'false':

            sent_id = int(mention.findtext('sentence'))
            start = int(mention.findtext('start'))
            end = int(mention.findtext('end'))

            if not (sent_id, start) in rep_dict:
                rep_dict[(sent_id, start)] = (end, rep_text)

for sentence in root.iterfind('./document/sentences/sentence'):
    sent_id = int(sentence.get('id'))
    org_rest = 0

    for token in sentence.iterfind('./tokens/token'):
        token_id = int(token.get('id'))

        if org_rest == 0 and (sent_id, token_id) in rep_dict:

            (end, rep_text) = rep_dict[(sent_id, token_id)]

            print('[' + rep_text + '] (', end='')
            org_rest = end - token_id

        print(token.findtext('word'), end='')

        if org_rest > 0:
            org_rest -= 1
            if org_rest == 0:
                print(')', end='')

        print(' ', end='')

    print()
