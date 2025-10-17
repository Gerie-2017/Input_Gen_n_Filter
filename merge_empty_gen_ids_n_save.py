import ast


def merge_id_from_the_files(file_paths):
    merged_ids = set()

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    ids_in_file = ast.literal_eval(content)
                    if isinstance(ids_in_file, set):
                        merged_ids.update(ids_in_file) 
        except FileNotFoundError:
            print(f"Warning: File not found: {file_path}")
        except (ValueError, SyntaxError) as e:
            print(f"Error parsing file {file_path}: {e}")
        return merged_ids
    


if __name__ == "__main__":
    files_to_merge = [
        "cpp_empty_gen_IDs.txt",
        "java_empty_gen_IDs.txt",
        "python_empty_gen_IDs.txt"
    ]

    all_unique_ids = merge_id_from_the_files(files_to_merge)
    print("All unique IDs: ")


    all_unique_ids_list = []
    with open('all_ids_with_empty_gen.txt', 'w', encoding='utf-8') as wrids:
        for ids in all_unique_ids:
            all_unique_ids_list.append(ids)
        wrids.write(str(all_unique_ids_list))

    print(all_unique_ids)

    print(f"\n Total number of unique IDs: {len(all_unique_ids)}")