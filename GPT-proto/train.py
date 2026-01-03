import torch
from torch import nn
from torch.nn import  functional as F

batch_size = 32
block_size = 8
max_iters = 3000
eval_interval = 300
eval_iter = 200
learning_rate = 1e-2
device= "cuda" if torch.cuda.is_available() else "cpu"

#----------------------------#
torch.manual_seed(42)

## download the text file
## open and read the file

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

chars = sorted(list(set(text)))
vocab_size = len(chars)


stoi = {val:i for i,val in enumerate(chars)}
itos = {i:val for i,val in enumerate(chars)}

encode  = lambda x :  [stoi[i] for i in x]
decode = lambda x : "".join([itos[i] for i in x])

data = torch.tensor(encode(text))

### lets split the data
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]


def get_batch(split= "train"):
    data = train_data if split == "train" else val_data
    idx =  torch.randint(len(data) - 8, (batch_size,))
    xb =  [data[i:i+block_size] for i in idx]
    yb = [data[i+1:i+block_size+1 ] for i in idx]
    x = torch.stack([i for i in xb])
    y = torch.stack([i for i in yb])
    x, y  = x.to(device), y.to(device)

    return x , y

@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ["train", "val"]:
        losses = torch.zeros(eval_iter)
        for k in range(eval_iter):
            xb, yb = get_batch(split)
            logits, loss = model(xb, yb)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out



class Biagram(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size,vocab_size)

    def forward(self, idx, targets=None):
        logits = self.token_embedding_table(idx) ## BTC
        if targets is None:
            loss = None
        else:
            B,T,C = logits.shape
            logits = logits.view(B*T,C)
            targets = targets.view(-1)
            loss = F.cross_entropy(logits, targets)
        return logits, loss

    
    def generate(self, idx, max_new_tokens=300):
        for _ in range(max_new_tokens):
            logits, _ = self(idx) ## BTC
            logits = logits[:,-1,:] #B,C
            # get probablioties
            probs = F.softmax(logits, dim=-1)
            idx_next = torch.multinomial(probs, num_samples=1)
            idx = torch.cat((idx, idx_next), dim=-1)
        return idx



model = Biagram(vocab_size=vocab_size)
model = model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

for iter in range(max_iters):

    if iter % eval_interval == 0:
        losses = estimate_loss()
        print(f"step {iter} : train loss: {losses["train"]} and val loss : {losses["val"]}")


    xb, yb = get_batch("train")

    logits, loss = model(xb,yb)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


a = torch.zeros((1,1), dtype=torch.long).to(device)
print(decode((model.generate(a)[0]).tolist()))



