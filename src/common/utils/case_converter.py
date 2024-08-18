class CaseConverter:
    @staticmethod
    def to_camel_case(s: str) -> str:
        temp = s.split("_")
        return temp[0] + "".join(ele.title() for ele in temp[1:])

    @staticmethod
    def to_snake_case(s: str) -> str:
        return "".join(["_" + i.lower() if i.isupper() else i for i in s]).lstrip("_")
