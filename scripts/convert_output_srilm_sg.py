import numpy as np
import argparse

# def get_surprisals(infile, outfile):
#     '''
#     Converts output of SRILM language model to tab-separated file
#     with two columns of the format <token\tsurprisal>.    
#     '''

#     with open(infile, 'r') as f:
#         lines = f.readlines()
#     lines = [s.strip('\n') for s in lines]

#     # get lines with probabilities, ignoring eos token
#     lines = [s for s in lines if ('p(' in s and '</s>' not in s)]
#     # print(lines)

#     # get tokens and probability values (strings)
#     splits = [s.split('=') for s in lines]
#     # print(splits)
#     tokens = [t[0].split('|')[0][4:-1] for t in splits]
#     probs = [t[1].split(']')[1] for t in splits]

#     # convert to floats
#     probs = np.array([float(p.split('[')[0].strip(' ')) for p in probs])
#     surprisals = np.log2(1 / probs)

#     with open(outfile, 'w') as f:
#         for i in range(len(tokens)):
#             f.write('{}\t{}\n'.format(tokens[i], surprisals[i]))

def get_surprisals(infile):
    '''
    Converts output of SRILM language model to tab-separated file
    with two columns of the format <token\tsurprisal>.    
    '''

    with open(infile, 'r') as f:
        lines = f.readlines()

    sentence_iter = 0
    token_iter = 0
    print('sentence_id\ttoken_id\ttoken\tsurprisal')
    for line in lines:
        line = line.strip('\n')
        if '<s>' in line:
            sentence_iter += 1
            token_iter = 0
        # get lines with probabilities, ignoring eos token
        if 'p(' in line and '</s>' not in line:
            token_iter += 1
            split = line.split('=')
            token = split[0].split('|')[0][4:-1]
            prob = split[1].split(']')[1]
            prob = float(prob.split('[')[0].strip(' '))
            surprisal = np.log2(1 / prob)
            print('{}\t{}\t{}\t{}'.format(sentence_iter, token_iter, token, surprisal))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reformat output of SRILM language model.')
    parser.add_argument('--infile', '-infile', type=str,
                        help='path to raw SRILM file')
    parser.add_argument('--outfile', '-outfile', type=str,
                         help='path to output file')
    args = parser.parse_args()

    get_surprisals(args.infile) #, args.outfile)