from pathlib import Path
import pandas as pd

CORA = Path(__file__).parent.parent.parent / "cora"
CITES = CORA / "cora.cites"
CONTENT = CORA / "cora.content"

def load_cora():
    content = pd.read_csv(CONTENT, delimiter="\t", header=None).values
    ids = content[:,0]
    data = content[:,1:-1]
    target = content[:,-1]
    edges = pd.read_csv(CITES, delimiter="\t", header=None).values
    return ids, data, target, edges


if __name__ == "__main__":
    load_cora()