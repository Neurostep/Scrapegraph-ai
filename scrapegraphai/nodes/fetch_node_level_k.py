"""
FetchNodeLevelK Module
"""
from typing import List, Optional
from .base_node import BaseNode

class FetchNodeLevelK(BaseNode):
    """
    A node responsible for fetching all the pages at a certain level of hyperlink the graph.

    Attributes:
        llm_model: An instance of a language model client, configured for generating answers.
        verbose (bool): A flag indicating whether to show print statements during execution.

    Args:
        input (str): Boolean expression defining the input keys needed from the state.
        output (List[str]): List of output keys to be updated in the state.
        node_config (dict): Additional configuration for the node.
        node_name (str): The unique identifier name for the node, defaulting to "Parse".
    """

    def __init__(
        self,
        input: str,
        output: List[str],
        node_config: Optional[dict] = None,
        node_name: str = "FetchLevelK",
    ):
        super().__init__(node_name, "node", input, output, 2, node_config)

        self.llm_model = node_config["llm_model"]
        self.embedder_model = node_config.get("embedder_model", None)
        self.verbose = (
            False if node_config is None else node_config.get("verbose", False)
        )
        self.cache_path = node_config.get("cache_path", False)

    def execute(self, state: dict) -> dict:
        pass
