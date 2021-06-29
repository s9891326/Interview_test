"""
Please use Python 3 to answer question
Welcome to answer with unit testing code if you can

After you finish coding, please push to your GitHub account and share the link with us.
"""

# Please write a function to reverse the following nested input value into output value

from typing import Dict, List, Union, Optional

# Input:
input_value = {
    'hired': {
        'be': {
            'to': {
                'deserve': 'I'
            }
        }
    }
}

# Output:
output_value = {
    'I': {
        'deserve': {
            'to': {
                'be': 'hired'
            }
        }
    }
}


def reversed_dict(input_dict: Union[Dict[str, Dict], Dict[str, str]]) -> List[str]:
    """
    reversed dictionary, ex: input: {"a": {"b": "c"}} => output: ["a", "b", "c"]
    :param input_dict:
    :return:
    """
    result = []
    if not isinstance(input_dict, dict):
        return []
    next_key = input_dict.keys()
    next_value = input_dict.values()

    while next_key:
        result.append(list(next_key)[0])
        temp_dict = list(next_value)[0]

        if isinstance(temp_dict, str):
            next_key = None
            result.append(temp_dict)
        else:
            next_key = temp_dict.keys()
            next_value = temp_dict.values()

    return result


def compose_dict(input_list: Optional[List[str]]) -> Union[Dict[str, Dict], str]:
    """
    compose dictionary, ex: input: ["a", "b", "c"] => output: {"c": {"b": "a"}}
    :param input_list:
    :return:
    """
    if not isinstance(input_list, list):
        return ""

    if len(input_list) == 1:
        return input_list[0]
    else:
        value = input_list.pop(0)
        return {value: compose_dict(input_list)}


def first_reversed_flow(input_dict: Union[Dict[str, Dict], Dict[str, str]]) -> Union[Dict[str, Dict], List]:
    reversed_list = reversed_dict(input_dict)
    if reversed_list:
        reversed_list.reverse()
        return compose_dict(reversed_list)
    else:
        return reversed_list


def second_reversed_dict(input_dict: Union[Dict[str, Dict], Dict[str, str]]) -> Union[Dict[str, Dict], List]:
    """
    reversed dictionary, ex: input: {"a": {"b": "c"}} => output: {"c": {"b": "a"}}
    :param input_dict:
    :return:
    """
    result = reversed_dict(input_dict)

    if result:
        ans = result[0]
        for i in range(1, len(result)):
            temp_dict = {result[i]: ans}
            ans = temp_dict
        return ans
    else:
        return result


if __name__ == '__main__':
    # print(reversed_dict(input_value))
    # print(compose_dict(["a", "b", "c"]))
    print(first_reversed_flow(input_value))
