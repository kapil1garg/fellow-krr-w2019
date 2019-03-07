from sheet_scraping import generate_krf_file_for_sheet_data


def main():
    """
    Generates full krf file with header to be used with Companion.

    :return: None
    """
    # load static facts file
    with open('../krf/facts.krf', 'r') as f:
        facts_krf = f.read()

    # load static query definitions file
    with open('../krf/query_definitions.krf', 'r') as f:
        query_definitions_krf = f.read()

    # load static queries file
    with open('../krf/queries.krf', 'r') as f:
        queries_krf = f.read()

    # generate and load in people file
    generate_krf_file_for_sheet_data()
    with open('../krf/people.krf', 'r') as f:
        people_krf = f.read()

    # create header
    krf_header = '\n'.join(['(in-microtheory KRR-Winter2019FactsMt)',
                            '(genlMt KRR-Winter2019FactsMt SocialModelingMt)',
                            '(genlMt KRR-Winter2019FactsMt NUPeopleLanguageInfoMt)',
                            '(genlMt KRR-Winter2019InClassMt KRR-Winter2019FactsMt)',
                            '(genlMt KRR-Winter2019RulesMt KRR-Winter2019FactsMt)'])
    krf_header += '\n\n'

    # create output file and save
    output_file_content = '\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n'.join([
        krf_header,
        ';;;;;;;;;;;;;;; FACTS ;;;;;;;;;;;;;;;', facts_krf,
        ';;;;;;;;; QUERY DEFINITIONS ;;;;;;;;;', query_definitions_krf,
        ';;;;;;;;;;;;;; QUERIES ;;;;;;;;;;;;;;', queries_krf,
        ';;;;;;;;;;;;;; PEOPLE ;;;;;;;;;;;;;;;', people_krf
    ])

    with open('../../dist/krf/fellow.krf', 'w') as output_file:
        output_file.write(output_file_content)


if __name__ == '__main__':
    main()
