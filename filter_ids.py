import json

python_empty_gen_ids = set()
java_empty_gen_ids = set()
cpp_empty_gen_ids = set()
def filter_empty_gen_ids(json_file, lang_tag):
    with open(json_file, "r", encoding="utf-8") as gen_file:
        for line in gen_file:
            if line.strip():
                data_samples = json.loads(line)
            if data_samples[f"{lang_tag}"] == "":
                eval(f"{lang_tag}_empty_gen_ids").add(data_samples["id"])
    print(f'{len(eval(f"{lang_tag}_empty_gen_ids"))} IDs extracted.')
    with open(f"{lang_tag}_empty_gen_IDs.txt", "w", encoding="utf-8") as fw:
        fw.write(str(eval(f"{lang_tag}_empty_gen_ids")))
    return eval(f"{lang_tag}_empty_gen_ids")

py_ids = filter_empty_gen_ids("python_samples_out_of_those_241_generated_valid_inputs.jsonl", "python")
cpp_ids = filter_empty_gen_ids("cpp_samples_out_of_those_241_generated_valid_inputs.jsonl", "cpp")
java_ids = filter_empty_gen_ids("java_samples_out_of_those_241_generated_valid_inputs.jsonl", "java")
print(py_ids, cpp_ids, java_ids)
