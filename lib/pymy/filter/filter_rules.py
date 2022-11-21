import html
import re


class FilterRules(object):
    '''
    静态筛选规则类
    '''

    @staticmethod
    def string_to_lower(value: str) -> str:
        return value.lower()

    @staticmethod
    def string_to_upper(value: str) -> str:
        return value.upper()

    @staticmethod
    def strip_scripts(value: str) -> str:
        value = re.sub(r"<script(?:\s*|\s+.*)>.*</script>", '', value, flags=re.I)
        value = re.sub(r"<link(?:\s*|\s+.*)(?:\s*/)?>", '', value, flags=re.I)

        return value

    @staticmethod
    def strip_tags(value: str) -> str:
        value = html.escape(value)

        return value

    @staticmethod
    def to_float(value) -> float:
        value = float(value)

        return value

    @staticmethod
    def to_int(value) -> int:
        value = int(value)

        return value

    @staticmethod
    def trim_string(value: str, options: dict = {}):
        char_list = options["char_list"] if "char_list" in options else None
        value = value.strip(char_list)

        return value