import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--json_file", type=str, required=True)
parser.add_argument("--dst_lang", type=str, required=True)
args = parser.parse_args()


ids_with_empty_test_case = set()
def filter_empty_gen_ids(json_file, dst_lang):
    with open(json_file, "r", encoding="utf-8") as gen_file:
        for line in gen_file:
            if line.strip():
                data_samples = json.loads(line)
            if data_samples["test_case"] == []:
                ids_with_empty_test_case.add(data_samples["id"])
    print(f'{len(ids_with_empty_test_case)} IDs extracted.')
    with open(f"{dst_lang}_sample_IDs_with_no_testcase.txt", "w", encoding="utf-8") as fw:
        fw.write(str(ids_with_empty_test_case))
    return ids_with_empty_test_case

ids_with_empty_case = filter_empty_gen_ids(args.json_file, args.dst_lang)

print(ids_with_empty_case)