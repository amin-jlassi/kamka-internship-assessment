from typing import TypedDict



class AgentState(TypedDict):
    query : str
    tool : str
    context : list[dict]
    answer : str
    filename: str | None