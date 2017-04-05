"""
Copyright 2017 Ryan Wick (rrwick@gmail.com)
https://github.com/rrwick/Porechop

This module contains the class and sequences for known adapters used in Oxford Nanopore library
preparation kits.

This file is part of Porechop. Porechop is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. Porechop is distributed in
the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details. You should have received a copy of the GNU General Public License along with Porechop. If
not, see <http://www.gnu.org/licenses/>.
"""


class Adapter(object):

    def __init__(self, name, start_sequence=None, end_sequence=None, both_ends_sequence=None):
        self.name = name
        self.start_sequence = start_sequence if start_sequence else []
        self.end_sequence = end_sequence if end_sequence else []
        if both_ends_sequence:
            self.start_sequence = both_ends_sequence
            self.end_sequence = both_ends_sequence
        self.best_start_score, self.best_end_score = 0.0, 0.0

    def best_start_or_end_score(self):
        return max(self.best_start_score, self.best_end_score)

    def is_barcode(self):
        return 'barcod' in self.name  # will catch 'barcode' and 'barcoding'

    def get_barcode_name(self):
        """
        Gets the barcode name for the output files. We want a concise name, so it looks at all
        options and chooses the shortest.
        """
        possible_names = [self.name, self.start_sequence[0], self.end_sequence[0]]
        barcode_name = sorted(possible_names, key=lambda x: len(x))[0]
        return barcode_name.replace(' ', '_')



