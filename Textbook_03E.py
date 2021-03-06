#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Greedy Motif Search with Pseudocounts
Chapter #: 03
Problem ID: E
URL: http://rosalind.info/problems/3e/
'''

from Textbook_03C import profile_most_probable_kmer
from Textbook_03D import score


def profile_with_pseudocounts(motifs):
    '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)+1) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search_pseudocounts(dna_list, k, t):
    '''Runs the Greedy Motif Search with Pseudocounts algorithm and retuns the best motif.'''
    # Initialize the best score as a score higher than the highest possible score.
    best_score = t*k

    # Run the greedy motif search.
    for i in xrange(len(dna_list[0]) - k + 1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [dna_list[0][i:i + k]]

        # Find the most probable k-mer in the next string, using pseudocounts.
        for j in xrange(1, t):
            current_profile = profile_with_pseudocounts(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        # Check to see if we have a new best scoring list of motifs.
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_3e.txt') as input_data:
        k, t = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data]

    # Run the Greedy Motif Search with Pseudocounts.
    best_motifs = greedy_motif_search_pseudocounts(dna_list, k, t)

    # Print and save the answer.
    print '\n'.join(best_motifs)
    with open('output/textbook/Textbook_03E.txt', 'w') as output_data:
        output_data.write('\n'.join(best_motifs))

if __name__ == '__main__':
    main()
