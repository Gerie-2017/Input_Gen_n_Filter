import argparse
import json
import ast

with open("all_ids_with_empty_gen.txt", "r", encoding="utf-8") as rids:
    ids = rids.read()
    try:
        ids_list = ast.literal_eval(ids)
    except (ValueError, SyntaxError) as e:
        print(f"Error Parsing file: {e}")

print(ids_list)


parser = argparse.ArgumentParser()
parser.add_argument("--dst_lang", type=str,required=True)
args = parser.parse_args()


file_path =f"{args.dst_lang}_samples_out_of_those_241_generated_valid_inputs.jsonl"
output_path = f"full_{args.dst_lang}_samples_out_of_those_241_generated_valid_inputs.jsonl"

filtered_samples = []
with open(file_path, "r", encoding="utf-8") as src_f:
    for line in src_f:
        if line.strip():
            sample_data = json.loads(line)
            if sample_data.get('id') not in ids_list:
                filtered_samples.append(line)

with open(output_path, "w", encoding="utf-8") as out_f:
    for records in filtered_samples:
        out_f.write(records)