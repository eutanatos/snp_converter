import csv

filename = '220120_TAS21040_GT.csv'
output = 'snp_translated.csv'
markers_filtered = list()
markers_translated = list()


def open_file(file):
    '''
    opens csv file with ; delimiter & filter homozygous parents
    :return: filtered markers, one element = one marker
    '''
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        headers = next(reader)
        markers = []
        for input_file_row in reader:
            markers.append(input_file_row)
    headers[0] = 'marker'
    return [marker for marker in markers if marker[1] != marker[2]]


def get_iupac_code_for_parents_combination(p1, p2):
    '''
    :param p1: parent_1 snp
    :param p2: parent_2 snp
    :return: sib undefined snp variant
    '''
    iupac_codes = ['R = A or G', 'Y = C or T', 'S = G or C', 'W = A or T', 'K = G or T', 'M = A or C']
    for element in iupac_codes:
        if p1 in element and p2 in element:
            return element[0]
    return 'Fail in get_iupac... function'


def translate_snp(marker_array):
    parent1 = marker_array[1]
    parent2 = marker_array[2]
    parents_combination = get_iupac_code_for_parents_combination(parent1,
                                                                 parent2) if parent1 != 'failed' \
                                                                             or parent2 != 'failed' else 0
    marker_array_translated = list()
    marker_array_translated.append(marker_array[0])  # get name of marker
    for snp in marker_array[1:]:
        if parent1 == 'failed':
            if snp == 'failed':
                marker_array_translated.append(1)
            elif snp == parent2:
                marker_array_translated.append(5)
            else:
                marker_array_translated.append(0)
        elif parent2 == 'failed':
            if snp == parent1:
                marker_array_translated.append(4)
            elif snp == 'failed':
                marker_array_translated.append(2)
            else:
                marker_array_translated.append(0)
        else:
            if snp == parent1:
                marker_array_translated.append(1)
            elif snp == parent2:
                marker_array_translated.append(2)
            elif snp == parents_combination:
                marker_array_translated.append(3)
            elif snp == 'failed':
                marker_array_translated.append(0)
            else:
                marker_array_translated.append(0)
    return marker_array_translated


def save_file(output_filename, markers_array):
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerows(markers_array)
        # for row in markers_array:
        #     writer.writerow(row)


markers_filtered = open_file(filename)
markers_translated = [translate_snp(marker) for marker in markers_filtered]
save_file(output, markers_translated)
