import json as default_json

from dynamodb_json import json_util as dynamo_json


def get_headers(file_content):
    first_line = file_content.pop(0)
    return first_line, file_content


def transform_json(old_content):
    new_content = []

    for line in old_content:
        new_line = []
        for item in line:
            try:
                value = default_json.loads(item)
                new_value = dynamo_json.loads(value)
            except:
                new_value = item

            new_line.append(new_value)
        new_content.append(new_line)

    return new_content
