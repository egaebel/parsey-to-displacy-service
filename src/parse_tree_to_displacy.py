def parse_tree_to_displacy_tree(root):
    """
    Takes a tree root of type ParseNode.
    Traverses the tree and constructs JSON to fit the displacy JSON format.
    Example of format:
    {
        "arcs": [
            {
              "dir": "left", 
              "end": 1, 
              "label": "nsubj", 
              "start": 0
            }, 
            {
              "dir": "left", 
              "end": 3, 
              "label": "advmod", 
              "start": 2
            }, 
            {
              "dir": "right", 
              "end": 3, 
              "label": "acomp", 
              "start": 1
            }
        ], 
        "words": [
            {
              "tag": "PRP", 
              "text": "I"
            }, 
            {
              "tag": "VBP", 
              "text": "am"
            }, 
            {
              "tag": "RB", 
              "text": "very"
            }, 
            {
              "tag": "JJ", 
              "text": "impressed."
            }
        ]
    }
    """
    arcs = []
    words = []
    sentence_list = root.to_list()
    sentence_list.sort(key=lambda node: node.sentence_word_order)
    for node in sentence_list:
        words.append(_create_word(node))
    for edge in root.get_edges():
        arcs.append(_create_arc(edge))

    return {"arcs": arcs, "words": words}


def _create_arc(edge):
    from_node = edge[0]
    to_node = edge[1]
    end = min(from_node.sentence_word_order, to_node.sentence_word_order)
    start = max(from_node.sentence_word_order, to_node.sentence_word_order)
    return {
        "dir": "right" if from_node.sentence_word_order < to_node.sentence_word_order else "left",
        "end": start,
        "label": to_node.sentence_role,
        "start": end
    }

def _create_word(node):
    return {"tag": node.part_of_speech, "text": node.word}