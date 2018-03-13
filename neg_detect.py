from konlpy.tag import Komoran

komoran = Komoran()

def detect(sentence):
    pos_result = komoran.pos(sentence)
    max_len = len(pos_result)

    negs = []
    for i, (morph, pos) in enumerate(pos_result):
        if (morph == '안' or morph == '못') and pos == 'MAG' and i < max_len-1:
            nxt = i+1
            if pos_result[nxt][1] == 'VV' or \
                pos_result[nxt][1] == 'VA' or \
                pos_result[nxt][1] == 'VX':
                negs.append("NEG: {} -> {}".format(morph, pos_result[i+1][0]))

        if (morph == '않') and pos == 'VX' and i > 1:
           prepre = i-2
           pre = i-1
           if ((pos_result[i-2][1] == 'VV' or \
                   pos_result[i-2][1] == 'VA' or \
                   pos_result[i-2][1] == 'XSV') and pos_result[i-1][1] == 'EC') or \
              (pos_result[i-2][1] == 'NNG' and \
                   (pos_result[i-1][1] == 'JKO' or pos_result[i-1][1] == 'JX')):
                negs.append("NEG: {} -> {}".format(morph, pos_result[i-2][0]))

    #print(pos_result)
    for e in negs:
        print(e)