ADAPTERS = [

            Adapter('SQK-MAP006',
                    start_sequence=('SQK-MAP006_Y_Top_SK63',    'GGTTGTTTCTGTTGGTGCTGATATTGCT'),
                    end_sequence=  ('SQK-MAP006_Y_Bottom_SK64', 'GCAATATCAGCACCAACAGAAA')),
            Adapter('SQK-MAP006 Short',
                    start_sequence=('SQK-MAP006_Short_Y_Top_LI32',    'CGGCGTCTGCTTGGGTGTTTAACCT'),
                    end_sequence=  ('SQK-MAP006_Short_Y_Bottom_LI33', 'GGTTAAACACCCAAGCAGACGCCG')),


            Adapter('SQK-NSK007',
                    start_sequence=('SQK-NSK007_Y_Top',    'AATGTACTTCGTTCAGTTACGTATTGCT'),
                    end_sequence=  ('SQK-NSK007_Y_Bottom', 'GCAATACGTAACTGAACGAAGT')),


            Adapter('Native barcoding 1',
                    start_sequence=('NB01_rev', 'AGGTTAACACAAAGACACCGACAACTTTCTTCAGCACC'),
                    end_sequence=  ('NB01',     'GGTGCTGAAGAAAGTTGTCGGTGTCTTTGTGTTAACCT')),
            Adapter('Native barcoding 2',
                    start_sequence=('NB02_rev', 'AGGTTAAACAGACGACTACAAACGGAATCGACAGCACC'),
                    end_sequence=  ('NB02',     'GGTGCTGTCGATTCCGTTTGTAGTCGTCTGTTTAACCT')),
            Adapter('Native barcoding 3',
                    start_sequence=('NB03_rev', 'AGGTTAACCTGGTAACTGGGACACAAGACTCCAGCACC'),
                    end_sequence=  ('NB03',     'GGTGCTGGAGTCTTGTGTCCCAGTTACCAGGTTAACCT')),
            Adapter('Native barcoding 4',
                    start_sequence=('NB04_rev', 'AGGTTAATAGGGAAACACGATAGAATCCGAACAGCACC'),
                    end_sequence=  ('NB04',     'GGTGCTGTTCGGATTCTATCGTGTTTCCCTATTAACCT')),
            Adapter('Native barcoding 5',
                    start_sequence=('NB05_rev', 'AGGTTAAAAGGTTACACAAACCCTGGACAAGCAGCACC'),
                    end_sequence=  ('NB05',     'GGTGCTGCTTGTCCAGGGTTTGTGTAACCTTTTAACCT')),
            Adapter('Native barcoding 6',
                    start_sequence=('NB06_rev', 'AGGTTAAGACTACTTTCTGCCTTTGCGAGAACAGCACC'),
                    end_sequence=  ('NB06',     'GGTGCTGTTCTCGCAAAGGCAGAAAGTAGTCTTAACCT')),
            Adapter('Native barcoding 7',
                    start_sequence=('NB07_rev', 'AGGTTAAAAGGATTCATTCCCACGGTAACACCAGCACC'),
                    end_sequence=  ('NB07',     'GGTGCTGGTGTTACCGTGGGAATGAATCCTTTTAACCT')),
            Adapter('Native barcoding 8',
                    start_sequence=('NB08_rev', 'AGGTTAAACGTAACTTGGTTTGTTCCCTGAACAGCACC'),
                    end_sequence=  ('NB08',     'GGTGCTGTTCAGGGAACAAACCAAGTTACGTTTAACCT')),
            Adapter('Native barcoding 9',
                    start_sequence=('NB09_rev', 'AGGTTAAAACCAAGACTCGCTGTGCCTAGTTCAGCACC'),
                    end_sequence=  ('NB09',     'GGTGCTGAACTAGGCACAGCGAGTCTTGGTTTTAACCT')),
            Adapter('Native barcoding 10',
                    start_sequence=('NB10_rev', 'AGGTTAAGAGAGGACAAAGGTTTCAACGCTTCAGCACC'),
                    end_sequence=  ('NB10',     'GGTGCTGAAGCGTTGAAACCTTTGTCCTCTCTTAACCT')),
            Adapter('Native barcoding 11',
                    start_sequence=('NB11_rev', 'AGGTTAATCCATTCCCTCCGATAGATGAAACCAGCACC'),
                    end_sequence=  ('NB11',     'GGTGCTGGTTTCATCTATCGGAGGGAATGGATTAACCT')),
            Adapter('Native barcoding 12',
                    start_sequence=('NB12_rev', 'AGGTTAATCCGATTCTGCTTCTTTCTACCTGCAGCACC'),
                    end_sequence=  ('NB12',     'GGTGCTGCAGGTAGAAAGAAGCAGAATCGGATTAACCT')),


            Adapter('PCR barcoding 1',
                    start_sequence=('BC01',     'GGTGCTGAAGAAAGTTGTCGGTGTCTTTGTGTTAACCT'),
                    end_sequence=  ('BC01_rev', 'AGGTTAACACAAAGACACCGACAACTTTCTTCAGCACC')),
            Adapter('PCR barcoding 2',
                    start_sequence=('BC02',     'GGTGCTGTCGATTCCGTTTGTAGTCGTCTGTTTAACCT'),
                    end_sequence=  ('BC02_rev', 'AGGTTAAACAGACGACTACAAACGGAATCGACAGCACC')),
            Adapter('PCR barcoding 3',
                    start_sequence=('BC03',     'GGTGCTGGAGTCTTGTGTCCCAGTTACCAGGTTAACCT'),
                    end_sequence=  ('BC03_rev', 'AGGTTAACCTGGTAACTGGGACACAAGACTCCAGCACC')),
            Adapter('PCR barcoding 4',
                    start_sequence=('BC04',     'GGTGCTGTTCGGATTCTATCGTGTTTCCCTATTAACCT'),
                    end_sequence=  ('BC04_rev', 'AGGTTAATAGGGAAACACGATAGAATCCGAACAGCACC')),
            Adapter('PCR barcoding 5',
                    start_sequence=('BC05',     'GGTGCTGCTTGTCCAGGGTTTGTGTAACCTTTTAACCT'),
                    end_sequence=  ('BC05_rev', 'AGGTTAAAAGGTTACACAAACCCTGGACAAGCAGCACC')),
            Adapter('PCR barcoding 6',
                    start_sequence=('BC06',     'GGTGCTGTTCTCGCAAAGGCAGAAAGTAGTCTTAACCT'),
                    end_sequence=  ('BC06_rev', 'AGGTTAAGACTACTTTCTGCCTTTGCGAGAACAGCACC')),
            Adapter('PCR barcoding 7',
                    start_sequence=('BC07',     'GGTGCTGGTGTTACCGTGGGAATGAATCCTTTTAACCT'),
                    end_sequence=  ('BC07_rev', 'AGGTTAAAAGGATTCATTCCCACGGTAACACCAGCACC')),
            Adapter('PCR barcoding 8',
                    start_sequence=('BC08',     'GGTGCTGTTCAGGGAACAAACCAAGTTACGTTTAACCT'),
                    end_sequence=  ('BC08_rev', 'AGGTTAAACGTAACTTGGTTTGTTCCCTGAACAGCACC')),
            Adapter('PCR barcoding 9',
                    start_sequence=('BC09',     'GGTGCTGAACTAGGCACAGCGAGTCTTGGTTTTAACCT'),
                    end_sequence=  ('BC09_rev', 'AGGTTAAAACCAAGACTCGCTGTGCCTAGTTCAGCACC')),
            Adapter('PCR barcoding 10',
                    start_sequence=('BC10',     'GGTGCTGAAGCGTTGAAACCTTTGTCCTCTCTTAACCT'),
                    end_sequence=  ('BC10_rev', 'AGGTTAAGAGAGGACAAAGGTTTCAACGCTTCAGCACC')),
            Adapter('PCR barcoding 11',
                    start_sequence=('BC11',     'GGTGCTGGTTTCATCTATCGGAGGGAATGGATTAACCT'),
                    end_sequence=  ('BC11_rev', 'AGGTTAATCCATTCCCTCCGATAGATGAAACCAGCACC')),
            Adapter('PCR barcoding 12',
                    start_sequence=('BC12',     'GGTGCTGCAGGTAGAAAGAAGCAGAATCGGATTAACCT'),
                    end_sequence=  ('BC12_rev', 'AGGTTAATCCGATTCTGCTTCTTTCTACCTGCAGCACC')),
            Adapter('PCR barcoding 13',
                    start_sequence=('BC13',     'GGTGCTGAGAACGACTTCCATACTCGTGTGATTAACCT'),
                    end_sequence=  ('BC13_rev', 'AGGTTAATCACACGAGTATGGAAGTCGTTCTCAGCACC')),
            Adapter('PCR barcoding 14',
                    start_sequence=('BC14',     'GGTGCTGAACGAGTCTCTTGGGACCCATAGATTAACCT'),
                    end_sequence=  ('BC14_rev', 'AGGTTAATCTATGGGTCCCAAGAGACTCGTTCAGCACC')),
            Adapter('PCR barcoding 15',
                    start_sequence=('BC15',     'GGTGCTGAGGTCTACCTCGCTAACACCACTGTTAACCT'),
                    end_sequence=  ('BC15_rev', 'AGGTTAACAGTGGTGTTAGCGAGGTAGACCTCAGCACC')),
            Adapter('PCR barcoding 16',
                    start_sequence=('BC16',     'GGTGCTGCGTCAACTGACAGTGGTTCGTACTTTAACCT'),
                    end_sequence=  ('BC16_rev', 'AGGTTAAAGTACGAACCACTGTCAGTTGACGCAGCACC')),
            Adapter('PCR barcoding 17',
                    start_sequence=('BC17',     'GGTGCTGACCCTCCAGGAAAGTACCTCTGATTTAACCT'),
                    end_sequence=  ('BC17_rev', 'AGGTTAAATCAGAGGTACTTTCCTGGAGGGTCAGCACC')),
            Adapter('PCR barcoding 18',
                    start_sequence=('BC18',     'GGTGCTGCCAAACCCAACAACCTAGATAGGCTTAACCT'),
                    end_sequence=  ('BC18_rev', 'AGGTTAAGCCTATCTAGGTTGTTGGGTTTGGCAGCACC')),
            Adapter('PCR barcoding 19',
                    start_sequence=('BC19',     'GGTGCTGGTTCCTCGTGCAGTGTCAAGAGATTTAACCT'),
                    end_sequence=  ('BC19_rev', 'AGGTTAAATCTCTTGACACTGCACGAGGAACCAGCACC')),
            Adapter('PCR barcoding 20',
                    start_sequence=('BC20',     'GGTGCTGTTGCGTCCTGTTACGAGAACTCATTTAACCT'),
                    end_sequence=  ('BC20_rev', 'AGGTTAAATGAGTTCTCGTAACAGGACGCAACAGCACC')),
            Adapter('PCR barcoding 21',
                    start_sequence=('BC21',     'GGTGCTGGAGCCTCTCATTGTCCGTTCTCTATTAACCT'),
                    end_sequence=  ('BC21_rev', 'AGGTTAATAGAGAACGGACAATGAGAGGCTCCAGCACC')),
            Adapter('PCR barcoding 22',
                    start_sequence=('BC22',     'GGTGCTGACCACTGCCATGTATCAAAGTACGTTAACCT'),
                    end_sequence=  ('BC22_rev', 'AGGTTAACGTACTTTGATACATGGCAGTGGTCAGCACC')),
            Adapter('PCR barcoding 23',
                    start_sequence=('BC23',     'GGTGCTGCTTACTACCCAGTGAACCTCCTCGTTAACCT'),
                    end_sequence=  ('BC23_rev', 'AGGTTAACGAGGAGGTTCACTGGGTAGTAAGCAGCACC')),
            Adapter('PCR barcoding 24',
                    start_sequence=('BC24',     'GGTGCTGGCATAGTTCTGCATGATGGGTTAGTTAACCT'),
                    end_sequence=  ('BC24_rev', 'AGGTTAACTAACCCATCATGCAGAACTATGCCAGCACC')),
            Adapter('PCR barcoding 25',
                    start_sequence=('BC25',     'GGTGCTGGTAAGTTGGGTATGCAACGCAATGTTAACCT'),
                    end_sequence=  ('BC25_rev', 'AGGTTAACATTGCGTTGCATACCCAACTTACCAGCACC')),
            Adapter('PCR barcoding 26',
                    start_sequence=('BC26',     'GGTGCTGCATACAGCGACTACGCATTCTCATTTAACCT'),
                    end_sequence=  ('BC26_rev', 'AGGTTAAATGAGAATGCGTAGTCGCTGTATGCAGCACC')),
            Adapter('PCR barcoding 27',
                    start_sequence=('BC27',     'GGTGCTGCGACGGTTAGATTCACCTCTTACATTAACCT'),
                    end_sequence=  ('BC27_rev', 'AGGTTAATGTAAGAGGTGAATCTAACCGTCGCAGCACC')),
            Adapter('PCR barcoding 28',
                    start_sequence=('BC28',     'GGTGCTGTGAAACCTAAGAAGGCACCGTATCTTAACCT'),
                    end_sequence=  ('BC28_rev', 'AGGTTAAGATACGGTGCCTTCTTAGGTTTCACAGCACC')),
            Adapter('PCR barcoding 29',
                    start_sequence=('BC29',     'GGTGCTGCTAGACACCTTGGGTTGACAGACCTTAACCT'),
                    end_sequence=  ('BC29_rev', 'AGGTTAAGGTCTGTCAACCCAAGGTGTCTAGCAGCACC')),
            Adapter('PCR barcoding 30',
                    start_sequence=('BC30',     'GGTGCTGTCAGTGAGGATCTACTTCGACCCATTAACCT'),
                    end_sequence=  ('BC30_rev', 'AGGTTAATGGGTCGAAGTAGATCCTCACTGACAGCACC')),
            Adapter('PCR barcoding 31',
                    start_sequence=('BC31',     'GGTGCTGTGCGTACAGCAATCAGTTACATTGTTAACCT'),
                    end_sequence=  ('BC31_rev', 'AGGTTAACAATGTAACTGATTGCTGTACGCACAGCACC')),
            Adapter('PCR barcoding 32',
                    start_sequence=('BC32',     'GGTGCTGCCAGTAGAAGTCCGACAACGTCATTTAACCT'),
                    end_sequence=  ('BC32_rev', 'AGGTTAAATGACGTTGTCGGACTTCTACTGGCAGCACC')),
            Adapter('PCR barcoding 33',
                    start_sequence=('BC33',     'GGTGCTGCAGACTTGGTACGGTTGGGTAACTTTAACCT'),
                    end_sequence=  ('BC33_rev', 'AGGTTAAAGTTACCCAACCGTACCAAGTCTGCAGCACC')),
            Adapter('PCR barcoding 34',
                    start_sequence=('BC34',     'GGTGCTGGGACGAAGAACTCAAGTCAAAGGCTTAACCT'),
                    end_sequence=  ('BC34_rev', 'AGGTTAAGCCTTTGACTTGAGTTCTTCGTCCCAGCACC')),
            Adapter('PCR barcoding 35',
                    start_sequence=('BC35',     'GGTGCTGCTACTTACGAAGCTGAGGGACTGCTTAACCT'),
                    end_sequence=  ('BC35_rev', 'AGGTTAAGCAGTCCCTCAGCTTCGTAAGTAGCAGCACC')),
            Adapter('PCR barcoding 36',
                    start_sequence=('BC36',     'GGTGCTGATGTCCCAGTTAGAGGAGGAAACATTAACCT'),
                    end_sequence=  ('BC36_rev', 'AGGTTAATGTTTCCTCCTCTAACTGGGACATCAGCACC')),
            Adapter('PCR barcoding 37',
                    start_sequence=('BC37',     'GGTGCTGGCTTGCGATTGATGCTTAGTATCATTAACCT'),
                    end_sequence=  ('BC37_rev', 'AGGTTAATGATACTAAGCATCAATCGCAAGCCAGCACC')),
            Adapter('PCR barcoding 38',
                    start_sequence=('BC38',     'GGTGCTGACCACAGGAGGACGATACAGAGAATTAACCT'),
                    end_sequence=  ('BC38_rev', 'AGGTTAATTCTCTGTATCGTCCTCCTGTGGTCAGCACC')),
            Adapter('PCR barcoding 39',
                    start_sequence=('BC39',     'GGTGCTGCCACAGTGTCAACTAGAGCCTCTCTTAACCT'),
                    end_sequence=  ('BC39_rev', 'AGGTTAAGAGAGGCTCTAGTTGACACTGTGGCAGCACC')),
            Adapter('PCR barcoding 40',
                    start_sequence=('BC40',     'GGTGCTGTAGTTTGGATGACCAAGGATAGCCTTAACCT'),
                    end_sequence=  ('BC40_rev', 'AGGTTAAGGCTATCCTTGGTCATCCAAACTACAGCACC')),
            Adapter('PCR barcoding 41',
                    start_sequence=('BC41',     'GGTGCTGGGAGTTCGTCCAGAGAAGTACACGTTAACCT'),
                    end_sequence=  ('BC41_rev', 'AGGTTAACGTGTACTTCTCTGGACGAACTCCCAGCACC')),
            Adapter('PCR barcoding 42',
                    start_sequence=('BC42',     'GGTGCTGCTACGTGTAAGGCATACCTGCCAGTTAACCT'),
                    end_sequence=  ('BC42_rev', 'AGGTTAACTGGCAGGTATGCCTTACACGTAGCAGCACC')),
            Adapter('PCR barcoding 43',
                    start_sequence=('BC43',     'GGTGCTGCTTTCGTTGTTGACTCGACGGTAGTTAACCT'),
                    end_sequence=  ('BC43_rev', 'AGGTTAACTACCGTCGAGTCAACAACGAAAGCAGCACC')),
            Adapter('PCR barcoding 44',
                    start_sequence=('BC44',     'GGTGCTGAGTAGAAAGGGTTCCTTCCCACTCTTAACCT'),
                    end_sequence=  ('BC44_rev', 'AGGTTAAGAGTGGGAAGGAACCCTTTCTACTCAGCACC')),
            Adapter('PCR barcoding 45',
                    start_sequence=('BC45',     'GGTGCTGGATCCAACAGAGATGCCTTCAGTGTTAACCT'),
                    end_sequence=  ('BC45_rev', 'AGGTTAACACTGAAGGCATCTCTGTTGGATCCAGCACC')),
            Adapter('PCR barcoding 46',
                    start_sequence=('BC46',     'GGTGCTGGCTGTGTTCCACTTCATTCTCCTGTTAACCT'),
                    end_sequence=  ('BC46_rev', 'AGGTTAACAGGAGAATGAAGTGGAACACAGCCAGCACC')),
            Adapter('PCR barcoding 47',
                    start_sequence=('BC47',     'GGTGCTGGTGCAACTTTCCCACAGGTAGTTCTTAACCT'),
                    end_sequence=  ('BC47_rev', 'AGGTTAAGAACTACCTGTGGGAAAGTTGCACCAGCACC')),
            Adapter('PCR barcoding 48',
                    start_sequence=('BC48',     'GGTGCTGCATCTGGAACGTGGTACACCTGTATTAACCT'),
                    end_sequence=  ('BC48_rev', 'AGGTTAATACAGGTGTACCACGTTCCAGATGCAGCACC')),
            Adapter('PCR barcoding 49',
                    start_sequence=('BC49',     'GGTGCTGACTGGTGCAGCTTTGAACATCTAGTTAACCT'),
                    end_sequence=  ('BC49_rev', 'AGGTTAACTAGATGTTCAAAGCTGCACCAGTCAGCACC')),
            Adapter('PCR barcoding 50',
                    start_sequence=('BC50',     'GGTGCTGATGGACTTTGGTAACTTCCTGCGTTTAACCT'),
                    end_sequence=  ('BC50_rev', 'AGGTTAAACGCAGGAAGTTACCAAAGTCCATCAGCACC')),
            Adapter('PCR barcoding 51',
                    start_sequence=('BC51',     'GGTGCTGGTTGAATGAGCCTACTGGGTCCTCTTAACCT'),
                    end_sequence=  ('BC51_rev', 'AGGTTAAGAGGACCCAGTAGGCTCATTCAACCAGCACC')),
            Adapter('PCR barcoding 52',
                    start_sequence=('BC52',     'GGTGCTGTGAGAGACAAGATTGTTCGTGGACTTAACCT'),
                    end_sequence=  ('BC52_rev', 'AGGTTAAGTCCACGAACAATCTTGTCTCTCACAGCACC')),
            Adapter('PCR barcoding 53',
                    start_sequence=('BC53',     'GGTGCTGAGATTCAGACCGTCTCATGCAAAGTTAACCT'),
                    end_sequence=  ('BC53_rev', 'AGGTTAACTTTGCATGAGACGGTCTGAATCTCAGCACC')),
            Adapter('PCR barcoding 54',
                    start_sequence=('BC54',     'GGTGCTGCAAGAGCTTTGACTAAGGAGCATGTTAACCT'),
                    end_sequence=  ('BC54_rev', 'AGGTTAACATGCTCCTTAGTCAAAGCTCTTGCAGCACC')),
            Adapter('PCR barcoding 55',
                    start_sequence=('BC55',     'GGTGCTGTGGAAGATGAGACCCTGATCTACGTTAACCT'),
                    end_sequence=  ('BC55_rev', 'AGGTTAACGTAGATCAGGGTCTCATCTTCCACAGCACC')),
            Adapter('PCR barcoding 56',
                    start_sequence=('BC56',     'GGTGCTGTCACTACTCAACAGGTGGCATGAATTAACCT'),
                    end_sequence=  ('BC56_rev', 'AGGTTAATTCATGCCACCTGTTGAGTAGTGACAGCACC')),
            Adapter('PCR barcoding 57',
                    start_sequence=('BC57',     'GGTGCTGGCTAGGTCAATCTCCTTCGGAAGTTTAACCT'),
                    end_sequence=  ('BC57_rev', 'AGGTTAAACTTCCGAAGGAGATTGACCTAGCCAGCACC')),
            Adapter('PCR barcoding 58',
                    start_sequence=('BC58',     'GGTGCTGCAGGTTACTCCTCCGTGAGTCTGATTAACCT'),
                    end_sequence=  ('BC58_rev', 'AGGTTAATCAGACTCACGGAGGAGTAACCTGCAGCACC')),
            Adapter('PCR barcoding 59',
                    start_sequence=('BC59',     'GGTGCTGTCAATCAAGAAGGGAAAGCAAGGTTTAACCT'),
                    end_sequence=  ('BC59_rev', 'AGGTTAAACCTTGCTTTCCCTTCTTGATTGACAGCACC')),
            Adapter('PCR barcoding 60',
                    start_sequence=('BC60',     'GGTGCTGCATGTTCAACCAAGGCTTCTATGGTTAACCT'),
                    end_sequence=  ('BC60_rev', 'AGGTTAACCATAGAAGCCTTGGTTGAACATGCAGCACC')),
            Adapter('PCR barcoding 61',
                    start_sequence=('BC61',     'GGTGCTGAGAGGGTACTATGTGCCTCAGCACTTAACCT'),
                    end_sequence=  ('BC61_rev', 'AGGTTAAGTGCTGAGGCACATAGTACCCTCTCAGCACC')),
            Adapter('PCR barcoding 62',
                    start_sequence=('BC62',     'GGTGCTGCACCCACACTTACTTCAGGACGTATTAACCT'),
                    end_sequence=  ('BC62_rev', 'AGGTTAATACGTCCTGAAGTAAGTGTGGGTGCAGCACC')),
            Adapter('PCR barcoding 63',
                    start_sequence=('BC63',     'GGTGCTGTTCTGAAGTTCCTGGGTCTTGAACTTAACCT'),
                    end_sequence=  ('BC63_rev', 'AGGTTAAGTTCAAGACCCAGGAACTTCAGAACAGCACC')),
            Adapter('PCR barcoding 64',
                    start_sequence=('BC64',     'GGTGCTGGACAGACACCGTTCATCGACTTTCTTAACCT'),
                    end_sequence=  ('BC64_rev', 'AGGTTAAGAAAGTCGATGAACGGTGTCTGTCCAGCACC')),
            Adapter('PCR barcoding 65',
                    start_sequence=('BC65',     'GGTGCTGTTCTCAGTCTTCCTCCAGACAAGGTTAACCT'),
                    end_sequence=  ('BC65_rev', 'AGGTTAACCTTGTCTGGAGGAAGACTGAGAACAGCACC')),
            Adapter('PCR barcoding 66',
                    start_sequence=('BC66',     'GGTGCTGCCGATCCTTGTGGCTTCTAACTTCTTAACCT'),
                    end_sequence=  ('BC66_rev', 'AGGTTAAGAAGTTAGAAGCCACAAGGATCGGCAGCACC')),
            Adapter('PCR barcoding 67',
                    start_sequence=('BC67',     'GGTGCTGGTTTGTCATACTCGTGTGCTCACCTTAACCT'),
                    end_sequence=  ('BC67_rev', 'AGGTTAAGGTGAGCACACGAGTATGACAAACCAGCACC')),
            Adapter('PCR barcoding 68',
                    start_sequence=('BC68',     'GGTGCTGGAATCTAAGCAAACACGAAGGTGGTTAACCT'),
                    end_sequence=  ('BC68_rev', 'AGGTTAACCACCTTCGTGTTTGCTTAGATTCCAGCACC')),
            Adapter('PCR barcoding 69',
                    start_sequence=('BC69',     'GGTGCTGTACAGTCCGAGCCTCATGTGATCTTTAACCT'),
                    end_sequence=  ('BC69_rev', 'AGGTTAAAGATCACATGAGGCTCGGACTGTACAGCACC')),
            Adapter('PCR barcoding 70',
                    start_sequence=('BC70',     'GGTGCTGACCGAGATCCTACGAATGGAGTGTTTAACCT'),
                    end_sequence=  ('BC70_rev', 'AGGTTAAACACTCCATTCGTAGGATCTCGGTCAGCACC')),
            Adapter('PCR barcoding 71',
                    start_sequence=('BC71',     'GGTGCTGCCTGGGAGCATCAGGTAGTAACAGTTAACCT'),
                    end_sequence=  ('BC71_rev', 'AGGTTAACTGTTACTACCTGATGCTCCCAGGCAGCACC')),
            Adapter('PCR barcoding 72',
                    start_sequence=('BC72',     'GGTGCTGTAGCTGACTGTCTTCCATACCGACTTAACCT'),
                    end_sequence=  ('BC72_rev', 'AGGTTAAGTCGGTATGGAAGACAGTCAGCTACAGCACC')),
            Adapter('PCR barcoding 73',
                    start_sequence=('BC73',     'GGTGCTGAAGAAACAGGATGACAGAACCCTCTTAACCT'),
                    end_sequence=  ('BC73_rev', 'AGGTTAAGAGGGTTCTGTCATCCTGTTTCTTCAGCACC')),
            Adapter('PCR barcoding 74',
                    start_sequence=('BC74',     'GGTGCTGTACAAGCATCCCAACACTTCCACTTTAACCT'),
                    end_sequence=  ('BC74_rev', 'AGGTTAAAGTGGAAGTGTTGGGATGCTTGTACAGCACC')),
            Adapter('PCR barcoding 75',
                    start_sequence=('BC75',     'GGTGCTGGACCATTGTGATGAACCCTGTTGTTTAACCT'),
                    end_sequence=  ('BC75_rev', 'AGGTTAAACAACAGGGTTCATCACAATGGTCCAGCACC')),
            Adapter('PCR barcoding 76',
                    start_sequence=('BC76',     'GGTGCTGATGCTTGTTACATCAACCCTGGACTTAACCT'),
                    end_sequence=  ('BC76_rev', 'AGGTTAAGTCCAGGGTTGATGTAACAAGCATCAGCACC')),
            Adapter('PCR barcoding 77',
                    start_sequence=('BC77',     'GGTGCTGCGACCTGTTTCTCAGGGATACAACTTAACCT'),
                    end_sequence=  ('BC77_rev', 'AGGTTAAGTTGTATCCCTGAGAAACAGGTCGCAGCACC')),
            Adapter('PCR barcoding 78',
                    start_sequence=('BC78',     'GGTGCTGAACAACCGAACCTTTGAATCAGAATTAACCT'),
                    end_sequence=  ('BC78_rev', 'AGGTTAATTCTGATTCAAAGGTTCGGTTGTTCAGCACC')),
            Adapter('PCR barcoding 79',
                    start_sequence=('BC79',     'GGTGCTGTCTCGGAGATAGTTCTCACTGCTGTTAACCT'),
                    end_sequence=  ('BC79_rev', 'AGGTTAACAGCAGTGAGAACTATCTCCGAGACAGCACC')),
            Adapter('PCR barcoding 80',
                    start_sequence=('BC80',     'GGTGCTGCGGATGAACATAGGATAGCGATTCTTAACCT'),
                    end_sequence=  ('BC80_rev', 'AGGTTAAGAATCGCTATCCTATGTTCATCCGCAGCACC')),
            Adapter('PCR barcoding 81',
                    start_sequence=('BC81',     'GGTGCTGCCTCATCTTGTGAAGTTGTTTCGGTTAACCT'),
                    end_sequence=  ('BC81_rev', 'AGGTTAACCGAAACAACTTCACAAGATGAGGCAGCACC')),
            Adapter('PCR barcoding 82',
                    start_sequence=('BC82',     'GGTGCTGACGGTATGTCGAGTTCCAGGACTATTAACCT'),
                    end_sequence=  ('BC82_rev', 'AGGTTAATAGTCCTGGAACTCGACATACCGTCAGCACC')),
            Adapter('PCR barcoding 83',
                    start_sequence=('BC83',     'GGTGCTGTGGCTTGATCTAGGTAAGGTCGAATTAACCT'),
                    end_sequence=  ('BC83_rev', 'AGGTTAATTCGACCTTACCTAGATCAAGCCACAGCACC')),
            Adapter('PCR barcoding 84',
                    start_sequence=('BC84',     'GGTGCTGGTAGTGGACCTAGAACCTGTGCCATTAACCT'),
                    end_sequence=  ('BC84_rev', 'AGGTTAATGGCACAGGTTCTAGGTCCACTACCAGCACC')),
            Adapter('PCR barcoding 85',
                    start_sequence=('BC85',     'GGTGCTGAACGGAGGAGTTAGTTGGATGATCTTAACCT'),
                    end_sequence=  ('BC85_rev', 'AGGTTAAGATCATCCAACTAACTCCTCCGTTCAGCACC')),
            Adapter('PCR barcoding 86',
                    start_sequence=('BC86',     'GGTGCTGAGGTGATCCCAACAAGCGTAAGTATTAACCT'),
                    end_sequence=  ('BC86_rev', 'AGGTTAATACTTACGCTTGTTGGGATCACCTCAGCACC')),
            Adapter('PCR barcoding 87',
                    start_sequence=('BC87',     'GGTGCTGTACATGCTCCTGTTGTTAGGGAGGTTAACCT'),
                    end_sequence=  ('BC87_rev', 'AGGTTAACCTCCCTAACAACAGGAGCATGTACAGCACC')),
            Adapter('PCR barcoding 88',
                    start_sequence=('BC88',     'GGTGCTGTCTTCTACTACCGATCCGAAGCAGTTAACCT'),
                    end_sequence=  ('BC88_rev', 'AGGTTAACTGCTTCGGATCGGTAGTAGAAGACAGCACC')),
            Adapter('PCR barcoding 89',
                    start_sequence=('BC89',     'GGTGCTGACAGCATCAATGTTTGGCTAGTTGTTAACCT'),
                    end_sequence=  ('BC89_rev', 'AGGTTAACAACTAGCCAAACATTGATGCTGTCAGCACC')),
            Adapter('PCR barcoding 90',
                    start_sequence=('BC90',     'GGTGCTGGATGTAGAGGGTACGGTTTGAGGCTTAACCT'),
                    end_sequence=  ('BC90_rev', 'AGGTTAAGCCTCAAACCGTACCCTCTACATCCAGCACC')),
            Adapter('PCR barcoding 91',
                    start_sequence=('BC91',     'GGTGCTGGGCTCCATAGGAACTCACGCTACTTTAACCT'),
                    end_sequence=  ('BC91_rev', 'AGGTTAAAGTAGCGTGAGTTCCTATGGAGCCCAGCACC')),
            Adapter('PCR barcoding 92',
                    start_sequence=('BC92',     'GGTGCTGTTGTGAGTGGAAAGATACAGGACCTTAACCT'),
                    end_sequence=  ('BC92_rev', 'AGGTTAAGGTCCTGTATCTTTCCACTCACAACAGCACC')),
            Adapter('PCR barcoding 93',
                    start_sequence=('BC93',     'GGTGCTGAGTTTCCATCACTTCAGACTTGGGTTAACCT'),
                    end_sequence=  ('BC93_rev', 'AGGTTAACCCAAGTCTGAAGTGATGGAAACTCAGCACC')),
            Adapter('PCR barcoding 94',
                    start_sequence=('BC94',     'GGTGCTGGATTGTCCTCAAACTGCCACCTACTTAACCT'),
                    end_sequence=  ('BC94_rev', 'AGGTTAAGTAGGTGGCAGTTTGAGGACAATCCAGCACC')),
            Adapter('PCR barcoding 95',
                    start_sequence=('BC95',     'GGTGCTGCCTGTCTGGAAGAAGAATGGACTTTTAACCT'),
                    end_sequence=  ('BC95_rev', 'AGGTTAAAAGTCCATTCTTCTTCCAGACAGGCAGCACC')),
            Adapter('PCR barcoding 96',
                    start_sequence=('BC96',     'GGTGCTGCTGAACGGTCATAGAGTCCACCATTTAACCT'),
                    end_sequence=  ('BC96_rev', 'AGGTTAAATGGTGGACTCTATGACCGTTCAGCAGCACC'))
            ]
